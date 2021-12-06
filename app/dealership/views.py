import re
from django.http.response import Http404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import CarSerializer, TruckSerializer
from .models import Cars, Trucks
class CarViewSet(ViewSet):
    # queryset = Cars.objects.all()
    # serializer_class = CarSerializer()

    """
    Get object with PK
    """
    def get_object(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404

    """
    List all cars
    """
    def list(self, request):
        cars = Cars.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Create car
    """
    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Get object
    """
    def retrieve(self, request, pk=None):
        car = self.get_object(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    """
    Update object
    """
    def update(self, request, pk=None):
        car = self.get_object(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """
    Delete object
    """
    def destroy(self, request, pk=None):
        car = self.get_object(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TruckViewSet(ViewSet):
    """
    Get object with PK
    """
    def get_object(self, pk):
        try:
            return Trucks.objects.get(pk=pk)
        except Trucks.DoesNotExist:
            return Http404
    """
    List all trucks
    """
    def list(self, request):
        trucks = Trucks.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Create truck
    """
    def create(self, request):
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Get object
    """
    def retrieve(self, request, pk=None):
        truck = self.get_object(pk=pk)
        serializer = TruckSerializer(truck)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Update object
    """
    def update(self, request, pk=None):
        truck = self.get_object(pk=pk)
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Delete object
    """
    def destroy(self, request, pk=None):
        truck = self.get_object(pk=pk)
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)