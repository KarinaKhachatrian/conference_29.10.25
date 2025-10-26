FROM python:3.12-slim-bullseye

WORKDIR /app/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .
COPY model ./model

RUN apt-get update && \
    apt-get install -y libxrender1 libxext6 libsm6 libexpat1 && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 80

CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "80"]