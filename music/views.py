from django.shortcuts import render
from musicbeats.models import Song
def index(request):
    song=Song.objects.all()
    return render(request,'index.html',{'song':song})

