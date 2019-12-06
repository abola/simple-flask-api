import functools
import math
import os
import random
import time

from flask import Flask, request, jsonify, abort
from waitress import serve

# init Flask
app = Flask(__name__)

@app.route('/api/v1.0/show/version', methods=['GET'])
def show_version():
  return '1.0'

@app.route('/api/v1.0/show/pod_name', methods=['GET'])
def show_pod_name():
  return os.getenv('HOSTNAME')


@app.route('/api/v1.0/add/cpu_load', methods=['GET'])
def cpu_load():
  return 'pi: {}'.format(easy_pi())

@app.route('/health', methods=['GET'])
def health():
  return 'ok', 200

def map_d(c):
  return math.hypot(random.random(), random.random())

def reduce_d(count_inside, d):
  if d < 1:
    return count_inside + 1
  return count_inside

def easy_pi():
  count = 1024*128
  d_list = map(map_d, range(0, count))
  count_inside = functools.reduce(reduce_d, d_list)
  return 4.0 * count_inside / count

# add raondom sleep time(1-10) before serve 
time.sleep(int(random.random()*10)+1)

# run Flask Restful service
serve(app, port=3000, host='0.0.0.0')
