# Use Ubuntu 22.04 LTS as the base image
FROM ubuntu:22.04

# Environment variables for PostgreSQL and Flask
ENV POSTGRES_USER=webuser1
ENV POSTGRES_PASSWORD=student
ENV POSTGRES_DB=csdashboard
ENV POSTGRES_HOST=192.168.56.20
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0  
# Avoid user interaction with apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install necessary packages
RUN apt-get update && \
    apt-get install -y sudo \
    net-tools \
    python3 \
    python3-pip \
    postgresql \
    postgresql-contrib && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a system user for web services
RUN useradd -m -s /bin/bash webuser1

# Set the working directory in the container
WORKDIR /home/student/Docker

# Copy the current directory contents into the container
COPY . /home/student/Docker

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Expose the PostgreSQL port
EXPOSE 5432

# Start Flask app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
