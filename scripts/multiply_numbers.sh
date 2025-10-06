#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <number1> <number2>" >&2
  exit 1
fi

for arg in "$1" "$2"; do
  if [[ ! $arg =~ ^-?[0-9]+$ ]]; then
    echo "Error: arguments must be integers" >&2
    exit 1
  fi
done

result=$(( $1 * $2 ))
printf '%s * %s = %s
' "$1" "$2" "$result"
