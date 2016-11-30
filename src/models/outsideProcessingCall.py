import sys
import os
import re
import traceback

class CmdProgress:

    def error(self, msg):
        print(msg)

    def setText(self, text):
        pass
        #print(text)

    def setPercentage(self, i):
        pass

    def setInfo(self, _):
        pass

    def setCommand(self, _):
        pass

    def setDebugInfo(self, _):
        pass

    def setConsoleInfo(self, text):
        print(text)

    def close(self):
        pass
  
if __name__ == "__main__":
    try:
        # Initialize QGIS and Processing if running as a subprocess
        # Find paths of QGIS Python libraries and of Processing 
        # Assumes OsGeo4W installation
        qgisPath = sys.executable

        qgisPath = os.path.dirname(os.path.dirname(qgisPath))
        qgisPath = os.path.join(qgisPath, "apps", "qgis", "python")
        sys.path.append(qgisPath)

        # Check if processing plugin is in the user directory (priority) or
        # QGIS directory (backup)
        if os.path.isdir(os.path.join(os.path.expanduser("~"), ".qgis2", "python", "plugins", "processing")):
	    processingPath = os.path.join(os.path.expanduser("~"), ".qgis2", "python", "plugins")
        else:
            processingPath = os.path.join(qgisPath, "plugins")
        sys.path.append(processingPath)

        # Initialise QGIS
        from qgis.core import QgsApplication       
        from PyQt4.QtCore import QCoreApplication
        QCoreApplication.setOrganizationName('QGIS')
        QCoreApplication.setApplicationName('QGIS2')        
        app = QgsApplication([], False)
        app.setPrefixPath(os.path.dirname(qgisPath))
        app.initQgis()
        # Initialise Processing

        import processing
        from processing.core.Processing import Processing
        Processing.initialize()
        # Initialise Processing GPF Provider plugin
        from processing_gpf.ProcessingGpfPlugin import ProcessingGpfPlugin
        plugin = ProcessingGpfPlugin(None)
        plugin.initGui()

        # Set progress to be displayed in the command prompt
        progress = CmdProgress()

        # Extract the algorithm name (first command line input) and
        # algorithm parameters (the rest) and run the algorithm
        alg = sys.argv[1]

        if len(sys.argv)>2:
	    params = sys.argv[2:]
	    for i in range(len(params)):
		try:
		    if "." in params[i]:
			params[i] = float(params[i])
		    elif params[i] == "True":
			params[i] = True
		    elif params[i] == "False":
			params[i] = False
		    else:
			params[i] = int(params[i])
		except Exception:
		    pass
        else:
            params = ""

        processing.runalg(alg, *params) #, progress = progress)    

    except :
        e = sys.exc_info()[0]
        print(e)
        traceback.print_exc()

    # Uncomment if you want the process to wait for user input before quitting
    #print("Press Enter...")
    #raw_input()
