from django.shortcuts import render

# Create your views here.

def showIndex(request):
    if request.method == 'GET':
        return render(request,'index.html')
    if request.method == 'POST':
        user_name=request.POST.get('t1')
        password=request.POST.get('t2')

        if user_name == 'hari' and password == 'gopal':
            return render(request,'index.html',{'message':'valid'})
        else:
            return render(request,'index.html',{'message':'invalid'})
    
