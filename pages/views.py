from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def home(request):
    hora_atual = datetime.now().hour

    if hora_atual < 12:
        saudacao = "Bom dia"
    else:
        saudacao = "Boa tarde"

    contexto = {
        "mensagem": f"{saudacao}! São {datetime.now().strftime("%H:%M")}h. Servidor ligado e respondendo. Atividade(s) da UC3, você colocou um back-end no ar.",
        "nome_aluno": "Nielsen Moreira",
        "curso": "Programação em Python - Módulo UC3: Desenvolver aplicações back-end para web com Python"
    }

    return render(request, "pages/home.html", contexto)

def contato(request):
    nome = "Nielsen"
    return render(request, "pages/contato.html", context={"nome":nome})

def saudacao(request, nome):
    return HttpResponse(
            f"<h1>Olá, {nome}! Bem-vindo(a) ao Senac!</h1>"
    )

