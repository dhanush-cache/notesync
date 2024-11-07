from django.db.models.aggregates import Avg
from django.shortcuts import render
from rest_framework import viewsets

from content import models, serializers


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = models.Chapter.objects.all()
    serializer_class = serializers.ChapterSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.prefetch_related("courses").all()
    serializer_class = serializers.StudentSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = models.Content.objects.all().annotate(
        average_rating=Avg("rating__score")
    )
    serializer_class = serializers.ContentSerializer
