# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (for future web UI; optional)
EXPOSE 8000

# Set environment variable for OpenAI key (can also use .env)
ENV PYTHONUNBUFFERED=1

# Run app
CMD ["python", "app.py"]