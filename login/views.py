from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_protect
from login.models import Usuario

@csrf_protect
def index(request):
    menu = ''
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

@csrf_protect
def entrar(request):
    global user
    nome_post = request.POST['nome']
    senha_post = request.POST['senha']
    user = authenticate(username=nome_post, password=senha_post)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('pesquisar.html',
                              {},
                              context_instance=RequestContext(request))
        else:
            return render_to_response('erro.html',
                              {},
                              context_instance=RequestContext(request))
    else:
        return render_to_response('erro.html',
                              {},
                              context_instance=RequestContext(request))

@csrf_protect   
@login_required
def cadastro(request):
    global user
    
    return render_to_response('cadastro.html',
                              {},
                              context_instance=RequestContext(request))

@csrf_protect
@login_required
def cadastrar(request):
    nome_post = request.POST['nome']
    senha_post = request.POST['senha']
    
    usuario_db = Usuario(nome = nome_post, senha = senha_post)
    usuario_db.save()
    
    return render_to_response('cadastrar.html',
                              {'nome':nome_post, 'senha':senha_post},
                              context_instance=RequestContext(request))

@csrf_protect
@login_required
def pesquisar(request):
    
    return render_to_response('pesquisar.html',
                              {},
                              context_instance=RequestContext(request))
    
@csrf_protect
@login_required
def pesquisa(request):
    nome_post = request.POST['nome']
    
    usuarios = Usuario.objects.all()
    usuarios_list = usuarios.filter(nome=nome_post)
    
    return render_to_response('pesquisa.html',
                              {'resultados':usuarios_list},
                              context_instance=RequestContext(request))