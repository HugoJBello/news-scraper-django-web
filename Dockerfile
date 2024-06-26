# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Mounts the application code to the image
COPY . .
WORKDIR /

EXPOSE 8003

# runs the production server
CMD ["gunicorn", "-b 127.0.0.1:8003", "scraper.wsgi"]