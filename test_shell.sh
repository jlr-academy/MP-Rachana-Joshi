#!/bin/bash 
set -eu
#project_dir = "$Home/Downloads/02 Training/Mini_Project"  
#pytest

if pytest
then
git add .
git commit
else
echo "Test Failed"
fi