from django.shortcuts import render, get_object_or_404
from .models import job, resume

# Create your views here.
def home(request):
    jobs = job.objects
    return render(request, 'home.html', {'jobs': jobs})

# def detail(request, job_id):
#     # print(job_id)
#     job_detail = get_object_or_404(job, pk = job_id)
#     return render(request, 'detail.html', {'job': job_detail})

def work(request):
    # work_details = job.objects.filter(id = 4)
    jobs = job.objects
    print(job, jobs)
    return render(request, 'work.html', {'jobs': jobs})

def detail(request, job_id):
    resume_detail = get_object_or_404(resume, pk = job_id)
    print(resume_detail, job_id)
    return render(request, 'detail.html', {'resume': resume_detail})
