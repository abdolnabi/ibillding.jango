sudo apt-get install python3-venv
python -m venv venv
source venv/bin/activate
sudo apt-get install libmysqlclient-dev
sudo apt-get install libpq-dev python-dev
sudo apt-get install gcc
sudo apt install python3-dev
sudo apt-get install libssl-dev
pip install -r requirments.txt

# to create database
mysql> create database bcm;
mysql> CREATE USER 'bcm'@'localhost' IDENTIFIED BY 'bcm';
mysql> GRANT ALL PRIVILEGES ON bcm.* to bcm@localhost;

python bcm/manage.py migrate
python bcm/manage.py collectstatic --noinput
sh run.sh
