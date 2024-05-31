# Hugging Face Report Generator

This project creates a Docker container that periodically generates reports by fetching data from the Hugging Face model hub, compiling a list of the top 10 downloaded models, and then stops. The container can be easily downloaded and run on a Linux machine.

## Prerequisites

- Docker installed on your Linux machine.

## Setup and Usage

### Clone the Repository

First, clone this repository to your local machine:

```
git clone https://github.com/Harsha0111/Precize-Docker-Task
cd Precize-Docker-Task
```

## Build the Docker Image

Build the Docker image using the provided `Dockerfile`:
```
docker build -t huggingface-report .
```

## Run the Docker Container
Run the Docker container to generate the report:

```
docker run --rm huggingface-report
```