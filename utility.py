import random
from PIL import Image, ImageChops
import numpy as np
import cv2


def randomize_offset(base, bias=10):
    '''
    add or sub a integer randomly
    '''
    return base + random.randint(-1 * bias, bias)


def randomize_scale(base, bias=0.3):
    '''
    scale randomly
    '''
    return base * random.uniform(1 - bias, 1 + bias)


def shuffle_list(x):
    return random.sample(x, len(x))


def calc_image_similarity(image_one, image_two):
    im1 = Image.open(image_one)
    im2 = Image.open(image_two)
    diff = np.asarray(ImageChops.difference(im1, im2))
    similarity = 1 - np.count_nonzero(diff) / diff.size
    # print('{} and {} similarity {}'.format(image_one, image_two, similarity))
    return similarity


def analyse_part_of_image(image, area):
    '''
    return avarage color of specified part of the image.
    image: a string which is image's filename (with path if not in current dir)
    area: [(x0,y0),(x1,y1)]
    Pay attention: x, y in cv2 is converse. And RGB changes to BGR
    '''
    img = cv2.imread(image)
    region = img[area[0][1]:area[1][1], area[0][0]:area[1][0]]
    # cv2.imshow('image',region)
    # cv2.waitKey(0)
    avg_color_per_row = np.average(region, axis=0)
    avg_color = list(np.average(avg_color_per_row, axis=0))
    # print('{} average: R: {}\tG:{}\tB:{}'.format(image, *avg_color[::-1]))
    return avg_color


def is_similar_color(color_one, color_two, bias=20):
    for i in range(3):
        if abs(color_one[i] - color_two[i]) > bias:
            return False
    return True
