#!/bin/bash

cd
git clone https://github.com/hydrology-tep/wois-workflow-share.git

export wf=$1
cp $wf ~/wois-workflow-share
cd ~/wois-workflow-share

git init
git add .
git commit -m "New workflow added."

git remote add origin https://github.com/hydrology-tep/wois-workflow-share.git

git push origin master

cd
rm -rf ~/wois-workflow-share

git clone https://github.com/hydrology-tep/wois-workflow-share.git
