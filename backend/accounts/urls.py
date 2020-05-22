from django.conf.urls import url, include
from django.urls import path
from .views import UserList, UserDetail

#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)


urlpatterns = [
    # path(/api)
    path('api/users_list/', UserList.as_view(), name='user_list'),  # save, fetch users
    path('api/users_list/<National_ID>/', UserDetail.as_view(), name='user_list'),
    # fetch user info where National_ID is specified.
]
