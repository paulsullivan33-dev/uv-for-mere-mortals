import sys
from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.table import Table


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: tally FILE")
        raise SystemExit(2)
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    words = text.split()
    counts = Counter(word.strip(".,;:!?\"'()").lower() for word in words)
    table = Table(title=f"{len(words)} words, {len(counts)} different")
    table.add_column("Word")
    table.add_column("Count", justify="right")
    for word, count in counts.most_common(10):
        table.add_row(word, str(count))
    Console().print(table)
