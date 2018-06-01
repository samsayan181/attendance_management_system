from django.contrib import admin
from diary.models import Student, Professor, Course, Attendance
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_filter = ('name', 'roll_no',)
	list_display = ('name', 'roll_no',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
	list_filter = ('name',)
	list_display = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_filter = ('name', 'paper_code', 'taken_by',)
	list_display = ('name', 'paper_code', 'taken_by',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	list_filter = ('course', 'date',)
	list_display = ('course', 'date',)
