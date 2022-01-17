from django.http.response import Http404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


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

    @swagger_auto_schema(
        responses={
            200: openapi.Response("Successful GET-LIST Request"),
            400: openapi.Response("Unprocessable Entity"),
        },
    )
    def list(self, request):
        cars = Cars.objects.all()
        serializer = CarSerializer(cars, many=True)

        output = {"details": "Successful GET-LIST Request", "output": serializer.data}

        return Response(output, status=status.HTTP_200_OK)

    """
    Create car
    """

    @swagger_auto_schema(
        responses={
            201: openapi.Response("Successful POST Request"),
            400: openapi.Response("Unprocessable Entity"),
        },
        request_body=CarSerializer,
    )
    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            output = {"details": "Successful POST Request", "output": serializer.data}

            return Response(output, status=status.HTTP_201_CREATED)

        output = {"details": "Failed POST Request", "output": serializer.errors}

        return Response(output, status=status.HTTP_400_BAD_REQUEST)

    """
    Get object
    """

    @swagger_auto_schema(
        responses={
            200: openapi.Response("Successful GET Request"),
            404: openapi.Response("Entity Not Found"),
        },
        manual_parameters=[
            openapi.Parameter(name="id", in_="path", type=openapi.TYPE_INTEGER),
        ],
    )
    def retrieve(self, request, pk=None):
        car = self.get_object(pk=pk)
        serializer = CarSerializer(car)

        output = {"details": "Successful GET Request", "output": serializer.data}

        return Response(output, status=status.HTTP_200_OK)

    """
    Update object
    """

    @swagger_auto_schema(
        responses={
            200: openapi.Response("Successful PUT Request"),
            400: openapi.Response("Unprocessable Entity"),
            404: openapi.Response("Entity Not Found"),
        },
        manual_parameters=[
            openapi.Parameter(name="id", in_="path", type=openapi.TYPE_INTEGER),
        ],
        request_body=CarSerializer,
    )
    def update(self, request, pk=None):
        car = self.get_object(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()

            output = {"details": "Successful PUT Request", "output": serializer.data}

            return Response(output, status=status.HTTP_200_OK)

        output = {"details": "Unsuccessful PUT Request", "output": serializer.errors}

        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)

    """
    Delete object
    """

    @swagger_auto_schema(
        responses={
            204: openapi.Response("Successful Delete Request"),
            404: openapi.Response("Entity Not Found"),
        },
        manual_parameters=[
            openapi.Parameter(name="id", in_="path", type=openapi.TYPE_INTEGER),
        ],
    )
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

    @swagger_auto_schema(
        responses={
            200: openapi.Response("Successful GET-LIST Request"),
            400: openapi.Response("Unprocessable Entity"),
        },
    )
    def list(self, request):
        trucks = Trucks.objects.all()
        serializer = TruckSerializer(trucks, many=True)

        output = {"details": "Successful GET-LIST Request", "output": serializer.data}

        return Response(output, status=status.HTTP_200_OK)

    """
    Create truck
    """

    @swagger_auto_schema(
        responses={
            201: openapi.Response("Successful POST Request"),
            400: openapi.Response("Unprocessable Entity"),
        },
        request_body=TruckSerializer,
    )
    def create(self, request):
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            output = {"details": "Successful POST Request", "output": serializer.data}

            return Response(output, status=status.HTTP_201_CREATED)

        output = {"details": "Unsuccessful POST Request", "output": serializer.errors}

        return Response(output, status=status.HTTP_400_BAD_REQUEST)

    """
    Get object
    """

    @swagger_auto_schema(
        responses={
            200: openapi.Response("Successful GET Request"),
            404: openapi.Response("Entity Not Found"),
        },
        manual_parameters=[
            openapi.Parameter(name="id", in_="path", type=openapi.TYPE_INTEGER),
        ],
    )
    def retrieve(self, request, pk=None):
        truck = self.get_object(pk=pk)
        serializer = TruckSerializer(truck)

        output = {"details": "Successful GET Request", "output": serializer.data}

        return Response(output, status=status.HTTP_200_OK)

    """
    Update object
    """

    @swagger_auto_schema(
        responses={
            200: openapi.Response("Successful PUT Request"),
            400: openapi.Response("Unprocessable Entity"),
            404: openapi.Response("Entity Not Found"),
        },
        manual_parameters=[
            openapi.Parameter(name="id", in_="path", type=openapi.TYPE_INTEGER),
        ],
        request_body=TruckSerializer,
    )
    def update(self, request, pk=None):
        truck = self.get_object(pk=pk)
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()

            output = {"details": "Successful PUT Request", "output": serializer.data}

            return Response(output, status=status.HTTP_200_OK)

        output = {"details": "Successful PUT Request", "output": serializer.errors}

        return Response(output, status=status.HTTP_400_BAD_REQUEST)

    """
    Delete object
    """

    @swagger_auto_schema(
        responses={
            204: openapi.Response("Successful Delete Request"),
            404: openapi.Response("Entity Not Found"),
        },
        manual_parameters=[
            openapi.Parameter(name="id", in_="path", type=openapi.TYPE_INTEGER),
        ],
    )
    def destroy(self, request, pk=None):
        truck = self.get_object(pk=pk)
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
