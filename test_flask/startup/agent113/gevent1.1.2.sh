#!/usr/bin/env bash


NAME=flask_gevent

# export TING_YUN_CONFIG_FILE=/home/nb/webapps/tfty/test_flask/config/agent_gevent.ini
case "$1" in
    start)
        echo -n "Starting ${NAME} "
        supervisorctl start ${NAME}
    ;;
    stop)
        echo -n "Gracefully shutting down ${NAME} "
        supervisorctl stop ${NAME}
    ;;
    restart)
        sh $0 stop
        sh $0 start
    ;;
    *)
        echo "Usage: $0 {start|stop}"
        exit 1
    ;;

esac
