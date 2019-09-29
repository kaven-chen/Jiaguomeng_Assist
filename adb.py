import subprocess
import os
from utility import randomize_offset, randomize_scale


class Adb():
    def __init__(self):
        assert self.is_connected()

    def is_connected(self):
        starting = 'List of devices attached'
        output = subprocess.check_output(
            "adb devices", shell=True).decode('utf-8')
        if output.startswith(starting) and output.find('device', len(starting)) != -1:
            return True
        else:
            return False

    def get_screenshot(self, filename):
        os.system('adb shell screencap -p /sdcard/{}'.format(filename))
        os.system('adb pull /sdcard/{}'.format(filename))

    def tap(self, location):
        os.system('adb shell input touchscreen tap {} {}'.format(
            randomize_offset(location[0]), randomize_offset(location[1])))

    def swipe(self, start, end, speed=400):
        os.system('adb shell input touchscreen swipe {} {} {} {} {}'.format(
            randomize_offset(start[0]), randomize_offset(start[1]),
            randomize_offset(end[0]), randomize_offset(end[1]),
            int(randomize_scale(speed))
        ))
