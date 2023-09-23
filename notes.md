```

```

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


`first()` function of `filter() `

return `None `
