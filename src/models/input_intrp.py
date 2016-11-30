import os, sys, urllib, subprocess, ssl, socket
import xml.etree.ElementTree as ET

input_product = sys.argv[1]
#context = ssl._create_unverified_context()

host = socket.gethostname()

input_product = input_product + '&do=' + host

file = urllib.urlopen(input_product) #, context=context)
data = file.read()
file.close()
root = ET.fromstring(data)
for child in root.findall('{http://www.w3.org/2005/Atom}entry'):
	prod_name = child.find('{http://purl.org/dc/elements/1.1/}identifier').text
	### To update ###
	block_first = 0
	for link in child.findall('{http://www.w3.org/2005/Atom}link'):
		if link.attrib['rel'] == 'enclosure' and block_first == 0:
			block_first = 1
			enclosure_link = link.attrib['href']
			prodName = os.path.basename(enclosure_link)
	####
tmp_dir = '/tmp/' + prodName + '/'
subprocess.Popen(['mkdir', tmp_dir])
os.chdir(tmp_dir)
wget = subprocess.Popen(['wget', '--content-disposition', enclosure_link])
wget.wait()
print tmp_dir + os.listdir(tmp_dir)[0]
