# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password service-user

WORKDIR /service
COPY service /service

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
USER service-user

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]
