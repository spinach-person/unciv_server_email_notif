#!/bin/bash

cd /home/juice/unciv_server/

bash ./update.sh

java -jar UncivServer.jar -p 25565
