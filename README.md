# Django URL Metadata Scraper

## Overview
This project is a web-based system where users can upload a CSV file containing a list of URLs. The system scrapes each URL asynchronously, extracts meta tags (title, description, keywords), and stores the results securely.

## Features
- User authentication using JWT (JSON Web Token)
- CSV file upload for bulk URL processing
- Asynchronous scraping using Celery and Redis
- Metadata extraction (title, description, keywords)
- PostgreSQL database for data storage
- API endpoints for uploading, checking status, and retrieving metadata
- Docker support for deployment

## Technologies Used
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Task Queue:** Celery with Redis
- **Authentication:** JWT (Django Simple JWT)
- **Containerization:** Docker & Docker Compose

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Redis
- Docker & Docker Compose (for containerized deployment)

### Setup Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/anurag8773/url-s-Scraper.git
   cd url-s-Scraper
   ```
2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the Database:**
   - Set up PostgreSQL and create a database.
   - Update `.env` with database credentials.
5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
8. **Start Redis & Celery:**
   ```bash
   redis-server  # Start Redis
   celery -A myproject worker --loglevel=info  # Start Celery Worker
   ```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/login/` | Authenticate & obtain JWT token |
| POST | `/api/upload/` | Upload CSV file for URL scraping |
| GET | `/api/status/{upload_id}/` | Check scraping status |
| GET | `/api/results/{upload_id}/` | Retrieve extracted metadata |

[Postman](https://documenter.getpostman.com/view/37271849/2sAYX9kek8)

## Docker Deployment
### Build and Run
1. **Build the Docker Containers:**
   ```bash
   docker-compose build
   ```
2. **Start the Application:**
   ```bash
   docker-compose up
   ```
3. **Run Migrations in the Container:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```
4. **Create a Superuser in the Container:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## Troubleshooting
- **Database Connection Issues:** Ensure PostgreSQL is running and credentials in `.env` are correct.
- **Celery Not Processing Tasks:** Check Redis is running and Celery is correctly configured.
- **Docker Issues:** Run `docker-compose logs` to debug errors.

## License
This project is licensed under the MIT License.

## Contributors
- **Anurag Kumar Maurya** - [GitHub](https://github.com/yourgithub)

---
### 🚀 Happy Coding! 🎯

