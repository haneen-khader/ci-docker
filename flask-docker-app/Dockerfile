# 1. Base image
FROM python:3.10-slim

# 2. Environment setup
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Working directory
WORKDIR /app

# 4. Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# 5. Expose port
EXPOSE 5000

# 6. Run the app
CMD ["python", "app.py"]
