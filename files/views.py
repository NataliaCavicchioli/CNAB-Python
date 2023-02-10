
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template import loader

from .forms import FileForm
from .models import File


class Home(TemplateView):
    template_name = "home.html"



def upload(request):
    if request.method == "POST" and request.FILES['document']:
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })

    
    return render(request, 'upload.html')

def view(request):
    template = loader.get_template('view.html')

    try:
        file = open("media/CNAB.txt", "r")
        # content = file.read()

        lines = file.readlines()
        list_dicts = []

        for line in lines:
            type = line[0:1]
            date = line[1:9]
            value = line[9:19]
            cpf = line[19:30]
            card = line[30:42]
            hour = line[42:48]
            store_owner = line[48:62]
            store_name = line[62:81]

            store_name = {
            "type": type,
            "date": date,
            "value": value,
            "cpf": cpf,
            "card": card,
            "hour": hour,
            "store_owner": store_owner,
            "store_name": store_name,
            }

            list_dicts.append(store_name)


        
        # context = {"list": list_dicts}
        
        print(list_dicts)
        
    finally:
        file.close()

    return render(request, 'view.html', {"list": list_dicts})