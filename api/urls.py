from django.urls import path

from .views import (
    ReviewDeleteApiView,
    ReviewPublicationView,)

review_url = [
    path('review/delete/<int:pk>/', ReviewDeleteApiView.as_view(), name='review_delete_api'),
    path('review/<int:pk>/publication/', ReviewPublicationView.as_view(),
         name='review_publication'),
]

urlpatterns = review_url
