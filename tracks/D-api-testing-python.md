# Track D: API testing automation and Python

- Target: API 3 -> 4, Python 3 -> 4
- Window: 2026-12-14 to 2027-02-12
- Done when: A pytest API suite with auth, schema checks and negative cases runs inside the Track C pipeline.

## Steps

- [ ] **D1** (by 2026-12-23) Learn pytest fixtures, parametrization and API token handling with requests or httpx.
- [ ] **D2** (by 2027-01-15) Automate BTS endpoint checks: status codes, response schema and negative cases.
- [ ] **D3** (by 2027-01-29) Add a sync check that the forward-sync result matches the database.
- [ ] **D4** (by 2027-02-12) Run the suite inside the Track C pipeline; shared setup lives in fixtures, no copy-pasted tests.

## Where to learn

- [freeCodeCamp: Scientific Computing with Python certification](https://www.freecodecamp.org/news/freecodecamp-certifications/) (page opened). Free curriculum, certificate after five projects.
- [Test Automation University](https://testautomationu.applitools.com/) (press release read). Free courses for test engineers. Badges and credits per a 2019 press release; no certificate mentioned.
- [pytest: getting started](https://docs.pytest.org/en/stable/getting-started.html) (not opened). Official docs, free. No certificate.
- [Postman Learning Center](https://www.postman.com/learn/) (not opened). Search results describe a Student Expert badge. Cost and eligibility not confirmed.

## Test

```
python quiz.py D -n 8
```
