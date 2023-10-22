# Website overview-

https://github.com/yj1910/Ice-Cream-parlour-Website/assets/83238190/c2941ef9-320b-46b3-99c3-97b3f2e8e11b



# Local setup
In this repo. I have created a ice-crem parlour website project by using python, django framework and using a sqlite3 database as a database.
Belows are the steps to download the project in your local system\
Import the project file in your local. Open in IDE and open terminal

**To install dependencies, run:**
```
python -m pip install --upgrade pip (Upgrading pip)
pip3 install -r requirements.txt
```

**To initialize the Database (sqlite3 file)**
```
del db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

**In order to run this project, execute:**
```
python manage.py runserver
```
open http://127.0.0.1:8000/ on your browser

