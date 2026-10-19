# Playbooks

One file per agent. Four sections, always in this order:

1. `## Current best` - the rules the agent runs from today. Under 300 words. Only learning-loop and Taka edit it. Every rule that came from data cites the ledger number.
2. `## Live experiment` - the one experiment running now: hypothesis, control, test, segment, metric, min sample, start date, decision rule.
3. `## Learned` - dated entries, newest first. Observation, number, what changed. Append only.
4. `## Retired` - variants and rules that lost, with the number that killed them. So nobody reruns them by accident.

Agents read sections 1 and 2 only. Sections 3 and 4 are the memory the learning loop reasons from.

Playbooks are seeded with sensible starting rules marked `seed`. Seeds are replaced by cited rules as the ledger fills. A `seed` rule still in `Current best` after 8 weeks means that agent's experiments are not running.
