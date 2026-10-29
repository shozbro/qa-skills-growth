# QA Skills Growth

Study plan and self-tests. Window: 30 Oct 2026 to 15 Mar 2027 (31 Mar is the hard limit).

## Everything on one page

Open **`index.html`** (double-click it after cloning). It has tabs for every track, study links, a tick list and the quizzes, all in one file with no install. To use it online, enable GitHub Pages: Settings, Pages, deploy from branch `main`, folder `/ (root)`.

This README holds the same plan. Click a track to expand it.

<details>
<summary><b>Track A: Git and code reviews</b> (finish by 2026-11-20)</summary>

Target: Git 2 -> 4, Code reviews 1 -> 3. Window: 2026-10-30 to 2026-11-20.

**Steps**

- [ ] by 2026-11-03: Keep your BTS automation in a Git repo and change it only through branches and PRs.
- [ ] by 2026-11-10: On a throwaway repo, practise rebase, merge-conflict resolution and cherry-pick.
- [ ] by 2026-11-17: Open PRs for your test changes and get them reviewed.
- [ ] by 2026-11-20: Review 5 teammates' PRs, with written comments on logic, naming and test coverage.

**Study here (free)**

- [freeCodeCamp: Relational Databases certification](https://www.freecodecamp.org/news/freecodecamp-certifications/) (page opened). Bash, PostgreSQL and Git. Free curriculum, certificate after five projects.
- [GitHub Skills](https://skills.github.com/) (not opened). Hands-on courses inside your own repo. No certificate confirmed.
- [Pro Git book](https://git-scm.com/book/en/v2) (not opened). Free to read online. No certificate.
- [Google engineering practices: code review](https://google.github.io/eng-practices/review/) (not opened). What reviewers look for and how to write comments. No certificate.

**Done when:** BTS test code is in a repo with PRs you opened, and you reviewed 5 PRs with written comments.

**Test:** `python quiz.py A` or the Quiz tab in `index.html`

</details>

<details>
<summary><b>Track B: Database testing</b> (finish by 2026-12-11)</summary>

Target: 2 -> 4. Window: 2026-11-02 to 2026-12-11.

**Steps**

- [ ] by 2026-11-13: Practise joins, aggregates and window functions on tables you already query, such as category_community.
- [ ] by 2026-11-27: Write read-only checks for null or duplicate Cms_Id, orphaned relations and parent_id chains.
- [ ] by 2026-12-04: Add config checks for null values in JSON fields such as space_settings.
- [ ] by 2026-12-11: Run the script against a BTS environment and produce a pass/fail report.

**Study here (free)**

- [freeCodeCamp: Relational Databases certification](https://www.freecodecamp.org/news/freecodecamp-certifications/) (page opened). The PostgreSQL part builds the SQL you need here.
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) (not opened). Official tutorial, free. No certificate.
- [SQLBolt](https://sqlbolt.com/) (not opened). Short interactive SQL lessons. No certificate.

**Done when:** A read-only SQL check script reports missing Cms_Ids, null configs and broken parent-child links on a BTS environment.

**Test:** `python quiz.py B` or the Quiz tab in `index.html`

</details>

<details>
<summary><b>Track C: CI/CD</b> (finish by 2027-01-15)</summary>

Target: 1 -> 4. Window: 2026-11-23 to 2027-01-15.

**Steps**

- [ ] by 2026-12-04: Learn GitHub Actions basics: workflow file, jobs, secrets and a manual trigger.
- [ ] by 2026-12-18: Run the BTS smoke suite headless in a workflow.
- [ ] by 2027-01-08: Post the run report to Slack and add the Track B database checks as a step.
- [ ] by 2027-01-15: Ask dev or DevOps how deploys start, then trigger the workflow after a deploy.

**Study here (free)**

- [Microsoft Learn: Automate your workflow with GitHub Actions](https://learn.microsoft.com/en-us/training/paths/automate-workflow-github-actions) (page opened). 4 modules. Shows achievement badges; the page states no certificate or price.
- [GitHub Skills](https://skills.github.com/) (not opened). Includes Actions courses. No certificate confirmed.
- [Playwright: continuous integration](https://playwright.dev/docs/ci-intro) (not opened). Run Playwright tests in a CI workflow. No certificate.

**Done when:** GitHub Actions runs the BTS smoke suite on demand or after a deploy and posts the report to Slack.

**Test:** `python quiz.py C` or the Quiz tab in `index.html`

</details>

<details>
<summary><b>Track D: API testing automation and Python</b> (finish by 2027-02-12)</summary>

Target: API 3 -> 4, Python 3 -> 4. Window: 2026-12-14 to 2027-02-12.

**Steps**

- [ ] by 2026-12-23: Learn pytest fixtures, parametrization and API token handling with requests or httpx.
- [ ] by 2027-01-15: Automate BTS endpoint checks: status codes, response schema and negative cases.
- [ ] by 2027-01-29: Add a sync check that the forward-sync result matches the database.
- [ ] by 2027-02-12: Run the suite inside the Track C pipeline; shared setup lives in fixtures, no copy-pasted tests.

**Study here (free)**

- [freeCodeCamp: Scientific Computing with Python certification](https://www.freecodecamp.org/news/freecodecamp-certifications/) (page opened). Free curriculum, certificate after five projects.
- [Test Automation University](https://testautomationu.applitools.com/) (press release read). Free courses for test engineers. Badges and credits per a 2019 press release; no certificate mentioned.
- [pytest: getting started](https://docs.pytest.org/en/stable/getting-started.html) (not opened). Official docs, free. No certificate.
- [Postman Learning Center](https://www.postman.com/learn/) (not opened). Search results describe a Student Expert badge. Cost and eligibility not confirmed.

**Done when:** A pytest API suite with auth, schema checks and negative cases runs inside the Track C pipeline.

**Test:** `python quiz.py D` or the Quiz tab in `index.html`

</details>

<details>
<summary><b>After the four tracks</b> (dated items finish by 15 Mar 2027)</summary>

- [ ] L1 (by 2027-02-26): Playwright, Selenium, Cypress 3 -> 4. Follows from Track C. Docs: https://playwright.dev/docs/intro
- [ ] L3 (by 2027-03-05): Troubleshooting, debugging and RCA 2 and 3 -> 4. Write a short RCA note per defect: logs, network calls, database check, root-cause line.
- [ ] L4 (by 2027-03-15): Performance testing 2 -> 3. Run a k6 load test on one endpoint and record a p95 baseline. Docs: https://grafana.com/docs/k6/latest/
- [ ] L2 (by 2027-03-15): Test estimations 2 -> 3. Log estimate vs actual for every ticket and review monthly. No course needed.
- [ ] L5 (no deadline): Mobile app testing and automation (parked). After March, optional. Needs the mobile KT first. Docs: https://appium.io/docs/en/latest/
- [ ] L6 (no deadline): Penetration testing (parked). After March, optional. OWASP Top 10, then PortSwigger labs: https://portswigger.net/web-security
- [ ] L7 (no deadline): Leadership (ongoing, no deadline). Practise on real work, such as the automation handover or a KT session.
- [ ] L8 (no deadline): Problem solving, creativity, curiosity, innovation (ongoing, no deadline). Practise on real work: write one problem, options, result note per quarter.

Performance and Estimation aim for 3, not 4, to fit the window. Parked and ongoing items are not part of the final test. Practical prompts for L2, L7 and L8 are in `tests/practical.md`.

</details>

## Test yourself

In the browser: open `index.html`, then the Quiz tab. In a terminal:

```
python quiz.py --list                   # skills and question counts
python quiz.py A --level beginner       # beginner, intermediate or advanced
python quiz.py A -n 8                   # 8 random questions
python quiz.py --final                  # a random set from every multiple choice skill
```

Pass mark is 70%. A missed question shows the correct answer, a short reason and a study link. The terminal quiz writes `results.csv`; the browser page keeps its scores in that browser only. Tick `PROGRESS.md` (or the boxes in `index.html`) as you go.

## Repo layout

- `index.html`: the one-page version (plan, links, ticks, quiz)
- `PROGRESS.md`: checklist to tick and commit
- `tracks/`: one file per track and `later-skills.md`
- `tests/`: question banks (`*.json`) and `practical.md`
- `quiz.py`: terminal quiz runner, standard library only

## Honest notes

- Question banks were written by Claude as practice material. They are not an official exam, and a few are tied to assumptions (for example, PostgreSQL syntax in Track B). Check anything doubtful against the docs.
- Links were not all opened. Only freeCodeCamp's certification page, the Microsoft Learn path and the Test Automation University press release were read. Every other link is a standard docs site that was not opened, so free status and certificates are unverified.
- Shortened plan: Performance and Estimation aim for 3, not 4. Parking mobile and penetration testing was a prioritisation choice, so change it if your work needs them sooner.
