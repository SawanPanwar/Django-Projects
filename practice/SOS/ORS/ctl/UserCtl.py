from ..models import User
from ..service.UserService import UserService


class UserCtl:
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

    def submit(self, request):
        self.request_to_form(request.POST)
        s = self.form_to_model(User())
        UserService().save(s)

    def edit(self, id):
        res = UserService().edit(id)
        return res
