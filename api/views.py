import json

from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Review
from .serializer import ReviewSerializer, ReviewPublicationSerializer


class ReviewDeleteApiView(APIView):
    def delete(self, **kwargs):
        objects = get_object_or_404(Review, pk=kwargs.get('pk'))
        objects.delete()
        return Response({"status": "success", "data": objects.pk})


class ReviewPublicationView(APIView):

    def patch(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        data = json.loads(self.request.body)
        serializer = ReviewPublicationSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
