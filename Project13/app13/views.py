from django.shortcuts import render

# Create your views here.

def showIndex(request):
    if request.method == 'GET' :
        return render(request,'index.html')

    elif request.method == 'POST' :
        user_name= request.POST.get('t1')
        password = request.POST.get('t2')

        if user_name == 'Ravi' and (password == 'ravi1234@' or password == 'kumar@123' or password == 'ravikumar@123'):
            type = request.POST.get('t3')
            if type == 'admin' :
                return render(request,'welcome.html',{'msg':'admin'})
            elif type == 'employee':
                return render(request,'welcome.html',{'msg':'emp'})
            elif type == 'customer':
                return render(request,'welcome.html',{'msg':'customer'})
        else :
            return render(request,'index.html',{'msg':'invalid'})
