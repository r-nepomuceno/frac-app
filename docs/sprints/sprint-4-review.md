# Sprint 4 — Review

**Date:** November 26, 2025  
**Sprint Goal:** Deploy production-ready marketplace with two-path UX, tag-based matching, A/B testing, and analytics integration  
**Status:** ✅ **ACHIEVED**

---

## What's Working (Demo)

### 1. Two-Path Homepage
- **URL:** `/`
- Clean homepage with two clear paths
- "I'm Hiring" button → For Startups landing page
- "I'm a Fractional" button → For Fractionals landing page
- Professional hero section with value proposition
- "Why fractional?" explanation card

### 2. Landing Pages
- **For Startups** (`/for-startups/`)
  - Value proposition for companies
  - Two action cards: Browse Executives, Post Opportunity
  - Cross-link to For Fractionals page
  
- **For Fractionals** (`/for-fractionals/`)
  - Value proposition for executives
  - Two action cards: Browse Opportunities, Create Profile
  - Cross-link to For Startups page

### 3. Tag System
- **Executive Profiles:** `skills_tags` field
  - Comma-separated skill tags (e.g., "finance, strategy, fundraising")
  - `get_tags_list()` method for parsing
  - Displayed as pill badges on profiles
  
- **Opportunities:** `required_skills_tags` field
  - Comma-separated required skills
  - `get_tags_list()` method for parsing
  - Displayed as pill badges on opportunities

### 4. Matching Algorithm
- **Module:** `classifieds/matching.py`
- **Functions:**
  - `get_matching_tags()` - Find intersection of tag sets
  - `calculate_match()` - Compute match percentage and count
  - `find_matching_opportunities_for_executive()` - Ranked opportunity matches
  - `find_matching_executives_for_opportunity()` - Ranked executive matches
  - `get_dashboard_matches()` - Dashboard suggestions

- **Features:**
  - Case-insensitive matching
  - Handles extra whitespace
  - Calculates match percentage based on required skills
  - Sorts by match count (descending)
  - Returns detailed match info

### 5. Dashboard with Suggested Matches
- **Suggested Opportunities** (for executives with profiles)
  - Shows opportunities matching user's skills
  - Displays match score (e.g., "2 skills match")
  - Highlights matching tags in green
  - Top 5 best matches displayed
  
- **Suggested Executives** (for startups with opportunities)
  - Shows executives matching opportunity requirements
  - Displays match score (e.g., "3 of 5 skills match")
  - Highlights matching tags in blue
  - Top 5 best matches displayed

### 6. Detail Pages with Match Indicators
- **Executive Detail:** Shows if logged-in user has matching opportunities
- **Opportunity Detail:** Shows if logged-in user has matching profiles
- Match boxes display:
  - Match count (e.g., "2 of 3 skills")
  - Match percentage
  - Highlighted matching tags

### 7. A/B Test Endpoint
- **URL:** `/b77952e/` (sha1("restless-sound")[:7])
- **Functionality:**
  - Random assignment to variant A or B on first visit
  - Session-based persistence (same user always sees same variant)
  - Variant A: Green "kudos" button
  - Variant B: Blue "thanks" button
  - Button has `id="abtest"` (exact requirement)
  - Click feedback displayed
  - No authentication required (public access)

### 8. Google Analytics Integration
- **Measurement ID:** G-94TQ21MWZ6
- **Tracking:**
  - Page views on all pages
  - Custom event tracking for A/B test clicks
  - Event parameters: variant (A/B), button_text (kudos/thanks)
- **Implementation:**
  - GA4 script on every template
  - Custom event function for A/B test interaction

### 9. Production Deployment
- **URL:** https://frac-app.onrender.com
- **Status:** All Sprint 4 features live
- **Database:** PostgreSQL with tag fields
- **Static Files:** CSS serving correctly
- **Environment:** All variables configured

---

## Completed Stories

| User Story | Story Points | Status | Notes |
|-----------|--------------|--------|-------|
| Two-path homepage | 5 | ✅ Complete | Clean, professional design |
| Tag system | 5 | ✅ Complete | Comma-separated, parsed correctly |
| Tag matching algorithm | 8 | ✅ Complete | Full matching.py module |
| Dashboard with suggested matches | 5 | ✅ Complete | Both directions working |
| For Startups landing page | 3 | ✅ Complete | Clear value prop |
| For Fractionals landing page | 3 | ✅ Complete | Clear value prop |
| A/B test endpoint | 3 | ✅ Complete | All requirements met |
| Google Analytics integration | 2 | ✅ Complete | GA4 tracking live |
| Production deployment | 3 | ✅ Complete | Deployed successfully |
| Final UI polish | 2 | ✅ Complete | Consistent styling |

**Planned:** 39 pts  
**Completed:** 39 pts  
**Velocity:** 39  
**Completion rate:** 100%

---

## Incomplete Stories

None - all planned stories completed.

---

## Demo: Enhanced User Journeys

### Journey 1: Executive Finding Matching Opportunities
1. Visit homepage → Choose "I'm a Fractional"
2. Land on For Fractionals page → Click "Create Profile"
3. Fill profile with skills: "finance, strategy, fundraising"
4. Visit Dashboard → See "Suggested Opportunities"
5. See opportunities ranked by match score
6. Click opportunity → See match indicator showing shared skills

### Journey 2: Startup Finding Matching Executives
1. Visit homepage → Choose "I'm Hiring"
2. Land on For Startups page → Click "Post Opportunity"
3. Fill opportunity with required skills: "finance, strategy"
4. Visit Dashboard → See "Suggested Executives"
5. See executives ranked by match score
6. Click executive → See match indicator

### Journey 3: A/B Test Interaction
1. Visit `/b77952e/`
2. See variant assignment (A or B)
3. See correctly labeled button ("kudos" or "thanks")
4. Click button → See feedback
5. Refresh page → See same variant (session persistence)
6. Check GA4 → Event recorded

---

## Technical Achievements

### Matching Algorithm Implementation
- Pure Python implementation, no external libraries
- Efficient set operations for tag matching
- Handles edge cases (empty tags, whitespace, case)
- Sortedranked results by relevance
- Reusable functions for both directions

### Two-Path UX Design
- Clear user segmentation on homepage
- Distinct value propositions for each user type
- Seamless navigation between paths
- Professional hero sections

### A/B Testing
- Session-based variant assignment using Django sessions
- Random 50/50 split on first visit
- Persistent across page views
- Integrated with Google Analytics
- Meets all rubric requirements

### Analytics Integration
- GA4 property created
- Tracking code on all pages
- Custom event structure for A/B test
- Event parameters capture variant details

---

## Lessons Learned

### What Worked Well
1. **Tag system simplicity:** Comma-separated strings were flexible and easy to implement
2. **Matching algorithm clarity:** Pure functions made testing and debugging straightforward
3. **Session management:** Django's built-in sessions handled A/B test persistence perfectly
4. **Two-path UX:** Clear user segmentation improved navigation

### Challenges Encountered
1. **CSS organization:** Multiple rounds of fixes led to fragmented styles
   - **Solution:** Used inline styles as fallback for stubborn issues
2. **A/B test requirements:** Initially built wrong variant (headlines vs button text)
   - **Solution:** Carefully re-read rubric and rebuilt correctly
3. **Button ID requirement:** Almost missed exact `id="abtest"` requirement
   - **Solution:** Double-checked rubric requirements before deployment

### Technical Decisions
- Used Django sessions for A/B variant (vs cookies or database)
- Chose comma-separated tags over ManyToMany (simpler for MVP)
- Inline styles for dashboard spacing (vs fighting CSS cascade)
- Single matching.py module (vs scattered functions)

---

## Velocity & Metrics

- **Sprint 1 Velocity:** 21 points
- **Sprint 2 Velocity:** 22 points
- **Sprint 3 Velocity:** 34 points
- **Sprint 4 Velocity:** 39 points
- **Cumulative Velocity:** 116 points across 4 sprints
- **Average Velocity:** 29 points/sprint
- **Velocity Change:** +14.7% increase from Sprint 3

**Analysis:** Continued velocity improvement showing:
- Increased Django expertise
- Better estimation accuracy
- Reusable patterns and components
- Efficient problem-solving

---

## Stakeholder Feedback

- Two-path UX clearly segments users
- Matching algorithm provides real value
- A/B test endpoint meets all requirements
- Professional appearance throughout
- Ready for final submission

---

## Acceptance Criteria Review

| Requirement | Criteria | Met? |
|-------------|----------|------|
| Authentication | Users can signup, login, logout | ✅ |
| Content Ownership | Users can only edit own content | ✅ |
| Two-Path Homepage | Clear paths for startups vs fractionals | ✅ |
| Dashboard | Users see their profiles and jobs | ✅ |
| Tags | Tags can be added and displayed | ✅ |
| Matching | Algorithm matches based on tags | ✅ |
| A/B Endpoint | `/b77952e` with kudos/thanks button | ✅ |
| Analytics | GA4 tracking on all pages | ✅ |
| Production | Deployed and accessible | ✅ |

---

## Deployment Status

- **Production URL:** https://frac-app.onrender.com
- **A/B Test URL:** https://frac-app.onrender.com/b77952e/
- **Status:** ✅ All features live
- **Database:** PostgreSQL with all migrations
- **Analytics:** GA4 collecting data
- **Uptime:** Stable

---

## Backlog for Post-Sprint 4

**High Priority (for final submission):**
- Comprehensive README
- Burndown/velocity chart
- Final project report
- A/B test traffic analysis

**Medium Priority:**
- Staging environment
- Expanded test coverage
- Code linting
- CSS refactoring

**Low Priority (post-submission):**
- Search and filtering
- Email notifications
- Profile photos
- Advanced analytics

---

## Next Steps

**Before December 12 deadline:**
1. Create comprehensive README
2. Generate burndown chart for all 4 sprints
3. Analyze A/B test data from Google Analytics
4. Write final project report
5. Final testing and bug fixes