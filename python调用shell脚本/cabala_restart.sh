#!/bin/sh
kill -9 `ps -ef|grep apache-tomcat-server|grep -v grep|awk '{print $2}'`
kill -9 `ps -ef|grep -v grep|grep common-bus|awk '{print $2}'`
filePath=applicationContext.xml
serverPath=
busPath=
sleep 2
sed -i "s#`cat $filePath | grep -v \*|grep cronExpression|awk -F "=" '{print $3}'|awk '{print $5}'`#`date +%m`#g" $filePath
sed -i "s#`cat $filePath | grep -v \*|grep cronExpression|awk -F "=" '{print $3}'|awk '{print $4}'`#`date +%d`#g" $filePath
sed -i "s#`cat $filePath | grep -v \*|grep cronExpression|awk -F "=" '{print $3}'|awk '{print $3}'`#`date +%H`#g" $filePath
sed -i "s#`cat $filePath | grep -v \*|grep cronExpression|awk -F "=" '{print $3}'|awk '{print $2}'`#`date +%M`#g" $filePath

sleep 2
$serverPath/bin/startup.sh

sleep 10
$busPath/bin/startup.sh

