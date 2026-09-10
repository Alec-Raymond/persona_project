# Meaning between stages

The editor, trimming pass, and every rewrite receive the same complete synthesis
context. Each group includes its machine names, combination mode, analysis, and
result. The text is passed directly, without another summary or length cutoff.

Previously, only the editor received the synthesis outputs. Trimming and rewrites
received the BwO and conversation, so they depended on the state prose to retain
the concrete meaning. They now have both sources. The rewrite prompt asks the
model to repair the fit problem while preserving the substantive point.

The fit checker remains a separate reader. It receives the situation, conversation,
and candidate reply. It has no access to the interior or group syntheses because
it judges what the other person could hear in the reply.

## What persists

The BwO remains free-form prose. It is the interior state carried to the next turn.
The next turn also receives recent conversation history. Past synthesis outputs
remain in the trace; they do not become a second persistent state store.

The editor's change log records the source groups and its explanation for each
change. The replay shows these explanations under **State changes**. These are
the editor's own accounts, not independent proof that a group's meaning survives.

The current prompt favors indirect description and preserving most of the prior
surface. This can preserve useful continuity, but it can also retain old imagery
at the expense of a clear statement of the current concern. Passing the syntheses
to rewrites removes that dependency within a turn. It does not establish how much
meaning the BwO preserves across later turns.

## Verification

`tests/test_pipeline_context.py` runs the complete pipeline with fake model outputs.
It forces two failed fit checks and checks every subsequent rewrite and trimming
call. Each receives the complete synthesis analysis and result, group identity,
updated state, and conversation. The fit reader does not receive interior context.
The tests make no model calls and do not claim to measure response quality.
