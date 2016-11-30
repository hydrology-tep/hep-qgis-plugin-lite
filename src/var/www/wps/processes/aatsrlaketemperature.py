"""
The ultimate process to test the status and update capabilities of the server
The processes shoul be requested as follows:
../wps.py?request=execute
&service=wps
&version=1.0.0
&identifier=hello
&status=true
&storeExecuteResponse=true
"""

from pywps.Process import WPSProcess
class Process(WPSProcess):
    def __init__(self):
	WPSProcess.__init__(self,
			    identifier = "aatsrlaketemperature",
			    version = "1.0.0",
			    title = "AATSR Lake Temperature",
			    storeSupported = "true",
			    statusSupported = "true",
			    abstract="",
			    grassLocation =False)

	self.inParam0 = self.addComplexInput(identifier="file_input", title="Input raster (AATSR)")
	self.inParam1 = self.addLiteralInput(identifier="boolean_adddeltalongandlatbands", title="Add delta Long and Lat bands", type=type(False), default=False, allowedValues = [True, False])
	self.inParam2 = self.addLiteralInput(identifier="number_invalidsstpixels", title="Invalid SST Pixels", type=type(0.0), default=-999.0)
	self.outputName0 = self.addLiteralInput(identifier="out0", title="Name of the output file for: Output Product", type=type(""))
	self.metadataOut = self.addComplexOutput(identifier="result_metadata", title="Metadata XML URL", formats = [{"mimeType":"application/xml","mimetype":"text/xml"}], asReference=True)

    def execute(self):
	import time
	import os, sys
	import subprocess
	import xml.etree.ElementTree as ET
	
	self.status.set("Preparing....", 0)
	time.sleep(2)
	uuid = self.pywps.UUID
	subprocess.Popen(['mkdir', '/var/www/wps/wpsoutputs/' + uuid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.Popen(['chmod', '777', '/var/www/wps/wpsoutputs/' + uuid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  
	inputfile0 = self.inParam0.getValue()
	f = open(inputfile0, 'r')
	xml = f.read()
	root = ET.fromstring(xml)
	for child in root.findall('{http://www.w3.org/2005/Atom}entry'):
		self.prodURL0 = child.find('{http://www.w3.org/2005/Atom}id').text

	import socket
	self.ip = socket.gethostname()
	import StringIO
	self.metadataOut.setValue(StringIO.StringIO('<wps:Reference href="http://' + self.ip + '/wpsoutputs/' + uuid + '/metadata.xml" method="GET" mimeType="application/atom+xml" />'))
	l=subprocess.Popen(["/var/www/wps/run_model.sh", "aatsrlaketemperature", self.prodURL0, str(self.inParam1.getValue()), str(self.inParam2.getValue()), "/var/www/wps/wpsoutputs/" + uuid + "/" + self.outputName0.getValue()],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err =l.communicate()
	print out
	print err
	errcode = l.returncode
	self.status.set("Finished", 0)
