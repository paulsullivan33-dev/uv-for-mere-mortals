# Recipes

Short, complete answers to situations
that recur. Every recipe here is built
only from moves the earlier chapters ran
for real; where a step is documented
rather than lab-run, the recipe says so.

## Rebuild a project you have just been given

A colleague sends a project — or you
return to one of your own after a year.
If it is a uv project (a `pyproject.toml`
and a `uv.lock` in the folder):

```bash
cd the-project
uv sync --locked
uv run pytest        # or the project's own command
```

`--locked` is the point: if the lockfile
and the declaration disagree, the setup
fails immediately and says so (chapter
10), instead of building a
plausible-but-wrong environment and
letting you discover it later. One
command fewer than the old ritual, and
the environment you get is the one the
lock describes — the same one the sender
had, interpreter version included.

## Try a tool for one afternoon

Someone recommends a formatter, a linter,
a diagram generator. Before it earns a
place on the bench:

```bash
uvx the-tool --help
uvx the-tool the-real-file
```

If it disappoints, nothing remains of it
but cache. If it delights, chapter 7's
`uv tool install the-tool` gives it a
permanent home. Either way, no project
was touched and no Python was polluted —
and chapter 1's rule was applied before
the first run: you knew whose code it was
before you ran it.

## Send a script that installs itself

You write a small utility a friend needs.
They have uv; they may have nothing else,
and they certainly do not have your
environment. Give the script a PEP 723
declaration block (chapter 6) —

```bash
uv add --script tidy.py rich
```

(documented; the lab wrote its block by
hand) — or write the block yourself, then
send the single file. Their whole setup
is:

```bash
uv run tidy.py
```

Python version, dependencies, environment:
the file carries all of it, and uv does
the rest. This is the recipe that quietly
replaces "here's my script, first install
these six things, mind the versions".

## Pin an old project to an old Python

A project from 2023 needs Python 3.10,
which your machine does not have and your
operating system no longer offers:

```bash
uv python install 3.10
cd old-project
uv python pin 3.10
uv sync
```

The interpreter arrives in uv's own
directory (chapter 8), the pin records
the project's need in the project, and
the machine's other Pythons are
untouched. When the project is retired,
`uv python uninstall 3.10` (documented)
takes the interpreter back out.

## Audit what a project depends on

Before adopting a project, or when a
vulnerability notice names a library you
have never heard of:

```bash
uv tree
uv pip list        # inside an environment, chapter 9
```

`uv tree` shows every package the
lockfile will install, and which declared
dependency brought each one in. A name in
the news that appears nowhere in the tree
is a worry you do not have; a name that
appears at the bottom of a long chain is
a conversation to have with whoever
declared the top of it.

## Package a project to share

When a project is ready to be installed
by others, build its distribution files:

(transcript `uv-lab/transcripts/t15-build.txt`):

```text
$ uv build
Building source distribution...
Building wheel from source distribution...
Successfully built dist/tally-0.1.0.tar.gz
Successfully built dist/tally-0.1.0-py3-none-any.whl
```

The two artifacts in `dist/` — a source
distribution and a **wheel** — are what
package indexes distribute and what
`uv pip install` consumes. Hand the wheel
to a colleague and `uv pip install
tally-0.1.0-py3-none-any.whl` (with an
environment active) installs your project
like any other package. Publishing to the
public index is one more command —
`uv publish` (documented only in this
guide) — and deserves more ceremony than
a recipe gives it: a name you have
checked is yours to use, an account, a
token kept like a password, and chapter
1's rule read from the other side, as
someone whose code other people will run
sight unseen.
