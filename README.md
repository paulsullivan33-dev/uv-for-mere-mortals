# uv for Mere Mortals

Python has never lacked tools for
installing packages. It has lacked one
tool that does the whole job. For years
the ordinary setup was a pile of them:
**pip** to install, a **virtual
environment** made by hand for each
project, **pyenv** or the operating system
to supply the Python itself, and
**pip-tools** to pin down exact versions —
plus the notes you kept for yourself about
which combination you had used where.
**uv** is one program, written by the
Astral team, that takes over all of those
jobs at once: projects, packages,
interpreters, and standalone tools, fast
enough that the waiting simply leaves the
workflow.

This guide explains how uv thinks about a
project, how to start one and add
packages to it, how to run code — project
commands, single scripts that carry their
own dependencies, and tools you never
install — and how the **lockfile** lets
another machine, or your own machine next
month, rebuild exactly the environment
you have today. It also covers the **pip
interface**, uv's drop-in replacement for
existing pip workflows, and states the
limits plainly, including the one that
matters most: speed is not safety.

The rule that governs everything here is
stated in chapter 1 and repeated where it
bites: **installing a package runs its
code — add only dependencies you would
run sight unseen, and let the lockfile,
not a machine's memory, say what the
project needs.** Everything in the lab
obeyed it: a handful of small, well-known
packages, each named in the text, and
nothing installed that the guide does
not show you.

The lab behind this guide ran the real
thing: **uv 0.13.6**, the standalone
binary from the project's own GitHub
releases, on a small Linux machine. Against
the real Python Package Index it started
a project, resolved and installed real
packages, deleted the project's
environment and rebuilt it from the
lockfile alone, ran a tool it had never
installed, ran a script that declares its
own dependencies, downloaded and
installed two full Python interpreters,
broke a lockfile on purpose and repaired
it, and built a distributable package.
Every transcript is kept in
`uv-lab/transcripts/`.

What the lab could not do, it did not
fake. It had one Linux machine, so the
Windows and macOS install routes are
taught from the project's documentation
and labelled as such. Publishing a
package to the index, multi-package
workspaces, and private package indexes
are likewise described, not demonstrated;
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What uv is**](what-uv-is.md) —
  the pile of tools uv replaces, the
  one-binary idea, and the rule about
  dependencies that the whole guide
  follows
- [**The moving parts**](the-moving-parts.md) —
  the four families of commands, the
  files that hold a project (pyproject,
  lockfile, environment), the cache, and
  where everything lives on disk
- [**Installing uv**](installing-uv.md) —
  the standalone routes, what the lab's
  download contained, the version check,
  and keeping uv up to date
- [**Your first project**](your-first-project.md) —
  `uv init`, a tour of the files it
  writes (including the code's surprising
  address), and the first `uv run`
- [**Adding packages**](adding-packages.md) —
  `uv add` and `uv remove`, what changes
  in pyproject and the lockfile, the
  dependency tree, and development-only
  dependencies
- [**Running code**](running-code.md) —
  project commands, `uv run` with a
  borrowed package, and single-file
  scripts that declare their own
  dependencies
- [**Tools and uvx**](tools-and-uvx.md) —
  running a tool without installing it,
  installing one properly, and the PATH
  warning that catches everyone once
- [**Managing Pythons**](managing-pythons.md) —
  listing, downloading and pinning Python
  versions, and the two files that ask
  for a Python: `.python-version` and
  `requires-python`
- [**The pip interface**](the-pip-interface.md) —
  `uv pip` against an ordinary virtual
  environment, and `uv pip compile`, the
  pip-tools successor
- [**Lockfiles and syncing**](lockfiles-and-syncing.md) —
  what the lockfile records, `uv sync`,
  the `--locked` check that refuses a
  stale lock, and breaking one on
  purpose
- [**Recipes**](recipes.md) — rebuild a
  project from a fresh clone, try a tool
  for one afternoon, send a script that
  installs its own dependencies, package
  a project to share
- [**The neighbours**](the-neighbours.md) —
  pip, venv, pyenv, pip-tools, Poetry,
  PDM, Hatch, conda and pipx: what each
  still does well, and when to reach for
  it instead
- [**Limits**](limits.md) — Python
  packages only, installing is executing,
  a lockfile is not a machine, and the
  choices uv cannot make for you
- [**Troubleshooting**](troubleshooting.md) —
  the missing main.py, the pip refusal,
  the stale lockfile, the tool that
  seems not to exist, and the Python
  that was quietly downloaded for you
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Publishing packages to PyPI — the guide
builds a package but does not upload one,
and the credentials and care that
publishing deserves are a subject of
their own. Multi-package **workspaces**
(monorepos) are described in chapter 2
and chapter 13 but the lab's project is
deliberately small and single. Private
and company package indexes, and the
authentication they need, are pointed at,
not taught. And uv's speed records are
not benchmarked here: the lab's timings
are quoted as they happened, on a small
machine, and chapter 12 explains why a
stopwatch is the least interesting
difference between these tools.

## How to use this guide

Read chapter 1 for the idea and the rule,
and chapter 2 before installing anything —
knowing which file holds what turns later
confusion into a named problem. Chapter 4
starts a project in the same sitting as
the install, and chapter 5 gives it a real
job, so do those two together. Chapter 7
is the one to read before you need it: the
first time someone says "just run this
tool," you will already know what `uvx`
does and what it asks of you. Chapter 10
is the chapter future-you cares about —
the lockfile discipline there is what makes
a project still work next year. The lab's
project is `uv-lab/tally/`, its script is
`uv-lab/greet.py`, its transcripts live in
`uv-lab/transcripts/`, and its notes are
`examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Python for Mere Mortals](https://paulsullivan33-dev.github.io/python-for-mere-mortals/)
- [Jupyter for Mere Mortals](https://paulsullivan33-dev.github.io/jupyter-for-mere-mortals/)
- [Hugging Face for Mere Mortals](https://paulsullivan33-dev.github.io/hugging-face-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/uv-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/uv-for-mere-mortals/blob/main/LICENSE-CODE).
