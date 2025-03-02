# Contributing

First of all, thank you for your desire to contribute!

<!-- textlint-disable -->

There may be a [TODO.txt](TODO.txt) file which may be a nice place to start.

<!-- textlint-enable -->

We also have a [Code of Conduct](CODE_OF_CONDUCT.md) that is worth reading!

If you want to find an area that currently needs improving, have a look at the
[open issues](https://github.com/jhatler/jhatler/issues) for this repository.

## Reporting Bugs

If you've found a bug thanks for letting us know!
It is a good idea to describe in detail how to reproduce
the bug (when you know how), what environment the bug appeared and so on.
Please tell us at least the following things:

- What's the release were you using? Please include that in your report.
- What commands did you execute to get to where the bug occurred?
- What did you expect?
- What happened instead?
- Do you know how to reproduce the bug?

As more information you provide, the earlier we'll correct it!.

## Development Environment

A [devcontainer](containers.dev) environment is maintained for this
repository and can be used via GitHub Codespaces.

## Providing Patches

Please provide the patches for each bug or feature in a separate branch and
open up a pull request for each.

Every time you create a pull request, we'll run different tests. We won't
merge any code that doesn't pass the tests. If you need help to make the test
pass don't hesitate to call for help! Having a PR with failing tests is nothing
to be ashamed of; on the other hand, that happens regularly for all of us.

## Git Commits

Ensuring that every contributor follows the same style conventions when creating
Git commits makes makes reviewing code, browsing the history and triaging bugs
much easier.

Generally, Git commit messages have a very terse summary in the first line of the
commit message, followed by an empty line, followed by a more verbose description
or a list of changed things. For examples, please refer to the excellent [How to
Write a Git Commit Message](https://chris.beams.io/posts/git-commit/).

If you change/add multiple different things that aren't related at all, try to
make several smaller commits. This is much easier to review. Using `git add -p`
allows staging and committing only some changes.

Specifically, **ALL** commits to this repository are expected to follow the
1.0.0 [Conventional Commits](https://www.conventionalcommits.org/) specification.

The supported commit types are:

- Features: "feat", "feature"
- Bugfixes: "fix"
- Performance Improvements: "perf"
- Reverts: "revert"
- Documentation: "docs"
- Styles: "style"
- Miscellaneous Chores: "chore"
- Code Refactoring: "refactor"
- Tests: "test"
- Build tool: "build"
- Continuous Integration: "ci"

### Commit Message Bodies

An empty commit message body is not permitted under any cases.

This part of the commit should explain what your change does, and why it's needed.
Be specific.
A body that says "Fixes stuff" will be rejected.
Be sure to include the following as relevant:

- what the change does,
- why you chose that approach,
- what assumptions were made, and
- how you know it works -- for example, which tests you ran.

Each line in your commit message must be 72 characters or less.
Use newlines to wrap longer lines.
Exceptions include lines with long URLs, email addresses, etc.

### References

If the change is in reference to a GitHub issue or some other
commit please include a line of the form:

```text
Refs: [issue]
```

Where [issue] is the relevant issue identifier. Example:

**GitHub Issue:**

```text
Fixes: #1234
Signed-off-by: ...
```

### Identifying Contribution Origin

When adding a new file to the tree, it is important to detail the source
of origin on the file, provide attributions, and detail the intended usage.
In cases where the file is an original, the commit message should include
the following ("Original" is the assumption if no Origin tag is present):

```text
Origin: Original
```

In cases where the file is imported from an external project, the commit
message **SHALL** contain details regarding the original project, the
location of the project, the SHA-id of the origin commit for the file
and the intended purpose.

For example, a copy of a locally maintained import:

```text
Origin: Contiki OS
License: BSD 3-Clause
URL: http://www.contiki-os.org/
commit: 853207acfdc6549b10eb3e44504b1a75ae1ad63a
Purpose: Introduction of networking stack.
```

For example, a copy of an externally maintained import in a module repository:

```text
Origin: Tiny Crypt
License: BSD 3-Clause
URL: https://github.com/01org/tinycrypt
commit: 08ded7f21529c39e5133688ffb93a9d0c94e5c6e
Purpose: Introduction of TinyCrypt
```

## Code Review

We encourage actively reviewing the code so it's common practice
to receive comments on provided patches.

If you are reviewing other contributor's code please consider the following
when reviewing:

- Be nice. Please make the review comment as constructive as possible so all
  participants will learn something from your review.

As a contributor you might be asked to rewrite portions of your code to make it
fit better into the upstream sources.
