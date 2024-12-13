#!/usr/bin/env bash

set -o errexit
set -o nounset

cmd="$*"

bash /app/wait-for-it.sh "$RMQ_HOST:$RMQ_PORT"

# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd
