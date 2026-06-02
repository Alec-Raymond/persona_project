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


class MachineSummary(BaseModel):
    machine: str
    summary: str = Field(description="The machine's output, compressed to one line.")


class GroupSynthesis(BaseModel):
    """One group's machine outputs combined under a chosen synthesis mode."""

    mode: str = Field(
        description="Chosen mode: connective | disjunctive | conjunctive | transcendent."
    )
    summaries: list[MachineSummary] = Field(
        description="Each machine's output restated in one line."
    )
    result: str = Field(
        description="The synthesis itself, in the chosen mode. Showing-mode prose."
    )


class FinalOutput(BaseModel):
    """The final machine's composite write."""

    bwo: str = Field(
        description="The edited BwO surface — the persona's interior after this turn. "
        "Showing-mode, intensive prose. Keep under ~250 words; let old content contract."
    )
    response: str = Field(
        description="What the persona actually says this turn. Spoken from the BwO, "
        "not a report of it."
    )
