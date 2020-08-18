
old_hash=$(git rev-parse HEAD)
echo $old_hash
# git pull
new_hash=$(git rev-parse HEAD)
echo $new_hash

if [ $old_hash = $new_hash ]
then
    echo `date` "没有更新"
else
    supervisorctl restart home
    echo `date` "重启服务"
fi