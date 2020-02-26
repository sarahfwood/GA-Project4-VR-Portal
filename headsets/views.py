from django.shortcuts import render
from django.views import View

from .models import Headset

# Create your views here.
class ListView(View):

    def get(self, request):
        headsets = Headset.objects.all()

        return render(request, 'index.html', {'headsets': headsets})


class DetailView(View):
  
    def get(self, request, pk):
        headset = Headset.objects.get(pk=pk)

        return render(request, 'show.html', {'headset': headset})