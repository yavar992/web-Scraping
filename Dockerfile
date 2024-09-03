# official python runtime as a parent image
FROM python:3.9-slim

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install the required python package / depdendecy
RUN pip install --no-cache-dir request beautifulsoup4 pandas

# commans to run your project
CMD ["python" , "webscrapping.py"]

