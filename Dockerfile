# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Update the package list and install necessary packages
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git
    
RUN pip3 install PyYAML

# Copy the Python script to /usr/bin/
COPY feed.py /usr/bin/feed.py

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Give execute permission to the entrypoint script
RUN chmod +x /entrypoint.sh

# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
