from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Book
from mysql import connector
def fun(request):
    obj=Book.objects.all()
    return render(request,'ind.html',{"obj":obj})
def save(request):
    # obj = Book(name=request.POST["name"],nofp=int(request.POST["pages"]),prize=int(request.POST["price"]))
    # obj.save()
    db=connector.connect(user='root',password='akshay',host='localhost',database='notesdb',auth_plugin="mysql_native_password")
    cur=db.cursor()
    cur.execute("set sql_safe_updates=0")
    sql="insert into notes_book(name,nofp,prize) values(%s,%s,%s)"
    val=(request.POST["name"],request.POST["pages"],request.POST["price"])
    cur.execute(sql,val) 
    db.commit()
    db.close()
    return JsonResponse({"name":request.POST["name"],"pages":request.POST["pages"],"price":request.POST["price"]})
def dele(request):
    # a=Book.objects.get(name=request.POST["name"],pages=request.POST["pages"],prize=request.POST["price"])
    # a.delete()
    db=connector.connect(user='root',password='akshay',host='localhost',database='notesdb',auth_plugin="mysql_native_password")
    cur=db.cursor()
    cur.execute("set sql_safe_updates=0")
    cur.execute("delete from notes_book where name="+repr(request.POST['name'])+" and nofp="+(request.POST['pages'])+" and prize="+(request.POST['price']))
    db.commit()
    db.close()
    return HttpResponse("delete from notes_book where name="+repr(request.POST['name'])+" and nofp="+(request.POST['pages'])+" and prize="+(request.POST['price']))