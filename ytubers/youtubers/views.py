from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Youtuber
# Create your views here.

def youtubers(request):
    youtubers=Youtuber.objects.order_by('-created_date')
    data={
        'youtubers':youtubers
    }
    return render(request,'youtubers/youtubers.html',data)

def search(request):
    tubers=Youtuber.objects.order_by('-created_date')
    camera_search=Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search=Youtuber.objects.values_list('category',flat=True).distinct()
    city_search=Youtuber.objects.values_list('city',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        tubers=tubers.filter(desc__icontains=keyword)
    if 'city' in request.GET:
        city=request.GET['city']
        tubers=tubers.filter(city__iexact=city)
    if 'category' in request.GET:
        category=request.GET['category']
        tubers=tubers.filter(category__iexact=category)
    if 'camera_type' in request.GET:
        camera_type=request.GET['camera_type']
        tubers=tubers.filter(camera_type__iexact=camera_type)
    data={
        'tubers':tubers,
        'camera_search':camera_search,
        'category_search':category_search,
        'city_search':city_search
    }
    return render(request,'youtubers/search.html',data)

def youtuber_detail(request,id):
    
    ytuber=get_object_or_404(Youtuber,pk=id)
    data={
    'ytuber':ytuber
}
    return render(request,'youtubers/youtuber_detail.html',data)
    

    
    