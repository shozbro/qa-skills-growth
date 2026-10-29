# After the four tracks

Mobile automation and penetration testing aim for 3, not 4.

- [ ] **L1** (by 2027-01-15) Playwright, Selenium, Cypress 3 -> 4. Follows from Track C. Docs: https://playwright.dev/docs/intro
- [ ] **L2** (by 2027-01-31) Test estimations 2 -> 4. Log your estimate and the actual time for every ticket and compare monthly.
- [ ] **L3** (by 2027-03-31) Troubleshooting, debugging and RCA 2 and 3 -> 4. Write a short RCA note per defect: logs, network calls, database check, root-cause line.
- [ ] **L4** (by 2027-04-30) Performance testing 2 -> 4. Run a k6 load test on one endpoint and record a p95 baseline. Docs: https://grafana.com/docs/k6/latest/
- [ ] **L5** (by 2027-06-30) Mobile app testing 3 -> 4 and automation 1 -> 3. Get the mobile KT first, then automate one smoke flow. Docs: https://appium.io/docs/en/latest/
- [ ] **L6** (by 2027-06-30) Penetration testing 1 -> 3. OWASP Top 10, then a ZAP scan on an environment you may test. Free labs: https://portswigger.net/web-security
- [ ] **L7** (by 2027-06-30) Leadership 2 -> 4. Own something end to end, such as the automation handover or a KT session for the team.
- [ ] **L8** (by 2027-06-30) Problem solving, creativity, curiosity, innovation 2 and 3 -> 4. Ship one small tool or improvement proposal a quarter, written up as problem, options, result.

Tests: `python quiz.py L1` for multiple choice skills (L1, L3, L4, L5, L6). L2, L7, L8: see `tests/practical.md`.
