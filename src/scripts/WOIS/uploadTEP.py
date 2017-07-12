#Definition of inputs and outputs
#==================================
##Tools=group
##Upload to TEP=name

##ParameterRaster|raster|Select raster output to publish on TEP|True|
##ParameterBoolean|quicklook|Generate Quick Look from raster|False
##ParameterFile|vector|Select vector output to publish on TEP|False
##ParameterString|remoteDir|Remote directory (ignore if include script on a model)|/
##ParameterString|user|Storage owner username (ignore if include script on a model)|None
##ParameterString|password|Password (ignore if include script on a model)|None


#Algorithm body
#==================================

import os, sys
import glob, subprocess, PIL
from osgeo import gdal, gdalconst, ogr
from gdalconst import *
from PIL import Image
from PyQt4.QtGui import *
from PyQt4.QtCore import QSize
from PyQt4.QtCore import QFileInfo
from qgis.core import *
import qgis.utils
import datetime, socket

results = []
result = ''

if raster:

    outputDir = os.path.dirname(raster)

    if "/var/www/wps/wpsoutputs" in outputDir:

    	f = open(outputDir + '/metadata.xml', 'w')
    	metadataStr = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title type="text">Discovery feed for WPS result local data</title>
    <subtitle type="text">This OpenSearch Service allows the discovery of the different items which are part of the localdata collection. This search service is in accordance with the OGC 10-032r3 specification.</subtitle>
    <generator>Terradue Web Server</generator>
        """

    	outputRaster = os.path.basename(raster)
    	outputName, ext = os.path.splitext(outputRaster)
    	ext = ext[1:]

    	data = gdal.Open(raster, GA_ReadOnly)
    	width = data.RasterXSize
    	height = data.RasterYSize
    	gt = data.GetGeoTransform()
    	ul_x = str(gt[0])
    	ul_y = str(gt[3] + width*gt[4] + height*gt[5])
    	lr_x = str(gt[0] + width*gt[1] + height*gt[2])
    	lr_y = str(gt[3])

    	date_and_time = datetime.datetime.now().isoformat()
    	host = socket.gethostname()
    	uid = os.path.basename(os.path.normpath(outputDir))

   	metadataStr = metadataStr + """
    <entry>
        <id>http://""" + host + """/wpsoutputs/""" + uid + """/""" + outputRaster + """</id>
        <title type="text">""" + outputRaster + """</title>
        <published>""" + date_and_time + """Z</published>
        <updated>""" + date_and_time + """Z</updated>
        <link href="http://""" + host + """/wpsoutputs/""" + uid + """/""" + outputRaster + """?op=OPEN" rel="enclosure" type="application/octet-stream"/>
        <identifier xmlns="http://purl.org/dc/elements/1.1/">""" + outputRaster + """</identifier>
        <where xmlns="http://www.georss.org/georss/10" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <Polygon xmlns="http://www.opengis.net/gml">
            <exterior>
              <LinearRing>
	 	<posList srsDimension="2">""" + ul_y + ' ' + ul_x + ' ' + ul_y + ' ' + lr_x + ' ' + lr_y + ' ' + lr_x + ' ' + lr_y + ' ' + ul_x + ' ' + ul_y + ' ' + ul_x + """</posList>
              </LinearRing>
            </exterior>
          </Polygon>
        </where>
        <box xmlns="http://www.georss.org/georss">""" + ul_y + ' ' + ul_x + ' ' + lr_y + ' ' + lr_x + """</box>
        <offering xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.opengis.net/owc/1.0" code="http://www.opengis.net/spec/owc-atom/1.0/req/png">
          <content href="http://""" + host + """/wpsoutputs/""" + uid + """/""" + outputRaster + """?op=OPEN" type="image/""" + ext + """" />
        </offering>
    </entry>
    """

    	if quicklook == True:
	    try:
		os.environ['LD_LIBRARY_PATH'] = " /usr/local/lib/:/usr/local/qwtpolar-0.1.0/lib/:/usr/local/qwt-5.2.3/lib/:/opt/anaconda/lib/:/usr/local/Trolltech/Qt-4.8.5/lib/"
		os.environ['PATH'] = "/opt/anaconda/bin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/OTB-5.0.0/bin:/home/woisuser/bin"
		os.environ['GDAL_DATA'] = "/opt/anaconda/share/gdal"
		os.environ['PYTHONPATH'] = "/usr/local/share/qgis/python"
		#os.system('/opt/anaconda/bin/python /home/woisuser/models/ql.py ' + raster)
		QgsApplication.setPrefixPath("/usr/local", True)
		QgsApplication.initQgis()
	        quicklookFile = outputName + '.png'
	        quicklookFilepath = outputDir + '/' + quicklookFile
		os.system("chown apache:wois " + raster)
		fileInfo = QFileInfo(raster)
	        baseName = fileInfo.baseName()
	    	rlayer = QgsRasterLayer(raster, baseName)
	    	QgsMapLayerRegistry.instance().addMapLayer(rlayer)

	    	w=rlayer.width()
	    	h=rlayer.height()
	    	img = QImage(QSize(w, h), QImage.Format_ARGB32_Premultiplied)
	    	color = QColor(255, 255, 255)
	    	img.fill(color.rgb())

	    	p = QPainter()
	    	p.begin(img)
	    	#p.setRenderHint(QPainter.Antialiasing)

	    	render = QgsMapRenderer()

	    	lst = [rlayer.id()]
	    	render.setLayerSet(lst)

	    	rect = QgsRectangle(render.fullExtent())
	    	rect.scale(1.0)

	    	render.setExtent(rect)
	    	render.setOutputSize(img.size(), img.logicalDpiX())
	    	render.render(p)
	    	p.end()

	    	img.save(quicklookFilepath,"png")

	    	#im = Image.open(quicklookFilepath)

	    	#datas = im.getdata()
	    	#newData = []
	    	#for item in datas:
    		#    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        	#	newData.append((255, 255, 255, 0))
		#    elif item[0] == 0 and item[1] == 0 and item[2] == 0:
		#	newData.append((255, 255, 255, 0))
    		#    else:
        	#	newData.append(item)
	    	#im.putdata(newData)

	    	#im.save(quicklookFilepath, "PNG")
		
	    	metadataStr = metadataStr + """
    <entry>
        <id>http://""" + host + """/wpsoutputs/""" + uid + """/""" + quicklookFile + """</id>
        <title type="text">""" + quicklookFile + """</title>
        <published>""" + date_and_time + """Z</published>
        <updated>""" + date_and_time + """Z</updated>
        <link href="http://""" + host + """/wpsoutputs/""" + uid + """/""" + quicklookFile + """?op=OPEN" rel="enclosure" type="application/octet-stream"/>
        <identifier xmlns="http://purl.org/dc/elements/1.1/">""" + quicklookFile + """</identifier>
        <where xmlns="http://www.georss.org/georss/10" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <Polygon xmlns="http://www.opengis.net/gml">
            <exterior>
              <LinearRing>
	        <posList srsDimension="2">""" + ul_y + ' ' + ul_x + ' ' + ul_y + ' ' + lr_x + ' ' + lr_y + ' ' + lr_x + ' ' + lr_y + ' ' + ul_x + ' ' + ul_y + ' ' + ul_x + """</posList>
              </LinearRing>
            </exterior>
          </Polygon>
        </where>
        <box xmlns="http://www.georss.org/georss">""" + ul_y + ' ' + ul_x + ' ' + lr_y + ' ' + lr_x + """</box>
        <offering xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.opengis.net/owc/1.0" code="http://www.opengis.net/spec/owc-atom/1.0/req/png">
          <content href="http://""" + host + """/wpsoutputs/""" + uid + """/""" + quicklookFile + """?op=OPEN" type="image/png" />
        </offering>
    </entry>
    """

	    except Exception as e:
		pass
		
		'''
		try:
			#quicklookFile = outputName + '.png'
			quicklookFile = 'quicklook.png'
                	quicklookFilepath = outputDir + '/' + quicklookFile
			os.system('/opt/anaconda/bin/gdal_translate -of "PNG" -scale -q ' + raster + ' ' + quicklookFilepath)
			metadataStr = metadataStr + """
    <entry>
        <id>http://""" + host + """/wpsoutputs/""" + uid + """/""" + quicklookFile + """</id>
        <title type="text">""" + quicklookFile + """</title>
        <published>""" + date_and_time + """Z</published>
        <updated>""" + date_and_time + """Z</updated>
        <link href="http://""" + host + """/wpsoutputs/""" + uid + """/""" + quicklookFile + """?op=OPEN" rel="enclosure" type="application/octet-stream"/>
        <identifier xmlns="http://purl.org/dc/elements/1.1/">""" + quicklookFile + """</identifier>
        <where xmlns="http://www.georss.org/georss/10" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <Polygon xmlns="http://www.opengis.net/gml">
            <exterior>
              <LinearRing>
                <posList srsDimension="2">""" + ul_y + ' ' + ul_x + ' ' + ul_y + ' ' + lr_x + ' ' + lr_y + ' ' + lr_x + ' ' + lr_y + ' ' + ul_x + ' ' + ul_y + ' ' + ul_x + """</posList>
              </LinearRing>
            </exterior>
          </Polygon>
        </where>
        <box xmlns="http://www.georss.org/georss">""" + ul_y + ' ' + ul_x + ' ' + lr_y + ' ' + lr_x + """</box>
        <offering xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.opengis.net/owc/1.0" code="http://www.opengis.net/spec/owc-atom/1.0/req/png">
          <content href="http://""" + host + """/wpsoutputs/""" + uid + """/""" + quicklookFile + """?op=OPEN" type="image/png" />
        </offering>
    </entry>
    """

		except Exception as ex:
			pass		
		'''
    	metadataStr = metadataStr + """<identifier xmlns="http://purl.org/dc/elements/1.1/">localdata</identifier>
    <queryTime xmlns="http://purl.org/dc/elements/1.1/">0.0002</queryTime>
    <startIndex xmlns="http://a9.com/-/spec/opensearch/1.1/">1</startIndex>
    <itemsPerPage xmlns="http://a9.com/-/spec/opensearch/1.1/">50</itemsPerPage>
    <os:Query os:count="50" os:language="" os:searchTerms="" os:startIndex="" os:startPage="" xmlns:os="http://a9.com/-/spec/opensearch/1.1/" xmlns:param="http://a9.com/-/spec/opensearch/extensions/parameters/1.0/"/>
</feed>
    """
        f.write(metadataStr)
        f.close()

    else:
        remoteDir = remoteDir.replace('\r','')
	remoteDir = remoteDir.replace(' ','')
	user = user.replace('\r','')
        user = user.replace(' ','')
	password = password.replace('\r','')
        password = password.replace(' ','')

	if user == "None" or password == "None":
		w = QWidget()
		QMessageBox.warning(w, "Warning", "Storage username and password are mandatory.", QMessageBox.Ok);
	else:
		check_credentials = subprocess.Popen("curl -u '" + user + "':'" + password + "' https://store.terradue.com/" + user + "/",shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
		check_credentials.wait()
		w = QWidget()
		if 'Bad credentials' in check_credentials.stdout.read():
	               	QMessageBox.warning(w, "Warning", "Wrong user or password.", QMessageBox.Ok);
		else:
			f = open(outputDir + '/metadata.xml', 'w')
        		metadataStr = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title type="text">Discovery feed for WPS result local data</title>"""

			outputRaster = os.path.basename(raster)
		        outputName, ext = os.path.splitext(outputRaster)
        		ext = ext[1:]

	        	data = gdal.Open(raster, GA_ReadOnly)
	        	width = data.RasterXSize
		        height = data.RasterYSize
        		gt = data.GetGeoTransform()
		        ul_x = str(gt[0])
        		ul_y = str(gt[3] + width*gt[4] + height*gt[5])
	        	lr_x = str(gt[0] + width*gt[1] + height*gt[2])
		        lr_y = str(gt[3])

		        date_and_time = datetime.datetime.now().isoformat()
        		host = socket.gethostname()
		        uid = os.path.basename(os.path.normpath(outputDir))

			if remoteDir == '/':
				os.system("curl -u '" + user + "':'" + password + "' -X PUT https://store.terradue.com/" + user + "/" + outputRaster + " -T " + raster)
			else:
				os.system("curl -u '" + user + "':'" + password + "' -X PUT https://store.terradue.com/" + user + "/" + remoteDir + '/' + outputRaster + " -T " + raster)

			metadataStr = metadataStr + """
    <entry>
	<identifier xmlns="http://purl.org/dc/elements/1.1/">""" + remoteDir + '/' + outputRaster + """</identifier>
        <title type="text">""" + outputRaster + """</title>
        <georss:polygon xmlns:georss="http://www.georss.org/georss">""" + ul_y + ' ' + ul_x + ' ' + ul_y + ' ' + lr_x + ' ' + lr_y + ' ' + lr_x + ' ' + lr_y + ' ' + ul_x + ' ' + ul_y + ' ' + ul_x + """</georss:polygon>
        <published>""" + date_and_time + """Z</published>
	<updated>""" + date_and_time + """Z</updated>
	"""
			if remoteDir == '/':
        			metadataStr = metadataStr + """<link href="https://store.terradue.com/""" + user + "/" + outputRaster + """" rel="enclosure" type="application/octet-stream"/>
    </entry>"""
			else:
				metadataStr = metadataStr + """<link href="https://store.terradue.com/""" + user + "/" + remoteDir + '/' + outputRaster + """" rel="enclosure" type="application/octet-stream"/>
    </entry>"""

	        	if quicklook == True:
	        	    try:
        	        	QgsApplication.setPrefixPath("/usr/", True)
	        	        QgsApplication.initQgis()
        	        	quicklookFile = outputName + '.png'
	                	quicklookFilepath = outputDir + '/' + quicklookFile

		                fileInfo = QFileInfo(raster)
        		        baseName = fileInfo.baseName()
	                	rlayer = QgsRasterLayer(raster, baseName)

		                QgsMapLayerRegistry.instance().addMapLayer(rlayer)

	        	        w=rlayer.width()
        	        	h=rlayer.height()
	        	        img = QImage(QSize(w, h), QImage.Format_ARGB32_Premultiplied)
        	        	color = QColor(255, 255, 255)
	                	img.fill(color.rgb())

		                p = QPainter()
        		        p.begin(img)
                		p.setRenderHint(QPainter.Antialiasing)

		                render = QgsMapRenderer()

        		        lst = [rlayer.id()]
                		render.setLayerSet(lst)

	                	rect = QgsRectangle(render.fullExtent())
	        	        rect.scale(1.0)

		                render.setExtent(rect)
        		        render.setOutputSize(img.size(), img.logicalDpiX())
                		render.render(p)
		                p.end()

        		        img.save(quicklookFilepath,"png")

                		#im = Image.open(quicklookFilepath)

		                #datas = im.getdata()
        		        #newData = []
                		#for item in datas:
	                	#    if item[0] == 255 and item[1] == 255 and item[2] == 255:
	        	        #        newData.append((255, 255, 255, 0))
        	        	#    elif item[0] == 0 and item[1] == 0 and item[2] == 0:
                	        #	newData.append((255, 255, 255, 0))
		                #    else:
        		        #        newData.append(item)
                		#im.putdata(newData)

	                	#im.save(quicklookFilepath, "PNG")

			        if remoteDir == '/':
        			        os.system("curl -u '" + user + "':'" + password + "' -X PUT https://store.terradue.com/" + user + "/" + quicklookFile + " -T " + quicklookFilepath)
			        else:
        			        os.system("curl -u '" + user + "':'" + password + "' -X PUT https://store.terradue.com/" + user + "/" + remoteDir + '/' + quicklookFile + " -T " + quicklookFilepath)

	                	metadataStr = metadataStr + """
    <entry>
	<identifier xmlns="http://purl.org/dc/elements/1.1/">""" + remoteDir + '/' + quicklookFile + """</identifier>
        <title type="text">""" + quicklookFile + """</title>
        <georss:polygon xmlns:georss="http://www.georss.org/georss">""" + ul_y + ' ' + ul_x + ' ' + ul_y + ' ' + lr_x + ' ' + lr_y + ' ' + lr_x + ' ' + lr_y + ' ' + ul_x + ' ' + ul_y + ' ' + ul_x + """</georss:polygon>
        <published>""" + date_and_time + """Z</published>
	<updated>""" + date_and_time + """Z</updated>
		"""
				if remoteDir == '/':
        		        	metadataStr = metadataStr + """<link href="https://store.terradue.com/""" + user + "/" + quicklookFile + """" rel="enclosure" type="application/octet-stream"/>
    </entry>"""
        			else:
                			metadataStr = metadataStr + """<link href="https://store.terradue.com/""" + user + "/" + remoteDir + '/' + quicklookFile + """" rel="enclosure" type="application/octet-stream"/>
    </entry>"""


		            except Exception as e:
        		        w = QWidget()
                		QMessageBox.critical(w, "Error", "Quicklook generation failed.", QMessageBox.Ok);

			metadataStr = metadataStr + """
</feed>
    """

        		f.write(metadataStr)
	        	f.close()

			os.system("curl -u '" + user + "':'" + password + "' -XPOST -H 'Accept: application/json' -H 'Content-Type: application/atom+xml' -d@" + outputDir + "/metadata.xml" + " 'https://catalog.terradue.com/" + user + "'")
			w = QWidget()
			QMessageBox.information(w, "Information", "Output(s) uploaded with success", QMessageBox.Ok);

elif vector:

    outputDir = os.path.dirname(vector)

    if "/var/www/wps/wpsoutputs" in outputDir:

    	f = open(outputDir + '/metadata.xml', 'w')
    	metadataStr = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title type="text">Discovery feed for WPS result local data</title>
    <subtitle type="text">This OpenSearch Service allows the discovery of the different items which are part of the localdata collection. This search service is in accordance with the OGC 10-032r3 specification.</subtitle>
    <generator>Terradue Web Server</generator>
        """

    	outputVector = os.path.basename(vector)
    	outputName, ext = os.path.splitext(outputVector)
    	ext = ext[1:]

	g = ogr.Open( vector )
    	layer = g.GetLayer( 0 )
    	lyr = layer.GetExtent()
    	ul_x = str(lyr[0])
    	ul_y = str(lyr[3])
    	lr_x = str(lyr[1])
    	lr_y = str(lyr[2])

    	date_and_time = datetime.datetime.now().isoformat()
    	host = socket.gethostname()
    	uid = os.path.basename(os.path.normpath(outputDir))

    	metadataStr = metadataStr + """
    <entry>
        <id>http://""" + host + """/wpsoutputs/""" + uid + """/""" + outputVector + """</id>
        <title type="text">""" + outputVector + """</title>
        <published>""" + date_and_time + """Z</published>
        <updated>""" + date_and_time + """Z</updated>
        <link href="http://""" + host + """/wpsoutputs/""" + uid + """/""" + outputVector + """?op=OPEN" rel="enclosure" type="application/octet-stream"/>
        <identifier xmlns="http://purl.org/dc/elements/1.1/">""" + outputVector + """</identifier>
        <where xmlns="http://www.georss.org/georss/10" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <Polygon xmlns="http://www.opengis.net/gml">
            <exterior>
              <LinearRing>
	        <posList srsDimension="2">""" + ul_y + ' ' + ul_x + ' ' + ul_y + ' ' + lr_x + ' ' + lr_y + ' ' + lr_x + ' ' + lr_y + ' ' + ul_x + ' ' + ul_y + ' ' + ul_x + """</posList>
              </LinearRing>
            </exterior>
          </Polygon>
        </where>
        <box xmlns="http://www.georss.org/georss">""" + ul_y + ' ' + ul_x + ' ' + lr_y + ' ' + lr_x + """</box>
        <offering xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.opengis.net/owc/1.0" code="http://www.opengis.net/spec/owc-atom/1.0/req/png">
          <content href="http://""" + host + """/wpsoutputs/""" + uid + """/""" + outputVector + """?op=OPEN" type="image/""" + ext + """" />
        </offering>
    </entry>
    """

    	### IMPLEMENT QUICKLOOK FOR VECTOR DATA ###

    	metadataStr = metadataStr + """<identifier xmlns="http://purl.org/dc/elements/1.1/">localdata</identifier>
    <queryTime xmlns="http://purl.org/dc/elements/1.1/">0.0002</queryTime>
    <startIndex xmlns="http://a9.com/-/spec/opensearch/1.1/">1</startIndex>
    <itemsPerPage xmlns="http://a9.com/-/spec/opensearch/1.1/">50</itemsPerPage>
    <os:Query os:count="50" os:language="" os:searchTerms="" os:startIndex="" os:startPage="" xmlns:os="http://a9.com/-/spec/opensearch/1.1/" xmlns:param="http://a9.com/-/spec/opensearch/extensions/parameters/1.0/"/>
</feed>
    """
    	f.write(metadataStr)
    	f.close()

    else:
        remoteDir = remoteDir.replace('\r','')
        remoteDir = remoteDir.replace(' ','')
        user = user.replace('\r','')
        user = user.replace(' ','')
        password = password.replace('\r','')
        password = password.replace(' ','')

	if user == "None" or password == "None":
                w = QWidget()
                QMessageBox.warning(w, "Warning", "Storage username and password are mandatory.", QMessageBox.Ok);
	else:
		check_credentials = subprocess.Popen("curl -u '" + user + "':'" + password + "' https://store.terradue.com/" + user + "/",shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                check_credentials.wait()
                w = QWidget()
                if "Bad credentials" in check_credentials.stdout.read():
                        QMessageBox.warning(w, "Warning", "Wrong user or password.", QMessageBox.Ok);
                else:
			f = open(outputDir + '/metadata.xml', 'w')
        		metadataStr = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title type="text">Discovery feed for WPS result local data</title>"""

			outputVector = os.path.basename(vector)
	        	outputName, ext = os.path.splitext(outputVector)
		        ext = ext[1:]

        		g = ogr.Open( vector )
		        layer = g.GetLayer( 0 )
        		lyr = layer.GetExtent()
	        	ul_x = str(lyr[0])
		        ul_y = str(lyr[3])
        		lr_x = str(lyr[1])
		        lr_y = str(lyr[2])

        		date_and_time = datetime.datetime.now().isoformat()
	        	host = socket.gethostname()
	        	uid = os.path.basename(os.path.normpath(outputDir))

		        if remoteDir == '/':
        		        os.system("curl -u '" + user + "':'" + password + "' -X PUT https://store.terradue.com/" + user + "/" + outputVector + " -T " + vector)
		        else:
        		        os.system("curl -u '" + user + "':'" + password + "' -X PUT https://store.terradue.com/" + user + "/" + remoteDir + '/' + outputVector + " -T " + vector)

			metadataStr = metadataStr + """
    <entry>
        <identifier xmlns="http://purl.org/dc/elements/1.1/">""" + remoteDir + '/' + outputVector + """</identifier>
        <title type="text">""" + outputVector + """</title>
        <georss:polygon xmlns:georss="http://www.georss.org/georss">""" + ul_y + ' ' + ul_x + ' ' + ul_y + ' ' + lr_x + ' ' + lr_y + ' ' + lr_x + ' ' + lr_y + ' ' + ul_x + ' ' + ul_y + ' ' + ul_x + """</georss:polygon>
        <published>""" + date_and_time + """Z</published>
	<updated>""" + date_and_time + """Z</updated>
	"""
	        	if remoteDir == '/':
        	        	metadataStr = metadataStr + """<link href="https://store.terradue.com/""" + user + "/" + outputVector + """" rel="enclosure" type="application/octet-stream"/>
    </entry>"""
	        	else:
        	        	metadataStr = metadataStr + """<link href="https://store.terradue.com/""" + user + "/" + remoteDir + '/' + outputVector + """" rel="enclosure" type="application/octet-stream"/>
    </entry>"""

		        ### IMPLEMENT QUICKLOOK FOR VECTOR DATA ###

        		metadataStr = metadataStr + """
</feed>
    """
	        	f.write(metadataStr)
	        	f.close()

			os.system("curl -u '" + user + "':'" + password + "' -XPOST -H 'Accept: application/json' -H 'Content-Type: application/atom+xml' -d@" + outputDir + "/metadata.xml" + " 'https://catalog.terradue.com/" + user + "'")
			w = QWidget()
			QMessageBox.information(w, "Information", "Output(s) uploaded with success", QMessageBox.Ok);

else:
    w = QWidget()
    QMessageBox.warning(w, "Warning", "Select an output to upload.", QMessageBox.Ok);

