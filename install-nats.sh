#!/bin/bash

# Download the get-pip.py script:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Run the get-pip.py script to install pip:
python get-pip.py

# Install pip and kafka-python
pip install nats-py