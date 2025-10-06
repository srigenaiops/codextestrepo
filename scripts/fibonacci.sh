#!/usr/bin/env bash
set -euo pipefail

count=${1:-10}

if [[ ! $count =~ ^[0-9]+$ ]] || (( count <= 0 )); then
  echo "Usage: $0 [positive-integer-terms]" >&2
  exit 1
fi

prev=0
curr=1

for ((i = 0; i < count; i++)); do
  printf '%s' "$prev"
  if (( i < count - 1 )); then
    printf ' '
  else
    printf '\n'
  fi
  next=$((prev + curr))
  prev=$curr
  curr=$next
done
