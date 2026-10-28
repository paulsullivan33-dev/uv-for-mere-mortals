# Tools and uvx

Some Python programs are not libraries for
your projects but instruments for your
workbench: a linter, a formatter, a
converter, a notebook server. Installing
such a tool the old way meant either
pouring it into the system Python (where
its dependencies could fight with
something else's) or keeping a dedicated
environment for it by hand — the job
**pipx** was invented to do. uv folds the
whole idea in, in two strengths: run a
tool once, right now, with `uvx`; or
install it properly, with `uv tool`, when
you reach for it every week.

## Run it once: `uvx`

`uvx` is a separate command (it arrived
in the same download as `uv`, chapter 3),
and it is short for "uv execute". Give it
a tool's name and its arguments:

(transcript `uv-lab/transcripts/t07-uvx-and-tools.txt`):

```text
$ uvx cowsay -t "uv ran me without installing me"
Installed 1 package in 6ms
  _______________________________
| uv ran me without installing me |
  ===============================
...
```

Behind that one line, uv resolved the
`cowsay` package, built it a private
environment from the cache, ran its
command, and kept the environment cached
for next time. Nothing was installed into
any project or any Python you own; the
tool's dependencies met nothing. A second
`uvx cowsay` starts at once, out of the
cache. Versions can be pinned when it
matters — `uvx cowsay@6.1`, or
`uvx --from cowsay==6.1 cowsay` when the
package and the command have different
names (the pinning forms are documented;
the lab ran the plain form).

This is the chapter to have read before
someone on the internet says "just run
this". What `uvx` asks of you is exactly
chapter 1's rule: the tool is code, from
the index, running with your permissions.
For a known tool from its real project —
a linter, a formatter, the cowsay — that
is an easy yes. For a name you met thirty
seconds ago in a comment thread, `uvx`
has made it *easy* to run, not *wise*;
the ease is not the endorsement.

## Keep it: `uv tool install`

A tool you use weekly deserves a fixed
place. `uv tool install` gives it one —
its own permanent environment under the
tools directory of chapter 2, and its
command linked into `~/.local/bin`:

```text
$ uv tool install cowsay
Resolved 1 package in 1ms
Installed 1 package in 2ms
 + cowsay==6.1
Installed 1 executable: cowsay
warning: `/home/hatch/.local/bin` is not on your PATH. To use installed tools, run `export PATH="/home/hatch/.local/bin:$PATH"` or `uv tool update-shell`.
```

The lab has left the warning in the
transcript on purpose: it is the single
most common uv beginner moment. The tool
*is* installed; your shell simply does
not look in the folder where its command
lives. Either add `~/.local/bin` to your
path the way your shell prefers, or let
`uv tool update-shell` do it for you.
Chapter 14 meets the same warning from
the troubleshooting side. With the folder
on the path, the installed tool runs like
any command:

```text
$ uv tool list
cowsay v6.1
- cowsay
```

`uv tool list` is the inventory — worth
running on a machine you have not touched
in a while, because tools installed this
way are deliberately invisible to
everything else. Each can be upgraded
(`uv tool upgrade cowsay`, or
`--all`) or removed as cleanly as it
came:

```text
$ uv tool uninstall cowsay
Uninstalled 1 executable: cowsay

$ uv tool list
No tools installed
```

(Upgrade is documented; install, list and
uninstall are in transcript t07.)

## Which strength, when

Reach for `uvx` when the tool is
occasional, when you are following a
guide that names a tool once, or when you
want a specific version for a single job.
Reach for `uv tool install` when the tool
is part of your bench — when you type its
name without thinking. The two are not
rivals: most tools start as a `uvx`,
graduate to an install, and the cost of
either mistake is one command to undo.
What neither should ever be is an install
into a *project's* environment: a linter
your project does not import does not
belong in its dependency list (chapter 5's
dev group is for tools the project's own
development needs, which is a different,
deliberate thing).
