from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import UserList, UserDetail


urlpatterns = [
    # path('api/users_list/', UserList.as_view(), name='register'),
    path('api/register', UserList.as_view(), name='register'),# save, fetch users
    path('api/register/<National_ID>', UserDetail.as_view(), name='register'),# fetch user info where National_ID is specified.
    path('api/login/refresh/', TokenRefreshView.as_view()),
    path('api/login', TokenObtainPairView.as_view()),
    # path('api-auth/', include('rest_framework.urls')),

]
