from django.shortcuts import render, get_object_or_404
from .models import job, resume

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail(request, job_id):
    # print(job_id)
    job_detail = get_object_or_404(job, pk = job_id)
    print(job_detail)
    if job_id == 4:
        resume_detail = resume.objects.filter(id__in = [1,2])
        print(resume_detail)
    elif job_id == 5:
        resume_detail = resume.objects.filter(id__in = [3,4])
        print(resume_detail)
    else:
        resume_detail = resume.objects.filter(id = 5)
    return render(request, 'detail.html', {'job': job_detail, 'resume': resume_detail})

def work(request):
    jobs = job.objects
    return render(request, 'work.html', {'jobs': jobs})