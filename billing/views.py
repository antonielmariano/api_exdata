from rest_framework import generics
from billing.models import Billing
from rest_framework.views import APIView, Response, status, Request
from .serializers import BillingSerializer, BillingValueQuantitySerializer
from sqlalchemy import create_engine
import pandas as pd
import math


class BillingView(APIView):
    def post(self, request: Request) -> Response:
        file = pd.read_excel(request.FILES['table'])
        arr = []
        for item in file.values:
            dict_1 = {
                "client_code" : item[0],
                "category_product" : item[1],
                "sku_product" : item[2],
                "date" : item[3],
                "quantity" : item[4],
                "value_billing" : item[5]
            }
            arr.append(
                Billing(**dict_1)
            )
        Billing.objects.bulk_create(arr)
        return Response("Enviado e salvo com sucesso", status.HTTP_201_CREATED)
        
class BillingAllVIew(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer


class BillingByDateView(generics.ListAPIView):
    serializer_class = BillingValueQuantitySerializer

    def get_queryset(self):
        month = self.kwargs["month"]

        if month:
            queryset = Billing.objects.filter(date__gte=f'2022-{month}-1')
            return queryset

class BillingByClientView(generics.ListAPIView):
    serializer_class = BillingValueQuantitySerializer

    def get_queryset(self):
        client = self.kwargs["client"]

        if client:
            queryset = Billing.objects.filter(client_code=client)
            return queryset

class BillingByCategoryView(generics.ListAPIView):
    serializer_class = BillingValueQuantitySerializer

    def get_queryset(self):
        category = self.kwargs["category"]

        if category:
            queryset = Billing.objects.filter(category_product=category)
            return queryset

class BillingByProductView(generics.ListAPIView):
    serializer_class = BillingValueQuantitySerializer

    def get_queryset(self):
        product = self.kwargs["product"]

        if product:
            queryset = Billing.objects.filter(sku_product=product)
            return queryset


class BillingByQuarterlyView(generics.ListAPIView):
    serializer_class = BillingSerializer

    def get_queryset(self):
        quarter_1 = [1, 2, 3]
        quarter_2 = [4, 5, 6]
        quarter_3 = [7, 8, 9]
        quarter_4 = [10, 11, 12]
        quarter = self.kwargs["quarter"]
        current_quarter = []

        if quarter == 1:
            current_quarter = quarter_1
        if quarter == 2:
            current_quarter = quarter_2
        if quarter == 3:
            current_quarter = quarter_3
        if quarter == 4:
            current_quarter = quarter_4
  
        queryset = Billing.objects.filter(date__month__in=current_quarter)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        value = 0
        quantity = 0
        for item in serializer.data:
            value += float(item['value_billing'])
            quantity += int(item['quantity'])
        result = {
            'Valor': value,
            'Quantidade': quantity
        }

        return Response(result)
