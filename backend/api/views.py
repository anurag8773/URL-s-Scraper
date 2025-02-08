import csv
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Upload, Metadata
from .serializers import MetadataSerializer
from .tasks import scrape_url_task


class UploadCSV(APIView):
    """Handles CSV file uploads and triggers scraping tasks asynchronously."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get('file')
        if not file or not file.name.endswith('.csv'):
            return Response({"error": "Only CSV files are allowed"}, status=400)

        file_path = default_storage.save(f"uploads/{file.name}", file)
        upload_instance = Upload.objects.create(user=request.user, file=file_path)

        # Read CSV and trigger Celery tasks
        with default_storage.open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                url = row[0].strip()
                scrape_url_task.delay(request.user.id, url)

        return Response({"message": "File uploaded, scraping started!", "upload_id": upload_instance.id}, status=201)


class ScrapingStatus(APIView):
    """Returns the status of the scraping process based on uploaded file ID."""

    permission_classes = [IsAuthenticated]

    def get(self, request, upload_id):
        upload = Upload.objects.filter(id=upload_id, user=request.user).first()
        if not upload:
            return Response({"error": "Upload not found"}, status=404)

        scraped_count = Metadata.objects.filter(user=request.user).count()
        return Response({"upload_id": upload_id, "scraped_count": scraped_count})


class MetadataResults(ListAPIView):
    """Returns the extracted metadata for a user."""

    permission_classes = [IsAuthenticated]
    serializer_class = MetadataSerializer

    def get_queryset(self):
        return Metadata.objects.filter(user=self.request.user)
