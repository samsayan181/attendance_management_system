from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=200)
	roll_no = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return "{} ({})".format(self.name, self.roll_no)

class Professor(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=200)
	paper_code = models.CharField(max_length=50, unique=True)
	taken_by = models.ForeignKey('Professor', on_delete=models.CASCADE)

	def __str__(self):
		return "{} ({})".format(self.name, self.taken_by)

class Attendance(models.Model):
	course = models.ForeignKey('Course', on_delete=models.CASCADE)
	date = models.DateField()
	students = models.ManyToManyField('Student')

	def __str__(self):
		return "{}-{}".format(self.course, self.date)
