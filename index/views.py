from django.shortcuts import render, redirect

# Create your views here.
from index.form import MessageModelForm
from index.models import Message


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def page_error(request, exception):
    return render(request, '500.html', status=500)


def index(request):
    messages = Message.objects.all().order_by("_id")
    if request.method == "POST":
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'index.html', locals())

