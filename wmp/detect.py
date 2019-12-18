class Face:
    def __init__(self):
        self.thumbnail_data = None
        self.encoding = None
        self.landmarks = None
        self.box = None
        self.source = FaceImage()
        self.name = None

class FaceImage:
    def __init__(self):
        self.image_data = None
        self.source_name = None
        self.faces = []


class FaceBatch:
    def __init__(self):
        self.batch_faces = []




class FaceDetector:
    def __init__(self):
        pass

    def find_faces(self):
        pass

class FaceRecognizer(FaceBatch):
    def __init__(self):
        self.comparison_matrix = None

    def predict_name(self):
        pass

    def predict_names(self):
        pass
    


class FaceValidator:
    def __init__(self):
        pass

    def write_prediction(self):
        pass
