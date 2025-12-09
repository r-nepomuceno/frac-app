# Frac - Fractional Executive Marketplace

A Django-based marketplace connecting fractional executives with startups seeking part-time, senior-level talent. The platform enables executives to showcase their expertise and companies to post opportunities, with intelligent tag-based matching to connect the right talent with the right opportunities.

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Live Deployment](#live-deployment)
- [Local Development Setup](#local-development-setup)
- [A/B Test Endpoint](#ab-test-endpoint)
- [Project Structure](#project-structure)
- [Team Contributions](#team-contributions)
- [Sprint History](#sprint-history)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)

---

## Problem Statement

Not every company needs a full-time CFO, CTO, or CMO—but every company deserves access to that level of expertise. Traditional hiring models force startups to choose between:
- **Full-time executives:** High cost, long-term commitment, often more capacity than needed
- **No senior leadership:** Missing strategic guidance during critical growth phases
- **Expensive consultants:** Fragmented relationships, inconsistent engagement

**The gap:** There's no dedicated marketplace connecting fractional executives with companies that need their expertise on a flexible, part-time basis.

---

## Solution

Frac provides a two-sided marketplace where:
- **Fractional executives** can create profiles showcasing their skills, rates, and availability
- **Startups and companies** can post opportunities and browse qualified candidates
- **Intelligent matching** connects executives and opportunities based on required skills
- **Transparent pricing** displays rates and budgets upfront
- **Flexible engagements** enable part-time, project-based, or ongoing relationships

---

## Features

### Core Functionality
- **User Authentication** - Secure signup, login, and session management
- **Executive Profiles** - Detailed profiles with skills, rates, location, and bio
- **Opportunity Postings** - Job postings with budget, duration, and required skills
- **User Dashboard** - Personalized view of owned content with suggested matches
- **Tag-Based Matching** - Algorithm matches executives to opportunities based on skills
- **Two-Path UX** - Separate entry points for executives vs. companies

### Advanced Features
- **Suggested Matches** - Dashboard displays ranked matches with match scores
- **Content Ownership** - Users can only edit/delete their own content
- **Professional UI** - Custom CSS framework with responsive design
- **A/B Testing** - Experimental endpoint for analytics and optimization
- **Google Analytics** - Comprehensive tracking across all pages

---

## Technology Stack

### Backend
- **Django 5.2.8** - Python web framework
- **PostgreSQL** - Production database (via Render)
- **SQLite** - Local development database
- **Python 3.11/3.12** - Programming language

### Frontend
- **HTML5** - Semantic markup
- **Custom CSS** - Anthropic-inspired design system (~200 lines)
- **Vanilla JavaScript** - Minimal JS for interactions

### Deployment & Infrastructure
- **Render** - Cloud hosting platform
- **WhiteNoise** - Static file serving
- **Gunicorn** - WSGI HTTP server
- **GitHub** - Version control and CI/CD

### Analytics & Testing
- **Google Analytics 4** - User tracking and behavior analysis
- **Django Testing Framework** - 26 comprehensive tests
- **Ruff** - Python linting and code quality

---

## Live Deployment

### Production
- **URL:** https://frac-app.onrender.com
- **Status:** ✅ Active
- **Database:** PostgreSQL (Render)
- **Deployment:** Auto-deploy on git push to main branch

### A/B Test Endpoint
- **URL:** https://frac-app.onrender.com/b77952e/
- **Description:** Experimental endpoint testing button variants ("kudos" vs "thanks")
- **Tracking:** Google Analytics event tracking

### Staging
- **URL:** (In progress - see staging environment section)
- **Purpose:** Testing environment mirroring production

---

## Local Development Setup

### Prerequisites
- Python 3.11 or 3.12
- pip (Python package manager)
- Git
- PostgreSQL (optional - SQLite works for local development)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/r-nepomuceno/frac-app.git
cd frac-app
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:
```bash
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=  # Leave empty for SQLite
```

To generate a secure SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

5. **Run database migrations**
```bash
python manage.py migrate
```

6. **Create a superuser (optional, for admin access)**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Main site: http://localhost:8000
- Admin panel: http://localhost:8000/admin/
- A/B test: http://localhost:8000/b77952e/

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific test file
python manage.py test classifieds.tests

# Run with verbose output
python manage.py test --verbosity=2
```

### Linting
```bash
# Check code quality
ruff check .

# Auto-fix issues
ruff check . --fix
```

---

## A/B Test Endpoint

### Computing the Endpoint URL

The A/B test endpoint URL is computed from the team nickname using SHA-1 hashing:

```python
import hashlib

team_nickname = "restless-sound"
hash_object = hashlib.sha1(team_nickname.encode())
hex_digest = hash_object.hexdigest()
endpoint = hex_digest[:7]  # First 7 characters

print(f"Endpoint: /{endpoint}/")
# Output: /b77952e/
```

### Endpoint Requirements
- **URL:** `/b77952e/`
- **Button ID:** `id="abtest"` (exact requirement for rubric)
- **Variant A:** Green "kudos" button
- **Variant B:** Blue "thanks" button
- **Session Persistence:** Users see the same variant across visits
- **Public Access:** No authentication required
- **Analytics:** Tracks page views and button clicks in Google Analytics

### Testing the Endpoint

**Local:**
```bash
# Visit the endpoint
open http://localhost:8000/b77952e/
```

**Production:**
```bash
# Visit the endpoint
open https://frac-app.onrender.com/b77952e/
```

Expected behavior:
1. First visit: Random assignment to variant A or B
2. Subsequent visits: Same variant shown (session-based)
3. Button click: Feedback displayed, event sent to Google Analytics
4. Different browser/incognito: Different random assignment

---

## Project Structure

```
frac-app/
├── classifieds/              # Main Django app
│   ├── migrations/           # Database migrations
│   ├── static/               # CSS and static files
│   │   └── frac-app.css      # Custom stylesheet
│   ├── templates/            # HTML templates
│   │   └── classifieds/      # App-specific templates
│   ├── admin.py              # Django admin configuration
│   ├── forms.py              # Django forms
│   ├── matching.py           # Tag matching algorithm
│   ├── models.py             # Database models
│   ├── tests.py              # Test suite (26 tests)
│   ├── urls.py               # URL routing (executives)
│   ├── opportunity_urls.py   # URL routing (opportunities)
│   └── views.py              # View functions
├── fracsite/                 # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Main URL routing
│   └── wsgi.py               # WSGI configuration
├── docs/                     # Project documentation
│   └── sprints/              # Sprint planning/review/retro docs
├── tests/                    # Additional tests
│   └── test_health.py        # Health check test
├── .env.example              # Example environment variables
├── .gitignore                # Git ignore rules
├── build.sh                  # Render build script
├── manage.py                 # Django management script
├── README.md                 # This file
├── render.yaml               # Render deployment config
└── requirements.txt          # Python dependencies
```

---

## Team Contributions

### Team Members
- **Robby Nepomuceno** - Product Owner, Backend Development, Deployment
- **Wit Wattananimitgul** - UX/Research, Frontend Development
- **Dylan Safyer** - Backend Development, Database Design
- **Henry Melzner** - Frontend Development, Testing
- **Joseph Dobson** - Backend Development, Documentation

### Development Approach
- **Agile Methodology** - 4 one-week sprints with planning, review, and retrospectives
- **Version Control** - Git with feature branches and pull requests
- **Code Review** - All changes reviewed before merging to main
- **Test-Driven Development** - 26 tests covering models, views, and matching algorithm
- **Continuous Deployment** - Auto-deploy to Render on push to main branch

---

## Sprint History

### Sprint 1 (Nov 5-12, 2025) - Foundation
- **Goal:** Set up Django project with basic models and database
- **Velocity:** 21 story points
- **Key Deliverables:** Project setup, ExecutiveProfile and Job models, admin interface

### Sprint 2 (Nov 12-19, 2025) - Deployment
- **Goal:** Deploy to Render with PostgreSQL and public views
- **Velocity:** 22 story points
- **Key Deliverables:** Production deployment, WhiteNoise static files, list/detail views

### Sprint 3 (Nov 19-26, 2025) - Core Features
- **Goal:** Authentication, CRUD operations, and professional UI
- **Velocity:** 34 story points
- **Key Deliverables:** User authentication, dashboard, forms, custom CSS framework

### Sprint 4 (Nov 25-26, 2025) - Advanced Features
- **Goal:** Two-path UX, matching algorithm, A/B testing, analytics
- **Velocity:** 39 story points
- **Key Deliverables:** Tag matching, suggested matches, A/B test endpoint, Google Analytics

**Total Velocity:** 116 story points across 4 sprints  
**Average Velocity:** 29 points/sprint  
**Completion Rate:** 100% across all sprints

---

## Testing

### Test Coverage
- **26 comprehensive tests** covering:
  - Model creation and validation
  - Tag parsing and normalization
  - Matching algorithm correctness
  - View authentication and authorization
  - A/B test session persistence
  - Form validation

### Running Tests
```bash
# Run all tests
python manage.py test

# Run with coverage report
python manage.py test --verbosity=2

# Example output:
# Found 26 test(s).
# ..........................
# Ran 26 tests in 10.058s
# OK
```

### Test Categories
1. **Model Tests** - ExecutiveProfile and Opportunity creation
2. **Matching Tests** - Tag matching algorithm accuracy
3. **View Tests** - HTTP responses and authentication
4. **Integration Tests** - End-to-end user flows

---

## Future Enhancements

### High Priority
- **Search & Filtering** - Filter opportunities by budget, skills, location
- **Advanced Matching** - Weighted skills, location proximity, rate compatibility
- **Messaging System** - In-app communication between executives and companies
- **Email Notifications** - Alerts for new matches and messages

### Medium Priority
- **Profile Photos** - Upload and display executive headshots
- **Company Logos** - Branding for opportunity postings
- **Reviews & Ratings** - Feedback system for completed engagements
- **Calendar Integration** - Availability scheduling

### Low Priority
- **Payment Processing** - Secure transactions through the platform
- **Contract Templates** - Pre-built agreements for engagements
- **Mobile Apps** - iOS and Android native applications
- **API Access** - RESTful API for third-party integrations

---

## License

This project is part of an academic assignment for Yale School of Management (MGT 802).

---

## Acknowledgments

- **Django Documentation** - Comprehensive framework guidance
- **Render** - Seamless deployment platform
- **Anthropic Claude** - Development assistance and code review
- **Yale SOM MGT 802** - Course structure and requirements

---

## Contact

For questions or feedback about this project:
- **Repository:** https://github.com/r-nepomuceno/frac-app
- **Live Site:** https://frac-app.onrender.com

---

**Last Updated:** December 8, 2025