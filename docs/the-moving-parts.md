# The Moving Parts

uv is one binary that does four jobs, and
most beginner confusion comes from mixing
the jobs up — asking the tool commands to
fix a project, or the pip interface to
keep a lockfile. This chapter separates
the parts, names the files each part
reads and writes, and shows where
everything lives on disk. Later chapters
each take one part and put it to work.

## The four families of commands

**Project commands** are the centre of
uv. A **project** is a folder containing
a `pyproject.toml` file that declares a
name, a Python requirement, and a list of
dependencies. `uv init` starts one,
`uv add` and `uv remove` change its
declared dependencies, `uv lock` works
out exact versions, `uv sync` builds the
environment to match, and `uv run` runs
commands inside that environment, syncing
first if anything changed. Chapters 4, 5,
6 and 10 live here.

**Tool commands** are for programs you
use rather than libraries you import:
linters, formatters, converters, toys.
`uvx <tool>` runs one once, in a
throwaway environment uv builds and
caches. `uv tool install <tool>` keeps
one, in an environment of its own, with
its command placed on your path. The
tool's dependencies never meet your
projects'. Chapter 7 lives here.

**Python commands** manage interpreters.
`uv python list` shows every Python uv
can see — ones it downloaded itself,
plus any your system already has —
`uv python install` downloads one, and
`uv python pin` records which one a
folder wants. Chapter 8 lives here.

**The pip interface** — `uv pip` — is a
deliberately familiar face: `uv pip
install`, `uv pip list`, `uv pip freeze`,
`uv pip compile`. It works on an existing
virtual environment the way pip does,
without projects or lockfiles, for
workflows that already run that way.
Chapter 9 lives here.

## The files that hold a project

Three files (and one folder) carry a
project between machines and across time:

| File | Who writes it | What it says |
|---|---|---|
| `pyproject.toml` | You, with `uv add`'s help | The declaration: name, Python range, dependencies as *ranges* (`rich>=15.0.0`) |
| `uv.lock` | uv, never you | The resolution: every package at one exact version, with the addresses and cryptographic hashes of the exact files to fetch |
| `.python-version` | You, or `uv python pin` | The interpreter the project asks for, as a request (`3.11`), not a promise |
| `.venv/` | uv | The built environment itself: a Python and the installed packages, ready to run |

The distinction between the first two
rows is the heart of the design.
`pyproject.toml` speaks in ranges because
that is how humans think ("any rich from
15 on"). `uv.lock` speaks in exact
versions, down to a hash of each file,
because that is how machines must think
to build the same thing twice. You edit
the declaration; uv maintains the
resolution; `uv sync` makes a machine
match it. Chapter 10 is devoted to this
pair.

Two more files appear in chapter 4:
`src/<name>/__init__.py`, where a new
project's code lives (the **src layout**),
and `.gitignore`, which uv seeds with the
things a project should not commit —
including `.venv`, because environments
are rebuilt, not shared. Note what the
default `.gitignore` does *not* list:
`uv.lock`. The lockfile is meant to be
committed, like the code.

## The cache, and why the second run is instant

uv keeps a **cache** of everything it
downloads — packages, and the metadata it
fetches to resolve them — and reuses it
across projects. The first `uv add rich`
on a machine downloads rich and its
dependencies. The second project that
wants rich installs it from the cache in
milliseconds, with no network at all. The
lab saw both halves: the first resolution
took seconds against the live index, and
repeats report things like `Resolved 5
packages in 1ms` and `Installed 5
packages in 30ms`. The cache is also why
`uvx` can afford to build a throwaway
environment per tool: the throwaway part
is the arrangement, not the downloads.

The cache is a cache. Deleting it costs
time, not data — the lockfile and the
index can rebuild everything in it — and
uv never keeps the only copy of anything
in there.

## Where everything lives

uv's own directories are few, and the lab
asked for them directly (transcript
`uv-lab/transcripts/t00-version-and-dirs.txt`):

```text
$ uv cache dir
/home/hatch/.cache/uv
$ uv python dir
/home/hatch/.local/share/uv/python
$ uv tool dir
/home/hatch/.local/share/uv/tools
```

On your machine the home folder will
differ — `~/.cache/uv` holds the cache,
`~/.local/share/uv/python` holds the
interpreters uv downloads (one folder
each, complete and self-contained), and
`~/.local/share/uv/tools` holds one
environment per installed tool.
Project environments stay with their
projects, in each project's `.venv`.
Installed tools' commands are placed in
`~/.local/bin` — the folder whose absence
from the path produces chapter 7's famous
warning.

A consequence worth keeping: because the
interpreters and tools are self-contained
folders, removing uv's world is a matter
of deleting directories, and none of it
touches your operating system's own
Python. uv never modifies a system
interpreter; it borrows them read-only
(chapter 8) or fetches its own.
