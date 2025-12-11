from django.http import HttpResponse
from django.db import connection

def db_test(request):
    try:
        connection.cursor()
        return HttpResponse("DATABASE CONNECTED SUCCESSFULLY ✔")
    except Exception as e:
        return HttpResponse(f"DATABASE ERROR ❌: {e}")
