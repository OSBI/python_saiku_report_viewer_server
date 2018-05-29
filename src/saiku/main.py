'''
Created on 2018/05/27

@author: Bruno Catao
'''

from flask import Flask
from saiku.saiku_report_server import SaikuReportServer

# Create Flask APP
app = Flask(__name__)

@app.route("/")
def hello():
  return SaikuReportServer.getInstance().hello_world()

if __name__ == '__main__':
  try:
    app.run(port='5002')
  finally:
    SaikuReportServer.getInstance().stop()
