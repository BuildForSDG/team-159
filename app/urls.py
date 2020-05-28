from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = "app"

urlpatterns = [
    path("users", CreateLoanView.as_view(), name="add-user"),
    path("user/update/<str:first_name>", UpdateLoanView.as_view(), name="update-user"),
    path("user/delete/<str:first_name>", DeleteLoanView.as_view(), name="delete-user"),
    path("business", CreateBusinessView.as_view(), name="add-business"),
    path("business/update/<str:name>", UpdateBusinessView.as_view(), name="update-business"),
    path("business/delete/<str:name>", DeleteBusinessView.as_view(), name="delete-business"),
    path("lender", CreateLenderView.as_view(), name="add-lender"),
    path("lender/update/<str:name>", UpdateLenderView.as_view(), name="update-lender"),
    path("lender/delete/<str:name>", DeleteLenderView.as_view(), name="delete-lender"),
    path("loan", CreateLoanView.as_view(), name="add-loan"),
    path("loan/update/<str:customer>", UpdateLoanView.as_view(), name="update-loan"),
    path("loan/delete/<str:customer>", DeleteLoanView.as_view(), name="delete-loan"),
    path("investor", CreateLoanView.as_view(), name="add-investor"),
    path("investor/update/<str:first_name>", UpdateLoanView.as_view(), name="update-investor"),
    path("investor/delete/<str:first_name>", DeleteLoanView.as_view(), name="delete-investor"),
    path("api/token", obtain_auth_token, name="obtain-token"),
    path("rest_auth/", include("rest_auth.urls"))
]
