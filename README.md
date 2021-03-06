# platzidjango

_Curso platzi de django 3.1.5 usando python 3.8.5 sobre ubuntu 20.04_

## Initial server configuration (suggestions)

1. Create a new user without home directory that it can run some root commands:

```
sudo useradd -g sudo -M <username>
```

2. Add password to new user:

```
sudo passwd <username>
```

3. Log in

```
su <username>
```

4. Install dependencies for python, postgres, git and nginx

```
sudo apt-get install python3-pip python3-dev postgresql postgresql-contrib libpq-dev git nginx
```

5. Install dependencies for Pillow

```
sudo apt-get install libjpeg-dev
```

6. This repository has a requirements.txt with the lib versions installed by pip.

7. You can use environment variables for protect secret fields like database fields, and add this one to bashrc file.


## Localenv

1. Verify python3 and pip3

```
python3 --version
pip3 --version
```

2. Create virtualenv with python3:

```
python3 -m venv .env
python3 -m venv ENTORNO
```

3. Activate / Deactivate virtualenv

```
source .env/bin/activate
deactivate
```

4. Install django and other libs

```
pip install Django
pip install psycopg2
pip install wheel
pip install Pillow
```

5. Verify with pip freeze

6. Start project / apps

```
django-admin startproject platzigram .
```

7. Remember

```
python3 manage.py check
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## How to run it?

```
For now... 
http://127.0.0.1:8000/
```

## Database Settings

```
sudo -u postgres psql
CREATE DATABASE dbtest;
CREATE USER uadmin WITH PASSWORD 'ppasswd';
GRANT ALL PRIVILEGES ON DATABASE dbtest TO uadmin;
\q

python manage.py createsuperuser
Username: admintest
Email address: admintest@example.com
Password: ptest123
```


#### Users for test

```
User: crivera
Password: cr123456
Carmen Rivera
crivera@example.com

User: lmendez
Password: lm123456
Liliana Mendez
lmendez@example.com
```

#### Django shell

```
python3 manage.py shell

platzi_users = User.objects.filter(email__endswith='platzi.com')

platzi_users = platzi_users.update(is_admin=True)
```

By [dcarolinahdev](https://github.com/dcarolinahdev)
