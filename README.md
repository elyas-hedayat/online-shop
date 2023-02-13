setup your env 

install project requirements=pip install -r requirements

setup your database config 

run:
  python manage.py migrate
  
finally:
  python manage.py createcachetable
