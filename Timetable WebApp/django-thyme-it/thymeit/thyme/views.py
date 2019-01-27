from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Student, Faculty, Course, Classroom, Timeslot, Schedule
from .serializers import StudentSerializer, FacultySerializer, CourseSerializer, ClassroomSerializer, TimeslotSerializer, ScheduleSerializer


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class FacultyViewSet(ModelViewSet):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ClassroomViewSet(ModelViewSet):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()


class TimeslotViewSet(ModelViewSet):
    serializer_class = TimeslotSerializer
    queryset = Timeslot.objects.all()

class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
