.. _recognizing_face_batch_tutorial:

================================
Recognizing faces in large batch
================================

The goal of this guide is to explore some of the main ``wmp-face`` tools on a 
single task: recognizing all the faces in a batch of images

In this tutorial, we will see how to:

  - load all images of your persons-of-interest

  - extract feature vectors of your persons-of-interest and store for future 
    use

  - load all images you want to analyze 

  - perform face detection and recognition on images

  - verify results of face algorithms by hand

Tutorial setup
--------------

To get started with this tutorial, you must first install *wmp-face* and all of 
its required dependencies. We will be using 

Please refer to the :ref:`installation instructions <installation_instructions>`
page for more information and for system-specific instructions. The source of 
this tutorial can be found `on Github
<https://github.com/wmp-face/tree/master/doc/tutorial/recognize_batch>`_.


Loading images of your persons-of-interest
-------------------------------------------

In the following, we will use the built-in dataset loader from wmp-face::

  >>> from wmp.datasets import fetch_referenceportraits
  >>> images_filepaths = fetch_referenceportraits()

The returned object is a list of file paths to our reference portraits::

  >>> images_filepaths
  ['data/ref/Hillary_Clinton.jpg', 'data/ref/Donald_Trump.jpg', ...]

We can now load the list of files into ``FaceImage`` objects which will allow
us to store the image data and eventually all the faces contained in the
image::
  
  >>> images = [detect.FaceImage(i) for i in images_fp]
  >>> images[0].show()

.. image:: ../images/hillary_clinton.jpg
    :width: 120pt



Extracting and storing features of your persons-of-interest
-----------------------------------------------------------

Irure ut laborum mollit proident aute cillum eiusmod eu occaecat::

  >>> fd = detect.FaceDetector()
  >>> images = [fd.find_faces(i).faces[0] for i in images]
  >>> reference_batch = detect.FaceBatch(encoded_faces, is_reference=True)
  >>> with open("data/reference-encoded", "wb") as f:
  >>>     pickle.dump(reference_batch, f)


Output folder structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Irure ut laborum mollit proident aute cillum eiusmod eu occaeca


Loading images for analysis
------------------------------

Irure ut laborum mollit proident aute cillum eiusmod eu occaecat::

  >>> images_fp = utils.glob("data/reference-portraits", "[\w]+.*")
  >>> images = [detect.FaceImage(i) for i in images_fp]

Performing detection and recognition
-----------------------------------------------

Irure ut laborum mollit proident aute cillum eiusmod eu occaecat::

  >>> fr = detect.FaceRecognizer("data/reference-encoded")
  >>> images = [fd.find_faces(i) for i in images]  # list of FaceImages
  >>> images = [fr.predict_names(i) for i in images]

Displaying predicted names 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Irure ut laborum mollit proident aute cillum eiusmod eu occaecat::

  >>> names = [i.retrieve_names() for i in images]

Verifying results of face algorithms
-------------------------------------------

Irure ut laborum mollit proident aute cillum eiusmod eu occaecat::

  >>> fr.write_validation(images, VALIDATION_DIR)

Verification folder structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Irure ut laborum mollit proident aute cillum eiusmod eu occaeca
