from rest_framework import routers
from .api_views import NoteViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = router.urls
