.. _verifying_face_results:

================================
Manually verifying facial recognition results
================================

The goal of this guide is to explore some of the main ``wmp-face`` tools on a 
single task: recognizing all the faces in a batch of images

In this tutorial, we will see how to:

  - move images to correct classification

  - compare predictions to validated set



Tutorial setup
--------------

To get started with this tutorial, you must first install *wmp-face* and all of 
its required dependencies. 

Please refer to the :ref:`installation instructions <installation_instructions>`

Irure ut laborum mollit proident aute cillum eiusmod eu occaecat::

  >>> from wmp import detect, utils



Moving images to correct classification
---------------------------------

Irure ut laborum mollit proident aute cillum eiusmod eu occaecat::

  >>> fd = detect.FaceDetector()
  >>> images_fp = utils.glob("data/reference-portraits", "[\w]+.jpg")
  >>> images = [detect.FaceImage(i) for i in images_fp]

Output folder structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comparing predictions to validated set
-----------------------------------

Irure ut laborum mollit proident aute cillum eiusmod eu occaecat::

  >>> images = [fd.find_faces(i).faces[0] for i in images]
  >>> reference_batch = detect.FaceBatch(encoded_faces, is_reference=True)
  >>> with open("data/reference-encoded", "wb") as f:
  >>>     pickle.dump(reference_batch, f)





