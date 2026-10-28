# Glossary

**Build backend** — the machinery that
turns a project's source into a package;
`uv_build` is uv's own, named in
`pyproject.toml`'s `[build-system]`
(chapters 4 and 11).

**Cache** — uv's store of downloaded
packages and metadata, reused across
projects so repeat work is nearly free;
its address comes from `uv cache dir`
(chapter 2).

**Dependency** — a package your project
needs in order to run (or, in the dev
group, to be developed); declared as a
range in `pyproject.toml` (chapter 5).

**Dependency group** — a named bundle of
dependencies kept apart from the runtime
list; `dev` is the group `uv add --dev`
writes (chapter 5).

**Environment** — see *virtual
environment*.

**Freeze** — `uv pip freeze`: print an
environment's exact installed versions
in `name==version` form (chapter 9).

**Index** — a repository of packages uv
resolves and downloads from; PyPI is the
default and the public one (chapter 1).

**Inline script metadata** — the PEP 723
declaration block at the top of a single
file, naming its Python and its
dependencies (chapter 6).

**Lockfile** — `uv.lock`: uv's generated
record of one exact version — and the
hash of every file — per package
(chapter 10).

**Managed Python** — an interpreter uv
downloaded into its own Python directory
and maintains, as opposed to one it
borrows from the system (chapter 8).

**PEP 723** — the Python standard that
defines inline script metadata
(chapter 6).

**pip interface** — the `uv pip` family:
pip-style commands against an ordinary
virtual environment, with no project and
no lockfile (chapter 9).

**Project** — a folder whose
`pyproject.toml` declares a name, a
Python range and dependencies; the unit
uv's main commands serve (chapter 2).

**pyproject.toml** — the standard file
that declares a project; the half of the
record a human writes (chapters 2
and 4).

**.python-version** — a one-line file
naming the interpreter a folder asks for;
a choice, where `requires-python` is a
boundary (chapter 8).

**requires-python** — the range of Python
versions a project supports, declared in
`pyproject.toml` and honoured by the
resolver (chapters 4 and 8).

**Resolution** — the act of turning
declared ranges into one exact, mutually
compatible set of versions; the result
lives in the lockfile (chapters 2
and 10).

**Resolver** — the part of uv that
performs a resolution, and that refuses,
with its working shown, when no set can
satisfy every requirement (chapter 13).

**Script command** — a command a project
provides via `[project.scripts]`, such as
`tally` itself (chapter 4).

**Source distribution (sdist)** — a
package in source form, an archive a
machine must build before installing
(chapter 11).

**Src layout** — the arrangement where a
package's code lives under `src/`, apart
from the project's other files
(chapter 4).

**Sync** — `uv sync`: making an
environment match the lockfile exactly,
installing and removing as needed
(chapter 10).

**Tool** — in uv's vocabulary, a program
distributed as a Python package that you
run rather than import; served by `uvx`
and `uv tool` (chapter 7).

**uvx** — the companion command that runs
a tool once, in a cached throwaway
environment, installing nothing
(chapter 7).

**Virtual environment** — a private
folder (conventionally `.venv`) holding
a Python link and one project's
installed packages, so projects cannot
disturb each other (chapters 1 and 2).

**Wheel** — a package in ready-to-install
form: unzip it into place and it runs;
the format indexes mostly serve
(chapter 11).
