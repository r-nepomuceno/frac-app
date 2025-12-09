# Sprint 1 — Review

**Date:** November 12, 2025  
**Sprint Goal:** Set up Django project foundation with basic models, database, and deployment infrastructure  
**Status:** ✅ **ACHIEVED**

---

## What's Working (Demo)

### 1. Django Project Structure
- Project initialized with proper settings configuration
- Apps created: `classifieds` app for core functionality
- Static files configuration in place

### 2. Database Models
- **ExecutiveProfile model** with fields:
  - name, title, bio
  - skills_text, rate_text
  - email, timezone
  - created_at timestamp
- **Job model** with fields:
  - title, company, description_text
  - duration_text, budget_text
  - contact_email, is_active
  - created_at timestamp

### 3. Admin Interface
- Django admin accessible at `/admin/`
- Models registered and manageable
- Sample data can be added through admin

### 4. Database Configuration
- SQLite working locally for development
- PostgreSQL connection string configured for Render
- Migrations created and tracked in version control

### 5. Version Control
- GitHub repository created: `https://github.com/r-nepomuceno/frac-app`
- `.gitignore` properly configured
- Initial commits with meaningful messages

---

## Completed Stories

| User Story | Story Points | Status | Notes |
|-----------|--------------|--------|-------|
| Project setup (Django + Git) | 3 | ✅ Complete | Django 5.2.8, Git initialized |
| ExecutiveProfile model | 5 | ✅ Complete | All fields implemented |
| Job/Opportunity model | 5 | ✅ Complete | Basic job posting model |
| Database configuration | 3 | ✅ Complete | Local + Render setup |
| Admin interface setup | 2 | ✅ Complete | Models registered |
| Basic templates structure | 3 | ✅ Complete | Template directories created |

**Planned:** 21 pts  
**Completed:** 21 pts  
**Velocity:** 21  
**Completion rate:** 100%

---

## Incomplete Stories

None - all planned stories completed.

---

## Lessons Learned

### What Worked Well
1. **Clean project structure** - Following Django conventions made setup smooth
2. **Early database planning** - Thinking through models upfront saved rework
3. **Version control discipline** - Good commit messages helped track progress

### Challenges Encountered
1. **Model field naming** - Initially used generic names like `description_text`, later refined
2. **PostgreSQL vs SQLite** - Different behaviors required testing on both databases
3. **Static files confusion** - WhiteNoise configuration took some debugging

### Technical Decisions
- Used `CharField` for text fields with max_length instead of `TextField` for better validation
- Chose simple field names over complex nested structures
- Decided to add user ownership in Sprint 2 (not Sprint 1)

---

## Backlog Updates

**Moving to Sprint 2:**
- User authentication and ownership
- Public-facing views (list and detail pages)
- Health check endpoint
- Production deployment to Render
- Static file serving with WhiteNoise

**Deferred to Later Sprints:**
- Search and filtering
- Advanced form validation
- Image uploads
- Email notifications

---

## Deployment Status

- **Local environment:** ✅ Working
- **Staging/Production:** ⏳ Planned for Sprint 2
- **Database:** SQLite (local), PostgreSQL ready for deployment

---

## Velocity & Metrics

- **Sprint 1 Velocity:** 21 points
- **Completion Rate:** 100%
- **Team Satisfaction:** 8/10

**Sprint 2 Forecast:** 20-24 points based on Sprint 1 performance

---

## Next Steps

Sprint 2 will focus on:
1. Deploying to Render with PostgreSQL
2. Creating public-facing views
3. Adding user authentication
4. Implementing health check endpoint
5. Configuring static file serving