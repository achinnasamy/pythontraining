from garbagecollection.face_recognition_tensor import FaceRecognitionTensor


import gc as gc

if __name__ == "__main__":


    # Runs the garbage collection
    gc.collect()

    # Provides the list of objects that the collector found to be
    # unreachable and could not be freed.
    gc.garbage

    # Is the garbage collection enabled
    gc.isenabled()


    print (gc.isenabled())


    #FaceRecognitionTensor.INITIALIZE()
    face_recognition_tensor = FaceRecognitionTensor()

    face_recognition_tensor.compute_tensor()

    del face_recognition_tensor


