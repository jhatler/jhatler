#!/usr/bin/env bash

set -ex
set -o pipefail

liquidprompt_activate

docker pull ghcr.io/super-linter/super-linter:v5.7.2

exit 0
