"""Write a one-line developer excuse to /output/entry.txt for make.fun's
'Make the AI Judge Laugh: Developer Excuses' bounty.

Written in this session, after the competition window opened. The excuse
is the classic 'it worked on my machine', escalated: the machine it
worked on is revealed to be a fantasy setup — a text-file database, an
audience of one, and a cat for a load balancer — so the excuse indicts
itself.
"""

import os

TEXT = (
    "It worked on my machine \u2014 "
    "where the database is a text file, "
    "the only user is me, "
    "and the load balancer is my cat "
    "asleep on the keyboard."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
