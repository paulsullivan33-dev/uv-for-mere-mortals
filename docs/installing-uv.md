# Installing uv

uv is not itself a Python package you
must install with Python — that would be
a chicken asking the egg for a lift. It
is a single self-contained **binary**
(two, counting `uvx`, its twin for
chapter 7), written in Rust, with no
dependencies of its own. Every install
route is a way of putting those two
binaries on your machine: the project's
installer script, a direct download of
the release archive, or a package manager
you already trust.

## The route the lab took

The lab downloaded the release archive
for its platform straight from the
project's GitHub releases
(`github.com/astral-sh/uv/releases`), and
unpacked it in a scratch folder:

```bash
curl -LsSf -o uv.tar.gz \
  https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz
tar xzf uv.tar.gz
ls uv-x86_64-unknown-linux-gnu/
```

Inside the archive's folder are exactly
two files: `uv` and `uvx`. Nothing is
installed anywhere else; the folder can
be moved onto your path (the lab simply
added it to `PATH`), or the two binaries
copied to a folder already there, such as
`~/.local/bin`. The version check is the
whole acceptance test (transcript
`uv-lab/transcripts/t00-version-and-dirs.txt`):

```text
$ uv --version
uv 0.13.6 (x86_64-unknown-linux-gnu)
$ uvx --version
uvx 0.13.6 (x86_64-unknown-linux-gnu)
```

Check: both commands answer with the same
version. This guide's transcripts are all
from **0.13.6**; uv releases often, and
the version matters when you read other
people's advice, because options and even
whole commands still move between
releases.

## The other routes (documented)

The project's documentation offers, and
this guide lists without having run:

- **The installer script.** On Linux and
  macOS, `curl -LsSf https://astral.sh/uv/install.sh | sh`;
  on Windows, the equivalent PowerShell
  one-liner from the same site. The script
  performs the same download as the lab's
  route, places the binaries in
  `~/.local/bin`, and offers to add that
  folder to your path. Read any script
  before piping it into a shell — this
  guide's rule applies to uv's own
  installer too — or use the manual route
  above, which is the same journey taken
  in the open.
- **Package managers.** Homebrew, winget,
  Scoop, Cargo, and the repositories of
  several Linux distributions carry uv.
  These have the advantage of updating
  with the rest of your system, and the
  disadvantage of sometimes lagging the
  project's own releases.
- **pip and pipx.** `pip install uv`
  works — the binary is shipped inside a
  Python package as a delivery mechanism —
  and is a reasonable route on a machine
  where Python already runs your tools.
  It is not how uv is meant to be
  *used*, only another door into the
  same two binaries.

Whichever route you take, end with
`uv --version` and keep the number; the
rest of this guide assumes the two
commands answer.

## Keeping uv up to date

Installer-script and archive installs can
update themselves with `uv self update`,
which fetches the latest release and
replaces the binaries in place
(documented; the lab pinned its version
for reproducibility instead — a guide's
transcripts should not change under it
mid-writing). Package-manager installs
update with the manager, and `uv self
update` steps aside for them. Because uv
moves quickly, updating occasionally is
worth it; because it moves quickly, a
project's lockfile (chapter 10) is what
protects your work from a uv upgrade
changing its mind about versions — the
lockfile, once written, is honoured as
written.

## Removing uv

There is no uninstaller, because there is
nothing tangled to undo. Delete the two
binaries, and — if you want the whole
world gone — the directories of chapter 2:
the cache (`uv cache dir`), the downloaded
interpreters (`uv python dir`) and the
installed tools (`uv tool dir`). Project
`.venv` folders belong to their projects
and go when the projects go. Your system
Python was never modified and does not
notice any of this.
