python3 -m pip install -r requirements.txt
cpus=$(cat /proc/cpuinfo| grep "processor"| wc -l)
echo "cpu核心数：" $cpus
workers=$(((2*$cpus)+1))
echo "设定进程数：" $workers
cd home
python3 manage.py makemigrations
python3 manage.py migrate
gunicorn -b 127.0.0.1:8000 --workers=$workers home.wsgi