from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
import analyse
from analyse.views import disp, sgts
from guide.models import bookguide, gdet
from home.models import Profile


def home(request):

    return render(request,'userhome.html', {"id": id})
def holidays(request):
    return redirect('/analyse/disp')

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

def guides(request):
    form = User.objects.all()
    return render(request, 'dispguide.html', {'form': form})


def boo(request):
    if request.method == 'POST':
        gb=bookguide()
        gid=request.POST.get('gid')
        gg = get_object_or_404(User, id=gid)  # id of the packkage
        uid = request.session.get('id')  # user id of the buyer
        us = get_object_or_404(User, id=uid)
        gb.guide=gg
        gb.user=us
        gb.save()
        return render(request, 'success.html')
    else:
        return render(request, 'fail.html')


def logout_r(request):
    logout(request)
    return redirect('/')