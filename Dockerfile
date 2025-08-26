FROM python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

EXPOSE 8501
ENV APP_ENV=container
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]