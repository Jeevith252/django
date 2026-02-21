from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages   
from .models import Students
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def hello(request):
    if(request.method == 'POST'):
        data = request.POST
        name =data.get('name')
        email =data.get('email')
        age =data.get('age')
        adress=data.get('adress')
        
        Students.objects.create(
            name= name,
            email=email,
            age=age,
            adress=adress
        )
        print("The data is added succesfully")
    stu =Students.objects.all()
    
    if(request.GET.get('search')):
        stu =Students.objects.filter(name__icontains =request.GET.get('search') )
    
    print(stu)
    hello12="This is a String"
    con = {'hell':stu}
    return render(request,"j.html",con)

@login_required(login_url='/login/')
def dell(request, id):
    if request.method == "POST":
        Students.objects.get(id=id).delete()
    return redirect('/')

@login_required(login_url='/login/')
def upda(request,id):
    record=Students.objects.all().get(id=id)
    if(request.method == 'POST'):
        data =request.POST
        name =data.get('name')
        email =data.get('email')
        age =data.get('age')
        adress=data.get('adress')
        record.name=name
        record.email=email
        record.age=age
        record.adress=adress
        
        record.save()
        print("Updated")
        return redirect('/')
    return render(request,'update.html',{'hell' : record})

def register_pg(req):
    if req.method == 'POST':
        data = req.POST
        
        fname = data.get('first_name')
        lname = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(req, "Username already exists")
            return redirect('register')   

        user = User.objects.create(
            first_name=fname,
            last_name=lname,
            username=username
        )
        
        user.set_password(password)   
        user.save()

        return redirect('/admin/')   

    return render(req, "register.html")

def login_pg(req):
    if (req.method == "POST"):
        data =req.POST
        username = data.get("username")
        password = data.get("password")

        user=User.objects.filter(username = username)
        if not user.exists():
            messages.error(req,"Username is invalid")
            return redirect('login')

        user=authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect("/") 
        else:
            messages.error(req,"Password is invalid")
            return redirect("/login/")
    return render(req, "login.html")

def logout_pg(req):
    logout(req)
    return redirect("/login/")