# Sprint 2 — Review

**Date:** November 19, 2025  
**Sprint Goal:** Deploy working Django app to staging (Render) with PostgreSQL database and dynamic list/detail pages  
**Status:** ✅ **ACHIEVED**

---

## What's Working (Demo)

### 1. Production Deployment
- **Staging URL:** https://frac-app.onrender.com
- Application deployed and accessible
- Automatic deployments on Git push configured
- Build script (`build.sh`) running successfully

### 2. Database
- PostgreSQL connected via Render-provided database
- Migrations running automatically during build
- Sample data accessible through admin panel
- Database connection pooling configured

### 3. Static Files
- WhiteNoise middleware serving static files
- Django admin styling working correctly
- CSS files loading in production
- `collectstatic` running during build process

### 4. Public Views
- **Executive List** (`/executives/`) - Card-based layout with all profiles
- **Executive Detail** (`/executives/<id>/`) - Full profile information
- **Opportunity List** (`/opportunities/`) - All opportunity postings
- **Opportunity Detail** (`/opportunities/<id>/`) - Full opportunity details
- **Health Check** (`/health/`) - Returns "ok" for monitoring

### 5. Navigation
- Basic navigation between pages working
- URLs properly configured
- No broken links

---

## Completed Stories

| User Story | Story Points | Status | Notes |
|-----------|--------------|--------|-------|
| Render deployment with PostgreSQL | 5 | ✅ Complete | Auto-deploy configured |
| Static file serving (WhiteNoise) | 3 | ✅ Complete | Admin styling works |
| Executive list page | 3 | ✅ Complete | Card layout implemented |
| Executive detail page | 3 | ✅ Complete | All fields displayed |
| Opportunity list page | 2 | ✅ Complete | Basic list view |
| Opportunity detail page | 2 | ✅ Complete | Full details shown |
| Health check endpoint | 1 | ✅ Complete | Returns 200 OK |
| Build script automation | 1 | ✅ Complete | build.sh working |
| Basic form validation | 2 | ✅ Complete | Django forms validated |

**Planned:** 22 pts  
**Completed:** 22 pts  
**Velocity:** 22  
**Completion rate:** 100%

---

## Incomplete Stories

None - all planned stories completed.

---

## Technical Achievements

### Deployment Pipeline
- Created `build.sh` with three steps: install dependencies, collectstatic, migrate
- Configured `render.yaml` for infrastructure as code
- Set up environment variables: `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, `DATABASE_URL`

### Database Configuration
- Used `dj-database-url` for PostgreSQL connection string parsing
- Maintained SQLite for local development
- Connection pooling configured (`conn_max_age=600`)

### Static Files Solution
- Added WhiteNoise to middleware stack
- Configured `STATIC_ROOT = BASE_DIR / "staticfiles"`
- Used `CompressedManifestStaticFilesStorage` for performance
- Verified admin panel styling in production

---

## Lessons Learned

### What Worked Well
1. **Early deployment testing** - Caught issues before sprint end
2. **Build script automation** - Saved time on manual steps
3. **Environment-driven configuration** - Easy to switch between local/production
4. **WhiteNoise simplicity** - No need for separate CDN in MVP

### Challenges Encountered
1. **ALLOWED_HOSTS configuration** - Had duplicate settings causing conflict
2. **Database migrations** - Free tier has no shell access, had to run migrations via local `DATABASE_URL`
3. **Static files path** - Initially tried serving from wrong directory

### Solutions Implemented
- Consolidated all settings in `settings.py`, removed duplicates
- Documented migration process for future deployments
- Used WhiteNoise's static file discovery to handle paths automatically

---

## Velocity & Metrics

- **Sprint 1 Velocity:** 21 points
- **Sprint 2 Velocity:** 22 points
- **Cumulative Velocity:** 43 points across 2 sprints
- **Average Velocity:** 21.5 points/sprint
- **Velocity Change:** +4.8% improvement

**Sprint 3 Forecast:** 22-24 points based on consistent velocity

---

## Stakeholder Feedback

- Application successfully deployed and stable
- Public views functional and accessible
- Performance acceptable on free tier
- Ready to add user authentication in Sprint 3

---

## Backlog Updates

**Moving to Sprint 3:**
- User authentication (signup, login, logout)
- Content ownership (users can only edit their own content)
- User dashboard showing owned profiles/opportunities
- Enhanced styling and professional design
- Navigation improvements

**Deferred to Later Sprints:**
- Search and filtering
- Tag-based matching
- A/B testing endpoint
- Google Analytics integration

---

## Deployment Status

- **Production URL:** https://frac-app.onrender.com
- **Status:** ✅ Deployed and functional
- **Database:** PostgreSQL connected
- **Static Files:** Serving correctly via WhiteNoise
- **Uptime:** Monitored via health check endpoint

---

## Next Steps

Sprint 3 will focus on:
1. Implementing user authentication system
2. Adding content ownership and authorization
3. Building user dashboard
4. Improving UI/UX with professional styling
5. Enhancing navigation and user flows