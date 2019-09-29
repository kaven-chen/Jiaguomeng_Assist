import random
from PIL import Image, ImageChops
import numpy as np


def randomize_offset(base, bias=10):
    return base + random.randint(-1 * bias, bias)


def randomize_scale(base, bias=0.3):
    return base * random.uniform(1 - bias, 1 + bias)


def shuffle_list(x):
    return random.sample(x, len(x))


def calc_image_similarity(image_one, image_two):
    im1 = Image.open(image_one)
    im2 = Image.open(image_two)
    diff = np.asarray(ImageChops.difference(im1, im2))
    similarity = 1 - np.count_nonzero(diff) / diff.size
    print('{} and {} similarity {}'.format(image_one, image_two, similarity))
    return similarity
