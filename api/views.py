from django.shortcuts import render
import tensorflow as tf
import tensorflow_hub as hub
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
import os
import numpy as np

fss = FileSystemStorage()


class Flower_Detection_5(APIView):
    def post(self, request):
        try:
            model_path = "api/models/Flower_Detection_5/Flower_Detection_5.h5"
            model = tf.keras.models.load_model(
                model_path, custom_objects={"KerasLayer": hub.KerasLayer}
            )

            files = request.FILES["files"]
            if not os.path.exists("./api/images"):
                os.makedirs("./api/images")
            if not os.path.exists("./api/images/Flower_Detection_5"):
                os.makedirs("./api/images/Flower_Detection_5")
            fss.save("./api/images/Flower_Detection_5/" + files.name, files)

            img = tf.keras.preprocessing.image.load_img(
                "./api/images/Flower_Detection_5/" + files.name, target_size=(224, 224)
            )

            os.remove("./api/images/Flower_Detection_5/" + files.name)

            img_array = tf.keras.preprocessing.image.img_to_array(img)

            img_array = tf.expand_dims(img_array, 0)  # Create batch axis

            predictions = model.predict(img_array)

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
