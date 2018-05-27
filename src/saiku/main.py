'''
Created on 2018/05/27

@author: Bruno Catao
'''

import os
import javabridge
from flask import Flask

# Create Flask APP
app = Flask(__name__)

@app.route("/")
def hello():
  retval = '';
  
  # Start JVM 
  javaclasspath = [os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'lib', 'saiku-report-viewer-server.jar'))]
  javabridge.start_vm(class_path=[os.pathsep.join(javaclasspath)], run_headless=True)
  
  try:
    retval = javabridge.run_script('''
    var uriInfo = new JavaAdapter(javax.ws.rs.core.UriInfo, {
      getAbsolutePath: function() { return null; },
      getAbsolutePathBuilder: function() { return null; },
      getBaseUri: function() { return null; },
      getBaseUriBuilder: function() { return null; },
      getMatchedResources: function() { return null; },
      getMatchedURIs: function() { return null; },
      getPath: function() { return null; },
      getPathParameters: function() { return null; },
      getPathSegments: function() { return null; },
      getQueryParameters: function() { 
        return new javax.ws.rs.core.MultivaluedHashMap(); 
      },
      getRequestUri: function() { return null; },
      getRequestUriBuilder: function() { return null; },
      relativize: function() { return null; },
      resolve: function() { return null; }
    }); 
    
    var r = new org.saiku.reportviewer.server.api.ReportServerImpl();
    r.init();
    r.helloWorld();
    ''')
  finally:
    javabridge.kill_vm()

  return retval

if __name__ == '__main__':
  app.run(port='5002')
