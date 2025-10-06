#!/usr/bin/env bash
set -euo pipefail

fail() {
  echo "[FAIL] $1" >&2
  exit 1
}

pass() {
  echo "[PASS] $1"
}

run_script() {
  ./scripts/fibonacci.sh "$@"
}

# Test default count (10 terms)
expected_default="0 1 1 2 3 5 8 13 21 34"
output_default=$(run_script)
[[ "$output_default" == "$expected_default" ]] || fail "Default run expected '$expected_default' but got '$output_default'"
pass "Default run"

# Test custom count (1 term)
expected_one="0"
output_one=$(run_script 1)
[[ "$output_one" == "$expected_one" ]] || fail "1-term run expected '$expected_one' but got '$output_one'"
pass "One term"

# Test input validation (non positive)
if run_script 0 >/dev/null 2>&1; then
  fail "Zero terms should exit with error"
else
  pass "Zero terms validation"
fi

if run_script -3 >/dev/null 2>&1; then
  fail "Negative terms should exit with error"
else
  pass "Negative terms validation"
fi

if run_script foo >/dev/null 2>&1; then
  fail "Non-numeric terms should exit with error"
else
  pass "Non-numeric validation"
fi

echo "All fibonacci tests passed."
