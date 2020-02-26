from django.shortcuts import render
from django.views import View

from .models import Headset

# Create your views here.
class ListView(View):

    def get(self, request):
        headsets = Headset.objects.all()

        return render(request, 'index.html', {'headsets': headsets})