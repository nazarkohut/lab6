## service1/Dockerfile
#
## Use an official Python runtime as a parent image
#FROM python:3.8-slim
#
## Set the working directory to /app
#WORKDIR /app
#
## Copy the current directory contents into the container at /app
#COPY app.py /app/
#
## Install any needed packages specified in requirements.txt
## (assuming you have a requirements.txt file)
## RUN pip install --trusted-host pypi.python.org -r requirements.txt
#
## Make port 5000 available to the world outside this container
#EXPOSE 5000
#
## Define environment variable
#ENV NAME service1
#
## Run main.py when the container launches
#CMD ["python", "app.py"]


# service1/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app/

# Install any needed packages specified in requirements.txt
# (assuming you have a requirements.txt file)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME service1

# Run main.py when the container launches
CMD ["python", "app.py"]

