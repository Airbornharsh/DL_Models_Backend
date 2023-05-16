echo = "BUILD START"
python3 -m pip install -r requirements.txt
echo = "PIP INSTALL END"
python3.11 manage.py collectstatic --noinput --clear
echo = "BUILD END"