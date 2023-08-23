from ..service.UserService import UserService
from django.shortcuts import render, redirect


class UserListCtl:
    count = 1

    def __init__(self):
        self.form = {}
        self.form["pageNo"] = 1

    def request_to_form(self, requestForm):
        self.form['firstName'] = requestForm.get("firstName", None)
        self.form['ids'] = requestForm.getlist('ids', None)

    def search(self, request):
        if request.method == 'POST':
            self.form['firstName'] = request.POST["firstName"]
        record = UserService().search(self.form)
        data = record['data']
        res = render(request, "UserList.html", {"list": data, 'form': self.form})
        return res

    def next(self, request):
        UserListCtl.count += 1
        self.form['pageNo'] = UserListCtl.count
        return self.search(request)

    def previous(self, request):
        UserListCtl.count -= 1
        self.form['pageNo'] = UserListCtl.count
        return self.search(request)

    def delete(self, request):
        recordList = request.POST.getlist('ids', None)
        for ids in recordList:
            id = int(ids)
            if (id > 0):
                r = UserService().get(id)
                UserService().delete(r)
        return self.search(request)
