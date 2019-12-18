'''
================
Draw facemarks
================

In this example, we will demonstrate how wmp-face finds faces in input 
images, crops out a face thumbnail and draws "facemarks"

'''

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import detect, utils



def main():
    IMG = "../datasets/sample_image.jpg"
    OUT_DIR = "../datasets/sample-facemarks/"
    img_array = utils.load_image(IMG)
    
    fd = detect.FaceDetector() # can be different detectors
    unknown_faces = fd.find_faces(img_array)

    cropped_faces = [f.image_data for f in unknown_faces]
    marked_faces = [f.draw_landmarks() for f in unknown_faces]

    utils.write_images(
        cropped_faces, folder=OUT_DIR, basename="face_thumbnails", 
        filetype="jpg")

    utils.write_images(
        cropped_faces, folder=OUT_DIR, basename="facemarks", filetype="jpg")

if __name__ == "__main__":
    main()
