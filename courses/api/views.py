from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import detail_route, action

from ..models import Course, Subject, User
from .serializers import SubjectSerializer, CourseSerializer, UserSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(
        detail=True,
        methods=['post'],
        authentication_classes=(BasicAuthentication,),
        permission_classes=(IsAuthenticated,)
    )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})


class CreateUserView(generics.CreateAPIView):

    model = User
    permission_classes = [
        AllowAny,
    ]
    serializer_class = UserSerializer