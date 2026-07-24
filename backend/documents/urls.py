from rest_framework.routers import DefaultRouter
from .views import WorkspaceViewSet, DocumentViewSet

router = DefaultRouter()
router.register('workspaces', WorkspaceViewSet, basename='workspace')
router.register('documents', DocumentViewSet, basename='document')

urlpatterns = router.urls