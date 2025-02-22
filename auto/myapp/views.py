from django.shortcuts import render,redirect
from . models import Login,Team,Normal,News
import datetime


# Create your views here.
def index(request):
    nw=News.objects.all()
    return render(request,'index.html',{'nw':nw})

def login(request):
    nw=News.objects.all()
    return render(request,'login.html',{'nw':nw})

def teamreg(request):
    nw=News.objects.all()
    return render(request,'teamreg.html',{'nw':nw})

def normalreg(request):
    nw = News.objects.all()
    return render(request,'normalreg.html',{'nw':nw})

def normalhome(request):
    nw=News.objects.all()
    return render(request,'normalhome.html',{'nw':nw})

def tmhome(request):
    nw=News.objects.all()
    return render(request,'teamhome.html',{'nw':nw})

def treg(request):
    tmname = request.POST.get('tmname', '')
    tmwork = request.POST.get('tmwork', '')
    tmaddress = request.POST.get('tmaddress', '')
    tmcontactno = request.POST.get('tmcontactno', '')
    tmemailaddress = request.POST.get('tmemailaddress', '')
    aadharno = request.POST.get('aadharno', '')
    panno = request.POST.get('panno', '')
    password = request.POST.get('password', '')
    regdate = datetime.datetime.today()
    usertype = 'team'
    t=Team(tmname=tmname,tmwork=tmwork,tmaddress=tmaddress,tmcontactno=tmcontactno,tmemailaddress=tmemailaddress,aadharno=aadharno,panno=panno,regdate=regdate)
    log=Login(userid=tmemailaddress,password=password,usertype=usertype)
    t.save()
    log.save()
    msg='Registration is successfull'
    return render(request,'teamreg.html',{'msg':msg})


def nreg(request):
    name = request.POST.get('name', '')
    cpname = request.POST.get('cpname', '')
    cpcontactno = request.POST.get('cpcontactno', '')
    cpemailaddress = request.POST.get('cpemailaddress', '')
    gstno = request.POST.get('gstno', '')
    password = request.POST.get('password', '')
    regdate = datetime.datetime.today()
    usertype = 'normal'
    n=Normal(name=name,cpname=cpname,cpcontactno=cpcontactno,cpemailaddress=cpemailaddress,gstno=gstno,regdate=regdate)
    log=Login(userid=cpemailaddress,password=password,usertype=usertype)
    n.save()
    log.save()
    msg='Registration is successfull'
    return render(request,'normalreg.html',{'msg':msg})


def validate(request):
    userid=request.POST['userid']
    password=request.POST['password']
    usertype=request.POST['usertype']
    try:
        obj=Login.objects.get(userid=userid,password=password)
        if obj.usertype=='team':
            request.session['team']=userid
            return redirect('tmhome')
        elif obj.usertype=='normal':
            request.session['normal']=userid
            return redirect('normalhome')
        elif obj.usertype=='admin':
            request.session['admin']=userid
            return redirect('adminhome')
    except:
        msg='Invalid User'
    return render(request,'login.html',{'msg':msg})


