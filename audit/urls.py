from django.urls import path

from audit.views import recent_logs_view


urlpatterns = [
    path("logs/", recent_logs_view, name="recent_logs"),
]

app_name = "audit"
