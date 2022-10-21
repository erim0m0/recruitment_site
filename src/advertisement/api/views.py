from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .serializers import AdvertisementSerializer
from ..models import Advertisement


# class AdertisementsList(ListAPIView):
    # serializer_class = AdvertisementsListSerializer

class AvertisementApiView(ModelViewSet):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        data_serializer = self.get_serializer(queryset, many=True).data
        print(data_serializer)
        if data_serializer.get("is_show_salary"):
            data_serializer.pop("is_show_salary")
            data_serializer.pop("salary")
        return Response(data_serializer)
