#!/bin/bash

cd
git clone https://github.com/hydrology-tep/wois-workflow-share.git

cd ~/wois-workflow-share

export wf=$1
export wf_name=$2
wf_file=`echo ${wf##*/}`

if grep -Fxq "$wf_name" wf_names_list;
then
	touch name_repeated
else
	if grep -Fq "$wf_file" wf_list;
	then
		touch file_repeated
	else
		cp $wf .
		echo -ne "$wf_name" >> wf_names_list
		echo -ne "$wf_file" >> wf_list
		git add .
		git commit -m "New workflow added"
		git remote add origin https://github.com/hydrology-tep/wois-workflow-share.git
		git push origin master

		cd
	        rm -rf ~/wois-workflow-share

		git clone -n https://github.com/hydrology-tep/wois-workflow-share.git --depth 1
	        cd wois-workflow-share
        	git checkout HEAD $wf_file
	fi
fi
