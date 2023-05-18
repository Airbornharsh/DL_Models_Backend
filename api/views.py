# from rest_framework.
import tensorflow as tf
import tensorflow_hub as hub
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
import os
import numpy as np
from PIL import Image
import cv2

fss = FileSystemStorage()


class Flower_Detection_5(APIView):
    def post(self, request):
        try:
            model_path = "api/models/Flower_Detection_5/Flower_Detection_5.h5"
            model = tf.keras.models.load_model(
                model_path, custom_objects={"KerasLayer": hub.KerasLayer}
            )
            print(request.FILES)

            files = request.FILES["files"]

            if not os.path.exists("./api/images"):
                os.makedirs("./api/images")
            if not os.path.exists("./api/images/Flower_Detection_5"):
                os.makedirs("./api/images/Flower_Detection_5")
            fss.save("./api/images/Flower_Detection_5/" + files.name, files)

            img = Image.open("./api/images/Flower_Detection_5/" + files.name)

            os.remove("./api/images/Flower_Detection_5/" + files.name)

            img = img.resize((224, 224))
            new_img = np.asarray(img) / 255.0

            predictions = model.predict(new_img.reshape(1, 224, 224, 3))

            prediction = np.argmax(predictions)
            prediction_name = ""

            if prediction == 0:
                prediction_name = "Lilly"
            elif prediction == 1:
                prediction_name = "Lotus"
            elif prediction == 2:
                prediction_name = "Orchid"
            elif prediction == 3:
                prediction_name = "Sunflower"
            elif prediction == 4:
                prediction_name = "Tulip"
            else:
                prediction_name = "Unknown"

            return Response(
                data={"message": "Flower is " + prediction_name}, status=200
            )
        except Exception as e:
            print(e)
            return Response(data={"message": "error"}, status=400)


class Face_Expression_Detection(APIView):
    def post(self, request):
        def get_emotion(index):
            if index == 0:
                return "angry"
            elif index == 1:
                return "disgust"
            elif index == 2:
                return "fear"
            elif index == 3:
                return "happy"
            elif index == 4:
                return "neutral"
            elif index == 5:
                return "sad"
            else:
                return "surprise"

        try:
            model_path = "api/models/Face_Expression_Detection/face_expression-v1.h5"
            model = tf.keras.models.load_model(
                model_path, custom_objects={"KerasLayer": hub.KerasLayer}
            )
            print(request.FILES)

            files = request.FILES["files"]

            folder_location = "./api/images/Face_Expression_Detection/"
            file_location = folder_location + files.name

            if not os.path.exists("./api/images"):
                os.makedirs("./api/images")
            if not os.path.exists(folder_location):
                os.makedirs(folder_location)
            fss.save(file_location, files)

            img = cv2.imread(file_location, cv2.IMREAD_GRAYSCALE)

            os.remove(file_location)

            img = cv2.resize(img, (48, 48))
            new_img = np.asarray(img) / 255.0

            predictions = model.predict(new_img.reshape(1, 48, 48, 1))

            prediction = np.argmax(predictions)

            return Response(
                data={"message": "Emotion is " + get_emotion(prediction)}, status=200
            )
        except Exception as e:
            print(e)
            return Response(data={"message": "error"}, status=400)
