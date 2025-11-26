from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import ExecutiveProfile, Job
from .forms import JobForm, ExecutiveProfileForm
import random
from .matching import calculate_match, find_matching_jobs_for_executive, find_matching_executives_for_job, get_dashboard_matches


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
    """User dashboard with suggested matches."""
    my_profiles = ExecutiveProfile.objects.filter(owner=request.user)
    my_jobs = Job.objects.filter(owner=request.user)
    
    # Get all active jobs and profiles for matching
    all_jobs = Job.objects.filter(is_active=True)
    all_executives = ExecutiveProfile.objects.all()
    
    # Get suggested matches
    matches = get_dashboard_matches(request.user, all_jobs, all_executives)
    
    return render(request, "classifieds/dashboard.html", {
        "my_profiles": my_profiles,
        "my_jobs": my_jobs,
        "suggested_jobs": matches['suggested_jobs'][:5],  # Top 5
        "suggested_executives": matches['suggested_executives'][:5],  # Top 5
        "user_has_profile": matches['user_has_profile'],
        "user_has_jobs": matches['user_has_jobs'],
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


def for_startups(request):
    """Landing page for startups looking to hire"""
    return render(request, "classifieds/for_startups.html")


def for_fractionals(request):
    """Landing page for fractional executives"""
    return render(request, "classifieds/for_fractionals.html")


# ========== EXECUTIVE VIEWS ==========

def exec_list(request):
    execs = ExecutiveProfile.objects.order_by("-created_at")
    return render(request, "classifieds/exec_list.html", {"execs": execs})


def exec_detail(request, pk):
    """Executive detail page with job matching for logged-in users."""
    exec_profile = get_object_or_404(ExecutiveProfile, pk=pk)
    
    context = {
        'exec': exec_profile,
        'matching_jobs': [],
    }
    
    # If user is logged in and has job postings, show matches
    if request.user.is_authenticated:
        user_jobs = Job.objects.filter(owner=request.user, is_active=True)
        if user_jobs.exists() and exec_profile.skills_tags:
            for job in user_jobs:
                if job.required_skills_tags:
                    match_info = calculate_match(exec_profile.skills_tags, job.required_skills_tags)
                    if match_info['match_count'] > 0:
                        context['matching_jobs'].append({
                            'job': job,
                            'match_info': match_info,
                        })
    
    return render(request, "classifieds/exec_detail.html", context)


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
    """Job detail page with executive matching for logged-in users."""
    job = get_object_or_404(Job, pk=pk)
    
    context = {
        'job': job,
        'matching_profiles': [],
    }
    
    # If user is logged in and has executive profiles, show matches
    if request.user.is_authenticated:
        user_profiles = ExecutiveProfile.objects.filter(owner=request.user)
        if user_profiles.exists() and job.required_skills_tags:
            for profile in user_profiles:
                if profile.skills_tags:
                    match_info = calculate_match(profile.skills_tags, job.required_skills_tags)
                    if match_info['match_count'] > 0:
                        context['matching_profiles'].append({
                            'profile': profile,
                            'match_info': match_info,
                        })
    
    return render(request, "classifieds/job_detail.html", context)


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


def ab_test(request):
    """
    A/B Test endpoint at /b77952e
    Randomly assigns users to variant A or B and persists in session.
    """
    # Check if user already has a variant assigned
    if 'ab_variant' not in request.session:
        # Randomly assign A or B (50/50 split)
        request.session['ab_variant'] = random.choice(['A', 'B'])
    
    variant = request.session['ab_variant']
    
    # Define variant-specific content
    variants = {
        'A': {
            'headline': 'Find Your Perfect Fractional Executive',
            'subheadline': 'Connect with experienced leaders ready to scale your startup',
            'cta_text': 'Browse Executives',
            'color': '#667eea',  # Purple
        },
        'B': {
            'headline': 'Connect With Top Fractional Talent',
            'subheadline': 'Discover flexible executive solutions for your growing business',
            'cta_text': 'Explore Talent',
            'color': '#48bb78',  # Green
        }
    }
    
    return render(request, 'classifieds/ab_test.html', {
        'variant': variant,
        'content': variants[variant],
    })