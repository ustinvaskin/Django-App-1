from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer, PopulatedCatSerializer, PopulatedOwnerSerializer

# Create your views here.
class ListView(APIView):

    def get(self, request):
        cats = Cat.objects.all()
        serializer = PopulatedCatSerializer(cats, many=True)

        return Response(serializer.data)

    def post(self, request):
        cat = CatSerializer(data=request.data)
        if cat.is_valid():
            cat.save()
            return Response(cat.data, status=HTTP_201_CREATED)
        return Response(cat.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

class DetailView(APIView):

    def get(self, request, pk):
        cat = Cat.objects.get(pk=pk)
        serializer = PopulatedCatSerializer(cat)

        return Response(serializer.data)

    def put(self, request, pk):
        cat = Cat.objects.get(pk=pk)
        updated_cat = CatSerializer(cat, data=request.data)
        if (updated_cat.is_valid()):
            updated_cat.save()
            return Response(updated_cat.data)
        return Response(updated_cat.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        cat = Cat.objects.get(pk=pk)
        cat.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class OwnerListView(APIView):

    def get(self, request):
        owners = Owner.objects.all()
        serializer = PopulatedOwnerSerializer(owners, many=True)

        return Response(serializer.data)
