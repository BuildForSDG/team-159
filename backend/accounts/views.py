from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView, ListView,
)
from rest_framework import viewsets
from .models import (
    User,
    Business,
)
from .forms import BusinessForm
from .serializers import (
    UserSerializer,
    BusinessSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class NewBusiness(LoginRequiredMixin, CreateView):
    model = Business
    form_class = BusinessForm
    template_name = "accounts/new.html"
    success_url = "/"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            return super().form_valid(form)


class BusinessDetail(DetailView):
    model = Business
    template_name = "accounts/detail.html"


class UpdateBusiness(LoginRequiredMixin, UpdateView):
    model = Business
    success_url = "/"
    form_class = BusinessForm
    template_name = "accounts/new.html"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            return super().form_valid(form)


class DeleteBusiness(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Business
    success_url = "/"

    def test_func(self):
        if self.request.user.is_authenticated:
            return True
        return False


class AllBusiness(ListView):
    model = Business
    context_object_name = "business"
    template_name = "accounts/all.html"
