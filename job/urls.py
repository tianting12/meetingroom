from django.conf.urls import url
from django.urls import path
from django.conf import settings

from job import views

urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
    path('joblist/job/<int:job_id>/', views.detail, name='detail'),
]