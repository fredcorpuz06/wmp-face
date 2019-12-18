'''
==============================
Generate montage of images
==============================

In this example, we will demonstrate how wmp-face creates a montage from
an input folder of image.

'''

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import utils


def main():
    IN_DIR = "../datasets/sample-dir"
    OUT_DIR = "../data/sample-montage"

    montages = utils.create_montage(IN_DIR, ncol=5)
    utils.write_images(
        montages, folder=OUT_DIR,basename="montage", filetype="jpg")

        
if __name__ == "__main__":
    main()