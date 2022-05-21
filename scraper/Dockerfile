# Base image.
FROM python:alpine

# Work directory.
WORKDIR /app

# Updates.
RUN apk update && \
    apk upgrade

# Unprivileged user setup.
RUN addgroup -S rs-scraper && \
    adduser -G rs-scraper -S rs-scraper

# /app permissions.
RUN chown -R rs-scraper:rs-scraper /app

# Set user.
USER rs-scraper

# Install python packages.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy python files.
COPY *.py .

ENTRYPOINT ["python", "/app/scraper.py"]