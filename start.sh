#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd SCRIPT_DIR

bash ./update.sh

java -jar UncivServer.jar -p 25565
