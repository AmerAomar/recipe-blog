# lab class 29 Django X

## Project: Recipe Blog

## Author Amer Alomari

## Setup

```py
pip install -r requirements.txt
```

PORT=8000

## How to run the server

```py
python manage.py runserver
```

## How to run the server on different port number

```py
python manage.py runserver 8001 #you can change the port number
```

## Routes

- to get all recipes

```py
http://127.0.0.1:8000/recipe/
```

- to get recipe details

```py
http://127.0.0.1:8000/recipe/2/ #you can change the id
```

- to update recipe

```py
http://127.0.0.1:8000/recipe/2/update/ #you can change theid
```

- to delete recipe

```py
http://127.0.0.1:8000/recipe/2/delete/ #you can change the id
```

- to create recipe

```py
http://127.0.0.1:8000/recipe/create/
```
