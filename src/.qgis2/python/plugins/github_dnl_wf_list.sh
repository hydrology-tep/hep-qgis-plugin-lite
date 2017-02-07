#!/bin/bash

cd
git clone -n https://github.com/hydrology-tep/wois-workflow-share.git --depth 1

cd wois-workflow-share
git checkout HEAD wf_names_list
git checkout HEAD wf_list
