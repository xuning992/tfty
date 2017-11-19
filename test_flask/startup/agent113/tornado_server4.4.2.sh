#!/bin/bash


# tingyun.ini set the env in supervisor

NAME=flask_tornado_server

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
