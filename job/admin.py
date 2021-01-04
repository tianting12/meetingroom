from django.contrib import admin

from job.models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date') # 隐藏 创建人 创建时间 修改时间
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date') #显示的
    
    def save_model(self, request, obj, form, change):
        if obj.creator is None:
            obj.creator = request.user
        super().save_model(request, obj, form, change)




admin.site.register(Job, JobAdmin)