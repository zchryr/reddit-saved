# Base image.
FROM python:slim-bullseye

# Work directory.
WORKDIR /app

# Updates.
RUN apt update && \
    apt -y upgrade && \
    apt -y dist-upgrade

# Unprivileged user setup.
RUN addgroup --gid 1001 --system scraper && \
    adduser --disabled-password --uid 1001 --system --group scraper && \
    chown -R scraper:scraper /app
USER scraper

# Install python packages.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy python files.
COPY *.py .

ENTRYPOINT ["python", "/app/scraper.py"]