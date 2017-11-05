# Vending Machine

A short problem representative of incremental feature improvement.

## Getting Started

    $ git clone https://github.com/mchughmk/inVenTs.git
    $ cd inVenTs
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py createsuperuser

This will download the code, install the required packages and set up the
database.

    $ python manage.py runserver 0.0.0.0:3000

This will run the server and make it available over the HTTPS link if you are
working from [CodeAnywhere](https://codeanywhere.com).

## Process

We'll work through the process of adding new features to our simple vending
machine, like adding support for more kinds of currency, more products, and
price checking.
