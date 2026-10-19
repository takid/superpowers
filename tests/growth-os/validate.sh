#!/usr/bin/env bash
# Structural validation for the Growth OS layer.
# Checks that every agent named in the skill has an agent file and a playbook,
# that frontmatter is well formed, and that playbooks carry the four sections.
# No Claude API calls; runs in CI or locally in under a second.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SKILL_DIR="$ROOT/skills/growth-os"
AGENT_DIR="$ROOT/agents"
PLAYBOOK_DIR="$SKILL_DIR/playbooks"

AGENTS="growth-director lead-responder quote-closer prospector local-authority content-engine reputation ops-dispatcher retention-referral cash-collector capacity-recruiter learning-loop"

fail=0
pass=0

ok()   { pass=$((pass+1)); }
bad()  { fail=$((fail+1)); echo "FAIL: $1"; }

check_frontmatter() {
    local file="$1" expected_name="$2"
    [ "$(head -n1 "$file")" = "---" ] || { bad "$file: no opening frontmatter"; return; }
    local fm
    fm="$(awk 'NR==1{next} /^---$/{exit} {print}' "$file")"
    echo "$fm" | grep -q "^name: ${expected_name}$" || { bad "$file: name must be '${expected_name}'"; return; }
    echo "$fm" | grep -q "^description:" || { bad "$file: missing description"; return; }
    ok
}

# 1. Skill entry
[ -f "$SKILL_DIR/SKILL.md" ] && check_frontmatter "$SKILL_DIR/SKILL.md" "growth-os" || bad "skills/growth-os/SKILL.md missing"
fm_len=$(awk 'NR==1{next} /^---$/{exit} {print}' "$SKILL_DIR/SKILL.md" | wc -c)
[ "$fm_len" -le 1024 ] && ok || bad "SKILL.md frontmatter over 1024 chars ($fm_len)"
grep -q '^description: Use when' "$SKILL_DIR/SKILL.md" && ok || bad "SKILL.md description must start with 'Use when'"

# 2. Supporting docs referenced by the skill exist
for doc in scoreboard.md feedback-loop.md gates.md coverage-map.md schedule.md ledger/README.md ledger/example.csv playbooks/README.md; do
    [ -f "$SKILL_DIR/$doc" ] && ok || bad "missing $doc"
done

# 3. Every agent: file, frontmatter, playbook with four sections, listed in SKILL.md
for a in $AGENTS; do
    f="$AGENT_DIR/$a.md"
    [ -f "$f" ] || { bad "agent file missing: $f"; continue; }
    check_frontmatter "$f" "$a"
    grep -q '^model: inherit' "$f" && ok || bad "$f: model: inherit missing"
    grep -q "^| $a " "$SKILL_DIR/SKILL.md" && ok || bad "SKILL.md agent table missing $a"
    p="$PLAYBOOK_DIR/$a.md"
    [ -f "$p" ] || { bad "playbook missing: $p"; continue; }
    for section in "## Current best" "## Live experiment" "## Learned" "## Retired"; do
        grep -q "^$section" "$p" && ok || bad "$p: missing '$section'"
    done
    # Agents other than growth-director and learning-loop must name their autonomy tier
    if [ "$a" != "growth-director" ] && [ "$a" != "learning-loop" ]; then
        grep -q '^## Autonomy' "$f" && ok || bad "$f: missing Autonomy section"
    fi
    grep -q '^## Done' "$f" && ok || bad "$f: missing Done section"
done

# 4. Ledger example matches schema header
expected_header="row_id,ts,agent,action,channel,segment,variant,contact_ref,value_gbp,outcome,ref_row_id,note"
[ "$(head -n1 "$SKILL_DIR/ledger/example.csv")" = "$expected_header" ] && ok || bad "ledger/example.csv header does not match schema"

# 5. Every example ledger agent is a real agent
for agent in $(tail -n +2 "$SKILL_DIR/ledger/example.csv" | cut -d, -f3 | sort -u); do
    echo " $AGENTS " | grep -q " $agent " && ok || bad "ledger example uses unknown agent '$agent'"
done

echo "growth-os validation: $pass passed, $fail failed"
[ "$fail" -eq 0 ]
