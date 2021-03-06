#!/bin/bash


export TING_YUN_CONFIG_FILE=/home/nb/webapps/tfty/RabbitMQ_customer/agent.ini

HOME=/home/nb/webapps/tfty/RabbitMQ_customer/rabbitmq_customer.py
PID_PATH=/home/nb/staticfiles/pids
VIRENV=/home/nb/webapps/virenv/Agent1.3.1/Python2.7/flask/flask0.10-uwsgi2.0-gunicorn18.0-gevent1.0
PYTHON_PATH=${VIRENV}/bin/python
TINGYUN_PATH=${VIRENV}/bin/tingyun-admin
X1=$1
X2=$2
X3=$3
CMD_ARRAY=('queue;0' 'fanout;0' 'direct;0' 'topic;0' 'connect;1' 'slow_action;0' 'slow_action;2' 'other 0'
           'nosql;0' 'nosql;1' 'nosql;2')


function stop(){
    echo "stop $1 $2"
    pid=`ps -ef |grep nb|grep rabbitmq_customer|grep $1|grep $2|awk '{print $2}'`
    kill -9 ${pid}
    echo "done"
}


function stop_all(){
    for ((i=0;i<${#CMD_ARRAY[*]};i++))
    do
        cmd=${CMD_ARRAY[${i}]}
        cmd1=`echo ${cmd}|cut -d \; -f 1`
        cmd2=`echo ${cmd}|cut -d \; -f 2`
        stop ${cmd1} ${cmd2}
    done
}

function start_all(){
    for ((i=0;i<${#CMD_ARRAY[*]};i++))
    do
        cmd=${CMD_ARRAY[${i}]}
        cmd1=`echo ${cmd}|cut -d \; -f 1`
        cmd2=`echo ${cmd}|cut -d \; -f 2`
        run ${cmd1} ${cmd2}
    done
}


function run(){
    ${TINGYUN_PATH} run-program ${PYTHON_PATH} ${HOME} $1 $2
}

case ${X1} in
    all)
        if [ ${X2} == "start" ]
        then
            start_all
        elif [ ${X2} == "stop" ]
        then
            stop_all
        else
            echo "Usage $0 ${X1} {start|stop}"
        fi
    ;;

    stop)
        stop $2 $3
    ;;

    *)
        run ${X1} ${X2}
    ;;         
esac

   