from rest_framework.routers import DefaultRouter
from .views import ScenarioViewSet, ScenarioStepViewSet

router = DefaultRouter()
router.register(r"scenarios", ScenarioViewSet)
router.register(r"steps", ScenarioStepViewSet)

urlpatterns = router.urls
