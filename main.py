from adb import Adb
from config_1080x1920 import *
from utility import *
import time
import numpy as np


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
        self.new_hongbao_and_album_prompt_location = NEW_HONGBAO_AND_ALBUM_PROMPT_LOCATION
        self.short_interval = SHORT_INTERVAL
        self.medium_interval = MEDIUM_INTERVAL
        self.long_interval = LONG_INTERVAL
        self.same_image_threshold = SAME_IMAGE_THRESHOLD
        self.new_hongbao_and_album_prompt_color = NEW_HONGBAO_AND_ALBUM_PROMPT_COLOR
        self.building_area_offset = BUILDING_AREA_OFFSET
        self.hongbao_area_location = HONGBAO_AREA_LOCATION
        self.album_area_location = ALBUM__AREA_LOCATION

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

    def get_green_channel_value_of_buildings(self, filename):
        result = []
        for location in self.building_location:
            area = [tuple(np.add(location, item))
                    for item in self.building_area_offset]
            # area: [(x0,y0),(x1,y1)], where it will turn green (green light)
            # if that building is the target for transporting goods.
            x = analyse_part_of_image(filename, area)
            result.append(x[1])
        return result

    def try_transporting_goods(self):
        self.adb.get_screenshot('temp_not_pressed.png')
        self.medium_sleep()
        origin = self.get_green_channel_value_of_buildings(
            'temp_not_pressed.png')
        for i, start in enumerate(self.goods_location):
            self.adb.get_screenshot_while_touching('temp_pressed.png', start)
            self.medium_sleep()
            current = self.get_green_channel_value_of_buildings(
                'temp_pressed.png')
            print('Original green channel:\t', list(map(int, origin)))
            print('Current green channel:\t', list(map(int, current)))
            difference = list(np.subtract(current, origin))
            # 'difference' is a 9-element list, each of them is the difference of green
            # channel value between image captured with and without screen touched.
            # A difference bigger than a threshold value (Here it is just hard-coded as 20)
            # means after touching, the building is changing green (green light),
            # So it would be our target.
            table = [1 if item > 20 else 0 for item in difference]
            if sum(table) == 1:
                target = table.index(1)
                print(
                    'Building {} is the target. Begin transporting...'.format(target + 1))
                self.transport_goods_accurately(
                    start, self.building_location[target])
            else:
                print(
                    'Zero or multiple available targets found for cargo {}. Abandoned.'.format(i + 1))

            print('')

    def transport_goods_accurately(self, start, end):
        for _ in range(4):
            self.adb.swipe(start, end)
            self.short_sleep()

    def upgrade_building(self):
        self.adb.tap(self.upgrade_location)
        self.medium_sleep()
        for location in shuffle_list(self.building_location):
            self.adb.tap(location)
            for _ in range(3):
                self.adb.tap(self.upgrade_confirm_location)
                self.short_sleep()

        self.medium_sleep()
        self.adb.tap(self.upgrade_location)

    def is_same_frame(self, dest):
        '''
        Return True if current frame is the same (probably) as dest image.
        '''
        self.adb.get_screenshot('current.png')
        self.medium_sleep()
        if calc_image_similarity('current.png', dest) > self.same_image_threshold:
            return True
        else:
            return False

    def navigate_to_building(self):
        self.adb.tap(self.building_menu_location)

    def try_navigating_to_building(self):
        '''
        Diffenerce with 'navigate_to_building':
        'navigate_to_building' is only used at first to get an initial image.
        This initial image is used later by 'try_navigating_to_building'.
        (comparing the similarity between the initial image and the newly-got image)
        Same for 'navigate_to_shop' and 'try_navigating_to_shop'
        '''
        for _ in range(3):
            self.adb.tap(self.building_menu_location)
            self.medium_sleep()
            if self.is_same_frame('building.png'):
                return True
            self.medium_sleep()
        return False

    def navigate_to_shop(self):
        self.adb.tap(self.shop_menu_location)

    def try_navigating_to_shop(self):
        for _ in range(3):
            self.adb.tap(self.shop_menu_location)
            self.medium_sleep()
            if self.is_same_frame('shop.png'):
                return True
            self.medium_sleep()
        return False

    def bogo_click(self):
        '''
        Click edge area, used to skipping something.
        '''
        for i in range(3, 6):
            self.adb.tap(self.margin_location[i % len(self.margin_location)])
            self.short_sleep()

    def click_for_cancel_album(self):
        '''
        When opening album, if money is not sufficient,
        a dialog will be displayed, use this to cancel that dialog.
        '''
        for _ in range(3, 6):
            self.adb.tap(self.cancel_album_location)
            self.short_sleep()

    def click_hongbao_and_album(self):
        self.adb.get_screenshot('current_shop.png')
        for i in range(3):
            x = analyse_part_of_image(
                'current_shop.png', self.hongbao_area_location[i])
            red_channel = x[2]
            print('Hongbao {} BGR: '.format(i + 1), list(map(int, x)))
            if red_channel < 160:
                # Why just check red channel instead of green channel?
                # At first, I did so but it seems green channel value is nearly the same
                # between clickable and unclickable hongbao or album
                # So I just check all three channels and found that use red channel instead
                # is feasible. If you know why, plz tell me. Thx!
                print('Hongbao {} is available.'.format(i + 1))
                for _ in range(10):
                    # 10 times is necessary, because sometimes when open a hongbao or album,
                    # number of rewards can be even greater than 5
                    # if times is set lower, when that situation occurs,
                    # you may not be able to navigate to main window (building window)
                    self.adb.tap(self.hongbao_location[i])
                    self.medium_sleep()
                    self.bogo_click()
            else:
                print('Hongbao {} is not available.'.format(i + 1))

            print('')

        x = analyse_part_of_image(
            'current_shop.png', self.album_area_location)
        red_channel = x[2]
        print('Album BGR: ', list(map(int, x)))
        if red_channel < 160:
            # Check red channel instead of green is practicable, already explained about 15 lines above.
            print('Album is available.')
            for _ in range(10):
                # 10 times is necessary, already explained about 15 lines above.
                self.adb.tap(self.album_location)
                self.medium_sleep()
                self.click_for_cancel_album()
        else:
            print('Album is not available.')

    def has_new_hongbao_or_album(self):
        '''
        Check whether there is a red square on bottom "shop" button.
        '''
        self.adb.get_screenshot('temp.png')
        self.medium_sleep()
        x = analyse_part_of_image(
            'temp.png', self.new_hongbao_and_album_prompt_location)
        return is_similar_color(x, self.new_hongbao_and_album_prompt_color)

    def policy_update_available(self):
        # TODO
        return True

    def run(self):
        # Get initial "building window" image for checking similarity later
        self.navigate_to_building()
        self.medium_sleep()
        self.adb.get_screenshot('building.png')

        self.medium_sleep()

        # Get initial "shop window" image for checking similarity later
        self.navigate_to_shop()
        self.medium_sleep()
        self.adb.get_screenshot('shop.png')
        self.medium_sleep()
        while True:
            if self.try_navigating_to_building() == False:
                print('Error when navigating to building windows.')
                break

            self.collect_money()
            self.upgrade_building()

            self.medium_sleep()

            self.try_transporting_goods()

            self.medium_sleep()

            if self.policy_update_available():
                pass
                # TODO

            self.medium_sleep()

            if self.has_new_hongbao_or_album():
                print('Found new hongbao or album.')
                if self.try_navigating_to_shop() == False:
                    print('Error when navigating to shop windows.')
                    break
                self.click_hongbao_and_album()
            else:
                print('No new hongbao or album found.')

            print('Cycle finished. Sleep for some time to start new cycle.')
            self.long_sleep()


if __name__ == '__main__':
    assistor = Assistor()
    assistor.run()
