#!/bin/sh
export PATH="$PATH:/home/azureuser/.local/bin/"
cd /home/azureuser/resfes && yarn build && yarn start
