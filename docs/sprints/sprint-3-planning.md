# Sprint 3 — Planning

**Dates:** November 19-26, 2025  
**Sprint Goal:** Complete core marketplace functionality with user authentication, content ownership, professional UI, and full CRUD operations

---

## Sprint Objectives

1. Implement user authentication system (signup, login, logout)
2. Add content ownership and authorization
3. Build user dashboard for managing profiles and opportunities
4. Create professional, cohesive UI design
5. Enable full CRUD operations (Create, Read, Update, Delete)
6. Implement navigation system across all pages

---

## Selected User Stories

| User Story | Priority | Story Points | Assignee |
|------------|----------|--------------|----------|
| User authentication (signup/login/logout) | High | 5 | Team |
| Content ownership and authorization | High | 3 | Team |
| User dashboard | High | 5 | Team |
| Executive profile creation form | High | 5 | Team |
| Opportunity posting form | High | 5 | Team |
| Edit profile functionality | Medium | 3 | Team |
| Edit opportunity functionality | Medium | 3 | Team |
| Professional UI design (CSS framework) | High | 3 | Team |
| Navigation system | Medium | 2 | Team |

**Total Planned Points:** 34

---

## Team Capacity

- **Team members:** 5 (Robby, Wit, Dylan, Henry, Joseph)
- **Sprint duration:** 1 week
- **Estimated capacity:** 30-35 story points (scaling up from Sprint 1-2 average of 21.5)
- **Planned work:** 34 story points
- **Buffer:** 1 point (~3%)

---

## Dependencies

- Sprint 2 deployment working successfully
- Django authentication system available
- Forms framework for CRUD operations
- CSS design system (custom, not Bootstrap/Tailwind)
- Database migrations for user ownership fields

---

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Authentication complexity | High | Medium | Use Django's built-in auth system |
| CSS static file issues on Render | High | High | Test WhiteNoise configuration early |
| URL routing conflicts | Medium | High | Use separate URL config files |
| Form validation complexity | Medium | Medium | Start simple, iterate |
| Time constraint for styling | Medium | High | Focus on function first |

---

## Technical Approach

### Authentication Strategy
- Use Django's built-in User model
- Create custom signup/login templates  
- Add `@login_required` decorators
- Session-based authentication

### Content Ownership Strategy  
- Add `owner` ForeignKey to models
- Authorization checks in views
- Filter dashboard by owner
- Display ownership in templates

### UI Design Strategy
- Custom CSS framework (Anthropic-inspired)
- Card-based layouts
- Consistent color palette
- Responsive design
- Hover effects and transitions

---

## Definition of Done

- [ ] Users can sign up, log in, and log out
- [ ] Users can only edit their own content
- [ ] Dashboard shows user's content
- [ ] CRUD forms functional
- [ ] Professional CSS applied
- [ ] Navigation working
- [ ] Responsive on mobile/desktop
- [ ] Tested in production
- [ ] Code deployed

---

## Sprint Schedule

**Days 1-2:** Authentication & ownership  
**Days 3-4:** Forms & CRUD  
**Days 5-6:** Dashboard & UI  
**Day 7:** Testing & review