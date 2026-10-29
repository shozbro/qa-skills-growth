#!/usr/bin/env python3
"""Random quiz runner. Standard library only.

  python quiz.py A            5 random questions from Track A
  python quiz.py A -n 8       8 random questions
  python quiz.py --final      one random set from every multiple choice skill
  python quiz.py --list       show available skills
Add --seed N to repeat the same draw. Results are appended to results.csv.
"""
import argparse, csv, datetime, json, random, sys
from pathlib import Path

HERE = Path(__file__).parent
TESTS = HERE / "tests"
PASS = 0.70


def banks():
    out = {}
    for f in sorted(TESTS.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        out[d["skill"]] = d
    return out


def ask(skill, bank, n, rng):
    qs = rng.sample(bank["questions"], min(n, len(bank["questions"])))
    right, missed = 0, []
    print(f"\n=== {skill}: {bank['name']} ({len(qs)} questions) ===")
    for i, q in enumerate(qs, 1):
        order = list(range(len(q["options"])))
        rng.shuffle(order)
        print(f"\n{i}. {q['q']}")
        for pos, idx in enumerate(order):
            print(f"   {'abcd'[pos]}) {q['options'][idx]}")
        while True:
            try:
                a = input("   answer: ").strip().lower()
            except EOFError:
                a = ""
            if len(a) == 1 and a in "abcd"[: len(order)]:
                break
            if not sys.stdin.isatty():
                a = "x"
                break
            print("   enter a letter")
        correct_pos = order.index(q["answer"])
        if a == "abcd"[correct_pos]:
            right += 1
        else:
            missed.append((q, "abcd"[correct_pos]))
    pct = right / len(qs) if qs else 0
    verdict = "PASS" if pct >= PASS else "RETRY"
    print(f"\n{skill}: {right}/{len(qs)} ({pct:.0%}) {verdict}")
    for q, letter in missed:
        print(f"  - {q['q']}\n    correct: {q['options'][q['answer']]}\n    why: {q['why']}")
    return right, len(qs), verdict


def log(skill, right, total, verdict):
    path = HERE / "results.csv"
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["date", "skill", "right", "total", "verdict"])
        w.writerow([datetime.date.today().isoformat(), skill, right, total, verdict])


def main():
    p = argparse.ArgumentParser()
    p.add_argument("skill", nargs="?")
    p.add_argument("-n", type=int, default=5)
    p.add_argument("--final", action="store_true")
    p.add_argument("--list", action="store_true")
    p.add_argument("--seed", type=int)
    a = p.parse_args()
    b = banks()
    rng = random.Random(a.seed)
    if a.list or (not a.skill and not a.final):
        for k, d in b.items():
            print(f"{k:3} {d['name']} ({len(d['questions'])} questions)")
        print("L2, L7, L8: see tests/practical.md")
        return
    keys = list(b) if a.final else [a.skill.upper()]
    for k in keys:
        if k not in b:
            sys.exit(f"Unknown skill {k}. Use --list.")
        r, t, v = ask(k, b[k], a.n, rng)
        log(k, r, t, v)


if __name__ == "__main__":
    main()
