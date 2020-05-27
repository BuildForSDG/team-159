from .serializers import *
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework.generics import *


class IsLender(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_lender)


class RequestBusinessDataMixin:
    def get_queryset(self):
        """
        Filter the data associated with the current authenticated user
        :return: Business Object
        """
        queryset = Business.objects.filter(owner=self.request.user)
        return queryset


class RequestLenderDataMixin:
    def get_queryset(self):
        """
        Filter the data associated with the current authenticated Lender
        :return: Lender Object
        """
        queryset = Lender.objects.filter(slug=self.request)
        return queryset


class RequestLoanDataMixin:
    def get_queryset(self):
        """
        Filter the data associated with the current authenticated Lender
        :return: Lender Object
        """
        queryset = Lender.objects.filter(slug=self.request)
        return queryset


class SingleBusinessObjectMixin:
    """
    All Objects should have a single instance
    """

    def perform_create(self, serializer):
        """
        Authenticated Customer should have only a single business
        :param serializer:
        :return: Error, Object
        """
        try:
            exists = self.model.objects.get(owner=self.request.user)
        except self.model.DoesNotExist:
            return serializer.save()
        else:
            return self.permission_denied(request=self.request, message="Can only have one business")


class SingleLenderObjectMixin:
    """
    All Objects should have a single instance
    """

    def perform_create(self, serializer):
        """
        Register and Authenticated Lender should be unique
        :param serializer:
        :return: Error, Object
        """
        try:
            exists = self.model.objects.get(owner=self.request.user)
        except self.model.DoesNotExist:
            return serializer.save()
        else:
            return self.permission_denied(request=self.request, message="Can only have one business")


# Business Api
class CreateBusinessView(RequestBusinessDataMixin, SingleBusinessObjectMixin, ListCreateAPIView):
    """
    Create a Business GET, POST
    """
    serializer_class = BusinessSerializer
    model = Business
    permission_classes = (IsAuthenticated,)


class UpdateBusinessView(RequestBusinessDataMixin, RetrieveUpdateAPIView):
    """
    Update Business GET, PUT, PATCH
    """
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = "name"


class DeleteBusinessView(RequestBusinessDataMixin, RetrieveDestroyAPIView):
    """
    Delete a Business GET, DELETE
    """
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    lookup_field = "name"


# Lender Api
class CreateLenderView(RequestLenderDataMixin, SingleLenderObjectMixin, ListCreateAPIView):
    """
    Create a Lender GET, POST
    """
    serializer_class = LenderSerializer
    queryset = Lender.objects.all()
    permission_classes = (IsAuthenticated, IsLender,)
    lookup_field = "name"


class UpdateLenderView(RequestLenderDataMixin, RetrieveUpdateAPIView):
    """
    Update Lender GET, PUT, PATCH
    """
    serializer_class = LenderSerializer
    queryset = Lender.objects.all()
    permission_classes = (IsAuthenticated, IsLender,)


class DeleteLenderView(RequestLenderDataMixin, RetrieveDestroyAPIView):
    """
    Delete Lender GET, DELETE
    """
    serializer_class = LenderSerializer
    queryset = Lender.objects.all()
    permission_classes = (IsAuthenticated, IsLender, IsAdminUser)


# Loan Api
class CreateLoanView(RequestLoanDataMixin, ListCreateAPIView):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    permission_classes = (IsAuthenticated,)


class UpdateLoanView(RequestLoanDataMixin, RetrieveUpdateAPIView):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    permission_classes = (IsAuthenticated,)


class DeleteLoanView(RequestLoanDataMixin, RetrieveDestroyAPIView):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
