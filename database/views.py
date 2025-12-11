from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def db_test(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
        return HttpResponse("DATABASE CONNECTED ✔")
    except Exception as e:
        return HttpResponse("DATABASE ERROR ❌: " + str(e))
