from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.settings import api_settings


from .models import Project, Pledge
from .permissions import IsOwnerOrReadOnly
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer


# Create your views here.
class ProjectList(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS  # this is DRF magic to get the defaults from settings.py
    filterset_fields = ['owner__username', 'is_open']
    search_fields = ['title']

    def filter_queryset(self, queryset):
        """ take a queryset and apply the filter backends above, this is a copy of what the generic views do """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        projects = Project.objects.all()
        projects = self.filter_queryset(projects)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(instance=project, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['anonymous', 'project']

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)
