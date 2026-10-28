# The Neighbours

uv did not arrive in an empty field. Each
tool below does a job uv now also does,
and each is characterised here honestly —
what it is, what it still does well, and
when to reach for it instead. These are
characterisations from the tools'
documentation and long public record, not
benchmarks run by this guide's lab.

**pip** is the original installer, the
one bundled with Python itself, and the
reason `uv pip` exists as a face: a vast
world of instructions, Dockerfiles and
habits speaks pip. pip remains the
reference implementation — when uv and
pip disagree about an edge case, pip's
behaviour is the one the ecosystem was
built against — and it is maintained,
capable and much faster than its
reputation. uv's pip interface wins on
speed and on refusing to touch a system
Python; it does not make pip wrong.

**venv and virtualenv** make
environments, nothing more. `venv` is in
the standard library, which makes it the
one tool guaranteed present on any Python
machine — chapter 9 used it for exactly
that reason. virtualenv predates it and
is faster and richer. Neither resolves or
installs; they are the empty room, where
uv is the room, the furniture and the
inventory.

**pyenv** manages interpreters by
compiling them and shimming the `python`
command, and it works beyond uv's reach:
it serves *every* Python tool on the
machine, not just uv-driven ones, and its
plug-ins and shell integration are a
decade deep. If your whole working life,
in every shell, must bend around chosen
Pythons, pyenv is the system-level
answer. If the need is per-project, uv's
fetch-and-pin (chapter 8) is the smaller
machine.

**pip-tools** invented the workflow
`uv pip compile` continues: a loose
`.in` file for humans, a pinned
requirements file for machines, `# via`
comments and all. It still works exactly
as documented, and a team whose pipeline
is built on it loses nothing but time —
seconds per compile — by staying. uv
keeps the format and removes the wait.

**Poetry and PDM** are project managers
in uv's own category: declaration,
lockfile, environments, building,
publishing. Poetry has a large ecosystem
of plug-ins and a long head start in
corporate adoption; PDM is a close
contemporary with its own standards-first
design. A happy Poetry or PDM project has
no emergency to solve. uv's case is
consolidation and speed: the same loop,
plus interpreters and tools, in one
binary that starts instantly.

**Hatch** is a project manager with an
emphasis on environment *matrices* —
testing across many Python versions and
configurations from one declaration —
which remains its distinctive strength
and a thing uv does not attempt. Its
build backend, Hatchling, is also widely
used inside other people's projects,
including ones uv happily builds and
installs.

**conda** is the neighbour that is not
really in the same street. It manages
binary and system-level dependencies —
the compiled libraries for science and
geospatial stacks — across languages, and
creates whole software *prefixes*, not
just Python environments. Where a package
needs a specific system library, conda is
often the only civilised answer; uv
deliberately does not compete there
(chapter 13 names this as a limit, not an
oversight).

**pipx** did for tools what `uvx` and
`uv tool` now do inside uv: one isolated
environment per command-line program,
commands on the path. It remains a fine,
focused tool, and on a machine already
arranged around it there is little to
gain by moving. uv's advantage is only
that the tool bench and the projects now
share one cache, one resolver, and one
thing to update.
