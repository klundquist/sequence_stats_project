#!/bin/bash
#
mkdir sequence_stats_project
conda create -n hw1 python=3.10
pip install biopython
git init
git add run.sh
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:klundquist/sequence_stats_project.git
git push -u origin main

