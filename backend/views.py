from django.shortcuts import render
from .serializers import ApplicationSerializer
from rest_framework.views import APIView
from django.http import JsonResponse

class ApplicationView(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)
