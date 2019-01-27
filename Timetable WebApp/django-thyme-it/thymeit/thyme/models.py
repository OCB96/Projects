from django.db import models

# Create your models here.

class Student(models.Model):
    """
    Student Model
    Defines the attributes of a student
    """
    student_id = models.IntegerField(primary_key = True)
    student_name = models.CharField(max_length=255)
    batch = models.IntegerField()
    course_id = models.ForeignKey('Course', on_delete = models.CASCADE)


class Faculty(models.Model):
    """
    Faculty Model
    Defines the attributes of a faculty member
    """
    faculty_id = models.IntegerField(primary_key = True)
    faculty_name = models.CharField(max_length=255)
    faculty_type = models.CharField(max_length=255)
    faculty_contact = models.IntegerField()
    sex = models.CharField(max_length=255)


class Course(models.Model):
    """
    Course Model
    Defines the attributes of a course
    """
    course_id = models.IntegerField(primary_key = True)
    course_code = models.IntegerField()
    description = models.CharField(max_length=255)
    course_type = models.CharField(max_length=255)
    semester = models.IntegerField()
    faculty_id = models.ForeignKey('Faculty', on_delete = models.CASCADE)


class Classroom(models.Model):
    """
    Classroom Model
    Defines the attributes of a classroom
    """
    room_id = models.IntegerField(primary_key = True)
    room_number = models.IntegerField()
    room_capacity = models.IntegerField()


class Timeslot(models.Model):
    """
    Timeslot Model
    Defines the attributes of a timeslot
    """
    slot_id = models.IntegerField(primary_key = True)
    slot_type = models.DateTimeField(auto_now_add=True)


class Schedule(models.Model):
    """
    Schedule Model
    Defines the attributes of a scheduled item
    """
    schedule_id = models.IntegerField(primary_key = True)
    description = models.CharField(max_length=255)
    student_id = models.ForeignKey('Student', on_delete = models.CASCADE)
    course_id = models.ForeignKey('Course', on_delete = models.CASCADE)
    faculty_id = models.ForeignKey('Faculty', on_delete = models.CASCADE)
    room_id = models.ForeignKey('Classroom', on_delete = models.CASCADE)
    slot_id = models.ForeignKey('Timeslot', on_delete = models.CASCADE)
