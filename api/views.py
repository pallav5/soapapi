from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import DjangoObjectPermissions
from sector.models import Sector



from .serializers import SectorSerializer



class SectorView(viewsets.ModelViewSet):

    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


