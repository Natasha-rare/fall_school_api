from django.shortcuts import render, HttpResponse
import random

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from . import models, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data["text"]}'})
    return Response({'message': 'Hello world'})


# def index(request):
#     return HttpResponse('Hello world!')
class ItemViewSet(ModelViewSet):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()


class ItemAPIView(APIView):
    serializer_class = serializers.ItemSerializer
    def get(self, request):
        items = models.Item.objects.all()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def item_view(request):
    if request.method == 'GET':
        items = models.Item.objects.all()
        serializer = serializers.ItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# def new_index(request):
#     return render(request, 'myapp/index.html')
#
#
# def some_data(request):
#     array = models.Item.objects.all().values_list()
#     context = {'data': 'Hello world!', 'array': array}
#     return render(request, 'myapp/some_data.html', context)
#
#
# def random_data(request, start, end):
#     random_number = random.randint(int(start), int(end))
#     context = {'random_number': random_number}
#     return render(request, 'myapp/random_data.html', context)
#
#
# def new_instance(request, name, description, price):
#     new_item = models.Item.objects.create(name=name, description=description, price=price)
#     return HttpResponse(f'New item created: {new_item.name}')
#
#
# def update_instance(request, id, name, description, price):
#     item = models.Item.objects.get(id=id)
#     item.name = name
#     item.description = description
#     item.price = price
#     item.save()
#     return HttpResponse(f'Item updated: {item.name}')
#
#
# def delete_instance(request, id):
#     item = models.Item.objects.get(id=id)
#     item.delete()
#     return HttpResponse(f'Item deleted: {item.name}')