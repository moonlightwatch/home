
old_hash=$(git rev-parse HEAD)
echo $old_hash
git pull
new_hash=$(git rev-parse HEAD)
echo $new_hash

if [ $old_hash = $new_hash ]
then
    echo `date` "没有更新"
else
    python3 -m pip install -r requirements.txt
    cd home
    python3 manage.py makemigrations
    python3 manage.py migrate
    supervisorctl restart home
    echo `date` "重启服务"
fi