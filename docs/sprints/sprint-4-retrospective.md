# Sprint 4 — Retrospective

**Date:** November 26, 2025  
**Team:** restless-sound  
**Attendees:** Robby Nepomuceno, Wit Wattananimitgul, Dylan Safyer, Henry Melzner, Joseph Dobson

---

## Summary

Sprint 4 was highly successful, completing all mandatory requirements including production deployment, A/B testing endpoint, and Google Analytics integration. The team demonstrated strong velocity improvement from previous sprints, achieving 39 story points in a compressed 2-day sprint. This represents the culmination of the project's core MVP features.

---

## What Went Well 👍

### Achievements
- **All mandatory requirements completed** - A/B endpoint, analytics, production deployment all working
- **Tag matching algorithm** - Successfully implemented full matching system with dashboard suggestions
- **Two-path UX** - Clean separation between startup and fractional user journeys provides clear navigation
- **Velocity improvement** - Increased from 34 points (Sprint 3) to 39 points (Sprint 4), +14.7% improvement
- **Compressed timeline success** - Delivered in 2 days what normally takes a week

### Technical Wins
- **Django session management** - A/B variant persistence worked seamlessly with built-in session framework
- **Tag normalization** - `get_tags_list()` method provides clean, reusable tag handling across models
- **Matching algorithm elegance** - Pure Python functions with set operations made implementation straightforward
- **Inline CSS fallbacks** - Resolved stubborn styling issues quickly when CSS cascade proved difficult

### Process Wins
- **Day-by-day implementation approach** - Breaking work into daily chunks kept team organized
- **Testing each feature before moving on** - Prevented bug accumulation
- **Clear documentation in planning files** - Maintained focus on deliverables
- **Rubric review process** - Caught A/B test requirement details before implementation

---

## What Could Be Improved 👎

### Technical Debt
- **CSS fragmentation** - Multiple rounds of fixes led to disorganized stylesheet with inconsistent patterns
- **Template duplication** - GA script copied to all templates instead of using base template with inheritance
- **Inline styles proliferation** - Some templates have inline styles that should be in CSS file for maintainability
- **No base template** - Lack of template inheritance created duplication across templates

### Process Issues
- **A/B test requirements misread initially** - Built wrong variant (headlines instead of kudos/thanks button)
- **Requirements reading thoroughness** - Should have reviewed rubric more carefully before starting implementation
- **Late-stage rework** - Had to rebuild A/B test page after discovering requirements mismatch

### Challenges Encountered
- **Underline styling on card links** - Surprisingly difficult to override browser defaults, required multiple attempts
- **Render free tier deployment times** - ~8 minute deployment cycles slowed iteration speed
- **Browser CSS caching** - Made testing fixes frustrating, required hard refreshes
- **CSS specificity battles** - Fighting cascade led to inline style workarounds

---

## Action Items for Final Submission

### High Priority
1. [ ] **Refactor CSS into organized sections** - Group related styles, remove duplicates, add comments
2. [ ] **Create base template with GA script** - Eliminate duplication across templates
3. [ ] **Expand test coverage** - Add tests for matching algorithm, dashboard views, A/B endpoint
4. [ ] **Run linter and fix all issues** - Ensure code quality standards met

### Medium Priority
5. [ ] **Remove inline styles from templates** - Move to CSS file for maintainability
6. [ ] **Add comprehensive error handling** - Improve user experience on failures
7. [ ] **Create cumulative burndown chart** - Visualize velocity across all 4 sprints
8. [ ] **Document deployment process** - Step-by-step guide in README

### Low Priority
9. [ ] **Add loading states to forms** - Improve perceived performance
10. [ ] **Improve mobile responsiveness** - Polish mobile experience
11. [ ] **Add favicon** - Professional touch
12. [ ] **Optimize database queries** - Reduce N+1 queries in dashboard

---

## Team Feedback

### What should we start doing?
- **Reading requirements/rubric thoroughly** before implementation to avoid rework
- **Using base templates from start** of projects to eliminate duplication
- **Creating CSS organization system** upfront with naming conventions and structure
- **Deploying to staging frequently** to catch issues earlier

### What should we stop doing?
- **Adding quick inline style fixes** without documenting or refactoring later
- **Assuming requirements** without verifying against rubric or specs
- **Waiting until end of sprint** to deploy to production
- **Fighting CSS cascade** - sometimes inline styles are the pragmatic solution

### What should we continue doing?
- **Day-by-day implementation planning** - Kept work organized and focused
- **Testing features immediately** after implementation - Prevented bug accumulation
- **Committing frequently** with descriptive messages - Great version control hygiene
- **Problem-solving collaboratively** - Team debugging was effective

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
| Code Quality | Good |
| Test Coverage | Moderate |

---

## Key Learnings

### Technical Learnings
1. **Session-based A/B testing is straightforward** - Django's session framework makes variant persistence trivial, no database needed
2. **Free-form tags work well for MVP** - Comma-separated tags are flexible and user-friendly, avoiding complexity of ManyToMany
3. **CSS specificity matters deeply** - Browser defaults can override even `!important` rules if selectors don't match properly
4. **Pure Python algorithms are testable** - Matching logic with no framework dependencies is easy to test and debug
5. **Inline styles have their place** - When CSS cascade becomes too complex, inline styles are pragmatic

### Process Learnings
1. **Read requirements first, code second** - 10 minutes reading rubric saves hours of rework
2. **Deploy early and often** - Caught configuration issues when there was time to fix them
3. **Base templates save time** - Even small duplication adds up across many templates
4. **Documentation during development** - Writing docs after the fact is harder than during
5. **Velocity isn't everything** - Quality and maintainability matter as much as speed

### Team Learnings
1. **Compressed sprints are possible** - With focus and preparation, 2-day sprints can be productive
2. **Clear goals enable execution** - Well-defined objectives kept team aligned
3. **Collaborative debugging is faster** - Two sets of eyes catch issues quickly
4. **Celebrate small wins** - Acknowledging progress maintains momentum

---

## Team Dynamics Reflection

### Strengths
- **Rapid problem-solving:** When A/B test needed rework, team rebuilt quickly without frustration
- **Technical adaptability:** Pivoted to inline styles when CSS proved too complex
- **Focus under pressure:** Delivered 39 points in 2 days through clear prioritization
- **Quality maintenance:** Despite compressed timeline, maintained code quality standards

### Areas for Growth
- **Requirements verification:** Need to double-check specs before implementation
- **Technical debt management:** Should allocate time for refactoring, not just features
- **Testing discipline:** Should write tests alongside features, not after
- **Documentation timing:** Should document decisions when made, not retrospectively

### Team Health: 8/10
Team successfully delivered under compressed timeline while maintaining quality. Slight stress from tight deadline, but positive energy and collaboration throughout.

---

## Sprint 4 Wins 🎉

- ✅ 100% story completion rate (39/39 points)
- ✅ All mandatory requirements delivered
- ✅ Production deployment successful
- ✅ A/B test endpoint fully functional with analytics
- ✅ Matching algorithm providing real value
- ✅ Two-path UX improving user experience
- ✅ Highest velocity of any sprint (+14.7% over Sprint 3)

---

## Looking Ahead to Final Submission

With all MVP features complete, final work focuses on:
- **Documentation:** Comprehensive README, final report
- **Analysis:** Burndown chart, A/B test results, traffic analysis
- **Quality:** Test coverage, linting, code cleanup
- **Deployment:** Staging environment (if time permits)

The project is in excellent shape for final submission on December 12.

---

## Shoutouts 🌟

- **Django's built-in authentication system** - Made user management trivial
- **Render's auto-deploy feature** - Seamless CI/CD pipeline
- **Google Analytics 4** - Easy integration with comprehensive tracking
- **Python's set operations** - Made tag matching algorithm elegant
- **Django sessions** - Perfect solution for A/B test persistence

---

## Celebration Moments 🎉

- A/B test endpoint working perfectly on first production test
- Matching algorithm returning relevant results immediately
- Two-path homepage providing clear user journeys
- All 4 sprints completed with 100% story completion
- Team velocity increased every single sprint
- Production deployment stable and fast

---

## Final Thoughts

Sprint 4 represents the culmination of an exceptional development process. The team:
- Increased velocity from 21 points (Sprint 1) to 39 points (Sprint 4)
- Maintained 100% completion rate across all 4 sprints
- Delivered a production-ready application with professional quality
- Built complex features (authentication, matching, A/B testing) from scratch
- Established strong development practices and team collaboration

**Project Status:** ✅ Ready for final submission with minor documentation work remaining