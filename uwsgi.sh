#!/bin/bash
if [ ! "$1" ];then
    echo "Usages:sh uwsgi.sh [start | stop | restart]"
    exit 0
fi

if [ $1 == "start" ];then
    psid = `ps aux | grep "uwsgi" | grep -v "grep" | wc -l`
    if [ $psid -gt 4 ];then
        echo "uwsgi is running!"
        exit 0
    else
        /usr/local/bin/uwsgi --ini /root/blog/config.ini --daemonize /root/blog/logs/uwsgi.log
        echo "Start uwsgi service [OK]"
        exit 0
    fi
elif [ $1 == "stop" ];then
    killall -9 uwsgi
    echo "Stop uwsgi service [OK]"
    exit 0
elif [ $1 == "restart" ];then
    killall -9 uwsgi
    /usr/local/bin/uwsgi --ini /root/blog/config.ini --daemonize /root/blog/logs/uwsgi.log
    echo "Restart uwsgi service [OK]"
    exit 0
else
    echo "Usages: sh uwsgi.sh [start | stop | restart]"
    exit 0
fi
