echo = "BUILD START"
python3 -m pip install pipenv
pipenv install --system --deploy
python3 manage.py collectstatic --noinput --clear
echo = "BUILD END"