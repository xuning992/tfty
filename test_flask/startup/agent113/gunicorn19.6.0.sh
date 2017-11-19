
#!/usr/bin/env bash

TING_YUN_CONFIG_FILE=/home/nb/webapps/tfty/test_flask/config/agent_gunicorn.ini
NAME=flask_gunicorn
HOST="0.0.0.0"
PORT=5564
LOGFILE=/home/nb/logs/test_flask/gunicorn_flask.log
CHDIR=/home/nb/webapps/tfty/test_flask
LOGLEVEL=debug
PROCESSES=2
THREADS=2
WORKER_CLASS=tornado     # sync|eventlet|gevent|tornado|gthread|gaiohttp
PID=/home/nb/staticfiles/pids/${NAME}.pid
CMD=/home/nb/virenv/flask_env/bin/gunicorn
# CMD=TING_YUN_CONFIG_FILE=/home/nb/webapps/tfty/test_flask/config/agent_gunicorn.ini tingyun-admin run-program gunicorn -c gunicorn.conf main_flask:application -D -t 6000 --log-file ${LOGFILE} --log-level ${LOGLEVEL}

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

            # 19.6.0
            ${CMD} -w ${PROCESSES} -b ${HOST}:${PORT} --log-file ${LOGFILE} --log-level ${LOGLEVEL} --pid ${PID} -D -k ${WORKER_CLASS} --threads ${THREADS} --chdir ${CHDIR}  main_flask:application

            # 18.0
            # ${CMD} -w ${PROCESSES} -b ${HOST}:${PORT} --log-file ${LOGFILE} --log-level ${LOGLEVEL} --pid ${PID} -D -k ${WORKER_CLASS} --chdir ${CHDIR}  main_flask:application

            # 17.5
            # ${CMD} -w ${PROCESSES} -b ${HOST}:${PORT} --log-file ${LOGFILE} --log-level ${LOGLEVEL} --pid ${PID} -D main_flask:application

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

        kill -9 `cat ${PID}`
        # kill -9 `cat /home/nb/staticfiles/pids/xiha.pid`

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
        sh $0 start
    ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
    ;;

esac
