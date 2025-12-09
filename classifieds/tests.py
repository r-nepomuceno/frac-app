from django.test import TestCase, Client
from django.contrib.auth.models import User
from classifieds.models import ExecutiveProfile, Opportunity
from classifieds.matching import (
    get_matching_tags,
    calculate_match,
    find_matching_opportunities_for_executive,
    find_matching_executives_for_opportunity,
)


class ExecutiveProfileModelTests(TestCase):
    """Tests for ExecutiveProfile model"""
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
    
    def test_create_profile(self):
        """Test creating an executive profile"""
        profile = ExecutiveProfile.objects.create(
            name="Jane Doe",
            title="Fractional CFO",
            bio="Experienced CFO",
            location="San Francisco, CA",
            hourly_rate=250,
            skills_tags="finance, strategy, fundraising",
            email="jane@example.com",
            owner=self.user
        )
        self.assertEqual(profile.name, "Jane Doe")
        self.assertEqual(profile.title, "Fractional CFO")
        self.assertEqual(profile.owner, self.user)
    
    def test_get_tags_list(self):
        """Test tag parsing into list"""
        profile = ExecutiveProfile.objects.create(
            name="Test User",
            title="CTO",
            skills_tags="python, django, aws",
            email="test@example.com",
            owner=self.user
        )
        tags = profile.get_tags_list()
        self.assertEqual(tags, ['python', 'django', 'aws'])
    
    def test_get_tags_list_with_spaces(self):
        """Test tag parsing handles extra spaces"""
        profile = ExecutiveProfile.objects.create(
            name="Test User",
            title="CTO",
            skills_tags="python,  django,   aws  ",
            email="test@example.com",
            owner=self.user
        )
        tags = profile.get_tags_list()
        self.assertEqual(tags, ['python', 'django', 'aws'])
    
    def test_rate_display(self):
        """Test rate display property"""
        profile = ExecutiveProfile.objects.create(
            name="Test User",
            title="CFO",
            hourly_rate=300,
            email="test@example.com",
            owner=self.user
        )
        self.assertEqual(profile.rate_display, "$300/hour")
    
    def test_rate_display_none(self):
        """Test rate display when no rate set"""
        profile = ExecutiveProfile.objects.create(
            name="Test User",
            title="CFO",
            email="test@example.com",
            owner=self.user
        )
        self.assertIsNone(profile.rate_display)


class OpportunityModelTests(TestCase):
    """Tests for Opportunity model"""
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
    
    def test_create_opportunity(self):
        """Test creating an opportunity"""
        opportunity = Opportunity.objects.create(
            title="Fractional CFO",
            company="Tech Startup",
            description="Looking for experienced CFO",
            budget_amount=5000,
            budget_period="month",
            duration_amount=6,
            duration_period="months",
            required_skills_tags="finance, strategy",
            contact_email="hiring@techstartup.com",
            owner=self.user
        )
        self.assertEqual(opportunity.title, "Fractional CFO")
        self.assertEqual(opportunity.company, "Tech Startup")
        self.assertEqual(opportunity.owner, self.user)
    
    def test_budget_display(self):
        """Test budget display property"""
        opportunity = Opportunity.objects.create(
            title="Test Job",
            company="Test Co",
            description="Test",
            budget_amount=10000,
            budget_period="month",
            contact_email="test@test.com",
            owner=self.user
        )
        self.assertEqual(opportunity.budget_display, "$10,000 per month")
    
    def test_duration_display(self):
        """Test duration display property"""
        opportunity = Opportunity.objects.create(
            title="Test Job",
            company="Test Co",
            description="Test",
            duration_amount=3,
            duration_period="months",
            contact_email="test@test.com",
            owner=self.user
        )
        self.assertEqual(opportunity.duration_display, "3 months")


class MatchingAlgorithmTests(TestCase):
    """Tests for matching algorithm functions"""
    
    def test_get_matching_tags_exact(self):
        """Test exact tag matching"""
        tags1 = "python, django, aws"
        tags2 = "python, django, react"
        matching = get_matching_tags(tags1, tags2)
        self.assertEqual(matching, {'python', 'django'})
    
    def test_get_matching_tags_case_insensitive(self):
        """Test case-insensitive matching"""
        tags1 = "Python, Django"
        tags2 = "python, django"
        matching = get_matching_tags(tags1, tags2)
        self.assertEqual(matching, {'python', 'django'})
    
    def test_get_matching_tags_no_match(self):
        """Test when no tags match"""
        tags1 = "python, django"
        tags2 = "java, spring"
        matching = get_matching_tags(tags1, tags2)
        self.assertEqual(matching, set())
    
    def test_calculate_match(self):
        """Test match calculation"""
        exec_tags = "finance, strategy, fundraising, operations"
        opp_tags = "finance, strategy, leadership"
        match = calculate_match(exec_tags, opp_tags)
        
        self.assertEqual(match['match_count'], 2)
        self.assertEqual(match['total_required'], 3)
        self.assertEqual(match['matching_tags'], ['finance', 'strategy'])
        self.assertAlmostEqual(match['match_percentage'], 66.7, places=1)
    
    def test_calculate_match_100_percent(self):
        """Test perfect match"""
        exec_tags = "finance, strategy, operations"
        opp_tags = "finance, strategy"
        match = calculate_match(exec_tags, opp_tags)
        
        self.assertEqual(match['match_count'], 2)
        self.assertEqual(match['match_percentage'], 100.0)


class MatchingIntegrationTests(TestCase):
    """Integration tests for matching executives to opportunities"""
    
    def setUp(self):
        self.user1 = User.objects.create_user(username='exec1', password='pass')
        self.user2 = User.objects.create_user(username='startup1', password='pass')
        
        # Create executive profile
        self.executive = ExecutiveProfile.objects.create(
            name="Jane CFO",
            title="Fractional CFO",
            skills_tags="finance, strategy, fundraising",
            email="jane@example.com",
            owner=self.user1
        )
        
        # Create matching opportunity
        self.opportunity = Opportunity.objects.create(
            title="CFO Needed",
            company="Tech Startup",
            description="Need CFO help",
            required_skills_tags="finance, strategy",
            contact_email="hiring@techstartup.com",
            owner=self.user2
        )
    
    def test_find_matching_opportunities(self):
        """Test finding opportunities for executive"""
        opportunities = Opportunity.objects.all()
        matches = find_matching_opportunities_for_executive(self.executive, opportunities)
        
        self.assertEqual(len(matches), 1)
        matched_opp, match_info = matches[0]
        self.assertEqual(matched_opp, self.opportunity)
        self.assertEqual(match_info['match_count'], 2)
    
    def test_find_matching_executives(self):
        """Test finding executives for opportunity"""
        executives = ExecutiveProfile.objects.all()
        matches = find_matching_executives_for_opportunity(self.opportunity, executives)
        
        self.assertEqual(len(matches), 1)
        matched_exec, match_info = matches[0]
        self.assertEqual(matched_exec, self.executive)
        self.assertEqual(match_info['match_count'], 2)


class ViewTests(TestCase):
    """Tests for views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
    
    def test_home_page(self):
        """Test home page loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Frac')
    
    def test_exec_list_page(self):
        """Test executive list page loads"""
        response = self.client.get('/executives/')
        self.assertEqual(response.status_code, 200)
    
    def test_opportunity_list_page(self):
        """Test opportunity list page loads"""
        response = self.client.get('/opportunities/')
        self.assertEqual(response.status_code, 200)
    
    def test_create_profile_requires_login(self):
        """Test that profile creation requires login"""
        response = self.client.get('/executives/create/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_create_profile_when_logged_in(self):
        """Test profile creation when logged in"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/executives/create/')
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_requires_login(self):
        """Test dashboard requires login"""
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_ab_test_endpoint(self):
        """Test A/B test endpoint"""
        response = self.client.get('/b77952e/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="abtest"')
        # Check that variant is assigned
        self.assertIn('ab_variant', self.client.session)
    
    def test_ab_test_variant_persistence(self):
        """Test that A/B variant persists in session"""
        # First visit
        self.client.get('/b77952e/')
        variant1 = self.client.session['ab_variant']
        
        # Second visit
        self.client.get('/b77952e/')
        variant2 = self.client.session['ab_variant']
        
        # Should be same variant
        self.assertEqual(variant1, variant2)


class AuthenticationTests(TestCase):
    """Tests for authentication flows"""
    
    def setUp(self):
        self.client = Client()
    
    def test_signup(self):
        """Test user signup"""
        response = self.client.post('/signup/', {
            'username': 'newuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        # Should redirect after successful signup
        self.assertEqual(response.status_code, 302)
        # User should be created
        self.assertTrue(User.objects.filter(username='newuser').exists())
    
    def test_login(self):
        """Test user login"""
        # Create user
        User.objects.create_user(username='testuser', password='testpass123')
        # Login
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_logout(self):
        """Test user logout"""
        User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)