# Sprint 2 — Review
**Goal:** Working staging app with DB + dynamic page  
**Staging URL:** https://<your-app>.onrender.com

## What’s Working (demo)
- `/health/` returns `ok`
- `/executives/` lists profiles from DB (Render Postgres)
- `/executives/<id>/` detail page
- Django Admin accessible; sample data added

## Completed Stories
- #08 - "Basic form validation" - **2 pts**
- #01 — “Browse executives list page” — **3 pts**
- #02 — “Executive profile detail page” — **3 pts**
- #00 — “Health check route for uptime” — **1 pt**
- #00 — “Staging deploy w/ Postgres + static files” — **5 pts**

**Planned:** 14 pts  
**Completed:** 14 pts  
**Velocity:** 14  
**Completion rate:** 100%

## Incomplete Stories
- N/A (or list any, with reason and carryover plan)

## Lessons Learned
- Render free tier lacks shell → ran migrations via local `DATABASE_URL`
- WhiteNoise needed for admin/static in prod
- Env-driven `ALLOWED_HOSTS` prevents host errors

## Backlog Updates
- Add basic job classifieds model (Sprint 3)
- Add seed script/fixtures
- Simple search/filter (later)
