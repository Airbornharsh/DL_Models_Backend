echo = "BUILD START"
python3.11 -m pip install pipenv
pipenv install --system --deploy
python3.11 manage.py collectstatic --noinput --clear
echo = "BUILD END"