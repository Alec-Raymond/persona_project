"""Pydantic models used both as the domain model and as structured-output
schemas for the LLM calls that need them.

Per-machine outputs are plain text (richer, no schema overhead); the stages
that need structure — relevance voting, group synthesis, the final write —
use the models here.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class MachinePick(BaseModel):
    """One machine nominated by the relevance voter."""

    name: str = Field(description="Exact machine name from the roster.")
    score: float = Field(description="Relevance to this moment, 0.0–1.0.")
    reason: str = Field(description="One short clause: why it resonates now.")


class RelevanceVotes(BaseModel):
    """The machines most alive to the current situation."""

    picks: list[MachinePick]


class GroupSynthesis(BaseModel):
    """One group's machine texts woven into a single current, under a chosen mode."""

    mode: str = Field(
        description="Chosen mode: connective | disjunctive | conjunctive | transcendent."
    )
    thinking: str = Field(
        description="About 100 words of free association across the machine "
        "products — laying their movements alongside each other, chasing what "
        "their combination suggests. Standalone: keeps the machines' concrete "
        "anchors in its own sentences; its reader never sees the products."
    )
    result: str = Field(
        description="At least 250 words (longer welcome, shorter not): the "
        "synthesis itself in the chosen mode. Showing-mode prose, one current of "
        "the persona's interior, standing entirely on its own."
    )


class EditNote(BaseModel):
    """One recorded edit to the BwO, with the input that drove it.

    Engineering instrumentation, not the persona introspecting: this is the final
    machine logging which of its inputs it acted on, the way a compiler emits a
    source map. It never reaches the persona and is never shown to a later stage.
    """

    change: str = Field(description="What changed on the surface, in a short clause.")
    driven_by: list[str] = Field(
        description="Which inputs drove it. Use group labels exactly as given "
        "(e.g. 'Group 2'), and/or 'what was just said', and/or 'carried over'."
    )
    why: str = Field(description="Why that input produced this change. One sentence.")


class FitCheck(BaseModel):
    """A blind reader's verdict on whether a candidate reply fits the
    conversation — it sees only the situation, the exchange, and the reply."""

    explanation: str = Field(
        description="Why the reply fits or does not fit, concretely: what a "
        "person in this situation would hear in it. Written before the verdict."
    )
    fits: bool = Field(
        description="True if the reply is the kind of thing this person would "
        "plausibly say next, here; False otherwise."
    )


class BwoEdit(BaseModel):
    """The interior editor's full write: thinking, the new surface, its edit
    log, and the persona's initial (pre-armor) reply.

    Field order is generation order: the thinking runs first and the reply
    precipitates last. The voice governs only the reply, never the surface.
    """

    thinking: str = Field(
        description="At least 500 words of free association across the currents, "
        "the conversation, and the surface as it stands — what moved, what "
        "collided, what the persona wants and won't say, where the relation "
        "stands, what reply would be alive. Anchored to concrete referents; "
        "never leaves the pipeline but must still read on its own."
    )
    bwo: str = Field(
        description="The EDITED BwO surface — the persona's interior after this "
        "turn, about 500 words of showing-mode intensive prose. An edit of the "
        "existing surface, not a fresh composition: most of it survives, moved."
    )
    edits: list[EditNote] = Field(
        default_factory=list,
        description="One note per substantive change made to the surface, in the order "
        "they appear. Cover every real change; skip pure rewording.",
    )
    response: str = Field(
        description="The persona's reply to the other person, in the persona's "
        "voice — spoken from the interior surface just written, from where the "
        "persona now actually is. Whatever length it naturally comes to; a "
        "later stage cuts, so no pre-trimming and no manufacturing."
    )
    justification: str = Field(
        default="",
        description="Why the reply says what it says, grounded SOLELY in the "
        "surface — written as if the surface were the only document in the "
        "world. Point only at its currents; never at the conversation, the "
        "syntheses, or anything else. Instrumentation; never shown to the "
        "persona or any later stage."
    )
    revised_response: str = Field(
        default="",
        description="Only if writing the justification exposed the reply as "
        "unjustifiable — speaking from nowhere, or against what the surface "
        "holds: a second attempt that does speak from the surface. Leave "
        "empty when the original reply stands."
    )
