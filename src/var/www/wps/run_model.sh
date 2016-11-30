#!/bin/bash

woisuser=woisuser

model=$1
args=("${@:2}")

final_args=()
for input in "${args[@]}"
do
	if [[ $input == *"https://"* ]]; then
		final_input="$(sudo -u ${woisuser} PATH=/opt/anaconda/bin:$PATH /opt/anaconda/bin/python /home/${woisuser}/models/input_intrp.py ${input})"
		final_args+=($final_input)
	else
		final_args+=($input)
	fi
done

args_to_cmd="$(echo ${final_args[*]})"

sudo -u ${woisuser} PYTHONPATH=/usr/local/share/qgis/python:/home/${woisuser}/.qgis2/python/plugins:/usr/local/share/qgis/python/plugins:$PYTHONPATH LD_LIBRARY_PATH=/usr/local/lib/:/usr/local/qwtpolar-0.1.0/lib/:/usr/local/qwt-5.2.3/lib/:/opt/anaconda/lib/:/usr/local/Trolltech/Qt-4.8.5/lib/:$LD_LIBRARY_PATH GDAL_DATA=/opt/anaconda/share/gdal PATH=/opt/anaconda/bin:$PATH /opt/anaconda/bin/python /home/${woisuser}/models/outsideProcessingCall.py modeler:${model} ${args_to_cmd}

if [ -f "$final_input" ]; then
	sudo -u ${woisuser} PATH=/opt/anaconda/bin:$PATH /opt/anaconda/bin/python /home/${woisuser}/models/remove_temp_files.py ${final_input}
fi

exit $?

