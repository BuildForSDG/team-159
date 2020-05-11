from django.urls import path
from rest_framework import routers
from .views import (
    NewBusiness,
    UserViewSet,
    UpdateBusiness,
    DeleteBusiness,
    BusinessViewSet,
    BusinessDetail,
    AllBusiness
)

app_name = "accounts"

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register("businesses", BusinessViewSet)

urlpatterns = [
    path("new", NewBusiness.as_view(), name="new"),
    path("update/<int:pk>", UpdateBusiness.as_view(), name="update"),
    path("delete/<int:pk>", DeleteBusiness.as_view(), name="delete"),
    path("details/<int:pk>", BusinessDetail.as_view(), name="read"),
    path("details", AllBusiness.as_view(), name="all")
]

urlpatterns += router.urls
