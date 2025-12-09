# Sprint 3 Report - Fractional Executive Marketplace

**Team Members**: Dylan Safyer, Henry Melzner, Joseph Dobson, Robby Nepomuceno, Wit Wattananimitgul  
**Project**: Frac App - Fractional Executive Marketplace  
**Sprint Duration**: November 12-19, 2025  
**Date Submitted**: November 19, 2025

---

## 1. Sprint Goal & Achievement

**Sprint Goal**: Complete core marketplace functionality: Users can create executive profiles, browse executives, post jobs, and browse job listings with a professional UI.

**Achievement**: ✅ **GOAL MET**

We successfully completed all 21 planned story points, delivering two complete user journeys with professional styling and full CRUD functionality for both executives and jobs. The application is deployed and functional on Render with a PostgreSQL database.

---

## 2. User Journey Demo

### Complete User Journey 1: Executive Finding Opportunities

1. **Landing Page** → Executive visits home page (`/`) and sees hero section with four clear call-to-action buttons
2. **Profile Creation** → Clicks "Create Your Profile" button, navigates to `/executives/create/`
3. **Form Completion** → Fills out comprehensive profile form:
   - Name, professional title, bio
   - Skills (comma-separated list)
   - Hourly rate range (e.g., "$150-200/hr")
   - Email and timezone
4. **Profile Submission** → Submits form, redirected to `/executives/` list view
5. **Profile Display** → Sees their profile displayed as a professional card with rate badge, skills, and "View Profile" button
6. **Job Discovery** → Clicks "Jobs" in navigation bar, navigates to `/jobs/`
7. **Job Browsing** → Browses available job listings shown as cards with budget badges, company names, and duration labels
8. **Job Details** → Clicks on interesting job to view full description at `/jobs/<id>/`
9. **Application** → Reviews job details and clicks "Apply Now" to contact company via email

### Complete User Journey 2: Company Hiring Executives

1. **Landing Page** → Company representative visits home page
2. **Executive Discovery** → Clicks "Browse Executives" button, navigates to `/executives/`
3. **Talent Browsing** → Views grid of executive profile cards showing rates, titles, and skills
4. **Profile Review** → Clicks on promising candidate to see full profile with bio, timezone, and contact information
5. **Job Posting** → Clicks "Post a Job" in navigation or from home page, navigates to `/jobs/post/`
6. **Job Form** → Completes job posting form with:
   - Job title and company name
   - Detailed description
   - Duration (e.g., "3-6 months")
   - Budget range (e.g., "$5-8k/month")
   - Contact email
7. **Job Submission** → Submits form, redirected to `/jobs/` list
8. **Job Verification** → Sees their newly posted job in the job board

**Key Feature**: Both journeys are fully functional end-to-end with no authentication required (appropriate for MVP scope). Navigation is consistent across all pages, and all forms include proper validation.

---

## 3. Completed Work

### Story Points Breakdown

| User Story | Story Points | Status | Implementation Details |
|-----------|--------------|--------|----------------------|
| Executive profile creation form | 5 | ✅ Complete | `ExecutiveProfileForm` with 7 fields, custom labels |
| Executive profile browsing | 3 | ✅ Complete | Card-based grid layout, responsive design |
| Job posting functionality | 5 | ✅ Complete | Enhanced `JobForm` with 6 fields (title, company, description, duration, budget, email) |
| Job listing browsing | 3 | ✅ Complete | Card layout with budget badges and duration labels |
| Site-wide navigation system | 2 | ✅ Complete | Navigation bar on all pages, home page with CTAs |
| Professional UI design | 3 | ✅ Complete | Complete CSS framework, responsive grid, styled forms |
| **Total** | **21** | **100%** | |

### Technical Deliverables Completed
- ✅ Two Django models with full CRUD operations (ExecutiveProfile, Job)
- ✅ Seven complete templates with consistent styling
- ✅ Two form classes with validation and custom labels
- ✅ URL routing with separate configurations for executives and jobs
- ✅ Static file serving configured with WhiteNoise
- ✅ Professional CSS framework (~200 lines)
- ✅ Responsive design (mobile and desktop)
- ✅ Database migrations tracked in version control
- ✅ Deployment automation with `build.sh` script
- ✅ Home page with hero section and clear user paths

---

## 4. Velocity Tracking

### Sprint Velocity Metrics

- **Sprint 2 Velocity**: 15 points
  - Deployed initial application to Render
  - Created basic models for executives and jobs
  - Built initial template structure
  - Configured PostgreSQL database
  
- **Sprint 3 Velocity**: 21 points
  - Completed two full user journeys
  - Implemented comprehensive styling
  - Built navigation system
  - Enhanced forms with all required fields
  
- **Average Velocity**: 18 points per sprint
- **Velocity Improvement**: +40% from Sprint 2 to Sprint 3
- **Cumulative Velocity**: 36 points across Sprints 2-3

### Velocity Analysis

The significant velocity increase (40%) demonstrates:
1. **Team learning curve**: Increased familiarity with Django framework
2. **Better tooling**: Reusable CSS and template patterns
3. **Efficient problem-solving**: Quick debugging of URL routing and static file issues
4. **Realistic estimation**: Story points are calibrated appropriately

**Sprint 4 Forecast**: 20-22 story points based on established velocity trend.

---

## 5. Technical Progress

### What's Working Well

**1. Django Framework Implementation**
- Clean separation of concerns (models, views, templates, forms)
- Proper use of Django conventions and best practices
- Effective URL routing with separate configuration files

**2. Deployment Pipeline**
- Automated builds with `build.sh` script
- Static file collection and serving via WhiteNoise
- Database migrations run automatically on deployment
- Zero-downtime deployments to Render

**3. User Interface**
- Professional, cohesive design system
- Responsive layouts that work on all screen sizes
- Intuitive navigation with consistent patterns
- Accessible forms with clear labels

**4. Code Organization**
- Logical file structure following Django conventions
- Reusable CSS classes and template patterns
- Clear naming conventions
- Version-controlled migrations

### Technical Challenges Remaining

**1. No User Authentication** (Priority: High)
- Current state: Anyone can create/edit any content
- Impact: Not production-ready without user ownership
- Plan: Implement Django authentication in Sprint 4

**2. Limited Search/Filtering** (Priority: Medium)
- Current state: Users must scroll through all listings
- Impact: Poor UX with large datasets
- Plan: Add search by skills, budget, title in Sprint 4

**3. Basic Form Validation** (Priority: Medium)
- Current state: Forms have basic Django validation only
- Impact: Could allow malformed data
- Plan: Add custom validators and better error messages

**4. No Image/File Uploads** (Priority: Low)
- Current state: Text-only profiles and jobs
- Impact: Less engaging user experience
- Plan: Add profile photos and company logos in Sprint 5

**5. Manual Email Contact** (Priority: Low)
- Current state: Users must manually email each other
- Impact: Friction in application process
- Plan: Build in-app messaging in Sprint 5

---

## 6. Sprint Retrospective Highlights

### What Went Well
1. **Rapid problem-solving**: Fixed critical URL routing bug within minutes using systematic debugging
2. **Efficient styling implementation**: Achieved professional design in under 20 minutes with focused CSS work
3. **100% story completion**: All planned work finished, demonstrating accurate estimation

### What Didn't Go Well
1. **Static file configuration**: Initial template syntax errors required rework
2. **Late integration testing**: URL routing bug wasn't caught until end-to-end testing

### Key Action Items for Sprint 4
1. **Create end-to-end testing checklist** to catch integration issues earlier
2. **Build base template** with common elements to prevent missing tags
3. **Deploy incrementally** after each feature rather than all at once
4. **Add URL configuration tests** to catch routing issues automatically

### Team Dynamics
The team demonstrated strong problem-solving abilities and adaptability. Communication was clear, and velocity improved significantly. Team health: 8/10.

---

## 7. Sprint 4 Preview

### Planned Features (21 story points)

**High Priority: User Authentication (8 points)**
- User registration and login system
- Password reset functionality
- User-specific dashboards

**High Priority: Content Ownership (5 points)**
- Link profiles/jobs to user accounts
- Users can edit/delete only their own content
- Display "Posted by" information

**Medium Priority: Search & Filtering (5 points)**
- Search executives by skills or title
- Filter jobs by budget range
- Sort listings by date or rate

**Medium Priority: Enhanced Validation (3 points)**
- Email verification
- Rate/budget format validation
- Skills tag parsing and validation

### Strategic Direction
Sprint 4 focuses on moving from MVP to production-ready by adding essential user authentication and ownership features. This foundation enables advanced features like messaging, notifications, and analytics in Sprint 5.

---

## 8. Links & Resources

### Live Application
- **Staging Environment**: https://frac-app.onrender.com

### GitHub Repository
- **Repository**: https://github.com/r-nepomuceno/frac-app
- **Main Branch**: All Sprint 3 code merged
- **Sprint 3 Commits**: https://github.com/r-nepomuceno/frac-app/commits/main

### Sprint Documentation (in GitHub)
- **Sprint 3 Planning**: https://github.com/r-nepomuceno/frac-sprint-board/blob/main/docs/sprints/sprint-3-planning.md
- **Sprint 3 Review**: https://github.com/r-nepomuceno/frac-sprint-board/blob/main/docs/sprints/sprint-3-review.md
- **Sprint 3 Retrospective**: https://github.com/r-nepomuceno/frac-sprint-board/blob/main/docs/sprints/sprint-3-retrospective.md

### Project Management
- **GitHub Project Board**: https://github.com/users/r-nepomuceno/projects/1
- **Sprint 3 Milestone**: All 6 user stories closed
- **Sprint 4 Backlog**: 4 user stories planned

---

## Summary

Sprint 3 successfully delivered on all commitments with 100% story completion (21/21 points). The application now provides two complete, functional user journeys with professional styling and intuitive navigation. 

**Key Achievements**:
- ✅ Two working user journeys (executive and company paths)
- ✅ Professional UI with responsive design
- ✅ 40% velocity improvement over Sprint 2
- ✅ Clean codebase following Django best practices
- ✅ Deployed and functional on Render

**Next Steps**: Sprint 4 will focus on user authentication and search functionality, building on this solid MVP foundation to create production-ready features.

**Project Status**: ✅ On track for successful final submission
