# Sprint 2 — Planning

**Dates:** November 12-19, 2025  
**Sprint Goal:** Deploy working Django app to staging (Render) with PostgreSQL database and dynamic list/detail pages

---

## Sprint Objectives

1. Deploy application to Render with PostgreSQL
2. Configure static file serving with WhiteNoise
3. Create public-facing executive list and detail views
4. Create public-facing opportunity list and detail views
5. Add health check endpoint for monitoring
6. Set up automated build and deployment pipeline

---

## Selected User Stories

| User Story | Priority | Story Points | Assignee |
|------------|----------|--------------|----------|
| Render deployment with PostgreSQL | High | 5 | Team |
| Static file serving (WhiteNoise) | High | 3 | Team |
| Executive list page | High | 3 | Team |
| Executive detail page | High | 3 | Team |
| Opportunity list page | Medium | 2 | Team |
| Opportunity detail page | Medium | 2 | Team |
| Health check endpoint | Medium | 1 | Team |
| Build script automation | Medium | 1 | Team |
| Basic form validation | Low | 2 | Team |

**Total Planned Points:** 22

---

## Team Capacity

- **Team members:** 5 (Robby, Wit, Dylan, Henry, Joseph)
- **Sprint duration:** 1 week
- **Estimated capacity:** 20-24 story points (based on Sprint 1 velocity of 21)
- **Planned work:** 22 story points
- **Buffer:** 2 points (~9%)

---

## Dependencies

- Render account configured
- PostgreSQL database provisioned
- GitHub repository with Sprint 1 code
- Domain/subdomain for deployment (Render provides)
- WhiteNoise package installed

---

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Render free tier limitations | High | Medium | Test early, document workarounds |
| Static files not serving in prod | High | High | Configure WhiteNoise before deployment |
| Database migration failures | Medium | Medium | Test migrations locally first |
| ALLOWED_HOSTS misconfiguration | Medium | High | Set environment variables correctly |
| Build command errors | Low | Medium | Create build.sh script with error handling |

---

## Technical Approach

### Deployment Strategy
1. Configure `render.yaml` for infrastructure as code
2. Create `build.sh` script for automated builds
3. Set environment variables in Render dashboard
4. Test deployment with sample data

### Static Files Strategy
1. Install WhiteNoise middleware
2. Configure `STATIC_ROOT` and `STATICFILES_STORAGE`
3. Add `collectstatic` to build command
4. Test admin panel styling in production

### Database Strategy
1. Use `dj-database-url` for connection string parsing
2. Keep SQLite for local development
3. Use PostgreSQL in production
4. Create initial migrations before deployment

---

## Definition of Done

- [ ] Application deployed and accessible at Render URL
- [ ] PostgreSQL database connected and working
- [ ] Static files (CSS, admin assets) serving correctly
- [ ] Executive list and detail pages functional
- [ ] Opportunity list and detail pages functional
- [ ] Health check endpoint returns 200 OK
- [ ] No console errors in browser
- [ ] Build script runs successfully
- [ ] Environment variables documented

---

## Sprint Schedule

**Day 1-2:** Deployment infrastructure
- Configure Render
- Set up PostgreSQL
- Configure WhiteNoise

**Day 3-4:** Public views
- Executive list/detail pages
- Opportunity list/detail pages
- Basic styling

**Day 5-6:** Testing and polish
- Health check endpoint
- Test on production
- Fix any deployment issues

**Day 7:** Sprint review and retrospective