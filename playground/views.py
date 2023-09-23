from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    product = Product.objects.filter(pk=1).first()



    return render(request, 'hello.html', {'name': 'Rikkie'})
