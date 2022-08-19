from django.shortcuts import render,get_object_or_404
from .models import Projects
# Create your views here.
def home(request):
    projects=Projects.objects
    return render(request,'myprojects/home.html',{'projects':projects})

def detail(request,pro_id):
    pro_detail=get_object_or_404(Projects,pk=pro_id)
    return render(request,'myprojects/detail.html',{'pro':pro_detail})