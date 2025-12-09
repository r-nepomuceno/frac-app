# Sprint 2 — Retrospective
**Date:** 2025-11-12  
**Attendees:** Robby Nepomuceno, Wit Wattananimitgul, Dylan Safyer, Henry Melzner, Joseph Dobson

## What went well
1. End-to-end deploy to Render with Postgres
2. Static files fixed via WhiteNoise
3. Simple, testable health route and views

## What didn’t go well
1. `ALLOWED_HOSTS` conflict (duplicate setting) caused deploy hiccup
2. No shell on free tier slowed migrations

## What to improve (actionable)
1. Add a `collectstatic` step to Build Command — **Owner:** X — **Due:** Next deploy
2. Keep env-driven settings in one place; remove duplicates — **Owner:** Y — **Due:** Now

## Action Items
- Create DB fixture for demo data — issue #NN — **Due:** Sprint 3
- Add CI to run tests on push — issue #NN — **Due:** Sprint 3
