from django.shortcuts import render, redirect
class BaseCtl:
    def execute(self, request):
        path = request.META.get("PATH_INFO")
        print("in execute method....!!!!", path)
        if request.session.get('user') == None :
            print("in ifffffffffffff session none")
            return redirect('/ORS/Login')
        else:
            return redirect(path)

