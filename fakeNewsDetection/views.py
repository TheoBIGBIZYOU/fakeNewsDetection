from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    if request.method == "post":
        # Récupérer les données du formulaire de Django
        title = request.POST.get('title')

        # Préparer les données pour FastAPI
        data = {'title': title}

        # Envoyer la requête POST à FastAPI
        response = requests.post('http://127.0.0.1:8000/predict', json=data)

        # Afficher la réponse de FastAPI
        print(response.json())
    return render(request,'main/index.html')    