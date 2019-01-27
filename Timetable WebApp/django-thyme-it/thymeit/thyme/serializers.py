from rest_framework import serializers
from .models import Student, Faculty, Course, Classroom, Timeslot, Schedule

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'student_name', 'batch', 'course_id')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('faculty_id', 'faculty_name', 'faculty_type', 'faculty_contact', 'sex')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id','course_code', 'description', 'course_type', 'semester', 'faculty_id')


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('room_id', 'room_number', 'room_capacity')

class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslot
        fields = ('slot_id', 'slot_type')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('schedule_id', 'description', 'student_id', 'course_id', 'faculty_id', 'room_id', 'slot_id')
