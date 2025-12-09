# Sprint 1 — Planning

**Dates:** November 5-12, 2025  
**Sprint Goal:** Set up Django project foundation with basic models, database, and deployment infrastructure

---

## Sprint Objectives

1. Initialize Django project structure
2. Create ExecutiveProfile and Job models
3. Set up PostgreSQL database
4. Configure Git repository and version control
5. Establish deployment pipeline to Render
6. Create basic admin interface

---

## Selected User Stories

| User Story | Priority | Story Points | Assignee |
|------------|----------|--------------|----------|
| Project setup (Django + Git) | High | 3 | Team |
| ExecutiveProfile model | High | 5 | Team |
| Job/Opportunity model | High | 5 | Team |
| Database configuration (local + Render) | High | 3 | Team |
| Admin interface setup | Medium | 2 | Team |
| Basic templates structure | Medium | 3 | Team |

**Total Planned Points:** 21

---

## Team Capacity

- **Team members:** 5 (Robby, Wit, Dylan, Henry, Joseph)
- **Sprint duration:** 1 week
- **Estimated capacity:** 20-24 story points
- **Planned work:** 21 story points
- **Buffer:** 3 points (~14%)

---

## Dependencies

- Django 5.2.8 installed
- PostgreSQL database on Render
- GitHub repository created
- Team members familiar with Django basics

---

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Database setup delays | High | Medium | Use SQLite locally first |
| Render deployment issues | Medium | Medium | Test deployment early |
| Model design changes | Medium | High | Keep models simple initially |
| Git conflicts | Low | Medium | Establish branching strategy |

---

## Definition of Done

- [ ] Django project runs locally
- [ ] ExecutiveProfile and Job models created with migrations
- [ ] Admin interface accessible
- [ ] Code committed to GitHub
- [ ] Initial deployment to Render successful
- [ ] README.md with setup instructions created