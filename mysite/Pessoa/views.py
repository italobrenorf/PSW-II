from django.http import HttpResponse
from .models import Pessoa

def index(request):

    pessoas = Pessoa.objects.all()
    html = "<table>"
    html += "<tr>"
    html += "<th> Nome </th>"
    html += "<th> Idade </th>"
    html += "</tr>"
    for pessoa in pessoas:
        html += "<tr>"
        html += "<td>" + pessoa.nome + "</td>"
        html += "<td>" + str(pessoa.idade) + "</td>"
        html += "</tr>"
    html += "</table>"

    return HttpResponse(html)

def cria(request):
    return HttpResponse("<h3>Aqui cria!</h3>")

def edita(request):
    return HttpResponse(f"<h3>Aqui edita o registro!</h3>")

def deleta(request):
    return HttpResponse(f"<h3>Aqui deleta o registro!</h3>")