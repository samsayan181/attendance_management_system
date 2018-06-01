from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from diary.forms import AttendanceForm

def home(request):
	if not request.method == 'GET':
		raise Http404
	return render(request, 'home.html')

def Statistics(request):
	if not request.user.is_superuser:
		raise Http404
	if request.method == 'GET':
		form = AttendanceForm()
		return render(request, 'attendance.html', {'form': form})
	elif request.method == 'POST':
		pass
	else:
		raise Http404