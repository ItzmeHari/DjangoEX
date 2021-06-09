from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,'login.html')

def loginCheck(request):
    user_name = request.POST.get('t1')
    password = request.POST.get('t2')

    if user_name == 'hari' and password == 'gopal' :
        return render(request,'welcome.html')
    else:
        return render(request,'error.html')
    
