# Sprint 4 Report

**Team:** restless-sound  
**Sprint Duration:** November 25-26, 2025  
**Report Date:** November 26, 2025

---

## 1. Sprint Goal & Achievement

**Sprint Goal:** Deploy production-ready marketplace with authentication, A/B testing, and analytics

**Achievement:** ✅ ACHIEVED - All mandatory requirements completed and deployed to production.

---

## 2. Production Deployment

### Production URL
https://frac-app.onrender.com

### What's Working
- User authentication (signup, login, logout)
- Two-path homepage (For Startups / For Fractionals)
- Executive profiles with tag-based skills
- Job postings with required skills tags
- User dashboard with suggested matches
- Tag-based matching algorithm
- A/B test endpoint at /b77952e
- Google Analytics tracking on all pages

### What's Not Working
All core features are operational. Minor polish items remain for final submission.

### Deployment Process
1. Push code to GitHub main branch
2. Render auto-deploys from GitHub
3. Build command: `./build.sh` (runs collectstatic)
4. Migrations run automatically during build

---

## 3. A/B Test Endpoint

### Endpoint URL
https://frac-app.onrender.com/b77952e/

### Requirements Checklist
- ✅ Displays team nickname: restless-sound
- ✅ Shows team member nicknames
- ✅ Button with `id="abtest"`
- ✅ Variant A shows "kudos" button
- ✅ Variant B shows "thanks" button
- ✅ No authentication required (public)
- ✅ Analytics tracking visits and variant shown

---

## 4. Completed Work

| User Story | Status | Story Points |
|------------|--------|--------------|
| User Authentication | ✅ Complete | 5 |
| Content Ownership | ✅ Complete | 3 |
| Two-Path Homepage | ✅ Complete | 5 |
| User Dashboard | ✅ Complete | 5 |
| Tag System | ✅ Complete | 5 |
| Tag Matching Algorithm | ✅ Complete | 8 |
| A/B Test Endpoint | ✅ Complete | 3 |
| Google Analytics | ✅ Complete | 2 |
| Production Deployment | ✅ Complete | 3 |
| **Total** | | **39** |

---

## 5. Velocity Summary

| Sprint | Velocity (Points) |
|--------|-------------------|
| Sprint 2 | 24 |
| Sprint 3 | 31 |
| Sprint 4 | 39 |
| **Average** | **31.3** |

---

## 6. Readiness for Final Submission

### What's Complete
- All mandatory features deployed and working
- A/B test endpoint with proper button (`id="abtest"`)
- Google Analytics tracking on all pages
- Tag-based matching algorithm
- Production deployment on Render

### What Remains (9 days until Dec 12)
- Expand test coverage
- Run linter and fix issues
- Create cumulative burndown chart
- Prepare traffic analysis from analytics
- Write comprehensive final report
- UI polish and CSS cleanup

### Risks & Mitigation
| Risk | Mitigation |
|------|------------|
| Render free tier cold starts slow | Keep service warm before demo |
| Analytics data gaps | Generate traffic early to collect data |

---

## 7. Sprint Retrospective Highlights

### What Went Well
- Completed all mandatory requirements ahead of schedule
- Tag matching algorithm works effectively
- Two-path UX provides clear user journeys

### What Could Be Improved
- CSS organization became fragmented - needs refactoring
- Should have read A/B test requirements more carefully initially

### Key Learnings
- Django session management for A/B testing is straightforward
- Free-form tags with comma separation is simple but effective for MVP
- Inline styles can override stubborn CSS issues quickly

---

## 8. Links

| Resource | URL |
|----------|-----|
| Production | https://frac-app.onrender.com |
| A/B Test Endpoint | https://frac-app.onrender.com/b77952e/ |
| GitHub Repository | https://github.com/r-nepomuceno/frac-app |
| GitHub Project Board | https://github.com/r-nepomuceno/frac-sprint-board |
