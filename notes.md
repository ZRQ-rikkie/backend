## Setup

pipenv to mange python environment

use `django-admin` to start a new project

ctrl+shift+p-> python interpreter ->select environment

`pipenv --venv` search for the environment path

## App

* **view function:** is where to take the request and send response (A request handler)
* **urls:** mapping URL patterns to view functions, effectively directing incoming HTTP requests to the appropriate handling code.
* **templates:** generate dynamic HTML content, allowing the separation of presentation from business logic by defining placeholders and tags to insert data from the application layer.*(usually dont use this)*

## **Debugging Django in Vscode**

Add `"9000"` in

```
"args": [
                "runserver", "9000"
            ],
```

To prevent the clash with the port 8000 when debugging.

`ctrl+F5` :

Run without Debugging.
Django debug toolbar
The toolbar only shows when return a proper HTML documents(html,body)

## Models

Association class

Monolith

A good design should be:

**minimal coupling** and **high cohesion**(focus)

models

one to one relationship

one to many relationship

many to many relationship

Circular Dependency(should avoid)

Generic Relationships

Use `ContentType`

## SetUp Database

Default: sqlite
Meat Data
undo the last migration

```

python manage.py migrate store <number>

```

```
git log --online
git reset --hard HEAD~1
```

make the head pointer one step back

use

```
python manage.py makemigrations store --empty

```

```
operations = [
        migrations.RunSQL(
                        <!-- SQL -->

                        """
                          INSERT INTO store_collection(title)
                          VALUES('collection1')

                          """,
                        <!-- Reverse SQL -->

                          """
                          DELETE FROM store_collection
                          WHERE title = 'collection1'
                          """,)
    ]

```

Use [Mockaroo.com](https://www.mockaroo.com) for dummy data

## Django ORM

**Object-relational mappers**

* Reduce complexity in code
* Make the code more understandable
* get more done in less

Every model in django has an attribute called objects

This returns a manager object (Interface to the database)

### Filter Function

`first()` function of `filter()`return `None`

`exists()` return boolean

```
__gt
__lt
__gte
__lte
```

search for queryset API
[https://docs.djangoproject.com/en/4.2/ref/models/querysets/]()

* #### complex lookups using Q object

multi ways:

**AND**

```
SELECT ••• FROM store_product WHERE (store_product.inventory < 10 AND store_product.unit_price < 20)
```

* ```
  queryset = Product.objects.filter(
          inventory__lt=10, unit_price__lt=20)
  ```
* ```

  queryset = Product.objects.filter(
          inventory__lt=10).filter(unit_price__lt=20)

  ```

**OR**

```
SELECT ••• FROM store_product WHERE (store_product.inventory < 10 OR store_product.unit_price < 20)
```

1. ```
   from django.db.models import Q
   ```
2. ```
   queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
   ```

* #### Referencing Fields using F

```
SELECT ••• FROM store_product WHERE store_product.inventory = (store_product.unit_price)
```

1. ```
   from django.db.models import F
   ```
2. ```
   queryset = Product.objects.filter(inventory=F('unit_price'))
   ```

### Sorting Data

**ASC**

```
SELECT ••• FROM store_product ORDER BY store_product.title ASC
```

* ```
  queryset = Product.objects.order_by('title')
  ```

**DESC**

```
SELECT ••• FROM store_product ORDER BY store_product.title DESC
```

* ```
  queryset = Product.objects.order_by('-title')
  ```

**Unit Sort**

```
queryset = Product.objects.order_by('unit_price', '-title').reverse()
```

**.earliest()**
sort objects and get the first object

```
product = Product.objects.earlist('unit_price')
```

**.latest()**
sort objects in desending order and get the first object

```
product = Product.objects.latest('unit_price')
```

#### Limiting Results

```
 queryset = Product.objects.all()[:5]
```

#### Slecting Fields to Query

`.values()` returns dictionary

```
queryset = Product.objects.values('id','title')
```

```
reading related field
queryset = Product.objects.values('id','title','collection__title')
```

```
SELECT store_product.id,
       store_product.title,
       store_collection.title
  FROM store_product
 INNER JOIN store_collection
    ON (store_product.collection_id = store_collection.id)
```

`.value_list()` returns tuples
`.distinct()` to solve the duplicate

```
queryset = Product.objects.filter(id__in=OrderItem.objects.values(
        'product_id').distinct()).order_by('title')
```

Deferring Field

```
queryset = Product.objects.only('id','title')
```

`.only()` return objects
`.values()` return dictionary

`.defer()` the opposite from `.only()`

#### Slecting Related Object

```
queryset = Product.objects.select_related('collection').all()
```

```
SELECT ••• FROM store_product INNER JOIN store_collection ON (store_product.collection_id = store_collection.id)
```

select_related(1)
prefetch_related(n)

#### Aggregating

```
from django.db.models.aggregates import Count, Max,Min, Avg, Sum
```

return a dictionary

#### Annotating Objects

```
from django.db.models import Value
.annotate()
```

#### Calling Database Functions

CONCAT

```
from django.db.models.functions import Concat
```

#### Grouping Data

#### Expression Wrappers

from django.db.models import Expression Wrapper

#### Querying Generic Relationships

```
fromdjango.contrib.contenttypes.modelsimportContentType
```

```
content_type = ContentType.object.get_for_model(Product)
    queryset = TaggedItem.objects.select_related('tag').filter(
        content_type = content_type,
        object_id = 1
    )
```

#### Custom Manager

#### QuerySet Cache

read obect from the queryset cache

#### Creating objects

use tradtional way
or `use objects.create()`

* updating:
  get the object at first
  `.get()`
  or use `objects.update()`
* deleting:
  `.delete()`
  for delet multiple object first get a queryset

#### Transactions

```
from django.db import transaction
```

use decoration:
`@ transaction.atomic `or
`with transaction.atomic:`

Executing Raw SQL Queries

* method 1:
  ```
  queryset = Product.objects.raw('SELECT*FROM store_product')
  ```
* method 2:
  ```
  with connection.cursor() as cursor:
        cursor.execute('SELECT*FROM store_product')
  ```
* method 3:

```
  with connection.cursor() as cursor:
        cursor.callproc('SELECT*FROM store_product')
```

## Admin Interface

crate new admin:

```
python manage.py createsuperuser
```

Adding `django.contrib.sessions` to `INSTALLED_APP` and `migrate `command to generate the session table

#### Registering Models

admin.site.register(models.Collection)

#### Customize the listing page

use register decorater
Django ModelAdmin

#### Customize the listing page

Adding Computed Columns

```
list_display =
list_editable =
list_per_page =
```

#### Selecting Related Object

```
list_select_related
```

to preload the related objects

#### Overriding the base queryset

#### Providing Links to Other Pages

```
from django.utils.html import format_html
```

```
def products_count(self,collection):
        return format_html('<a href="http://google.com">{}</a>',collection.products_count)
```

```
from django.urls import reverse
```

```
def products_count(self,collection):
        url = reverse('admin:store_product_changelist')
        return format_html('<a href="{}">{}</a>',url,collection.products_count)
```

#### Adding search

```
search_fields = ['first_name','last_name']
```

`__startswith` lookup type

#### Adding filter

```
list_filter = ['collection', 'last_update']
```

create a filter:

```
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'    def lookups(self, request, model_admin):
        return [
            ('<10', 'low')        ]    def queryset(self, request, queryset:QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
```

#### Creating Custom Action

```
actions = ['clear_inventory']@admin.action(description='Set inventory to 0')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated'
        )
```

return error message:
`from django.contrib import admin, messages`

```
self.message_user(            request,            f'{updated_count} products were successfully updated',            messages.ERROR    )
```

#### Customize Forms

`files`,` exclude`, `readonly_fields`, `prepopulated_fields`

#### Adding Data Validation

make the value nullable
`blank=True`

set the min value

```
from django.core.validators import MinValueValidator unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators =[MinValueValidator(1)])
```

#### Editing Children Using Inlines

```
class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
```

admin.StackedInline

#### Using Generic Relations

```
from django.contrib.contenttypes.admin import GenericTabularInline
```

#### Extending Pluggable Apps

## RESTful API

**Restful:** Representational State Transfer

* Resources
* Representations
* HTTP Methods
  GET
  POST
  PUT
  PATCH
  DELTE

```
pipenv install djangorestframework
```

view function is take a request and return a response

```
from rest_framework.decorators import api_view
@api_view()
def product_list(request):
    return Response('ok')
```

#### Creating Serializers

```
from rest_framework import status
......
  return Response(status=status.HTTP_404_NOT_FOUND)
```

```
from django.shortcuts import get_object_or_404
this wrap off the try except
```

#### Custom Serializer Field

#### Serializing Relationships

* Primary Key
* String Values
* Nested Object
* Hyperlinks

#### Model Serializer

`serializers.ModelSerializer`

#### Deserializing Objects

save data from the clients

```
elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        # serializer.validated_data
        return Response('ok')
```

#### Data Validation

```
elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        return Response('ok')
```

#### Save data to the database

```
@api_view(['GET', 'PUT'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
```

#### Deleting Object

httpstatus.com

## Advanced API concepts

#### class based view

**benefit:**

* write cleaner code

#### Mixins

```
from rest_framework.mixins import ListModelMixin,CreateModelMixin
```

*search for gerneric views in Django docs*

#### Gerneric Vies