from django.shortcuts import render, get_object_or_404, redirect
from .models import ExecutiveProfile, Job
from .forms import JobForm


def exec_list(request):
    execs = ExecutiveProfile.objects.order_by("-created_at")
    return render(request, "classifieds/exec_list.html", {"execs": execs})


def exec_detail(request, pk):
    obj = get_object_or_404(ExecutiveProfile, pk=pk)
    return render(request, "classifieds/exec_detail.html", {"exec": obj})


def post_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobForm()

    return render(request, "classifieds/post_job.html", {"form": form})

def job_list(request):
    jobs = Job.objects.order_by("-created_at")
    return render(request, "classifieds/job_list.html", {"jobs": jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, "classifieds/job_detail.html", {"job": job})
