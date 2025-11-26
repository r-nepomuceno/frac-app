def get_matching_tags(tags1, tags2):
    """
    Find matching tags between two comma-separated tag strings or lists.
    Returns a set of matching tags (lowercase, stripped).
    """
    if isinstance(tags1, str):
        set1 = set(tag.lower().strip() for tag in tags1.split(',') if tag.strip())
    else:
        set1 = set(tag.lower().strip() for tag in tags1 if tag.strip())
    
    if isinstance(tags2, str):
        set2 = set(tag.lower().strip() for tag in tags2.split(',') if tag.strip())
    else:
        set2 = set(tag.lower().strip() for tag in tags2 if tag.strip())
    
    return set1.intersection(set2)


def calculate_match(executive_tags, job_tags):
    """
    Calculate match score between an executive's skills and a job's requirements.
    
    Args:
        executive_tags: String or list of executive's skill tags
        job_tags: String or list of job's required skill tags
    
    Returns:
        dict with matching_tags, match_count, match_percentage
    """
    matching = get_matching_tags(executive_tags, job_tags)
    
    # Parse job_tags to get count for percentage calculation
    if isinstance(job_tags, str):
        job_tag_count = len([t for t in job_tags.split(',') if t.strip()])
    else:
        job_tag_count = len([t for t in job_tags if t.strip()])
    
    # Calculate percentage based on job requirements
    if job_tag_count > 0:
        percentage = (len(matching) / job_tag_count) * 100
    else:
        percentage = 0
    
    return {
        'matching_tags': sorted(list(matching)),
        'match_count': len(matching),
        'match_percentage': round(percentage, 1),
        'total_required': job_tag_count,
    }


def find_matching_jobs_for_executive(executive, all_jobs):
    """
    Find jobs that match an executive's skills.
    
    Args:
        executive: ExecutiveProfile instance
        all_jobs: QuerySet of Job instances
    
    Returns:
        List of (job, match_info) tuples, sorted by match_count descending
    """
    if not executive.skills_tags:
        return []
    
    matches = []
    for job in all_jobs:
        if not job.required_skills_tags:
            continue
        
        match_info = calculate_match(executive.skills_tags, job.required_skills_tags)
        
        if match_info['match_count'] > 0:
            matches.append((job, match_info))
    
    # Sort by match count (highest first), then by percentage
    matches.sort(key=lambda x: (x[1]['match_count'], x[1]['match_percentage']), reverse=True)
    
    return matches


def find_matching_executives_for_job(job, all_executives):
    """
    Find executives that match a job's requirements.
    
    Args:
        job: Job instance
        all_executives: QuerySet of ExecutiveProfile instances
    
    Returns:
        List of (executive, match_info) tuples, sorted by match_count descending
    """
    if not job.required_skills_tags:
        return []
    
    matches = []
    for executive in all_executives:
        if not executive.skills_tags:
            continue
        
        match_info = calculate_match(executive.skills_tags, job.required_skills_tags)
        
        if match_info['match_count'] > 0:
            matches.append((executive, match_info))
    
    # Sort by match count (highest first), then by percentage
    matches.sort(key=lambda x: (x[1]['match_count'], x[1]['match_percentage']), reverse=True)
    
    return matches


def get_dashboard_matches(user, all_jobs, all_executives):
    """
    Get suggested matches for a user's dashboard.
    
    Returns:
        dict with 'suggested_jobs' and 'suggested_executives'
    """
    from .models import ExecutiveProfile, Job
    
    result = {
        'suggested_jobs': [],
        'suggested_executives': [],
        'user_has_profile': False,
        'user_has_jobs': False,
    }
    
    # Get user's executive profiles
    user_profiles = ExecutiveProfile.objects.filter(owner=user)
    user_jobs = Job.objects.filter(owner=user)
    
    result['user_has_profile'] = user_profiles.exists()
    result['user_has_jobs'] = user_jobs.exists()
    
    # Find matching jobs for user's executive profiles
    if user_profiles.exists():
        # Use the first profile's tags (or combine all)
        for profile in user_profiles:
            job_matches = find_matching_jobs_for_executive(profile, all_jobs.exclude(owner=user))
            for job, match_info in job_matches[:5]:  # Top 5
                result['suggested_jobs'].append({
                    'job': job,
                    'match_info': match_info,
                    'profile': profile,
                })
    
    # Find matching executives for user's job postings
    if user_jobs.exists():
        for job in user_jobs:
            exec_matches = find_matching_executives_for_job(job, all_executives.exclude(owner=user))
            for executive, match_info in exec_matches[:5]:  # Top 5
                result['suggested_executives'].append({
                    'executive': executive,
                    'match_info': match_info,
                    'job': job,
                })
    
    return result