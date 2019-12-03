import functools
import random
import math

from flask import Flask, request, jsonify, abort
from waitress import serve

# init Flask
app = Flask(__name__)

@app.route('/api/v1.0/show/version', methods=['GET'])
def show_version():
  return '1.0'

@app.route('/api/v1.0/add/cpu_load', methods=['GET'])
def cpu_load():
  return 'pi: {}'.format(easy_pi())

def map_d(c):
  return math.hypot(random.random(), random.random())

def reduce_d(count_inside, d):
  if d < 1:
    return count_inside + 1
  return count_inside

def easy_pi():
  count = 1024*512
  d_list = map(map_d, range(0, count))
  count_inside = functools.reduce(reduce_d, d_list)
  return 4.0 * count_inside / count

# run Flask Restful service
serve(app, port=3000, host='0.0.0.0')
