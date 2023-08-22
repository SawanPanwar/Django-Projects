from django.shortcuts import render, redirect
from .ctl.UserCtl import UserCtl
from .ctl.LoginCtl import LoginCtl


def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        UserCtl().submit(request)
        if request.POST["operation"] == "Update":
            return redirect('/ORS/UserList')
    return render(request, 'Registration.html')


def login(request):
    if request.method == 'POST':
        if request.POST["operation"] == "SignUp":
            return redirect('/ORS/Register')
        if request.POST["operation"] == "SignIn":
            user = LoginCtl().authenticate(request)
            print('---------->>>>>', user)
            if (user is None):
                msg = "Invalid ID or Password"
                return render(request, "LoginView.html", {"msg": msg})
            else:
                request.session["user"] = user
                return redirect('/ORS/UserList')
    return render(request, "LoginView.html")


def logout(request):
    request.session['user'] = None
    res = render(request, "LoginView.html")
    return res


def userList(request):
    res = UserCtl().search()
    return render(request, "UserList.html", {"list": res['data']})


def display(request, id=0):
    data = UserCtl().edit(int(id))
    return render(request, "UpdateUser.html", {"data":data})
