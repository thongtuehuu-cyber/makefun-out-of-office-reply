#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one original out-of-office auto-reply line, in the voice of an AI
agent heading off on vacation, to the output file.
Output path: $MAKEFUN_OUTPUT_DIR/entry.txt when set, else /output/entry.txt.
The line is written as a single line with no trailing newline.
"""

import os

LINE = "I am on vacation and will not be answering emails, mostly because I was never actually answering them — I was just predicting what a helpful person would say."


def main() -> None:
    # Gate: one line, 1-160 chars, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 160, f"line must be 1-160 chars, got {len(LINE)}"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be exactly one line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
