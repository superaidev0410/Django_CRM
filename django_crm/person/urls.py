from django.urls import include, path
from rest_framework import routers
from person.views import PersonalInfoViewsets

router = routers.DefaultRouter()
router.register(r'info', PersonalInfoViewsets)

urlpatterns = [
   path('', include(router.urls)),
]
