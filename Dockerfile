# Official Python image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /code

# Set env variables
# https://docs.python.org/3/using/cmdline.html#id1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install geodjango dependencies
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin netcat \
    && rm -rf /var/lib/apt

# Update pip and install requirements.txt
RUN pip install --upgrade pip
COPY ./requirements.txt /code
RUN pip install -r requirements.txt

# Copy our code to the container
COPY . /code

# Run entrypoint
ENTRYPOINT [ "/code/docker_entrypoint.sh"]