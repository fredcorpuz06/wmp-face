.. recognize_faces_batch:

==================================
Recognize faces in batch of images
==================================

::

    """
    In this example, we will demonstrate how wmp-face finds faces in input 
    images,crops out a face thumbnail and places the thumbnails into a 
    folder with the matching reference image.


    Returns:
        folders of face thumbnails: Donald_Trump/13424_5_20.jpg, 
        Hillary_Clinton/1341_20_10.jpg
        Unknown: Unknown/13415235_50_19.jpg
        No_Person: No_Person/134415.jpg

        comparison_matrix.csv


    """

    # Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

    from wmp import detect, utils
    import pandas as pd


    def main():
        FACE_COMP_THRES = 0.6
        ENCODED_REF_DIR = "wmp/datasets/reference-encoded"
        UNKNOWNS_DIR = "wmp/datasets/facebook-ad-images"
        VALIDATION_DIR = "wmp/datasets/sample-batch"

        fd = detect.FaceDetector()
        fr = detect.FaceRecognizer(ENCODED_REF_DIR)

        img_locs = utils.glob(UNKNOWNS_DIR, "[\w]+.*")
        images = [detect.FaceImage(i) for i in img_locs]

        # can be multiple faces per image
        images = [fd.find_faces(i) for i in images]  # list of FaceImages
        images = [fr.predict_names(i) for i in images]

        names = [i.retrieve_names() for i in images]
        fr.write_validation(images, VALIDATION_DIR)



    if __name__ == "__main__":
        main()
