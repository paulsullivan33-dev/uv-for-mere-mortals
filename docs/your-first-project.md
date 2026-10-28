# Your First Project

By the end of this chapter you will have
a project that runs — created, filled and
launched by three commands — and you will
know what each file in it is for. The
project is called **tally**. It will grow
into a small word-counting program in
chapter 5; for now it prints a greeting,
because the point of this chapter is the
scaffolding, not the program.

## Starting: `uv init`

```bash
uv init tally
```

(transcript `uv-lab/transcripts/t01-init.txt`):

```text
$ uv init tally
Initialized project `tally` at `/home/.../tally`

$ ls -la tally
drwxrwx--- 2 root root   98 .git
-rw-rw---- 1 root root  109 .gitignore
-rw-rw---- 1 root root    5 .python-version
-rw-rw---- 1 root root    0 README.md
-rw-rw---- 1 root root  274 pyproject.toml
drwxrwx--- 2 root root   10 src
```

uv has made the folder, started a git
repository in it (a `--no-vcs` option
exists if you do not want one), and
written a starter set of files. Note what
is not there yet: no environment, no
lockfile. Those arrive when the project
first *does* something.

## A tour of the files

The declaration, `pyproject.toml`
(transcript `uv-lab/transcripts/t02-init-files.txt`):

```toml
[project]
name = "tally"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[project.scripts]
tally = "tally:main"

[build-system]
requires = ["uv_build>=0.13.6,<0.14.0"]
build-backend = "uv_build"
```

Read it as three statements. The
`[project]` table is the declaration of
chapter 2: a name, a version, the range
of Pythons the project accepts
(`requires-python`), and an empty
dependency list — for now. `[project.scripts]`
names a **command** the project will
provide once installed: `tally`, which
runs the `main` function of the `tally`
package. And `[build-system]` names the
**build backend** — uv's own, `uv_build` —
the machinery that will package this code
when chapter 11 builds it. The
`description` line is a placeholder in
the project's own words; changing it is
your first safe edit.

`.python-version` contains one line,
`3.11`. It is a request, not a setting
carved in stone: "when this project needs
a Python, prefer 3.11." Why 3.11, when
chapter 2's `requires-python` also speaks
of 3.11? The first is the *choice*, the
second the *boundary* — any 3.11-or-newer
Python satisfies the project, and the pin
says which one uv reaches for first.
Chapter 8 pulls the two apart properly.

And the code itself? A first guess —
`cat main.py` — fails, and the lab kept
the failure in the transcript because
every reader will meet it:

```text
$ cat main.py
cat: main.py: No such file or directory
```

New projects use the **src layout**: the
package lives in a folder named `src`,
(transcript `uv-lab/transcripts/t02b-init-src-layout.txt`):

```text
$ find src -type f
src/tally/__init__.py

$ cat src/tally/__init__.py
def main() -> None:
    print("Hello from tally!")
```

The layout keeps importable code apart
from the project's other files, which
prevents a classic accident: a program
that works in its own folder only because
Python happened to find the code lying
next door, then fails when installed
anywhere else. The `main()` function is
the same `main` that `[project.scripts]`
points at.

## The first run

```bash
cd tally
uv run tally
```

(transcript `uv-lab/transcripts/t03-first-run.txt`):

```text
$ uv run tally
Using CPython 3.11.16
Creating virtual environment at: .venv
   Building tally @ file:///home/.../tally
      Built tally @ file:///home/.../tally
Installed 1 package in 2ms
Hello from tally!
```

Check: the final line is the program
running. Everything before it deserves
one look, because it is the whole
philosophy in five lines. uv needed a
Python 3.11; the machine's own Python was
3.12, so uv used a 3.11.16 it manages
itself (where that came from is chapter
8's story — the short version is that uv
fetches interpreters the way it fetches
packages). It created `.venv`, the
project's private environment. It *built*
the tally package and installed it into
that environment — the "1 package" is
tally itself. And quietly, in the folder,
a new file now exists: **`uv.lock`**, the
first resolution, recording that this
project, today, means exactly this set of
packages — a set of one.

From here on, `uv run` is quiet: the
environment exists, the lock is current,
so the command just runs. Run
`uv run tally` again and only the
greeting prints. That silence is the
sound of the declaration and the machine
being in agreement — chapter 10 shows
what uv says when they are not.
