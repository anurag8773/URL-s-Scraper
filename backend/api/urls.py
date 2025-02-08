from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UploadCSV, ScrapingStatus, MetadataResults

urlpatterns = [
    # Authentication Endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # CSV Upload & Scraping
    path('upload/', UploadCSV.as_view(), name='upload_csv'),
    path('status/<int:upload_id>/', ScrapingStatus.as_view(), name='scraping_status'),
    path('results/', MetadataResults.as_view(), name='metadata_results'),
]
