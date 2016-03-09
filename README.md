# tornado-template
Python tornado template

# Using with Docker

## Build

    cd tornado-template
    docker build -t tornado-template .

## Run
    
    docker run -d -p 8000:8000 tornado-template

# Using without Docker

## Install

    apt-get update
    apt-get install python2.7 python-pip nodejs
    npm install -g bower
    
    cd tornado-template
    pip install -r requirements.txt
    bower install

## Run
    
    python tornado-template [--debug]
