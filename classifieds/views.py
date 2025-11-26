from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import ExecutiveProfile, Job
from .forms import JobForm, ExecutiveProfileForm


# ========== AUTHENTICATION VIEWS ==========

def signup_view(request):
    """User registration"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect("home")
    else:
        form = UserCreationForm()
    
    return render(request, "classifieds/signup.html", {"form": form})


def login_view(request):
    """User login"""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to 'next' parameter or home
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    
    return render(request, "classifieds/login.html", {"form": form})


def logout_view(request):
    """User logout"""
    logout(request)
    return redirect("home")


@login_required
def dashboard(request):
    """User dashboard showing their profiles and jobs"""
    my_profiles = ExecutiveProfile.objects.filter(owner=request.user)
    my_jobs = Job.objects.filter(owner=request.user)
    
    return render(request, "classifieds/dashboard.html", {
        "my_profiles": my_profiles,
        "my_jobs": my_jobs,
    })


@login_required
def edit_profile(request, pk):
    """Edit an executive profile (must be owner)"""
    profile = get_object_or_404(ExecutiveProfile, pk=pk)
    
    # Authorization check: only owner can edit
    if profile.owner != request.user:
        return redirect("exec_list")  # Redirect if not owner
    
    if request.method == "POST":
        form = ExecutiveProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ExecutiveProfileForm(instance=profile)
    
    return render(request, "classifieds/edit_profile.html", {
        "form": form,
        "profile": profile
    })


@login_required
def edit_job(request, pk):
    """Edit a job posting (must be owner)"""
    job = get_object_or_404(Job, pk=pk)
    
    # Authorization check: only owner can edit
    if job.owner != request.user:
        return redirect("job_list")  # Redirect if not owner
    
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = JobForm(instance=job)
    
    return render(request, "classifieds/edit_job.html", {
        "form": form,
        "job": job
    })


# ========== HOME ==========

def home(request):
    return render(request, "classifieds/home.html")


# ========== EXECUTIVE VIEWS ==========

def exec_list(request):
    execs = ExecutiveProfile.objects.order_by("-created_at")
    return render(request, "classifieds/exec_list.html", {"execs": execs})


def exec_detail(request, pk):
    obj = get_object_or_404(ExecutiveProfile, pk=pk)
    return render(request, "classifieds/exec_detail.html", {"exec": obj})


@login_required
def create_profile(request):
    """Create a new executive profile (LOGIN REQUIRED)"""
    if request.method == "POST":
        form = ExecutiveProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user  # Assign owner
            profile.save()
            return redirect("exec_list")
    else:
        form = ExecutiveProfileForm()
    
    return render(request, "classifieds/create_profile.html", {"form": form})


# ========== JOB VIEWS ==========

def job_list(request):
    jobs = Job.objects.order_by("-created_at")
    return render(request, "classifieds/job_list.html", {"jobs": jobs})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, "classifieds/job_detail.html", {"job": job})


@login_required
def post_job(request):
    """Post a new job (LOGIN REQUIRED)"""
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user  # Assign owner
            job.save()
            return redirect("job_list")
    else:
        form = JobForm()

    return render(request, "classifieds/post_job.html", {"form": form})