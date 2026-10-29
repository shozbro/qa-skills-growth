# Track C: CI/CD

- Target: 1 -> 4
- Window: 2026-11-23 to 2027-01-15
- Done when: GitHub Actions runs the BTS smoke suite on demand or after a deploy and posts the report to Slack.

## Steps

- [ ] **C1** (by 2026-12-04) Learn GitHub Actions basics: workflow file, jobs, secrets and a manual trigger.
- [ ] **C2** (by 2026-12-18) Run the BTS smoke suite headless in a workflow.
- [ ] **C3** (by 2027-01-08) Post the run report to Slack and add the Track B database checks as a step.
- [ ] **C4** (by 2027-01-15) Ask dev or DevOps how deploys start, then trigger the workflow after a deploy.

## Where to learn

- [Microsoft Learn: Automate your workflow with GitHub Actions](https://learn.microsoft.com/en-us/training/paths/automate-workflow-github-actions) (page opened). 4 modules. Shows achievement badges; the page states no certificate or price.
- [GitHub Skills](https://skills.github.com/) (not opened). Includes Actions courses. No certificate confirmed.
- [Playwright: continuous integration](https://playwright.dev/docs/ci-intro) (not opened). Run Playwright tests in a CI workflow. No certificate.

## Test

```
python quiz.py C -n 8
```
