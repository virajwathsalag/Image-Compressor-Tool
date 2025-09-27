FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Make Python see /app as the root package path
ENV PYTHONPATH=/app

CMD ["python", "Controller/AccessPoint.py"]
EXPOSE 8080