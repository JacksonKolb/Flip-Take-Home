#!/bin/bash

# Build the Docker image
docker build -t pizza-assistant:1.0.0 .

# Run the Docker container
docker run -it pizza-assistant:1.0.0
