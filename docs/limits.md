# Limits

What uv cannot do, and what it must not
be asked to do — the chapter the rest of
the guide has been promising.

## It manages Python packages, not the machine

uv's world ends at the Python border. A
package that wraps a system library — an
XML toolkit, a database driver, a
geospatial engine — still needs that
library, of a workable version, from your
operating system, and uv neither provides
it nor checks for it in any deep way.
The failure, when it comes, arrives as a
build error or a missing-library message
from inside the package, wearing a
disguise. This is conda's home ground
(chapter 12), and also the distro package
manager's. Knowing the border exists is
most of the defence: when an install
fails in a way that mentions compilers,
headers or `.so` files, you have found
the edge of uv's country.

Relatedly, a few packages build native
code at install time. uv will hand them a
compiler's worth of work to do, but the
compiler is yours to have. "uv installed
it fine on the other machine" and "it
needs a C toolchain here" are both true
more often than anyone likes.

## Installing is executing, and nothing inspects the cargo

Chapter 1's rule gets its full statement
here. A package install can run code —
build scripts today, the library itself
the first time your program imports it —
and uv performs no inspection of what it
fetches beyond the lockfile's hashes,
which prove a file is the file the index
served, not that the file is *good*.
PyPI is a public index: names are claimed
first-come, lookalike names are a known
attack, and even honest packages are
only as trustworthy as their maintainers'
own account security. uv's speed is
neutral in this: it will fetch a bad
package in the same thirty milliseconds
as a good one. The defences are the
boring ones the rule prescribes — known
packages, names checked letter by letter,
a lockfile you can review, and suspicion
of anything whose installation
instructions hurry you.

## A lockfile reproduces packages, not a world

Chapter 10's promise has fine print.
`uv sync` on another machine reproduces
the locked *packages* exactly. It does
not reproduce the operating system, the
CPU architecture, the system libraries of
the section above, or the Python *build*
beyond its version. A project locked on
one platform can resolve to different
wheels on another — uv locks are
deliberately cross-platform, recording
the alternatives — but a package with no
wheel for the new platform falls back to
building from source, with the toolchain
caveat attached. And some differences no
tool can lock away: environment
variables, data files, the service the
program talks to. The lockfile is the
whole truth about dependencies. It is
not the whole truth about running
software.

## It will not choose for you

When requirements conflict — this package
needs that library below version 2, that
one needs it at 2 or above — uv's
resolver refuses and explains, sometimes
at a length that reads like a proof,
because it is one. That refusal is the
tool working. What uv cannot do is
decide which requirement should bend:
upgrade the first package, pin the
second, drop the third? Those are
judgements about *your* project's future,
and they stay yours. Beware anyone's
advice to delete the lockfile and "let
it re-resolve" as a first resort: the
lock is the record of a decision that
once worked, and chapter 14 treats the
error messages as reading matter, not
noise.

## The edges the lab did not walk

Three honest borders of this guide
itself, matching `criteria.md`'s ledger.
**Workspaces** — several packages in one
repository sharing a lockfile — exist and
are a real part of uv; the lab's project
was one small package, and multi-package
behaviour is described here from the
documentation only. **Publishing** is a
command away and a world of its own —
names, accounts, tokens, and the
responsibility of shipping code others
will run; chapter 11 builds the artifacts
and deliberately stops there.
**Private indexes** and their
authentication, which working teams need
and a one-person lab cannot honestly
demonstrate, are likewise documented
territory. A guide that pretends to have
run what it has only read is worse than
one that labels the difference; the
labels are in the criteria, and they
apply to this chapter too.

## Speed is not a virtue by itself

The last limit is a temptation. uv makes
operations cheap that used to be
expensive: re-resolving from scratch,
trying a dependency on a whim, rebuilding
an environment because it feels untidy.
Cheap is good. But a dependency added in
a careless minute is a dependency you
maintain for years, and an environment
rebuilt to fix a problem you did not
diagnose teaches the problem to hide.
The old pile's friction was never a
feature — and the discipline it forced
was never supplied by the friction. uv
removes the wait. The judgement, as ever,
is shipped separately, by you.
