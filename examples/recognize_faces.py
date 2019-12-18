''' 
==========================
Recognize faces in 1 image
==========================

In this example, we will demonstrate how wmp-face finds faces in input images,
crop out a face thumbnail and predicts a name
'''

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import detect, utils


def main():
    FACE_COMP_THRES = 0.6
    ENCODED_REF_DIR = "../datasets/reference-encoded"
    NEW_IMG = "../datasets/sample_image.jpg"

    fr = detect.FaceRecognizer(ref_batch)
    fd = detect.FaceDetector(ENCODED_REF_DIR)
    
    img_array = utils.load_image(NEW_IMG)
    unknown_faces = fd.find_faces(img_array)

    predicted_names = [fr.predict_name(f) for f in unknown_faces]
    print(predicted_names)
    # TODO: return comparison matrix
    # TODO: write face thumbnails w/ predicted names

    

if __name__ == "__main__":
    main()
