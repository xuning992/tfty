#coding:utf-8
from gevent import monkey; monkey.patch_socket()
import gevent
import requests
import sys
import getopt
import time
import signal

import logging
logging.basicConfig(level=logging.INFO)


urls = ["/admin/", 
"/resp_200/", 
# "/resp_500/", 
"/resp_json/", 
"/no_html_start/", 
"/no_html_end/", 
"/no_head_start/", 
"/no_head_end/", 
"/no_title_start/", 
"/no_title_end/", 
"/no_head_start_title_start/", 
"/no_head_start_title_end/", 
"/no_head/", 
"/no_title/", 
"/no_head_end_title_start/", 
"/no_head_end_title_end/", 
"/no_head_start_title/", 
"/no_head_title_start/", 
"/no_head_end_title/", 
"/html_start_has_attr/", 
"/html_end_has_attr/", 
"/html_has_attr_lang_en/", 
"/html_has_attr_lang_zh/", 
"/head_start_has_attr/", 
"/head_end_has_attr/", 
"/title_start_has_attr/", 
"/title_end_has_attr/", 
"/head_start_title_start_has_attr/", 
"/head_start_title_end_has_attr/", 
"/head_end_title_start_has_attr/", 
"/head_end_title_end_has_attr/", 
"/befor_head_start_has_head_note/", 
"/befor_title_start_has_head_note/", 
"/befor_title_end_has_head_note/", 
"/befor_head_end_has_head_note/", 
"/after_head_end_has_head_note/", 
"/befor_head_start_has_title_note/", 
"/befor_title_start_has_title_note/", 
"/befor_title_end_has_title_note/", 
"/befor_head_end_has_title_note/", 
"/after_head_end_has_title_note/", 
"/title_has_special_char/", 
"/head_has_special_char/", 
"/html_has_special_char/", 
"/size_gt_64k/", 
"/requests_get/", 
"/db/insert/", 
"/db/delete/", 
# "/db/update/", 
"/db/select/", 
# "/db/transaction/", 
"/test/template/", 
"/test/func_view/", 
"/test/class_view/"]

HOSTS = ["http://192.168.177.150:5664"]
NUM = 0


def req(number, url):
    try:
        resp = requests.get(url)
        status_code = resp.status_code
        logging.info("【{number}】 req url: [{url}] get status code {code}==>>".format(number=number, url=url, code=status_code))
    except Exception as e:
        logging.error("【{number}】 req url: [{url}] error ==>> {e}".format(number={number}, url=url, e=e))


def main():
    global NUM
    spawns = []
    for url in urls:
        for host in HOSTS:
            NUM += 1
            url_ = "{host}/{url}".format(host=host.strip("/"), url=url.lstrip("/"))
            spawns.append(gevent.spawn(req, NUM, url_))
    gevent.joinall(spawns)


def signal_handler(signal, frame):
    logging.info("total {num} url requested ==>>".format(num=NUM))
    sys.exit(0)


if __name__ == "__main__":
    # 处理信号
    signal.signal(signal.SIGINT, signal_handler)

    # 解析参数
    request_time = None
    opts, args = getopt.getopt(sys.argv[1:],"ht:",["t="])
    for opt, arg in opts:
        if opt in ("-t", "-time"):
            request_time = arg

    if request_time is None:
        # 没有"-t"参数情况
        while 1:
            main()
    else:
        # 有 "-t"参数情况
        start_time = time.time()
        while 1:
            if int(time.time() - start_time) >= int(request_time):
                break
            main()




# import signal
# import sys
# def signal_handler(signal, frame):
# print('You pressed Ctrl+C!')
# sys.exit(0)
# signal.signal(signal.SIGINT, signal_handler)
# print('Press Ctrl+C')
# signal.pause()

