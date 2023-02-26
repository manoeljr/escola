from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from escola.models import Aluno, Curso
from escola.models import Matricula

from escola.serializer import AlunoSerializer, CursoSerializer
from escola.serializer import ListaMatriculaAlunoSerializer
from escola.serializer import MatriculaSerializer
from escola.serializer import ListaAlunosMatriculadosSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todas alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursoViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """ Exibindo todas matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculaAluno(generics.ListAPIView):
    """ Listando as matriculas de um aluno ou aluna """

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculaAlunoSerializer


class ListaAlunosMatriculas(generics.ListAPIView):
    """ Listando alunos e alunas matriculados em um curso """

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
