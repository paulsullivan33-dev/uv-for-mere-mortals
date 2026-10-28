# Managing Pythons

Ask a room of Python users where their
Python came from and you will hear a
history of the operating system wars:
the one the distro shipped, two from a
version manager, one from an installer, a
conda, a Docker image, and a suspicion
that none of them is the one the current
project wants. Projects are picky —
chapter 4's tally declares
`requires-python = ">=3.11"` — and the
traditional tools for satisfying them
(pyenv, deadsnakes-style repositories, the
python.org installers) each manage a
slice of the problem. uv treats
interpreters the way it treats packages:
things to be found if present, fetched if
missing, and recorded either way.

## What you have: `uv python list`

(transcript `uv-lab/transcripts/t09-python-list.txt`,
trimmed):

```text
$ uv python list
cpython-3.14.10-linux-x86_64-gnu      <download available>
cpython-3.13.18-linux-x86_64-gnu      <download available>
cpython-3.12.16-linux-x86_64-gnu      <download available>
cpython-3.12.3-linux-x86_64-gnu       /usr/bin/python3.12
cpython-3.11.18-linux-x86_64-gnu      <download available>
cpython-3.11.16-linux-x86_64-gnu       /home/hatch/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu/bin/python3.11
cpython-3.10.22-linux-x86_64-gnu      <download available>
...
```

Three kinds of line appear. Pythons with
a path on your system already — the
lab's `/usr/bin/python3.12`, which uv will
happily borrow read-only. Pythons under
uv's own Python directory, which uv
downloaded earlier (the 3.11.16 — its
arrival is the story below). And versions
marked `<download available>`: known,
fetchable on demand, costing nothing
until wanted. The list also includes
other implementations (PyPy, GraalPy
appear further down the lab's full
transcript) — uv's fetching is not
limited to CPython, though CPython is
what this guide uses.

## The Python that arrived by itself

Chapter 4's first run printed `Using
CPython 3.11.16` although nobody had
installed a 3.11 on that machine. What
happened: the project's `.python-version`
asked for 3.11, no system 3.11 existed, so
uv downloaded one into its Python
directory and used it — no prompt, no
separate chore. That is the default
behaviour, and mostly it is a delight.
It is worth knowing it happens, because
the download is real (a full interpreter,
some thirty megabytes) and because "where
did this Python come from" is a question
with an answer — `uv python list` shows
its address, and chapter 14 returns to
this moment from the puzzled side.

## Fetching one on purpose: `uv python install`

(transcript `uv-lab/transcripts/t10-python-install-pin.txt`):

```text
$ uv python install 3.13
Downloading cpython-3.13.18-linux-x86_64-gnu (download) (33.8MiB)
 Downloaded cpython-3.13.18-linux-x86_64-gnu (download)
Installed Python 3.13.18 in 27.56s
 + cpython-3.13.18-linux-x86_64-gnu (python3.13)
```

Ask for a version as loosely (`3.13`) or
as exactly (`3.13.18`) as you like; uv
fetches the newest matching build from
the python-build-standalone project — the
same source most modern Python tooling
uses — and unpacks it into its own
directory, complete and independent of
your operating system. `uv python find
3.13` prints the interpreter's full path
when something (an editor, another tool)
needs to be told where it lives:

```text
$ uv python find 3.13
/home/hatch/.local/share/uv/python/cpython-3.13-linux-x86_64-gnu/bin/python3.13
```

Removing one is `uv python uninstall
3.13` (documented; the lab kept both of
its fetched interpreters). Deleting an
interpreter a project still wants is not
a crisis — the next `uv run` simply
fetches it again, which tells you
something about how uv regards its own
world: everything in it is rebuildable.

## Asking on paper: pin and `requires-python`

Two files ask for a Python, and the
difference between them causes real
confusion, so here it is plainly:

- **`.python-version`** names the
  interpreter to *use* — a choice, made
  by `uv python pin 3.13`, by
  `uv init --python 3.13`, or by typing
  the file yourself. Tools beyond uv
  (editors, other version managers)
  respect the same file, which is why it
  exists separately at all.
- **`requires-python`** in
  `pyproject.toml` names the range the
  project *supports* — a boundary, part
  of the published declaration, used when
  resolving dependencies and when other
  people install your package.

The pin must fit inside the boundary: pin
3.10 in a project whose `requires-python`
says `>=3.11` and uv will refuse or fetch
a conforming one rather than saw off the
branch the project stands on. The lab
demonstrated both writings of the pin
(transcript t10):

```text
$ uv python pin 3.13
Pinned `.python-version` to `3.13`

$ uv init --python 3.13 hello313
Initialized project `hello313` at `/home/.../hello313`
```

Check: in the new project, `uv run
hello313` printed `Using CPython 3.13.18`
— the fetched interpreter of this chapter,
chosen by a five-character file. One
project per version question, answered in
writing, in the project itself: that is
the whole system, and it replaces a shelf
of version-manager folklore.
