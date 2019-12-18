'''
==================================
Recognize faces in batch of images
==================================

In this example, we will demonstrate how wmp-face finds faces in input images,
crops out a face thumbnail and places the thumbnails into a folder with the 
matching reference image.


Returns:
    folders of face thumbnails: Donald_Trump/13424_5_20.jpg, Hillary_Clinton/1341_20_10.jpg
    Unknown: Unknown/13415235_50_19.jpg
    No_Person: No_Person/134415.jpg

    comparison_matrix.csv


'''

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import detect, utils
from wmp.detect import FaceImage

def main():
    FACE_COMP_THRES = 0.6
    BATCH_SIZE = 50
    ENCODED_REF_DIR = "../datasets/reference-encoded"
    UNKNOWNS_DIR = "../datasets/facebook-ad-images"

    fd = detect.FaceDetector()
    fr = detect.FaceRecognizer(ENCODED_REF_DIR)


    img_locs = utils.glob(UNKNOWNS_DIR, "*.jpg")
    img_arrays = [FaceImage(i) for i in img_locs]
    # can be multiple faces per image
    img_results = [fd.find_faces(i) for i in img_arrays]
    img_results_named = [
        fr.predict_name(face) for face in img.faces for img in img_results]
    
    # Write thumbnail to correct folder, No_Person, Unknown
    # _ = [fv.write_predictions(i) for i in img_results_named]

    # utils.write(comp_matrix, "comparison_matrix.csv")



if __name__ == "__main__":
    main()
    
