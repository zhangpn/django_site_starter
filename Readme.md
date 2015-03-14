To install django:
* First, remove existing/outdated version by finding the path:
    - run `python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"`
    - remove the django directory from the site-package or dist-package directory
* `sudo apt-get install python3-pip`
* `sudo pip3 install Django`

* Run the following commands:
* `django-admin.py startproject mysite`
* `python3 manage.py migrate`
* `python3 manage.py startapp attendance`
* In `mysite1/settings.py` add `attendance` in the `INSTALLED_APPS` list
* run `python3 manage.py createsuperuser` to create a new admin user
* After modifying the models.py file, run `python3 manage.py makemigrations`, which can be skipped first
followed by `python3 manage.py migrate`

To create models from existing schema:
* Run `python3 .createModels/runsql1.py NAZA_create.sql db.sqlite3` to create tables into db

* Then, run `python manage.py inspectdb > models.py` to create models based on database

To load data from a csv file to database
* run `python3 ./importData/load.py` to load data stored in data.csv into database
