from rest_framework import serializers
from .models import Cat, Owner, Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')

class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ('id', 'name', 'age', 'cats')

class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = ('id', 'name', 'breed', 'image', 'owner', 'tags')
        extra_kwargs = {'tags': {'required': False}}

class PopulatedCatSerializer(CatSerializer):

    owner = OwnerSerializer()
    tags = TagSerializer(many=True)

class PopulatedOwnerSerializer(OwnerSerializer):

    cats = CatSerializer(many=True)