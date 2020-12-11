from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from announce.models import Announce
from announce.serializer import AnnounceListSerializer, AnnounceDetailSerializer


class AnnounceListView(ListAPIView):
     queryset = Announce.objects.all()
     serializer_class = AnnounceListSerializer

class AnnounceDetailView(RetrieveAPIView):
     queryset = Announce.objects.all()
     serializer_class = AnnounceDetailSerializer
     lookup_field = 'pk'