# Sprint 4 Retrospective

**Team:** restless-sound  
**Sprint Duration:** November 25-26, 2025  
**Facilitator:** Team  
**Date:** November 26, 2025

---

## Summary

Sprint 4 was highly successful, completing all mandatory requirements including production deployment, A/B testing endpoint, and Google Analytics integration. The team demonstrated strong velocity improvement from previous sprints.

---

## What Went Well 👍

### Achievements
- **All mandatory requirements completed** - A/B endpoint, analytics, and production deployment all working
- **Tag matching algorithm** - Successfully implemented full matching system with dashboard suggestions
- **Two-path UX** - Clean separation between startup and fractional user journeys
- **Velocity improvement** - Increased from 31 points (Sprint 3) to 39 points (Sprint 4)

### Technical Wins
- Django session management for A/B variant persistence worked seamlessly
- Tag normalization with `get_tags_list()` method provides clean, reusable tag handling
- Inline CSS fallbacks resolved stubborn styling issues quickly

### Process Wins
- Day-by-day implementation approach kept work organized
- Testing each feature before moving to next prevented accumulating bugs
- Clear documentation in planning files helped maintain focus

---

## What Could Be Improved 👎

### Technical Debt
- **CSS fragmentation** - Multiple rounds of fixes led to disorganized stylesheet
- **Template duplication** - GA script copied to all templates instead of using base template
- **Inline styles** - Some templates have inline styles that should be in CSS file

### Process Issues
- **A/B test requirements** - Initially built wrong variant (headlines instead of kudos/thanks button)
- **Requirements reading** - Should have reviewed rubric more carefully before implementation

### Challenges Encountered
- Underline styling on card links was surprisingly difficult to override
- Render free tier deployment times (~8 minutes) slowed iteration
- Browser CSS caching made testing fixes frustrating

---

## Action Items for Next Sprint / Final Submission

### High Priority
1. [ ] Refactor CSS into organized sections
2. [ ] Create base template with GA script
3. [ ] Expand test coverage
4. [ ] Run linter and fix all issues

### Medium Priority
5. [ ] Remove inline styles from templates
6. [ ] Add more comprehensive error handling
7. [ ] Create cumulative burndown chart
8. [ ] Document deployment process

### Low Priority
9. [ ] Add loading states to forms
10. [ ] Improve mobile responsiveness
11. [ ] Add favicon

---

## Team Feedback

### What should we start doing?
- Reading requirements/rubric thoroughly before implementation
- Using base templates from the start of projects
- Creating a CSS organization system upfront

### What should we stop doing?
- Adding quick inline style fixes without documenting them
- Assuming requirements without verifying
- Waiting until end of sprint to deploy to production

### What should we continue doing?
- Day-by-day implementation planning
- Testing features immediately after implementation
- Committing frequently with descriptive messages

---

## Metrics

| Metric | Value |
|--------|-------|
| Planned Story Points | 39 |
| Completed Story Points | 39 |
| Completion Rate | 100% |
| Bugs Found | 3 |
| Bugs Fixed | 3 |
| Deployment Frequency | 5 deploys |

---

## Key Learnings

1. **Session-based A/B testing is simple** - Django's session framework makes variant persistence trivial
2. **Free-form tags work well for MVP** - Comma-separated tags are flexible and user-friendly
3. **CSS specificity matters** - Browser defaults can override even `!important` rules if selectors don't match
4. **Read requirements first** - 10 minutes reading saves hours of rework

---

## Shoutouts 🌟

- Django's built-in authentication system for making auth implementation quick
- Render's auto-deploy feature for seamless CI/CD
- Google Analytics 4 for easy integration

---

## Next Steps

1. Focus on final submission requirements
2. Generate traffic to collect analytics data
3. Polish UI and fix remaining CSS issues
4. Write comprehensive final report
5. Prepare for December 12 deadline
