# Adding Packages

A project with no dependencies is a
scaffold. This chapter gives tally a real
job — counting the words in a text file —
first with the standard library alone,
then with a library added the uv way:
`uv add`. You will see the declaration
change, the lockfile grow, and the
program get shorter to write and nicer
to read. You will also meet `uv remove`,
development-only dependencies, and the
`uv tree` view of what you have taken on.

## First, a program worth feeding

The lab replaced the greeting in
`src/tally/__init__.py` with a small word
counter (the file ships in
`uv-lab/tally/`): it reads a text file,
counts its words, and prints the ten most
common. Against a short invented sample
(`sample.txt`, a paragraph about a harbour
town waking up), plain `uv run` gives
(transcript `uv-lab/transcripts/t04-tally-runs.txt`):

```text
$ uv run tally sample.txt
58 words, 39 different
         the  15
          of  3
     harbour  2
```

It works. It is also, plainly, a table
trying to escape from a `print`
statement. The **rich** library draws
tables (and much else) properly, and
tally does not have it. Under the old
pile of tools, adding it would mean
activating the environment by hand, a pip
install, and then remembering to write
the dependency down somewhere before you
forgot. Here it is one command, run from
the project's folder:

## `uv add`

(transcript `uv-lab/transcripts/t05-add-rich.txt`):

```text
$ uv add rich
Resolved 5 packages in 6.36s
   Building tally @ file:///home/.../tally
      Built tally @ file:///home/.../tally
Downloading pygments (1.2MiB)
 Downloaded pygments
Prepared 5 packages in 2.82s
Uninstalled 1 package in 0.64ms
Installed 5 packages in 29ms
 + markdown-it-py==4.2.0
 + mdurl==0.1.2
 + pygments==2.21.0
 + rich==15.0.0
 ~ tally==0.1.0 (from file:///home/.../tally)
```

Read what happened, in order. uv
**resolved** the request — not just rich,
but everything rich itself needs
(`markdown-it-py`, `pygments`, and
`mdurl` beneath them) — five packages
that can coexist, at exact versions. It
downloaded what was not already cached
(one package, pygments), rebuilt tally
itself (its dependency list changed, so
the installed copy is replaced — the
`~`), and installed the set into `.venv`.
And it wrote both records: the
declaration now reads

```toml
dependencies = [
    "rich>=15.0.0",
]
```

and `uv.lock` holds the five exact
versions with their hashes. The command
is the whole workflow: no environment to
activate first, no requirements file to
keep in step by hand, no written note to
yourself. Chapter 1's rule applies on the
way in — `rich` is a long-established,
widely used library, which is the sort of
accounting the rule asks for — and the
lockfile now *says* what the project
runs, which is the other half of it.

With the program rewritten to build a
rich table, the same command produces
(transcript `uv-lab/transcripts/t06-rich-and-resync.txt`):

```text
$ uv run tally sample.txt
     58 words, 39 different
┏━━━━━━━━━┳━━━━━━━┓
┃ Word    ┃ Count ┃
┡━━━━━━━━━╇━━━━━━━┩
│ the     │    15 │
│ of      │     3 │
│ harbour │     2 │
...
```

Note that nothing about installing was
repeated: `uv run` noticed the code, not
the dependency list, had changed, and
simply ran.

## Seeing the shape of it: `uv tree`

Every dependency you add brings its own
dependencies, and honesty about that pile
is one command away:

```text
$ uv tree
tally v0.1.0
└── rich v15.0.0
    ├── markdown-it-py v4.2.0
    │   └── mdurl v0.1.2
    └── pygments v2.21.0
```

Run it whenever a project's requirements
surprise you. The tree is the resolution
drawn as a picture, and it is drawn from
the lockfile, so it never describes a
wish — only what will actually install.

## Taking something out: `uv remove`

`uv remove cowsay` (the lab added and
then removed a package in a scratch copy
of the project; transcript
`uv-lab/transcripts/t16-remove-and-dev.txt`)
reverses `uv add` completely: the line
leaves `pyproject.toml`, the lockfile is
re-resolved without it, and the
environment is rebuilt to match. Removal
is not an edit you make by hand in two
files and hope; it is the same single
motion as adding, backwards.

## Dependencies that are not for shipping

Tests, linters and other workshop tools
are dependencies of *developing* the
project, not of *running* it, and uv
keeps them in a separate list. The lab
added the pytest test runner that way
(transcript t16 again):

```text
$ uv add --dev pytest
Resolved 10 packages in 3.03s
...
 + pytest==9.2.0
```

In `pyproject.toml` the addition lands
not under `dependencies` but under a
`[dependency-groups]` table named `dev`,
and `uv tree` marks it:

```text
└── pytest v9.2.0 (group: dev)
```

The distinction matters when the project
is built into a package (chapter 11): the
shipped artifact carries its real
dependencies with it, and leaves the
workshop behind. `uv sync` installs the
dev group by default, so your own machine
gets the full bench; chapter 10 shows the
flag that leaves it out.
