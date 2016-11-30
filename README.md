# pywps-wois

This repository includes the WOIS integration (WOIS + new plugins developed), the pywps configuration files and other scripts to orchestrate the connection between pywps and QGIS.

This is the first version of the WOIS integration. Some features are being updated yet.

The folders inside src are:

- /var/www/wps/ : This folder contains the pywps orchestration between the pywps and QGIS. After copied to the VM some changes on the owner/group of the files/processes inside shall be maded:

  drwxr-xr-x 2 apache   woisuser 4096 Jun 13 15:53 logs
  drwxrwsrwx 2 apache   wois     4096 Nov 30 14:41 processes
  -rwxrwxr-x 1 apache   woisuser 1164 Oct  6 16:55 pywps.cfg
  -rwxrwxr-x 1 apache   woisuser 2720 Oct  6 16:52 pywps.wsgi
  -rwxrwxr-x 1 woisuser wois     1051 Oct 14 16:38 run_model.sh
  drwxrwsrwx 4 apache   wois     4096 Nov 30 14:45 wpsoutputs
  
- The folder models shall be on /home/user
- The folder .qgis2 will replace the .qgis2 folder on /home/user

The pywps and the httpd shall be configured before.
Tested on QGIS 2.8.1.
