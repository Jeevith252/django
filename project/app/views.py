from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Students

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

def dell(request, id):
    print(id)
    Students.objects.get(id=id).delete()
    return redirect('/')

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