from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import FundoImobiliarioSerializer
from .models import FundoImobiliario
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    queryset = FundoImobiliario.objects.all()
    serializer_class = FundoImobiliarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
    filterset_fields = ['codigo','setor']
    search_fields = ['codigo','setor']
    ordering = ['-dividend_yield_medio_12m']
    ordering_fields = [
        'dividend_yield_medio_12m',
        'setor',
        'vacancia_financeira',
        'vacancia_fisica',
        'quantidade_ativos'
    ]
    