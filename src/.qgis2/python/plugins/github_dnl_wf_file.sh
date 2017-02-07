#!/bin/bash

export wf_file=$1
export wfs_path=$2

cd
#git clone -n https://github.com/hydrology-tep/wois-workflow-share.git --depth 1
cd wois-workflow-share
git checkout HEAD $wf_file

cp $wf_file $wfs_path
