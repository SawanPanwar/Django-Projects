from ..models import User
from ..service.UserService import UserService
from .BaseCtl import BaseCtl


class LoginCtl(BaseCtl):
    def __init__(self):
        self.form = {}

    def request_to_form(self, requestForm):
        self.form["loginId"] = requestForm["loginId"]
        self.form["password"] = requestForm["password"]

    def form_to_model(self, obj):
        obj.loginId = self.form["loginId"]
        obj.password = self.form["password"]
        return obj

    def authenticate(self, request):
        self.request_to_form(request.POST)
        user = UserService().authenticate(self.form)
        return user
