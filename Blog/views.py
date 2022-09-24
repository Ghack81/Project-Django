from django.shortcuts import render

# Create your views here.
def hello(request):
    age_robin = 26
    poids_robin = 100
    #age est une clé que l'on associe une valeur age_robin
    context = {'age':age_robin, 'poids': poids_robin}
    #Passer le rendu du request 
    return render(request, 'index.html', context)