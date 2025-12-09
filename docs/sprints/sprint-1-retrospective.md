# Sprint 1 — Retrospective

**Date:** November 12, 2025  
**Attendees:** Robby Nepomuceno, Wit Wattananimitgul, Dylan Safyer, Henry Melzner, Joseph Dobson

---

## Summary

Sprint 1 successfully established the project foundation, completing all 21 planned story points. The team demonstrated strong technical skills and good collaboration, setting up a solid base for future sprints.

---

## What Went Well ✅

### 1. Clean Project Setup
Successfully initialized Django project with proper structure following best practices. Used Django 5.2.8 with standard app organization.

### 2. Model Design
Created two core models (ExecutiveProfile and Job) with appropriate fields. Models are simple and extensible for future enhancements.

### 3. Version Control Discipline
Established good Git practices from day one with:
- Clear commit messages
- Proper `.gitignore` configuration
- Logical commit groupings

### 4. Team Collaboration
All team members contributed to initial setup. Good communication about technical decisions and model structure.

---

## What Didn't Go Well ❌

### 1. Field Naming Inconsistency
Used generic suffixes like `_text` (e.g., `skills_text`, `description_text`) which felt redundant. Should have used cleaner names like `skills` and `description`.

**Root Cause:** Didn't establish naming conventions before starting model creation.

### 2. Database Configuration Confusion
Spent extra time figuring out PostgreSQL vs SQLite differences. Some team members had local database issues.

**Root Cause:** Didn't document database setup process upfront.

### 3. No Deployment in Sprint 1
Originally planned to deploy in Sprint 1 but pushed to Sprint 2. This created uncertainty about production readiness.

**Root Cause:** Underestimated deployment complexity, should have allocated more points.

---

## What to Improve 🎯

### 1. Establish Naming Conventions Early
**Action Item:** Create a coding standards document before Sprint 2
- **Owner:** Team
- **Deadline:** Before Sprint 2 begins
- **How:** Document field naming, function naming, and file organization standards

### 2. Document Setup Process
**Action Item:** Create comprehensive setup guide in README
- **Owner:** Robby
- **Deadline:** Week 1 of Sprint 2
- **How:** Write step-by-step instructions for local database, environment variables, and dependencies

### 3. Plan Deployment Earlier
**Action Item:** Include deployment tasks earlier in sprints, not at the end
- **Owner:** Team
- **Deadline:** Throughout Sprint 2
- **How:** Break deployment into smaller tasks and deploy incrementally

### 4. Test on Production-Like Environment
**Action Item:** Set up staging environment that mirrors production
- **Owner:** Team
- **Deadline:** Sprint 2
- **How:** Use Render free tier for staging with PostgreSQL

---

## Action Items Summary

| Action Item | Owner | Deadline | Status |
|------------|-------|----------|--------|
| Create coding standards document | Team | Sprint 2 Start | Pending |
| Write comprehensive README setup guide | Robby | Sprint 2 Week 1 | Pending |
| Deploy to staging environment | Team | Sprint 2 | Pending |
| Refactor model field names (remove _text suffix) | Team | Sprint 2 | Pending |

---

## Team Dynamics Reflection

### Strengths
- **Clear communication:** Team discussed technical decisions openly
- **Shared ownership:** Everyone contributed to project setup
- **Problem-solving:** Debugged issues collaboratively
- **Enthusiasm:** High energy and commitment to project success

### Areas for Growth
- **Earlier testing:** Should test on different environments sooner
- **Documentation:** Need to document decisions and setup as we go
- **Time estimation:** Underestimated some tasks (e.g., database config)

### Team Health: 8/10
Strong start with good momentum. Minor improvements in planning and documentation will strengthen process.

---

## Sprint 1 Wins 🎉

- ✅ 100% story completion rate
- ✅ Solid technical foundation established
- ✅ All models created with proper migrations
- ✅ Admin interface functional
- ✅ Git repository properly configured

---

## Looking Ahead to Sprint 2

With the foundation in place, Sprint 2 will focus on:
- **Deployment:** Get app live on Render with PostgreSQL
- **User-facing views:** Build public list and detail pages
- **Static files:** Configure WhiteNoise for production
- **Health check:** Add monitoring endpoint

The team is well-positioned to deliver these features given the strong Sprint 1 performance.

---

## Key Learnings

1. **Start simple:** Simple models are easier to extend than complex ones
2. **Document as you go:** Writing setup instructions later is harder than doing it during setup
3. **Plan deployment early:** Deployment is not a "final step" - should be tested throughout
4. **Naming matters:** Good naming conventions save refactoring time later

---

## Celebration Moments 🌟

- First Django project successfully initialized
- Models created and migrations working perfectly
- Admin interface up and running with sample data
- Team collaboration exceeded expectations