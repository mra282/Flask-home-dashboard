# Home Services Dashboard

**Note: This project is a work in progress and is in its very early stages.**

## Overview

The Home Services Dashboard is a project aimed at integrating various home services into a single, easy-to-use dashboard. Currently, it can pull data from Home Assistant, Pi-hole, and fetch weather data. More integrations are planned for the future.

## Getting Started

To launch the application, you need to have Docker installed on your machine. Run the following command to create the Redis container:

docker-compose up -d

python3 -m venv venv

source ./venv/bin/activate

pip install -r requirements.txt

flask --app run.py run

or 

flask --app run.py run --debug