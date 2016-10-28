#!/bin/python

from sys import exit, argv
from time import sleep
from os.path import exists
import requests
import json

sleeptime = 60000
logfile = "/tmp/log.txt"
url = "https://your_url"
method = "POST"
headers = {"Cookie": "PHPSESSID=42"}
last_output = None

def log(data):
  with open(logfile, "a+") as f:
    f.write(data)

def make_request():
  global last_output
  if method == "POST":
    r = requests.post(url, headers=headers)
  elif method == "GET":
    r = requests.get(url, headers=headers)
  elif method == "PUT":
    r = requests.put(url, headers=headers)
  elif method == "DELETE":
    r = requests.delete(url, headers=headers)
  output = {"text":r.text, "status_code":r.status_code}
  if last_output is None:
    last_output = output
  if output != last_output:
    log(json.dumps(output))
  print(r.status_code)
  print(r.text)

def set_args():
  global sleeptime, logfile, url, method
  for i, arg in enumerate(argv):
    if arg == "--sleeptime" and len(argv) > (i + 1):
      sleeptime = int(argv[i + 1])
    if arg == "--log" and len(argv) > (i + 1):
      logfile = argv[i + 1]
    if arg == "--url" and len(argv) > (i + 1):
      url = argv[i + 1]
    if arg == "--method" and len(argv) > (i + 1):
      method = argv[i + 1]

def	main():
  set_args()
  while not exists(logfile):
    make_request()
    sleep(sleeptime)
  return 0

if __name__ == '__main__':
  main()
