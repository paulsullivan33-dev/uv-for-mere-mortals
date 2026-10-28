# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's projects are small programs written for the
   purpose, and its packages are the public ones it names.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: it manages Python packages, not the system
   libraries some packages need; installing is executing, and
   no part of it inspects a package for malice; a lockfile
   reproduces versions, not the machine around them; a
   conflict between requirements ends in a decision only the
   reader can make; and speed supplies no judgement about what
   is worth depending on.
8. **The safety rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *installing a package runs
   its code: add only dependencies you would run sight unseen,
   and let the lockfile, not a machine's memory, say what the
   project needs* — before any procedure depends on it, and
   later chapters point back to it where a one-line install
   would make forgetting it easy.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu sandbox (system
Python 3.12.3). uv **0.13.6** was verified as the project's
official standalone binary: the release archive was downloaded
from astral-sh/uv's GitHub releases into a scratch folder,
unpacked there, and run from there — nothing was installed
system-wide, and no package was installed into any Python the
build machine itself depends on. All installs were resolved
against the real Python Package Index. All transcripts live
in `uv-lab/transcripts/`; the lab's project is `uv-lab/tally/`
and its script is `uv-lab/greet.py`.

Run for real, with transcripts as evidence:

- Version checks for `uv` and `uvx`, and the three directory
  answers (`uv cache dir`, `uv python dir`, `uv tool dir`)
  that chapter 2 maps (t00).
- `uv init tally`, the full tour of the files it writes —
  including the kept failure of `cat main.py`, which is how
  the src layout announces itself — and the first
  `uv run tally`, with the environment created, the project
  built and installed, and `uv.lock` appearing (t01, t02,
  t02b, t03).
- The lab's word-count program run with the standard library
  alone (t04); then `uv add rich` against the live index,
  the resulting `pyproject.toml`, and `uv tree` (t05); the
  rewritten program's table output, the project's `.venv`
  deleted outright, and `uv sync` rebuilding the exact
  environment from the lockfile (t06).
- `uv remove` and `uv add --dev pytest` in a scratch copy of
  the project, with the dependency-groups table and the
  group-marked tree (t16). `uv run --with emoji`, borrowing
  a package for one command while `pyproject.toml` provably
  stays unchanged (t17).
- `uvx cowsay` run without installing; `uv tool install
  cowsay` including its not-on-PATH warning verbatim; the
  installed command run from `~/.local/bin`; `uv tool list`
  and `uv tool uninstall` (t07).
- A PEP 723 script (`greet.py`) declaring its own dependency,
  run twice: the first run installs into its cached private
  environment, the second runs silently from it (t08).
- `uv python list` showing system, managed and downloadable
  interpreters (t09); `uv python install 3.13` downloading
  the real 33.8 MiB interpreter; `uv python find`, `uv python
  pin`, and `uv init --python 3.13` producing a project that
  runs under the fetched interpreter (t10). The guide's
  first-run transcript (t03) is also the record of an
  interpreter — CPython 3.11.16 — being fetched unasked
  because `.python-version` requested 3.11.
- The pip interface against a throwaway environment made by
  `python3 -m venv`: `uv pip install`, `uv pip list`,
  `uv pip freeze`, and the installed command run from the
  environment's own `bin` (t11); `uv venv` creating an
  environment itself (t18); `uv pip compile` turning a
  one-line `requirements.in` into a fully pinned,
  `# via`-annotated `requirements.txt` (t12); and the pip
  interface's refusal, exit code 2, when no environment
  exists (t14).
- The lockfile discipline end to end: `uv lock --check`
  passing, a hand edit to `pyproject.toml` making it fail
  with exit code 1, `uv sync --locked` refusing on the same
  stale lock with exit code 1, `uv lock` repairing it, and
  the check passing again (t13).
- `uv build` producing both a source distribution and a
  wheel of the lab's project (t15).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The installer-script route (`astral.sh/uv/install.sh` and
  its Windows counterpart), package-manager installs
  (Homebrew, winget, distro packages), the pip/pipx route,
  `uv self update`, and everything Windows- or macOS-specific.
  The lab's archive route is the same binaries, unpacked by
  hand so the transcripts show the whole journey.
- `uv tool upgrade`, `uv python uninstall`, `uv add --script`,
  `uv sync --no-dev`, the `--frozen` flag, the `--system`
  flag (deliberately unused anywhere in this guide), and
  `uvx`'s version-pinning forms.
- Publishing (`uv publish`): chapter 11 builds the artifacts
  and stops before the upload, which needs an account and a
  token the lab does not have and should not invent.
- Workspaces (multi-package projects sharing one lockfile),
  private and alternative package indexes and their
  authentication: real features, described from the
  documentation, outside what a one-project lab can honestly
  demonstrate.
- The comparison tools in chapter 12 are characterised, not
  benchmarked.

Fixtures are this guide's own and deliberately generic: a
twenty-line word counter over an invented paragraph about a
harbour town, a one-function greeting script, and four small,
well-known public packages (`rich`, `cowsay`, `pytest`,
`emoji`) plus the dependencies they themselves pulled in,
each named where it appears. No example is modelled on any
real person, network, service or organisation.
