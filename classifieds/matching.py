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


def calculate_match(executive_tags, opportunity_tags):
    """
    Calculate match score between an executive's skills and an opportunity's requirements.
    
    Args:
        executive_tags: String or list of executive's skill tags
        opportunity_tags: String or list of opportunity's required skill tags
    
    Returns:
        dict with matching_tags, match_count, match_percentage
    """
    matching = get_matching_tags(executive_tags, opportunity_tags)
    
    # Parse opportunity_tags to get count for percentage calculation
    if isinstance(opportunity_tags, str):
        opportunity_tag_count = len([t for t in opportunity_tags.split(',') if t.strip()])
    else:
        opportunity_tag_count = len([t for t in opportunity_tags if t.strip()])
    
    # Calculate percentage based on opportunity requirements
    if opportunity_tag_count > 0:
        percentage = (len(matching) / opportunity_tag_count) * 100
    else:
        percentage = 0
    
    return {
        'matching_tags': sorted(list(matching)),
        'match_count': len(matching),
        'match_percentage': round(percentage, 1),
        'total_required': opportunity_tag_count,
    }


def find_matching_opportunities_for_executive(executive, all_opportunities):
    """
    Find opportunities that match an executive's skills.
    
    Args:
        executive: ExecutiveProfile instance
        all_opportunities: QuerySet of Opportunity instances
    
    Returns:
        List of (opportunity, match_info) tuples, sorted by match_count descending
    """
    if not executive.skills_tags:
        return []
    
    matches = []
    for opportunity in all_opportunities:
        if not opportunity.required_skills_tags:
            continue
        
        match_info = calculate_match(executive.skills_tags, opportunity.required_skills_tags)
        
        if match_info['match_count'] > 0:
            matches.append((opportunity, match_info))
    
    # Sort by match count (highest first), then by percentage
    matches.sort(key=lambda x: (x[1]['match_count'], x[1]['match_percentage']), reverse=True)
    
    return matches


def find_matching_executives_for_opportunity(opportunity, all_executives):
    """
    Find executives that match an opportunity's requirements.
    
    Args:
        opportunity: Opportunity instance
        all_executives: QuerySet of ExecutiveProfile instances
    
    Returns:
        List of (executive, match_info) tuples, sorted by match_count descending
    """
    if not opportunity.required_skills_tags:
        return []
    
    matches = []
    for executive in all_executives:
        if not executive.skills_tags:
            continue
        
        match_info = calculate_match(executive.skills_tags, opportunity.required_skills_tags)
        
        if match_info['match_count'] > 0:
            matches.append((executive, match_info))
    
    # Sort by match count (highest first), then by percentage
    matches.sort(key=lambda x: (x[1]['match_count'], x[1]['match_percentage']), reverse=True)
    
    return matches


def get_dashboard_matches(user, all_opportunities, all_executives):
    """
    Get suggested matches for a user's dashboard.
    
    Returns:
        dict with 'suggested_opportunities' and 'suggested_executives'
    """
    from .models import ExecutiveProfile, Opportunity
    
    result = {
        'suggested_opportunities': [],
        'suggested_executives': [],
        'user_has_profile': False,
        'user_has_opportunities': False,
    }
    
    # Get user's executive profiles
    user_profiles = ExecutiveProfile.objects.filter(owner=user)
    user_opportunities = Opportunity.objects.filter(owner=user)
    
    result['user_has_profile'] = user_profiles.exists()
    result['user_has_opportunities'] = user_opportunities.exists()
    
    # Find matching opportunities for user's executive profiles
    if user_profiles.exists():
        for profile in user_profiles:
            opportunity_matches = find_matching_opportunities_for_executive(
                profile, 
                all_opportunities.exclude(owner=user)
            )
            for opportunity, match_info in opportunity_matches[:5]:  # Top 5
                result['suggested_opportunities'].append({
                    'opportunity': opportunity,
                    'match_info': match_info,
                    'profile': profile,
                })
    
    # Find matching executives for user's opportunity postings
    if user_opportunities.exists():
        for opportunity in user_opportunities:
            exec_matches = find_matching_executives_for_opportunity(
                opportunity, 
                all_executives.exclude(owner=user)
            )
            for executive, match_info in exec_matches[:5]:  # Top 5
                result['suggested_executives'].append({
                    'executive': executive,
                    'match_info': match_info,
                    'opportunity': opportunity,
                })
    
    return result