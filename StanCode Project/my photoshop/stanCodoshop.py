"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    pix_red = pixel.red
    pix_green = pixel.green
    pix_blue = pixel.blue
    avg_red = red
    avg_green = green
    avg_blue = blue

    red_dist = (avg_red - pix_red) ** 2
    green_dist = (avg_green - pix_green) ** 2
    blue_dist = (avg_blue - pix_blue) ** 2

    color_dist = (red_dist + green_dist + blue_dist) ** 0.5

    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """

    rgb = []
    red_pixel = 0
    blue_pixel = 0
    green_pixel = 0
    for pixel in pixels:
        red_pixel += pixel.red
        green_pixel += pixel.green
        blue_pixel += pixel.blue
    avg_red = int(red_pixel/len(pixels))
    rgb.append(avg_red)
    avg_green = int(green_pixel/len(pixels))
    rgb.append(avg_green)
    avg_blue = int(blue_pixel/len(pixels))
    rgb.append(avg_blue)

    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """


    minimum = 0
    for pixel in pixels:
        avg_list = get_average(pixels)  # get a list of pixel's avg rgb
        red_avg = avg_list[0]
        green_avg = avg_list[1]
        blue_avg = avg_list[2]
        dist = get_pixel_dist(pixel, red_avg, green_avg, blue_avg) # get distance btw pixel and avg rgb
        if minimum == 0:
            minimum += dist
            best_pixel = pixel # need to assign best_pixel here cause the first pixel might be it
        elif dist < minimum : # find the smallest distance
            minimum = dist
            best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for i in range(width):
        for j in range(height):
            pix_list = [] # pix_list need to renew everytime when getting a new (x,y) location
            for image in images:
                img_pix = image.get_pixel(i, j)
                pix_list.append(img_pix)
            best_pix = get_best_pixel(pix_list) # get best pixel among all img
            result_pix = result.get_pixel(i, j)
            result_pix.red = best_pix.red
            result_pix.green = best_pix.green
            result_pix.blue = best_pix.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
