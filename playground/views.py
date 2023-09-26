from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value
from django.db.models.functions import Concat


def say_hello(request):

    queryset = Product.objects.aggregate(Count('id'))

    return render(request, 'hello.html', {'name': 'Rikkie', 'products': queryset})
