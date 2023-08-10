from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import ProfileUpdateView, LogoutViewApi
from .views import LoginView, LogoutView, RegisterView, AccountDetailView, AccountListView, AccountUpdateView

account_url = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/<int:pk>/', AccountDetailView.as_view(), name='profile'),
    path('account/update/<int:pk>/', AccountUpdateView.as_view(), name='profile_update'),
    path('account/list/', AccountListView.as_view(), name='users'),
]

account_api_url = [
    path('login_api/', obtain_auth_token, name='api_token_auth'),
    path('logout_api/', LogoutViewApi.as_view(), name='api_token_delete'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update_api'),
]

urlpatterns = account_url
urlpatterns += account_api_url
