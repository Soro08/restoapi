from rest_framework import serializers

from .models import *


class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class SpecialiteSerializer(serializers.ModelSerializer):
    platspecial = PlatSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Specialite
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    platcateg = PlatSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Categorie
        fields = '__all__'
