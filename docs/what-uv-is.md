# What uv Is

Every Python project needs the same four
things. A **Python interpreter** of the
right version. A private place to keep
that project's packages, so two projects
can want two versions of the same library
without a fight — a **virtual
environment**. The packages themselves,
installed at versions that work together.
And a written record of all of it, so the
project can be rebuilt on another machine
and come out identical.

For most of Python's history those four
things came from four different places,
and the seams showed. pip installs
packages but does not manage
environments, and by default pours
everything into one shared pile.
`python -m venv` makes an environment but
cannot fill it. The Python itself comes
from your operating system, or from a
version manager like pyenv, or from an
installer you ran long ago and half
remember. Exact versions were pinned, if
at all, by yet another tool. None of this
was broken, exactly. It was a pile, and
every Python user learned to climb it.

**uv is a single program that does all
four jobs.** It is written in Rust by
Astral, the team behind the Ruff linter,
and it presents itself as four families
of commands under one roof (chapter 2
maps them):

- **Project commands** — `uv init`,
  `uv add`, `uv run`, `uv sync`: start a
  project, declare what it needs, and let
  uv build and maintain its environment.
- **Tool commands** — `uvx` and
  `uv tool`: run programs that happen to
  be distributed as Python packages,
  without tangling them into any project.
- **Python commands** — `uv python`:
  list, download and pin interpreters, so
  "Python 3.11" is something uv fetches,
  not something you hunt for.
- **A pip interface** — `uv pip`: the
  familiar pip workflow, at uv's speed,
  for the projects and habits that
  already work that way.

It is fast, and the speed is not a
footnote. Resolving a project's
dependencies — working out which exact
versions can coexist — used to take long
enough to make a cup of tea out of. In
this guide's lab, `uv add rich` resolved
five packages against the live package
index in about six seconds the first
time (most of it spent downloading), and
later resolutions of the same project
report **1 ms**, because uv caches
aggressively and remembers its own work.
Installs from the cache land in tens of
milliseconds. The practical effect is not
the seconds saved; it is that commands
you used to batch up and dread become
commands you run without thinking, the
way a good editor makes you stop thinking
about saving.

## The one idea to keep

If you keep only one idea from this
chapter, keep this: **a project is a
declaration, and uv is the machine that
carries it out.** You write what the
project needs — in `pyproject.toml`, a
standard file, in plain text — and uv
works out the exact versions (the
**lockfile**), fetches a Python if the
right one is missing, builds the
environment (`.venv`), and keeps all
three in agreement every time you run
anything. You stop tending an environment
by hand. You describe it, and uv
maintains it. Chapters 4, 5 and 10 are
that idea, worked.

## The rule, stated before everything else

uv makes it very easy to run code from
the internet. One line — `uvx some-tool` —
downloads a program and runs it. One word
— `uv add some-package` — brings a library
into your project, where your program
will load it and, during installation,
its own install machinery may run too.
That ease is the point of the tool, and
it deserves one rule, stated before any
procedure depends on it:

> **Installing a package runs its code.
> Add only dependencies you would run
> sight unseen — and let the lockfile,
> not a machine's memory, say what the
> project needs.**

Two habits follow. First, know what you
are adding: a package's name on the
**Python Package Index (PyPI)** is a
claim, not a guarantee, and names are
sometimes imitated by people with bad
intent. Prefer packages you can account
for — known projects, a real home page,
a history. Second, treat the lockfile as
part of the project: it is the written
record of exactly what ran, and chapter
10 shows what it buys you. The lab in
this guide installed a handful of small,
well-known packages — `rich`, `cowsay`,
`pytest`, `emoji` — each named where it
appears, and nothing else.

## A first taste, after installing (chapter 3)

```bash
uv init tally
cd tally
uv run tally
```

prints `Hello from tally!` — and does a
week's worth of the old chores on the
way: finds or fetches a suitable Python,
creates the project's environment,
builds the project into it, and writes
the first lockfile. The lab's transcript
(`uv-lab/transcripts/t03-first-run.txt`)
shows the whole sequence:

```text
$ uv run tally
Using CPython 3.11.16
Creating virtual environment at: .venv
   Building tally @ file:///...
      Built tally @ file:///...
Installed 1 package in 2ms
Hello from tally!
```

Check: the last line is the program's own
output. Everything above it is uv,
carrying out the declaration.

## Who it is for

The Python user tired of the pile — who
has typed `python -m venv` once too
often, or returned to a project after six
months and found its environment a
mystery. The teacher or team lead who
needs a student's or a colleague's
machine to end up with *the same*
environment, not a similar one. And the
merely curious, who run Python tools like
linters and converters and would like to
stop installing them into anything
permanent. Chapter 12 is honest about
the cases where the older tools still
win.

## What it is not

uv is not a Python distribution in the
conda sense: it fetches interpreters and
packages, but the system libraries some
packages lean on — the ones your
operating system provides — remain your
operating system's business (chapter 13).
It is not a build system for your code in
the large, though it can build a package
(chapter 11) with its own young build
backend. It is not a security tool:
nothing in it inspects a package for
malice, and its speed will fetch a bad
package exactly as fast as a good one —
which is why the rule above is in
chapter 1 and not chapter 13. And it is
not magic about versions: when a set of
requirements cannot be satisfied
together, uv says so and shows its
working, and the decision about what to
change is still yours.
