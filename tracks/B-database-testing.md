# Track B: Database testing

- Target: 2 -> 4
- Window: 2026-11-02 to 2026-12-11
- Done when: A read-only SQL check script reports missing Cms_Ids, null configs and broken parent-child links on a BTS environment.

## Steps

- [ ] **B1** (by 2026-11-13) Practise joins, aggregates and window functions on tables you already query, such as category_community.
- [ ] **B2** (by 2026-11-27) Write read-only checks for null or duplicate Cms_Id, orphaned relations and parent_id chains.
- [ ] **B3** (by 2026-12-04) Add config checks for null values in JSON fields such as space_settings.
- [ ] **B4** (by 2026-12-11) Run the script against a BTS environment and produce a pass/fail report.

## Where to learn

- [freeCodeCamp: Relational Databases certification](https://www.freecodecamp.org/news/freecodecamp-certifications/) (page opened). The PostgreSQL part builds the SQL you need here.
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) (not opened). Official tutorial, free. No certificate.
- [SQLBolt](https://sqlbolt.com/) (not opened). Short interactive SQL lessons. No certificate.

## Test

```
python quiz.py B -n 8
```
