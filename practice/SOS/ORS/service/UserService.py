from django.db import connection
from ..models import User


class UserService:

    def save(self, mobj):
        mobj.save()

    def authenticate(self, params):
        q = User.objects.filter()
        val = params.get("loginId", None)
        q = q.filter(loginId=val)
        val = params.get("password", None)
        q = q.filter(password=val)
        userList = [user.to_json() for user in q]
        print("=================>>>>>>>>>>>>>>>", type(userList[0]), userList[0])
        if (userList[0]):
            return userList[0]
        else:
            return None

    def search(self):
        sql = "select * from sos_user"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "loginId", "password")
        res = {
            "data": []
        }
        for x in result:
            print(x)
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def edit(self, val):
        q = User.objects.filter()
        q = q.filter(id=val)
        userList = [user.to_json() for user in q]
        if (userList[0]):
            return userList[0]
        else:
            return None
