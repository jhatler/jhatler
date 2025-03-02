# Copyright and license policy

Copyright (C) 2025 Jaremy Hatler

## Copyright

### Copyright statements

Copyright author must be included in:

- `LICENSE` file in the root of the repository.
- Headers of all source code files.

Each copyright holder must have their own copyright statement::

```text
Copyright (C) 2019 Some company
```

### Copyright holders

Each copyright holder **must** be a legal entity.

Copyright is tracked for non-trivial contributions (i.e. creative work). By
default anything above 15 lines is considered a non-trivial contribution.
An example for which copyright is not tracked is fixing a typo.

### Maintainer responsibility

Maintainers are responsible for asking each contributor who is the copyright
holder of a given contribution (often, it's the employer who holds the
copyright).

### Attribution

Attribution is not tracked via copyright, but via the `AUTHORS` file.

## License

All released source code should by default be licensed under the
MIT License. Exceptions will be made to this on a case-by-case basis.

### Tracking Licenses

Make sure to include the following SPDX identifier and license information
as a comment in header of your original contributions after the copyright.

```text
SPDX-License-Identifier: MIT
```

Respect the licensing of any contributions you make which include the original
work of others (such as open source projects).

Do NOT remove copyright or license information from the original work of others.
Do NOT replace copyright or license information you were not authorized to modify.

### Developer Certification of Origin (DCO)

To ensure licensing criteria are met, all contributors must agree to
the Developer Certificate of Origin (DCO) for each contribution.

The DCO agreement is shown below and was retreived from
[developercertificate.org](https://developercertificate.org/)
on 9 April 2023.

**By adding a Signed-off-by tag to your contirubutions to this Git repository, you signify your agreement to the DCO.**

```text
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

The DCO is an attestation that is attached to every contribution
made by every developer. This is accomplished through the use of
the Signed-off-by tag at the footer of each commit message of the
contribution.

When a developer submits a contribution with the Signed-off-by tag,
it is a commitment that they have the right to submit the contribution
per the license.

See `--signoff` in
[git-commit(1)](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff)
for details on how to add the Signed-off-by tag more easily.

## Explicit agreement

All contributions should be opened via pull requests on GitHub.

This way contributors have agreed to the
[GitHub Terms of Use](https://help.github.com/articles/github-terms-of-service/),
which states:

```text
"Whenever you make a contribution to a repository containing notice of a
license, you license your contribution under the same terms, and you agree
that you have the right to license your contribution under those terms."
```

This method helps aid in the enforcement of the Developer Certificate of Origin.
