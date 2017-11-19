# -*- coding: utf-8 -*-

'''
使用说明: 省略
'''


import os
from sys import exit


# extra package for install flask: installed Jinja2-2.8 MarkupSafe-0.23 Werkzeug-0.11.13
#                                  click-6.6 flask-0.12 itsdangerous-0.24

# $shell python version         # support version
tingyun_version = '1.3.1'
python_version = '2.7'   # 2.6 2.7
framework_name = 'web.py'
framework_version = '0.40.dev0'

uwsgi_version = "2.0.14"   # 0.9.x-2.0.x
gunicorn_version = "19.6.0"  # 17.x-19.x.x
gevent_version = "1.1.2"   # 1.0-1.1.x

# env package`s version
# mod_wsgi_version = ""

python_path = "/usr/local/python27"
# python_path = "/home/nb/virenv/flask_env"
resource = "https://pypi.douban.com/simple/"
pip_path = "/home/nb/webapps/tfty/test_django/auto_build/pip-9.0.1.tar.gz"
agent_path = "/home/nb/webapps/tfty/test_flask/auto_build/tingyun-1.3.0.zip"

# package`s version
# add packages


packages = [framework_name, 'uWSGI', 'gevent', "gunicorn"]

versions = {
    framework_name: framework_version,       # yum install postgresql-devel
    'uWSGI': uwsgi_version,
    'gevent': gevent_version,
    'gunicorn': gunicorn_version
}


def build_virtualenv():

    print "build virtualenv".center(80, "*")
    virenv_name = "%s%s-uwsgi%s-gunicorn%s-gevent%s" % (
        framework_name, framework_version, uwsgi_version,gunicorn_version, gevent_version)

    virenv_path = "/home/nb/webapps/virenv/Agent%s/Python%s/%s/%s" % (
        tingyun_version, python_version, framework_name, virenv_name)

    get_ = os.system("ls %s" % virenv_path)
    if get_ != 0:
        print "removing the old virenv..."
        os.system("rm -rf %s" % virenv_path)

    get_ = os.system("%s/bin/virtualenv %s --no-download" % (python_path, virenv_path))
    if get_ != 0:
        print "error is happend when created virtualenv"
        exit()

    os.system("chmod 777 -R %s " % virenv_path)

    global env_pip
    env_pip = "%s/bin/pip" % virenv_path

    print "upgrade pip".center(80, "*")
    get_ = os.system("%s install %s" % (env_pip, pip_path))
    if get_ != 0:
        print "error is happend when upgrade pip"
        exit()

    print ("install Agent(%s)" % tingyun_version).center(80, "*")
    get_ = os.system("%s install %s" % (env_pip, agent_path))
    if get_ != 0:
        print "error is happend when install Agent(%s)" % tingyun_version
        exit()


def installer(package, version_, results):

    print ("install %s" % package).center(80, "*")

    get_ = os.system("%s install %s==%s -i %s" % (env_pip, package, version_, resource))
    if get_ != 0:
        results.append(package)


def collect_install_info():

    pip_list = os.popen("%s list" % env_pip).read()
    install_infoes = {}

    for package in packages:

        result = "install successful"

        if "%s (%s)" % (package, (versions[package])) not in pip_list:
            result = "install fail"

        install_infoes[package] = result

    return install_infoes


def collect_error_info(results):
    print "error install package".center(80, "*")
    print results
    virenv_name = "CentOS6.8-Agent%s-Py%s-uWSGI%s-%s%s" % (tingyun_version, python_version, uwsgi_version,
                                                           framework_name, framework_version )
    print ("build complete! %s" % virenv_name).center(80, "*")


def main():

    build_virtualenv()

    results = []
    for package in packages:
        if package:
            installer(package, versions[package], results)

    collect_error_info(results)

    # install_result = collect_install_info()
    # print install_result


if __name__ == "__main__":
    main()
