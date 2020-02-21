"""
================
Draw facemarks
================

In this example, we will demonstrate how wmp-face finds faces in input 
images, crops out a face thumbnail and draws "facemarks"

"""

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import detect, utils


def main():
    IMG = "wmp/datasets/sample_image.jpg"
    OUT_DIR = "wmp/datasets/sample-facemarks/"

    fd = detect.FaceDetector()  # can be different detectors

    face_image = detect.FaceImage(IMG)
    unknown_faces = fd.find_faces(face_image)

    cropped_faces = [f.thumbnail_image for f in unknown_faces]
    marked_faces = [f.draw_landmarks() for f in unknown_faces]

    utils.write_images(
        cropped_faces, folder=OUT_DIR, basename="face_thumbnails", filetype="jpg"
    )

    utils.write_images(
        cropped_faces, folder=OUT_DIR, basename="facemarks", filetype="jpg"
    )


if __name__ == "__main__":
    main()
