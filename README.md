# CallerAPI

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up](#setting-up)
- [Data Population](#data-population)
- [Running the Code](#running-the-code)
- [API Endpoints](#api-endpoints)

## Prerequisites

Make sure you have the following installed on your system:

- Python
- pip (Python package installer)

## Installation

```bash
pip install django djangorestframework
pip install psycopg #to_connect_to_database
pip install faker #to_populate_the_data 
```

## Setting Up

1.. Create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Create a superuser:

```bash
python manage.py createsuperuser
```

## Data Population

Run the data population script:

```bash
python manage.py populate
```

## Running the Code

Start the development server:

```bash
python manage.py runserver
```

Access the API Root interface at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## API Endpoints

- `/register/`: Register using details to use the other Endpoints
- `/login/`: Login using details to use the other Endpoints
- `/users/`: List all registered users with details.
- `/contacts/`: List and create Contacts.
- `/search/`: Search Name and Phone Number using [http://127.0.0.1:8000/search/?Search="your_search_query"]([http://127.0.0.1:8000/search/?Search="your_search_query")
