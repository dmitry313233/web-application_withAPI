from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from electronics_sales.models import Factory, RetailNetwork, IndividualEntrepreneur
from electronics_sales.permissions import IsActivePermission
from electronics_sales.serializers import FactorySerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer
from electronics_sales.service import FactoryFilter, RetailNetworkFilter, IndividualEntrepreneurFilter


class FactoryCreateListAPIView(generics.ListCreateAPIView):
    """Создание и просмотр завода"""
    serializer_class = FactorySerializer
    permission_classes = [IsActivePermission]
    queryset = Factory.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FactoryFilter


class FactoryView(RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление завода """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActivePermission]


class RetailNetworkCreateListAPIView(generics.ListCreateAPIView):
    """Создание и просмотр розничной сети"""
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsActivePermission]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RetailNetworkFilter


class RetailNetworkView(RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление розничной сети"""
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsActivePermission]


class IndividualEntrepreneurCreateListAPIView(generics.ListCreateAPIView):
    """Создание и просмотр индивидуального предпринимателя"""
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsActivePermission]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IndividualEntrepreneurFilter


class IndividualEntrepreneurView(RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление индивидуального предпринимателя"""
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsActivePermission]
