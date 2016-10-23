#!/bin/python

from sys import exit
from time import sleep
from os.path import exists
import requests
import json

sleeptime = 60000
logfile = "/tmp/log.txt"
url = "https://intra.epitech.eu/module/2016/M-ADS-775/PAR-9-1/register?format=json"
headers = {"Cookie": "PHPSESSID=0snv902iu8ks0cf7n61b2nad61; _ga=GA1.3.1102579131.1476529245; _gat=1"}
last_output = None

def log(data):
  with open(logfile, "a+") as f:
    f.write(data)

def make_request():
  global last_output
  r = requests.post(url, data=data, headers=headers)
  output = {"text":r.text, "status_code":r.status_code}
  if last_output is None:
    last_output = output
  if output != last_output:
    log(json.dumps(output))
  print(r.status_code)
  print(r.text)
  
def	main():
  while not exists(logfile):
    make_request()
    sleep(sleeptime)
  return 0

if __name__ == '__main__':
  main()
