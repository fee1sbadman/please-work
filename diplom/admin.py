from django.contrib import admin
from .models import Discipline, Test, Question

# Register your models here.


admin.site.register(Discipline)
admin.site.register(Test)
admin.site.register(Question)