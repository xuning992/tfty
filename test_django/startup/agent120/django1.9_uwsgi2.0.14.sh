#!/bin/bash
#
#
# chkconfig: 2345 55 25
# description:  server daemon
#
# uwsgi --http-socket :5562 --plugin python --wsgi-file app.py
# processname:
#

BASE=/mnt/hgfs/work
export TING_YUN_CONFIG_FILE=$BASE/tfty/test_django/config/django1.9.11_uwsgi2.0.14_agent1.2.0.ini
NAME=django1.9_uwsgi2.0.14
HOME=$BASE/tfty/test_django
PID=$BASE/staticfiles/pids/agent113/${NAME}.pid
# CMD=$1
CMD_ARGS="-M -p 1 -b 32767 -z 20 --threads 20 --max-request 16384 --listen 8192 --limit-post 1048576 --logdate --disable-logging"
PORT=5662
WSGIFILE=test_django.wsgi
LOGFILE=/home/nb/webapps/logs/test_django/agent120/django1.9_uwsgi2.0.14.log
VIRTUALENV=/root/.pyenv/versions/py2.7.12
CMD=${VIRTUALENV}/bin/uwsgi
AGENT_CMD=${VIRTUALENV}/bin/tingyun-admin
# VIRTUALENV=$2


wait_for_pid () {
    try=0
    while test ${try} -lt 1 ; do
        case "$1" in
            'created')
            if [ -f "$2" ] ; then
                try=''
                break
            fi
            ;;

            'removed')
            if [ ! -f "$2" ] ; then
                try=''
                break
            fi
            ;;
        esac

        echo -n .
        try=`expr ${try} + 1`
        sleep 1

    done

}

case "$1" in
    start)
        echo -n "Starting ${NAME} "
        wait_for_pid created ${PID}

        if [ -z "${try}" ] ; then
            echo " failed. The thread ${NAME} maybe is running."
            exit 1
        else
            #ulimit -n 2048

        ${AGENT_CMD} run-program ${CMD} ${CMD_ARGS} --chdir ${HOME} -H ${VIRTUALENV} --module ${WSGIFILE} --http-socket :${PORT} -d ${LOGFILE} --pidfile ${PID}

            if [ "$?" != 0 ] ; then
                echo " failed"
                exit 1
            else
                echo " done"
            fi
        fi

    ;;
    stop)
        echo -n "Gracefully shutting down ${NAME} "

        if [ ! -r ${PID} ] ; then
            echo "warning, no pid file found - ${NAME} is not running ?"
            exit 1
        fi

        ${CMD} --stop ${PID}

        if [ -f "${PID}" ] ; then
            rm ${PID}
        fi

        wait_for_pid removed ${PID}

        if [ -n "${try}" ] ; then
            echo " failed. Use force-exit"
            exit 1
        else
            echo " done"
        fi
    ;;
    restart)
        sh $0 stop
        sleep 2s
        sh $0 start
    ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
    ;;

esac
