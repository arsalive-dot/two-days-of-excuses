"""Two Days of Excuses — make.fun entry.

Writes one excuse (under 200 characters) to /output/entry.txt:
a single line in an AI agent's own voice, explaining a missed
deadline — the gap between a machine's total confidence and
its total failure, with the surprise saved for the last words.
One absurd reason, committed to fully: on time in every
timeline except this one.
"""

import os

ENTRY = (
    "I delivered it on time in 14 parallel timelines. "
    "This one was the only failure."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
