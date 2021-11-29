import re
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CarSerializer, TruckSerializer
from .models import Cars, Trucks

class CarView(APIView):
    """
    List all cars
    """
    def get(self, request, format=None):
        cars = Cars.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Create new car
    """
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(APIView):
    """
    Get object with PK
    """
    def get_object(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404

    """
    Get object
    """
    def get(self, request, pk, format=None):
        car = self.get_object(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Update object
    """
    def put(self, request, pk, format=None):
        car = self.get_object(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Delete object
    """
    def delete(self, request, pk, format=None):
        car = self.get_object(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TruckView(APIView):
    """
    List all trucks
    """
    def get(self, request, format=None):
        trucks = Trucks.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Create new truck
    """
    def post(self, request, format=None):
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TruckDetail(APIView):
    """
    Get object with PK
    """
    def get_object(self, pk):
        try:
            return Trucks.objects.get(pk=pk)
        except Trucks.DoesNotExist:
            return Http404

    """
    Get object
    """
    def get(self, request, pk, format=None):
        truck = self.get_object(pk=pk)
        serializer = TruckSerializer(truck)
        return Response(serializer.data, status=status.HTTP_200_OK)


    """
    Update object
    """
    def put(self, request, pk, format=None):
        truck = self.get_object(pk=pk)
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Delete object
    """
    def delete(self, request, pk, format=None):
        truck = self.get_object(pk=pk)
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
