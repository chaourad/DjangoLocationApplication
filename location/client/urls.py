from rest_framework import routers

from location.client.views import ClientSet

router = routers.DefaultRouter()
router.register('client', ClientSet , basename="client")