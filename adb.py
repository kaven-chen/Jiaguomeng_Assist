import subprocess
import os
import time
import multiprocessing
from utility import randomize_offset, randomize_scale


class Adb():
    def __init__(self):
        assert self.is_correctly_connected()

    def is_correctly_connected(self):
        # Return True if ADB enrivonment is correct, and only one divice is connected.
        output = subprocess.check_output(
            "adb devices", shell=True).decode('utf-8')
        if output.startswith('List of devices attached') and output.count('device') == 2:
            return True
        else:
            return False

    def get_screenshot(self, filename):
        os.system('adb shell screencap -p /sdcard/{}'.format(filename))
        os.system('adb pull /sdcard/{}'.format(filename))

    def get_screenshot_while_touching(self, filename, location, pressed_time=6):
        p = multiprocessing.Process(
            target=self.tap_continuously, args=[location, pressed_time])
        p.start()
        time.sleep(2)
        self.get_screenshot(filename)
        time.sleep(0.5)
        p.join()

    def tap(self, location, with_bias=True):
        if with_bias:
            location = map(randomize_offset, location)
        os.system('adb shell input touchscreen tap {} {}'.format(*location))

    def tap_continuously(self, location, duration):
        self.swipe(location, location, duration * 1000)

    def tap_periodically(self, location, times, interval=0.2):
        for _ in range(times):
            self.tap(location)
            time.sleep(interval)

    def swipe(self, start, end, duration=400, with_bias=True):
        if with_bias:
            start = map(randomize_offset, start)
            end = map(randomize_offset, end)
            duration = int(randomize_scale(duration))
        os.system('adb shell input touchscreen swipe {} {} {} {} {}'.format(
            *start, *end, duration
        ))


if __name__ == '__main__':
    adb = Adb()
    # time.sleep(5)
    # adb.get_screenshot('eee.png')
