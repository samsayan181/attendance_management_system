from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Count

from diary.forms import AttendanceForm
from diary.models import Student, Attendance, Course

def home(request):
	if not request.method == 'GET':
		raise Http404
	return render(request, 'home.html')

def StatbyRoll(request):
	students = Student.objects.all()
	return render(request, 'statroll.html', { 'students': students})

def StatByPaper(request):
	papers = Course.objects.all()
	return render(request, 'statpaper.html', {'papers': papers})

def StatStudent(request, pk=None):
	try:
		student = Student.objects.get(pk=pk)
		attendances = Attendance.objects.filter(students__in=[student])
		counts = {}
		for attendance in attendances:
			counts[attendance.course.paper_code] = counts.get(attendance.course.paper_code, 0) + 1
		return render(request, 'statstudent.html', {"counts" : counts, "student": student})
	except:
		raise Http404

def StatPaper(request, pk=None):
	paper = Course.objects.get(pk=pk)
	attendances = Attendance.objects.filter(course=paper)
	total = attendances.count()
	counts = {}
	for attendance in attendances:
		for student in attendance.students.all():
			counts[student.name] = counts.get(student.name, 0) + 1
	return render(request, 'statcourse.html', { "total": total, "counts": counts, 'course': paper})
