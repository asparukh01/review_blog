from django.urls import path
from .views import (
    ReviewListView, 
    ReviewCreateView, 
    ReviewDeleteView, 
    ReviewDetailView, 
    ReviewUpdateView, 
    RejectedListView, 
)

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('rejected/', RejectedListView.as_view(), name='rejected'),
    path('review_create/', ReviewCreateView.as_view(), name='review_create'),
    path('review_detail/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review_update/<int:pk>/', ReviewUpdateView.as_view(), name='review_update'),
    path('review_delete/<int:pk>/', ReviewDeleteView.as_view(), name='review_delete'),
]