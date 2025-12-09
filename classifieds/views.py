from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import ExecutiveProfile, Opportunity
from .forms import OpportunityForm, ExecutiveProfileForm
import random
from .matching import calculate_match, get_dashboard_matches


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
    my_opportunities = Opportunity.objects.filter(owner=request.user)
    
    # Get all active opportunities and profiles for matching
    all_opportunities = Opportunity.objects.filter(is_active=True)
    all_executives = ExecutiveProfile.objects.all()
    
    # Get suggested matches
    matches = get_dashboard_matches(request.user, all_opportunities, all_executives)
    
    return render(request, "classifieds/dashboard.html", {
        "my_profiles": my_profiles,
        "my_opportunities": my_opportunities,
        "suggested_opportunities": matches['suggested_opportunities'][:5],
        "suggested_executives": matches['suggested_executives'][:5],
        "user_has_profile": matches['user_has_profile'],
        "user_has_opportunities": matches['user_has_opportunities'],
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
def edit_opportunity(request, pk):
    """Edit an opportunity posting (must be owner)"""
    opportunity = get_object_or_404(Opportunity, pk=pk)
    
    # Authorization check: only owner can edit
    if opportunity.owner != request.user:
        return redirect("opportunity_list")  # Redirect if not owner
    
    if request.method == "POST":
        form = OpportunityForm(request.POST, instance=opportunity)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = OpportunityForm(instance=opportunity)
    
    return render(request, "classifieds/edit_opportunity.html", {
        "form": form,
        "opportunity": opportunity
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
    """Executive detail page with opportunity matching for logged-in users."""
    exec_profile = get_object_or_404(ExecutiveProfile, pk=pk)
    
    context = {
        'exec': exec_profile,
        'matching_opportunities': [],
    }
    
    # If user is logged in and has opportunity postings, show matches
    if request.user.is_authenticated:
        user_opportunities = Opportunity.objects.filter(owner=request.user, is_active=True)
        if user_opportunities.exists() and exec_profile.skills_tags:
            for opportunity in user_opportunities:
                if opportunity.required_skills_tags:
                    match_info = calculate_match(exec_profile.skills_tags, opportunity.required_skills_tags)
                    if match_info['match_count'] > 0:
                        context['matching_opportunities'].append({
                            'opportunity': opportunity,
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


# ========== OPPORTUNITY VIEWS ==========

def opportunity_list(request):
    opportunities = Opportunity.objects.order_by("-created_at")
    return render(request, "classifieds/opportunity_list.html", {"opportunities": opportunities})


def opportunity_detail(request, pk):
    """Opportunity detail page with executive matching for logged-in users."""
    opportunity = get_object_or_404(Opportunity, pk=pk)
    
    context = {
        'opportunity': opportunity,
        'matching_profiles': [],
    }
    
    # If user is logged in and has executive profiles, show matches
    if request.user.is_authenticated:
        user_profiles = ExecutiveProfile.objects.filter(owner=request.user)
        if user_profiles.exists() and opportunity.required_skills_tags:
            for profile in user_profiles:
                if profile.skills_tags:
                    match_info = calculate_match(profile.skills_tags, opportunity.required_skills_tags)
                    if match_info['match_count'] > 0:
                        context['matching_profiles'].append({
                            'profile': profile,
                            'match_info': match_info,
                        })
    
    return render(request, "classifieds/opportunity_detail.html", context)


@login_required
def post_opportunity(request):
    """Post a new opportunity (LOGIN REQUIRED)"""
    if request.method == "POST":
        form = OpportunityForm(request.POST)
        if form.is_valid():
            opportunity = form.save(commit=False)
            opportunity.owner = request.user  # Assign owner
            opportunity.save()
            return redirect("opportunity_list")
    else:
        form = OpportunityForm()

    return render(request, "classifieds/post_opportunity.html", {"form": form})


def redirect_jobs_to_opportunities(request):
    """Legacy redirect from /jobs/ to /opportunities/"""
    return redirect("opportunity_list", permanent=True)


@login_required
def delete_profile(request, pk):
    """Delete an executive profile (must be owner, POST only)"""
    profile = get_object_or_404(ExecutiveProfile, pk=pk)
    
    # Authorization check: only owner can delete
    if profile.owner != request.user:
        return redirect("dashboard")
    
    if request.method == "POST":
        profile.delete()
    
    return redirect("dashboard")


@login_required
def delete_opportunity(request, pk):
    """Delete an opportunity (must be owner, POST only)"""
    opportunity = get_object_or_404(Opportunity, pk=pk)
    
    # Authorization check: only owner can delete
    if opportunity.owner != request.user:
        return redirect("dashboard")
    
    if request.method == "POST":
        opportunity.delete()
    
    return redirect("dashboard")


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
            'button_text': 'kudos',
            'color': '#48bb78',  # Green
        },
        'B': {
            'button_text': 'thanks',
            'color': '#667eea',  # Blue
        }
    }
    
    return render(request, 'classifieds/ab_test.html', {
        'variant': variant,
        'content': variants[variant],
    })