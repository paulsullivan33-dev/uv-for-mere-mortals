# Running Code

Everything so far has funnelled into one
command: `uv run`. This chapter takes it
apart — what it guarantees before your
code starts, the three shapes of thing it
can run, and its most surprising trick, a
single-file script that declares its own
dependencies and runs anywhere uv does.

## What `uv run` does before anything runs

`uv run <command>` performs a short
ritual, every time, in the project's
folder:

1. It reads the declaration —
   `pyproject.toml`, `.python-version`.
2. It checks the lockfile still matches
   the declaration, and re-resolves if
   you changed something (chapter 10
   shows it refusing, when told to, rather
   than drifting).
3. It makes `.venv` match the lockfile
   exactly — installing what is missing,
   removing what is no longer declared.
4. It runs your command inside that
   environment.

Steps 1–3 are why chapters 4 and 5 could
be so short: there is no "did I activate
the environment, is it up to date" —
there is only "run it", and correctness
is the command's problem, not yours. When
nothing changed, the ritual is silent and
takes milliseconds; you saw both the full
ceremony (the first run) and the silence
(every run since).

## The three shapes

**A command the project provides.** The
`[project.scripts]` entry made `tally`
itself a command:

```bash
uv run tally sample.txt
```

Any command installed into the environment
— including ones your dependencies bring
— can be run the same way, which is how
you will run test runners and linters in
chapter 5's dev group: `uv run pytest`.

**Python itself, and plain scripts.**
`uv run python` starts the project's
interpreter — the pinned one, with the
project's packages importable — and
`uv run somefile.py` runs a file in that
same environment:

```bash
uv run python -c "import rich; print(rich.__version__)"
```

**A borrowed package, for one run.**
Sometimes a command needs a library the
project does not depend on — an experiment,
a one-off conversion. `--with` lends it
for that run only (transcript
`uv-lab/transcripts/t17-run-with.txt`):

```text
$ uv run --with emoji python -c "import emoji; print(emoji.emojize(':thumbs_up: borrowed for one run only'))"
Installed 1 package in 1ms
👍 borrowed for one run only
```

The lab checked afterwards: `pyproject.toml`
still lists only `rich`. The borrowed
package arrived from the cache, served
one command, and joined nothing. This is
the honest way to try a library before
chapter 1's rule has been fully applied
to it — try with `--with`, adopt with
`uv add`.

## Scripts that carry their own shopping list

The neatest idea in modern Python is not
uv's own; it is a standard (PEP 723) that
uv implements particularly well. A single
`.py` file may declare, in a comment
block at its top, the Python it needs and
the packages it imports:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "cowsay",
# ]
# ///

import cowsay

cowsay.cow("a script that carries its own shopping list")
```

This is the lab's `uv-lab/greet.py`,
word for word. Running it — from any
folder, with no project in sight — the
lab watched uv build a small private
environment for the script, install
`cowsay` into it from the cache, and run
(transcript `uv-lab/transcripts/t08-pep723-script.txt`):

```text
$ uv run greet.py
Installed 1 package in 6ms
  ___________________________________________
| a script that carries its own shopping list |
  ===========================================
...
```

And the second run prints no install
line at all: the script's environment is
cached, keyed by the declarations in the
file, so the script starts instantly —
and if you edit the dependency block, uv
notices and rebuilds. `uv add --script greet.py cowsay`
will write or update the declaration
block for you, which is the tidy way to
grow such a script (documented here; the
lab wrote its block by hand so the
transcript shows the whole file).

Check: a script like this can be copied
to any machine with uv on it — a
colleague's, a fresh laptop, a server —
and `uv run greet.py` reproduces its
needs exactly, Python version included.
No README of instructions, no
requirements file travelling separately
and getting lost. The script *is* the
project, at the smallest size a project
can be. Chapter 11 uses this for its
most useful recipe.
