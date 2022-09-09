from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET', 'POST'])
def countries_list(request):
    if request.method == 'GET':
        countries = countries.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            countries = countries.filter(name__icontains=name)

        countries_serailizer = CountriesSerializer(countries, many = True)
        return JsonResponse(countries_serailizer.data, safe = False)

    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serailizer = CountriesSerializer(data=countries_data)
        if countries_serailizer.is_valid():
            countries_serailizer.save()
            return JsonResponse(countries_serailizer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serailizer.errors, status = status.HTTPS_400_BAD_REQUEST)

@api_view(['GET', 'POST', "DELETE"])
def countries_details(request, pk):
    try:
        countries = countries.objects.get(pk-pk)
    except Countries.DoesNotExist:
        return JsonResponse({'message': 'The country does not exist'}, status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        countries_serailizer = CountriesSerializer(countries)
        return JsonResponse(countries_serializer.data)

    elif request.method =='PUT':
        countries_data = JSONParser().parse(request)
        countries_serailizer = CountriesSerializer(countries, data = countries_data)
        if countries_serailizer.is_valid():
            countries_serailizer.save()
            return  JsonResponse(countries_serailizer.data)
        return JsonResponse(countries_serailizer.errors, status = status.HTTPS_400_BAD_REQUEST)

    elif request.method =='DELETE':
        countries.delete()
        return JsonResponse({'message': 'Country was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
