from django.shortcuts import render
from django.db import transaction
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem, Collection, Order
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):

    with connection.cursor() as cursor:
        cursor.execute('SELECT*FROM store_product')
    return render(request, 'hello.html', {'name': 'Rikkie'})
