'''
Created on 2018/05/27

@author: Bruno Catao
'''

from flask import Flask
from flask import request
from saiku.saiku_report_server import SaikuReportServer

# Create Flask APP
app = Flask(__name__)

# Setup the webservice routes
@app.route("/")
def hello():
  return SaikuReportServer.getInstance().hello_world()

@app.route("/render")
def render():
  reportId = request.args.get('id') or 'demo'
  outputFormat = request.args.get('format') or 'pdf'
  return SaikuReportServer.getInstance().render(reportId, outputFormat, {})

# Start the development server
if __name__ == '__main__':
  try:
    app.run(port='5002', threaded=False)
  finally:
    SaikuReportServer.getInstance().stop()
