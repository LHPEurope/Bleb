#!/bin/bash

cd /home/pi/Source/Bleb/
git add ./logs
git add ./info
git commit ./logs -m "new data"
git commit ./info -m "new info"
git push -f