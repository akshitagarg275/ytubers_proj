from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.
def home(request):
    sliders=Slider.objects.all()
    team=Team.objects.all()
    all_ytubers=Youtuber.objects.order_by('-created_date')
    featured_ytubers=Youtuber.objects.order_by('created_date').filter(is_featured=True)
    data={'sliders':sliders,'team':team,'all_ytubers':all_ytubers,'featured_ytubers':featured_ytubers}
    return render(request,'webpages/home.html',data)

def about(request):
    return render(request,'webpages/about.html')

def contact(request):
    return render(request,'webpages/contact.html')

def services(request):
    return render(request,'webpages/service.html')