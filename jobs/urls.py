from django.urls import path
import jobs.views



urlpatterns = [
    path('', jobs.views.home, name='home'),
    path('jobs/<int:job_id>', jobs.views.detail, name='detail'),

]