# Troubleshooting

The failures this guide's lab actually
met, and the ones its transcripts explain
in advance. Each entry is the symptom,
the cause, and the check that tells them
apart.

## "No such file or directory": the missing main.py

**Symptom.** In a new project you look
for the program at the top level —
`cat main.py`, an editor opening the
folder — and it is not there.

**Cause.** Chapter 4's lesson: the src
layout. The code is at
`src/<project-name>/__init__.py`, on
purpose, so the package cannot be
imported by accident from its own folder.

**Check.** `find src -type f` shows the
real address (transcript
`uv-lab/transcripts/t02b-init-src-layout.txt`).
If you truly want a flat layout, that is
a project-structure choice to make at
`uv init` time and in the build
configuration — not something to fix by
moving files and hoping the packaging
follows.

## uv pip refuses: "No virtual environment found"

**Symptom.** `uv pip install something`
stops with:

```text
error: No virtual environment found; run `uv venv` to create an environment, or pass `--system` to install into a non-virtual environment
```

(transcript `uv-lab/transcripts/t14-pip-no-venv.txt`).

**Cause.** No environment is active and
none was named — and the pip interface
will not guess, and will not use the
system Python unasked (chapter 9).

**Fix.** Activate an environment
(`source .venv/bin/activate`), create one
with `uv venv`, or point at one with
`--python path/to/python`. Reach for
`--system` only on a machine built to be
thrown away, and know that you did.

## "The lockfile needs to be updated"

**Symptom.** `uv sync --locked` or
`uv lock --check` fails with:

```text
error: The lockfile at `uv.lock` needs to be updated, but `--check` was provided.
hint: To update the lockfile, run `uv lock`.
```

**Cause.** `pyproject.toml` changed —
usually a hand edit — and the lockfile
was not re-resolved afterwards, so the
two records disagree (chapter 10 staged
exactly this).

**Fix.** Run `uv lock`, review what it
reports adding or removing, and commit
both files together. If the edit was not
yours, that review *is* the security
check: the lock diff shows precisely what
new code the project would run.

## The tool that "isn't installed"

**Symptom.** `uv tool install` reported
success — it even said `Installed 1
executable` — but the shell answers
`command not found`.

**Cause.** The tool's command went into
`~/.local/bin`, and that folder is not on
your `PATH`. uv warned you in the install
output itself (chapter 7 kept the
warning):

```text
warning: `/home/hatch/.local/bin` is not on your PATH. To use installed tools, run `export PATH="/home/hatch/.local/bin:$PATH"` or `uv tool update-shell`.
```

**Fix.** Run `uv tool update-shell`, or
add the folder to your shell's startup
file yourself, then open a fresh terminal.
Check with `uv tool list` that the tool
is present, and `which <tool>` that the
shell now finds it.

## A Python appeared — or the wrong one was used

**Symptom.** `uv run` prints `Using
CPython 3.11.16`, a version you never
installed; or a project runs under 3.13
when you expected 3.11.

**Cause.** Chapter 8's machinery working
as designed. `.python-version` asked for
a version no system Python matched, so uv
fetched one into its own directory; or
the pin and `requires-python` say
different things from what you
remembered, and the files won.

**Check.** `cat .python-version` and the
`requires-python` line in
`pyproject.toml` are the two inputs; `uv
python list` shows every candidate with
its address, and `uv python find 3.11`
shows which interpreter a request
resolves to. Nine times out of ten the
files are right and the memory is stale
— which is the argument for recording the
choice in files at all.

## The first run is slow, the second is instant

**Symptom.** A command takes seconds —
once. The identical command later takes
milliseconds.

**Cause.** Not a fault: the first run
paid for downloads and resolution, and
the cache (chapter 2) has been paying
you back since. The lab's transcripts
show both ends of this (`Resolved 5
packages in 6.36s` on first meeting,
`Resolved 5 packages in 1ms` thereafter).

**Check.** If *every* run is slow, the
cache is not being reused — a different
user account, a container discarding the
home directory, or an environment
variable pointing the cache elsewhere.
`uv cache dir` prints where uv thinks its
cache lives; start there.

## It works in the project, fails outside it

**Symptom.** A script imports a package
happily under `uv run` in its project and
fails with `ModuleNotFoundError` when run
any other way.

**Cause.** The package lives in the
project's `.venv`, which only `uv run`
(or an activated shell) puts in play.
Outside the project there is no pile of
packages any more — that is the design,
not a defect.

**Fix.** Give the script its own
declaration (chapter 6's PEP 723 block)
and keep using `uv run script.py` — or
accept the script as a project member and
run it from home. What not to do is
recreate the old global pile to make the
error stop; the error is the honest
statement that the script's needs were
never written down.
