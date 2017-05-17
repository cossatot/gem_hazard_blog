#!/usr/bin/env python

from flask import Flask, request
from subprocess import call, check_call
import json
import os

app = Flask(__name__)
port = 8002

cur_dir = os.getcwd()
namespace = 'hazard'
repo = 'blog'
www = '~/html'


def clone():
    if not os.path.isdir(repo):
        check_call(["git clone git@gitlab.openquake.org:" + namespace + "/"
                    + repo + ".git"], shell=True)


@app.route('/', methods=['POST'])
def deploy():
    data = json.loads(request.data)
    if 'object_kind' in data and 'object_attributes' in data:
        if(data['object_kind'] == 'merge_request' and
           data['object_attributes']['action'] == 'merge' and
           data['object_attributes']['target_branch'] == 'master'):
            print "Deploy START"
            clone()
            os.chdir(repo)
            call(["git pull origin master"], shell=True)
            call(["pelican --settings publishconf.py --output " + www +
                  " content"], shell=True)
            os.chdir(cur_dir)
            print "Deploy STOP"

    return "OK"

if __name__ == '__main__':
    clone()
    app.run(host='0.0.0.0', port=port)
