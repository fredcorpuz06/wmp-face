"""
=====================================
Create FaceBatch for reference images
=====================================

Return face-batch object to compare all new images too + create folder

Input: folder of good portraits of people
Out: face-batch object + create folder

ref_img_dir
    ├───Donald_Trump
    │       _reference.jpg
    │
    ├───Hillary_Clinton
    │       _reference.jpg
    │
    ├───Bernie_Sanders
    │       _reference.jpg
    │
    └───reference_faces_encoded.pickle
            


"""

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import detect, utils
import pickle
import os


def main():
    REF_DIR = "wmp/datasets/reference-portraits"
    OUT_DIR = "wmp/datasets/reference-encoded"

    fd = detect.FaceDetector()

    utils.create_reference_dir(REF_DIR, OUT_DIR)
    utils.add_subdirectory(OUT_DIR, "Unknown", "No_Person")

    portraits = utils.glob(REF_DIR, "[\w]+.jpg")
    reference_images = [detect.FaceImage(p) for p in portraits]
    # assuming only 1 face in each portrait
    encoded_faces = [fd.find_faces(r)[0] for r in reference_images]

    reference_batch = detect.FaceBatch(encoded_faces, is_reference=True)
    pickled_fp = os.path.join(OUT_DIR, "reference_batch.p")

    with open(pickled_fp, "wb") as f:
        pickle.dump(reference_batch, f)


if __name__ == "__main__":
    main()
