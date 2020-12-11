from rest_framework import serializers
from announce.models import Announce

class AnnounceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announce
        fields = '__all__'

class AnnounceListSerializer(serializers.ModelSerializer):
    production_year = serializers.DateField(format='%Y')
    class Meta:
        model = Announce
        fields = ('id','name','price','production_year')

