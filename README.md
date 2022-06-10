git clone https://gitlab.com/qamar.satti5/test.git
cd test
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
