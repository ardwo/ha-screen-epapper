FROM python:3.9-slim-buster

ARG BUILD_FROM
ARG BUILD_ARCH

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install-deps
RUN playwright install chromium

COPY . .

CMD ["python", "-u", "main.py"]
