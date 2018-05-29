'''
Created on 2018/05/27

@author: Bruno Catao
'''

import os
import javabridge

class SaikuReportServer:
  instance = None
  
  @staticmethod
  def getInstance():
    if not SaikuReportServer.instance:
      SaikuReportServer.instance = SaikuReportServer()
    return SaikuReportServer.instance
  
  def __init__(self):
    self._performInit()
    
  def _performInit(self):
    # Set the classpath
    javaclasspath = [os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'lib', 'saiku-report-viewer-server.jar'))]
    # Start JVM 
    javabridge.start_vm(class_path=[os.pathsep.join(javaclasspath)], run_headless=True)
    javabridge.attach()
    
    # Init the Saiku Report Server Implementation
    self.reportServerImpl = javabridge.JClassWrapper('org.saiku.reportviewer.server.api.ReportServerImpl')()
    self.reportServerImpl.init()
  
  def stop(self):
    javabridge.kill_vm()

  def hello_world(self):
    return self.reportServerImpl.helloWorld()

  def render(self, reportId, outputFormat, params):
    uriInfo = javabridge.JClassWrapper('org.saiku.reportviewer.server.util.MockUriInfo')()
    return self.reportServerImpl.render(reportId, outputFormat, uriInfo)
    