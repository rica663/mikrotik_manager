from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class MikrotikDeviceViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["get"])
    def test(self, request):
        return Response({"message": "Devices endpoint funcionando 🚀"})
