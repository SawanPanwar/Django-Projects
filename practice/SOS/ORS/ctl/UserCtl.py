from django.shortcuts import render, redirect
from ..models import User
from ..service.UserService import UserService
from .BaseCtl import BaseCtl


class UserCtl(BaseCtl):
    def __init__(self):
        self.form = {}

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form["firstName"] = requestForm["firstName"]
        self.form["lastName"] = requestForm["lastName"]
        self.form["loginId"] = requestForm["loginId"]
        self.form["password"] = requestForm["password"]

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.firstName = self.form["firstName"]
        obj.lastName = self.form["lastName"]
        obj.loginId = self.form["loginId"]
        obj.password = self.form["password"]
        return obj

    def display(self, request):
        return render(request, self.get_template())

    def submit(self, request):
        self.request_to_form(request.POST)
        s = self.form_to_model(User())
        self.get_service().save(s)
        return render(request, self.get_template())

    def edit(self, id):
        res = UserService().edit(id)
        return res

    def get_service(self):
        return UserService()

    def get_template(self):
        return "Registration.html"
