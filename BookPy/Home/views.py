from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Bookform
from .models import Book
def home(request):
    return render (request,'base.html')

def formBook(request):
    if request.method == "POST":
        form = Bookform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except: 
                pass
    else:
        form = Bookform()
        return render (request,'index.html',{'form':form})
    
def show(request):
    books = Book.objects.all()
    return render(request, "show.html",{'books':books})

def edit(request, id):
    book = Book.objects.get(id=id)
    return render(request,'edit.html',{'book':book})

def update(request, id):
    book = Book.objects.get(id=id)
    form = Bookform(request.POST,instance=book)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html',{'book':book})

def destroy(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/show")