import os
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import cv2


def plot_picture(picture, title='hello'):
	plt.imshow(picture)
	plt.title(title)
	plt.show()	 


def get_contrast_pic(picture, title='contranst'):
	new_picture = 255 - picture
	plot_picture(new_picture, title)
	plt.show()


def log_pic(picture, title='log'):
	picture_1 = picture.astype(float) / 255.
	picture_2 = 3 * np.log(1 + picture_1) 
	picture_2 = (picture_2 * 255).astype(np.uint8)
	plot_picture(picture_2, title)


def main(*args, **kwargs):
	pic_path = 'log.jpg'
	image = plt.imread(pic_path)

	plot_picture(image, 'init')
	log_pic(image)	


if __name__ == '__main__':
	main()
