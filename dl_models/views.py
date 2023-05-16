from rest_framework.views import APIView
from rest_framework.response import Response


class home(APIView):
    def get(self, request):
        return Response(
            data={"message": "Welcome to Deep Learning Models API"}, status=200
        )
