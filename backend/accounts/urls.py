from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'customers', views.CustomerViewSet, basename='customers')

urlpatterns = router.urls
urlpatterns+= [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]