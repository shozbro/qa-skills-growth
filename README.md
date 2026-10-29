# QA Skills Growth

Learning plan, progress list and random self-tests for raising QA skills over Oct 2026 to Jun 2027.

## Layout

- `PROGRESS.md`: checklist to tick and commit
- `tracks/`: one file per track (steps with dates, free resources, done-when) and `later-skills.md`
- `tests/`: question banks (`*.json`) and `practical.md` for soft skills
- `quiz.py`: random quiz runner, standard library only
- `results.csv`: created on your first quiz, one line per attempt

## Use

```
python quiz.py --list
python quiz.py A -n 8        # one track
python quiz.py --final       # a random set from every multiple choice skill
```

Pass mark is 70%. Missed questions are shown with the correct answer and a short reason.

## Honest notes

- Question banks were written by Claude as practice material. They are not an official exam, and a few are tied to assumptions (for example, PostgreSQL syntax in Track B). Check anything doubtful against the docs.
- Resource links are tagged `page opened` or `not opened`. Not opened means free status and certificate availability were not verified. Only freeCodeCamp's two certifications were confirmed to exist.
- The banks are small (10 questions per track, 5 per later skill), so random draws repeat. Add your own questions to the JSON files as you learn; the format is `q`, `options`, `answer` (index), `why`.
