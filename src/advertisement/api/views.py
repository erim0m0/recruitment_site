from typing import Dict

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .serializers import AdvertisementsListSerializer,AdvertisementSerializer
from ..models import Advertisement
from permissions import IsFounderOrStaff


# class AdertisementsList(ListAPIView):
#     serializer_class = AdvertisementsListSerializer
#     queryset = Advertisement.objects.all()
#     # TODO: Edit Permission class
# permission_classes =

class AdertisementsList(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = AdvertisementsListSerializer
    filterset_fields = [
        "title",
        "city",
        "company"
    ]

    # TODO: add a feature for is_known field from company's profile
    def get_queryset(self):
        queryset = Advertisement.objects.values(
            "title", "city", "company__name"
        )
        return queryset

class AdvertisementAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [IsFounderOrStaff]

    def get_object(self):
        obj = get_object_or_404(
            Advertisement.objects.select_related("company"),
            pk = self.kwargs["pk"]
        )
        self.check_object_permissions(self.request, obj)
        return obj
    def show_data(self) -> Dict:
        instance = self.get_object()
        company_field = instance.company

        serializer = self.get_serializer(instance)
        serializer_data: Dict = serializer.data
        serializer_data["company"] = company_field.name
        return serializer_data
    def retrieve(self, request, *args, **kwargs):
        result: Dict = self.show_data()
        return Response(
            result,
            status=status.HTTP_200_OK
        )


# class AvertisementApiView(ModelViewSet):
#     serializer_class = AdvertisementSerializer
#     queryset = Advertisement.objects.all()
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         data_serializer = self.get_serializer(queryset, many=True).data
#         print(data_serializer)
#         if data_serializer.get("is_show_salary"):
#             data_serializer.pop("is_show_salary")
#             data_serializer.pop("salary")
#         return Response(data_serializer)
