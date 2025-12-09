# Sprint 4 — Planning

**Dates:** November 25-26, 2025  
**Sprint Goal:** Deploy production-ready marketplace with two-path UX, tag-based matching, A/B testing, and analytics integration

---

## Sprint Objectives

1. Build two-path homepage experience (For Startups / For Fractionals)
2. Implement tag-based matching system
3. Create user dashboard with suggested matches
4. Add A/B test endpoint at `/b77952e`
5. Integrate Google Analytics tracking
6. Deploy to production with all features
7. Final polish and optimization

---

## Selected User Stories

| User Story | Priority | Story Points | Assignee |
|------------|----------|--------------|----------|
| Two-path homepage | High | 5 | Team |
| Tag system (comma-separated skills) | Medium | 5 | Team |
| Tag matching algorithm | Medium | 8 | Team |
| Dashboard with suggested matches | High | 5 | Team |
| For Startups landing page | Medium | 3 | Team |
| For Fractionals landing page | Medium | 3 | Team |
| A/B test endpoint | High | 3 | Team |
| Google Analytics integration | High | 2 | Team |
| Production deployment | High | 3 | Team |
| Final UI polish | Medium | 2 | Team |

**Total Planned Points:** 39

---

## Team Capacity

- **Team members:** 5 (Robby, Wit, Dylan, Henry, Joseph)  
- **Sprint duration:** 2 days (compressed sprint)
- **Estimated capacity:** 40 story points
- **Planned work:** 39 story points
- **Buffer:** 1 point (~2.5%)

**Note:** This is a compressed sprint (2 days vs typical 7 days) due to project timeline. Velocity scaled accordingly.

---

## Dependencies

- Sprint 3 authentication and CRUD working
- Models support tags/skills fields
- Render production environment ready
- Google Analytics account (GA4)
- A/B test endpoint requirements from rubric

---

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Compressed timeline | High | High | Prioritize MVP features, defer nice-to-haves |
| A/B test requirements unclear | Medium | Medium | Review rubric carefully before implementation |
| Matching algorithm complexity | Medium | Low | Start simple with exact tag matching |
| CSS conflicts | Low | High | Use inline styles as fallback |
| Render deployment issues | High | Low | Test deployment early in sprint |

---

## Technical Approach

### Two-Path Homepage
- Redesign home page with two clear paths
- "For Startups" card linking to `/for-startups/`
- "For Fractionals" card linking to `/for-fractionals/`
- Each landing page explains value proposition
- Clear CTAs to relevant actions

### Tag System
- Add `skills_tags` field to ExecutiveProfile (comma-separated)
- Add `required_skills_tags` field to Opportunity (comma-separated)
- Create `get_tags_list()` method for parsing
- Display tags as pill badges in UI

### Matching Algorithm
- Create `matching.py` module
- `get_matching_tags()` - find intersection of tag sets
- `calculate_match()` - compute match percentage
- `find_matching_opportunities_for_executive()` - ranked matches
- `find_matching_executives_for_opportunity()` - ranked matches
- Sort by match count and percentage

### Dashboard Enhancements
- Add "Suggested Opportunities" section for executives
- Add "Suggested Executives" section for startups
- Display match scores (e.g., "3 of 5 skills match")
- Highlight matching tags
- Link to detail pages

### A/B Test Endpoint
- URL: `/b77952e/` (sha1("restless-sound")[:7])
- Random assignment to variant A or B
- Store variant in Django session
- Variant A: "kudos" button (green)
- Variant B: "thanks" button (blue)
- Button must have `id="abtest"`
- Track clicks with Google Analytics

### Google Analytics
- Sign up for GA4 account
- Get measurement ID
- Add GA script to all templates
- Track page views
- Track custom events (A/B test clicks)

---

## Sprint Schedule

**Day 1 (November 25):**
- Morning: Two-path homepage + landing pages
- Afternoon: Tag system + matching algorithm

**Day 2 (November 26):**
- Morning: Dashboard enhancements + A/B test endpoint
- Afternoon: Google Analytics + deployment + testing

---

## A/B Test Requirements (Critical)

Based on rubric requirements:
- Endpoint at specific URL (computed from team name)
- Button with exact ID `id="abtest"`
- Variant A shows "kudos"
- Variant B shows "thanks"
- No authentication required (public)
- Session-based variant persistence
- Analytics tracking for both variants

---

## Definition of Done

- [ ] Two-path homepage implemented
- [ ] For Startups and For Fractionals landing pages created
- [ ] Tag system working (add, display, parse)
- [ ] Matching algorithm returns ranked matches
- [ ] Dashboard shows suggested matches
- [ ] A/B test endpoint at `/b77952e/` working correctly
- [ ] Button has `id="abtest"`
- [ ] Google Analytics tracking on all pages
- [ ] GA tracking A/B test interactions
- [ ] All features deployed to production
- [ ] End-to-end testing completed
- [ ] Sprint review conducted

---

## Success Criteria

### Functional Requirements
- Users can see two clear paths on homepage
- Matching algorithm returns relevant results
- Dashboard displays personalized suggestions
- A/B test endpoint meets all rubric requirements
- Analytics collecting data

### Technical Requirements
- All features work in production
- No breaking bugs
- Static files serving correctly
- Database migrations successful
- Session management working

### UX Requirements
- Navigation intuitive
- Match scores clearly displayed
- Tags visually distinct
- Two-path homepage compelling
- A/B test page functional

---

## Key Deliverables

1. **Two-Path Homepage:** Clear entry points for two user types
2. **Matching System:** Algorithm + UI for showing matches
3. **A/B Test Endpoint:** Fully functional with analytics
4. **Analytics Integration:** GA4 tracking across site
5. **Production Deployment:** Everything live and working