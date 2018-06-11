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
			counts[attendance.course] = counts.get(attendance.course, 0) + 1
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

def statbyDate(request):
	courses = Course.objects.all()
	attendances = Attendance.objects.all()
	date = course = None
	if request.method == "POST":
		date = request.POST.get('date', None)
		course = request.POST.get('course', None)
		if date:
			attendances = attendances.filter(date=date)
		if course:
			course = Course.objects.get(pk=course)
			attendances = attendances.filter(course=course)
	print(attendances)
	return render(request, 'statdate.html', { "courses" : courses, "attendances": attendances, "date": date, "course": course})

def statAll(request):
	courses = Course.objects.all().order_by('name')
	attendances = Attendance.objects.all()
	total_lectures = attendances.count()
	data = {}
	total_course = [0] * courses.count()
	total_lectures = Attendance.objects.count()
	for student in Student.objects.all():
		data[student.name] = { 'roll_no' : student.roll_no , 'attendances': [0] * courses.count() , 'total' : 0, 'percentage': 0}
	index = 0
	for course in courses:
		for attendance in Attendance.objects.filter(course=course):
			total_course[index] += 1
			for student in attendance.students.all():
				data[student.name]['total'] += 1
				data[student.name]['percentage'] = data[student.name]['total'] / total_lectures * 100 
				data[student.name]['attendances'][index] += 1
		index += 1
	return render(request, 'allstat.html', {'courses': courses, 'data': data, 'total_lectures': total_lectures, 'total_course': total_course})
