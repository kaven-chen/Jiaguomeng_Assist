from adb import Adb
from config_1080x1920 import *
from utility import randomize_scale, shuffle_list, calc_image_similarity
import time


class Assistor():
    def __init__(self):
        self.adb = Adb()
        self.building_location = BUILDING_LOCATION
        self.goods_location = GOODS_LOCATION
        self.building_menu_location = BUILDING_MENU_LOCATION
        self.shop_menu_location = SHOP_MENU_LOCATION
        self.margin_location = MARGIN_LOCATION
        self.upgrade_location = UPGRADE_LOCATION
        self.upgrade_confirm_location = UPGRADE_CONFIRM_LOCATION
        self.hongbao_location = HONGBAO_LOCATION
        self.album_location = ALBUM_LOCATION
        self.cancel_album_location = CANCEL_ALBUM_LOCATION
        self.short_interval = SHORT_INTERVAL
        self.medium_interval = MEDIUM_INTERVAL
        self.long_interval = LONG_INTERVAL
        self.same_image_threshhod = SAME_IMAGE_THRESHHOLD

    def short_sleep(self):
        time.sleep(randomize_scale(self.short_interval))

    def medium_sleep(self):
        time.sleep(randomize_scale(self.medium_interval))

    def long_sleep(self):
        time.sleep(randomize_scale(self.long_interval))

    def collect_money(self):
        for location in shuffle_list(self.building_location):
            self.adb.tap(location)
            self.short_sleep()

    def transport_goods(self):
        for _ in range(4):
            for start in shuffle_list(self.goods_location):
                for end in shuffle_list(self.building_location):
                    self.adb.swipe(start, end)
                    self.short_sleep()

    def upgrade_building(self):
        self.adb.tap(self.upgrade_location)
        self.short_sleep()
        for location in shuffle_list(self.building_location):
            self.adb.tap(location)
            for _ in range(10):
                self.adb.tap(self.upgrade_confirm_location)
                self.short_sleep()

        self.adb.tap(self.upgrade_location)
        self.medium_sleep()

    def is_same_frame(self, dest):
        self.adb.get_screenshot('current.png')
        if calc_image_similarity('current.png', dest) > self.same_image_threshhod:
            return True
        else:
            return False

    def navigate_to_building(self):
        self.adb.tap(self.building_menu_location)

    def try_navigating_to_building(self):
        for _ in range(3):
            self.adb.tap(self.building_menu_location)
            self.short_sleep()
            if self.is_same_frame('building.png'):
                return True
            self.medium_sleep()
        return False

    def navigate_to_shop(self):
        self.adb.tap(self.shop_menu_location)

    def try_navigating_to_shop(self):
        for _ in range(3):
            self.adb.tap(self.shop_menu_location)
            self.short_sleep()
            if self.is_same_frame('shop.png'):
                return True
            self.medium_sleep()
        return False

    def bogo_click(self):
        for i in range(3, 6):
            self.adb.tap(self.margin_location[i % len(self.margin_location)])
            self.short_sleep()

    def click_for_cancel_album(self):
        for _ in range(3, 6):
            self.adb.tap(self.cancel_album_location)
            self.short_sleep()

    def click_hongbao_and_album(self):
        for _ in range(2):
            self.adb.tap(self.album_location)
            self.medium_sleep()
            self.click_for_cancel_album()
            for i in range(3):
                # or range(3)
                self.adb.tap(self.hongbao_location[i])
                self.medium_sleep()
                self.bogo_click()

    def run(self):
        self.navigate_to_building()
        self.short_sleep()
        self.adb.get_screenshot('building.png')

        self.medium_sleep()

        self.navigate_to_shop()
        self.short_sleep()
        self.adb.get_screenshot('shop.png')
        while True:
            # Do something in main window
            if self.try_navigating_to_building() == False:
                print('Error when navigating to building windows.')
                break
            for _ in range(5):
                self.collect_money()
                self.transport_goods()
            self.upgrade_building()

            self.medium_sleep()

            # Do something in shop window
            if self.try_navigating_to_shop() == False:
                print('Error when navigating to shop windows.')
                break
            self.click_hongbao_and_album()

            self.long_sleep()


if __name__ == '__main__':
    assistor = Assistor()
    assistor.run()
