from django.contrib import admin
from .models import Profile,Education,WorkExperience,Project,Certification
# Register your models here.


admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Project)
admin.site.register(Certification)