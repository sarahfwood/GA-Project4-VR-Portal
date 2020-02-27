from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Headset
from .serializers import HeadsetSerializer

# Create your views here.
class ListView(APIView):

    def get(self, _request):
        headsets = Headset.objects.all()
        serializer = HeadsetSerializer(Headsets, many=True)

        return Response(serializer.data)


class DetailView(APIView):

    def get(self, _request, pk):
        headset = Headset.objects.get(pk=pk)
        serializer = HeadsetSerializer(headset)

        return Response(serializer.data)