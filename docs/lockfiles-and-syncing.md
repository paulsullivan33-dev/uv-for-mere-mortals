# Lockfiles and Syncing

This is the chapter the rest of the guide
has been promising: the machinery that
makes "it works on my machine" into "it
is the same on every machine". It is
about one file — `uv.lock` — what it
records, how `uv sync` spends it, and how
to make the spending strict. It ends by
breaking a lockfile the way a tired human
breaks one, so you can watch the guard
rails do their work.

## What the lockfile records

Open `uv.lock` (the lab's copy ships at
`uv-lab/tally/uv.lock`) and you find, per
package, an exact statement of fact:

```toml
[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/...", hash = "sha256:bb413d29...", size = 8729 }
wheels = [
    { url = "https://files.pythonhosted.org/...", hash = "sha256:84008a41...", size = 9979 },
]
```

The version is one version, not a range.
The source is named. And every file uv
might fetch — the source distribution and
each wheel — is listed with its address
*and its sha256 hash*, so an install can
verify that what arrived is byte-for-byte
what the lock recorded. The declaration
in `pyproject.toml` said `rich>=15.0.0`;
the lockfile says what that turned out to
mean on the day it was resolved, in a
form no later change of mind on the index
can quietly alter.

You never edit `uv.lock` by hand. You
change the declaration — with `uv add`,
`uv remove`, or an edit to
`pyproject.toml` — and let uv re-resolve.
The lockfile is a generated artifact that
you *commit*, like a compiled program you
ship: source is yours, the artifact is
the machine's, both travel together.

## Spending it: `uv sync`

`uv sync` makes the current machine match
the lockfile: creates `.venv` if needed,
installs exactly the locked versions,
removes anything extra. Chapter 5's
climax was a sync in anger — the lab
deleted the entire environment and
rebuilt it from the lock alone
(transcript `uv-lab/transcripts/t06-rich-and-resync.txt`):

```text
$ rm -rf .venv

$ uv sync
Using CPython 3.11.16
Creating virtual environment at: .venv
Resolved 5 packages in 2ms
Installed 5 packages in 30ms
 + markdown-it-py==4.2.0
 + mdurl==0.1.2
 + pygments==2.21.0
 + rich==15.0.0
 + tally==0.1.0 (from file:///home/.../tally)
```

Thirty milliseconds, from nothing to the
exact environment, because the cache held
the downloads (chapter 2) and the lock
left nothing to decide. On a colleague's
machine the same command takes as long as
the downloads take, and produces the same
set. `uv run` performs a sync silently
whenever things have drifted; `uv sync`
is the same act performed on purpose, in
the open — the command a setup script, a
CI job, or a new team member's first hour
should use. By default it includes the
dev dependency group of chapter 5;
`uv sync --no-dev` builds the leaner,
ship-shape environment without it
(documented).

## Keeping it strict: `--locked` and `--check`

A lockfile protects you only if it is
*current* — if someone edited the
declaration and forgot to re-resolve,
the two files tell different stories.
uv's guard is a flag that turns sync and
run into auditors. The lab broke a copy
of the project the human way — edited
`pyproject.toml` by hand, adding `cowsay`
to the dependencies, and did not run
anything (transcript
`uv-lab/transcripts/t13-lockfile-checks.txt`):

```text
$ uv lock --check
Resolved 6 packages in 15ms
error: The lockfile at `uv.lock` needs to be updated, but `--check` was provided.

hint: To update the lockfile, run `uv lock`.
exit code: 1
```

and the same story from sync:

```text
$ uv sync --locked
Creating virtual environment at: .venv
Resolved 6 packages in 9ms
error: The lockfile at `uv.lock` needs to be updated, but `--locked` was provided.

hint: To update the lockfile, run `uv lock`.
exit code: 1
```

Nothing was installed, nothing drifted:
the command *refused*, with a non-zero
exit code a script or CI job can catch.
The repair is the named one —

```text
$ uv lock
Resolved 6 packages in 5ms
Added cowsay v6.1

$ uv lock --check
Resolved 6 packages in 2ms
```

— after which the check passes in
silence. (`--frozen` is the stricter
cousin: it uses the lockfile exactly as
found, without even checking it against
the declaration — documented here; the
lab's strict runs used `--locked`, whose
refusal is the lesson worth having.)

The working agreements this chapter
recommends are three, and they are the
whole discipline:

- **Commit `uv.lock`** with the code. A
  project whose lock is not in version
  control has a record that can be lost;
  that is the machine's-memory failure of
  chapter 1's rule, in a trench coat.
- **Change dependencies with `uv add` and
  `uv remove`**, which keep the two files
  in step as one motion — and when you do
  edit by hand, run `uv lock` in the same
  sitting.
- **Build and test with `uv sync --locked`**
  anywhere the result matters, so a stale
  lock fails the build loudly instead of
  passing silently on a drifted machine.
