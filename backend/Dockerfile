# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port for the Django app
EXPOSE 8000

# Run migrations and start Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
