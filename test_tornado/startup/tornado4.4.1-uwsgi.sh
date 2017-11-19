#!/bin/bash
#
#
# chkconfig: 2345 55 25
# description:  server daemon
#
# uwsgi --http-socket :5562 --plugin python --wsgi-file app.py
# processname:
#

HOME=/mnt/hgfs/work/tfty/test_tornado
VIRTHALENVPATH=/root/.pyenv/versions/py2.7.12/bin
STARTSCRIPT=run_uwsgi.py
NAME=tornado4.4.1-uwsgi
PORT=8090
LOGFILE=${HOME}/doc/tornado_uwsgi.log

export TING_YUN_CONFIG_FILE=${HOME}/doc/tingyun_uwsgi.ini
PID=/mnt/hgfs/work/pid/${NAME}.pid

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

            #${VIRTHALENVPATH}/tingyun-admin run-program ${VIRTHALENVPATH}/uwsgi --chdir ${HOME} --module ${STARTSCRIPT} --http-socket :${PORT} -d ${LOGFILE} --pidfile ${PID}
            echo "${VIRTHALENVPATH}/tingyun-admin run-program ${VIRTHALENVPATH}/uwsgi --chdir ${HOME}/app --module ${STARTSCRIPT} --http-socket :${PORT} --pidfile ${PID}"
            ${VIRTHALENVPATH}/tingyun-admin run-program ${VIRTHALENVPATH}/uwsgi --chdir ${HOME}/app --wsgi-file ${STARTSCRIPT} --callable application --http-socket :${PORT} --pidfile ${PID}

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
