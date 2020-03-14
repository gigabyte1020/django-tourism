import profile

from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
import analyse
from analyse.views import disp, sgts
from guide.models import gdet
from home.models import Profile


def home(request):
    # movie = get_object_or_404(gdet, id=id)
    return render(request,'guidehome.html', {"id": id})
def status(request):
    return render(request,'appstat.html', {"id": id})


def sgt(request):
        if request.method == 'POST':
            if request.POST.get('t1'):
                sgt = sgts()
                sgt.s_name = request.POST.get('t1')
                sgt.s_url = request.POST.get('t2')

                sgt.save()
                return render(request, 'sgt.html')
            else:
                return render(request, 'sgt.html')
        else:
            return render(request, 'sgt.html')

def logout_r(request):
    logout(request)
    return redirect('/')