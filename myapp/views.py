from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import Curso
from . import forms
from django.urls import reverse


def index(request):
    ctx = {
        "nombre": "Juan",
        "cursos": 5,
        "curso_actual": {"nombre": "Python & Django", "turno": "Noche"},
        "cursos_anteriores": ["Java", "PHP", "JavaScript", "Python"]
    }
    return render(request, "myapp/index.html", ctx)

def acerca_de(request):
        return HttpResponse("<html><strong>Curso de Python y Django!</strong></html>")

def cursos(request):
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)



def cursos_json(request):
    cursos = list(Curso.objects.values("nombre", "inscriptos"))
    return JsonResponse(cursos, safe=False)


def curso(request, nombre_curso):
    curso = get_object_or_404(Curso, nombre=nombre_curso)
    ctx = {"curso": curso}
    return render(request, "myapp/curso.html", ctx)


def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            Curso.objects.create(
                nombre=form.cleaned_data["nombre"],
                inscriptos=form.cleaned_data["inscriptos"]
            )
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCurso()
    return render(request, "myapp/nuevo_curso.html", {"form": form})
