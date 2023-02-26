from django.contrib import admin
from django.urls import path

from escola.views import AlunosViewSet, CursoViewSet

from rest_framework import routers

from escola.views import ListaAlunosMatriculas
from escola.views import ListaMatriculaAluno
from escola.views import MatriculaViewSet

router = routers.DefaultRouter()

router.register('alunos', AlunosViewSet, basename='alunos')
router.register('cursos', CursoViewSet, basename='cursos')
router.register('matriculas', MatriculaViewSet, basename='matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/<int:pk>/matriculas/', ListaMatriculaAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculas.as_view()),
] + router.urls
