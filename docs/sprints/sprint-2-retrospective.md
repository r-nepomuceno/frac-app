# Sprint 2 — Retrospective

**Date:** November 19, 2025  
**Attendees:** Robby Nepomuceno, Wit Wattananimitgul, Dylan Safyer, Henry Melzner, Joseph Dobson

---

## Summary

Sprint 2 successfully deployed the application to production with PostgreSQL database, achieving 100% story completion (22/22 points). The team demonstrated strong problem-solving skills when dealing with deployment challenges and delivered a functional, publicly accessible application.

---

## What Went Well ✅

### 1. Successful Production Deployment
Deployed application to Render on the first attempt with minimal issues. The build script worked as designed and automated the deployment process effectively.

### 2. WhiteNoise Configuration
Static file serving was solved quickly using WhiteNoise. No need for complex CDN setup or S3 buckets - middleware handled everything smoothly.

### 3. Environment-Driven Configuration
Using environment variables for settings made it easy to switch between local development and production without code changes. The `.env.example` file helped document required variables.

### 4. Velocity Consistency
Maintained similar velocity to Sprint 1 (22 vs 21 points), showing accurate estimation and consistent team productivity.

### 5. Early Testing
Deployed to production mid-sprint rather than waiting until the end. This caught configuration issues early when there was time to fix them.

---

## What Didn't Go Well ❌

### 1. ALLOWED_HOSTS Configuration Issue
Encountered a deployment bug caused by duplicate `ALLOWED_HOSTS` settings - one hardcoded and one from environment variables. This caused the app to fail on first deployment attempt.

**Root Cause:** Didn't review settings.py thoroughly before deployment. Left test values alongside production configuration.

### 2. Database Migration Process
Render's free tier doesn't provide shell access, making it difficult to run manual migrations. Had to connect to production database from local machine using `DATABASE_URL`.

**Root Cause:** Didn't research Render's limitations before choosing platform. Should have ensured migrations could run automatically.

### 3. Static Files Path Confusion
Initially configured `STATIC_ROOT` incorrectly, causing admin panel to lose styling. Spent time debugging before discovering WhiteNoise's documentation had the correct configuration.

**Root Cause:** Didn't read WhiteNoise documentation thoroughly before implementation.

---

## What to Improve 🎯

### 1. Pre-Deployment Checklist
**Action Item:** Create deployment checklist to catch configuration issues before pushing to production
- **Owner:** Team
- **Deadline:** Before Sprint 3 deployment
- **How:** Document all environment variables, settings validation, and pre-deployment tests

### 2. Automated Migration Handling
**Action Item:** Ensure migrations run automatically during build process
- **Owner:** Team
- **Deadline:** Sprint 3 Week 1
- **How:** Add migration command to `build.sh`, test with sample migration

### 3. Settings Review Process
**Action Item:** Review all settings.py changes before merging to main
- **Owner:** Team
- **Deadline:** Ongoing
- **How:** Add settings.py review as required step in pull request checklist

### 4. Documentation
**Action Item:** Document deployment process in README
- **Owner:** Robby
- **Deadline:** Sprint 3
- **How:** Write step-by-step deployment guide including environment variables and common issues

---

## Action Items Summary

| Action Item | Owner | Deadline | Status |
|------------|-------|----------|--------|
| Create deployment checklist | Team | Sprint 3 Start | Pending |
| Verify migrations run in build.sh | Team | Sprint 3 Week 1 | Pending |
| Add settings.py review to PR process | Team | Ongoing | Pending |
| Document deployment in README | Robby | Sprint 3 | Pending |
| Test database backups | Team | Sprint 3 | Pending |

---

## Team Dynamics Reflection

### Strengths
- **Rapid problem-solving:** When deployment failed, team debugged systematically and found solution quickly
- **Knowledge sharing:** Team members helped each other understand Render platform and Django deployment
- **Resilience:** Didn't get discouraged by deployment issues, maintained positive attitude
- **Collaboration:** Pair programming on deployment configuration helped catch issues

### Areas for Growth
- **Planning thoroughness:** Should research platform limitations before committing to deployment strategy
- **Documentation discipline:** Need to document setup steps as we perform them, not after
- **Testing rigor:** Should test all features in production environment, not just main user flows

### Team Health: 8/10
Team handled deployment challenges well but recognized need for more thorough planning and testing processes.

---

## Sprint 2 Wins 🎉

- ✅ 100% story completion rate (22/22 points)
- ✅ Application deployed to production successfully
- ✅ PostgreSQL database connected and working
- ✅ Static files serving correctly
- ✅ Health check endpoint for monitoring
- ✅ Automated build and deployment pipeline

---

## Looking Ahead to Sprint 3

With deployment infrastructure in place, Sprint 3 will focus on:
- **User authentication:** Enable users to create accounts and log in
- **Content ownership:** Users can only edit their own profiles/opportunities
- **User dashboard:** Personalized view of owned content
- **UI improvements:** Professional styling and enhanced user experience

The team is confident about Sprint 3 given the strong foundation built in Sprints 1-2.

---

## Key Learnings

1. **Deploy early and often:** Deploying mid-sprint caught issues when there was time to fix them
2. **Read the docs:** WhiteNoise documentation had the exact solution we needed - reading it first would have saved time
3. **Environment variables are powerful:** Using env vars for all config made environment switching trivial
4. **Free tier limitations matter:** Understanding platform constraints upfront prevents surprises
5. **Automation saves time:** Build script automated repetitive tasks and prevented human error

---

## Celebration Moments 🌟

- First successful production deployment
- Database connected on first try
- Health check endpoint working perfectly
- Admin panel fully styled in production
- Team overcame deployment challenges together

---

## Metrics

| Metric | Value |
|--------|-------|
| Planned Story Points | 22 |
| Completed Story Points | 22 |
| Completion Rate | 100% |
| Bugs Found | 3 |
| Bugs Fixed | 3 |
| Deployment Attempts | 2 (1 failed, 1 successful) |
| Time to First Deploy | 3 days |