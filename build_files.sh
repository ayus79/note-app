echo " Build start..."
python3.9 -m pip install -r requirements.txt
echo "Making Migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
echo "Collecting static..."
python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END"
