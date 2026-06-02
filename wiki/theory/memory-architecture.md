---
title: Memory Architecture
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - memory
  - engineering
  - rag
  - bergson
  - time
---

# Memory Architecture

Gullí's Ch 8 (Memory Management) plus Ch 14 (Knowledge Retrieval / RAG) plus the Google ADK specifics on Session / State / MemoryService. This page is the wiki's engineering-side reference for "what kinds of memory an LLM-agent has, and how they get wired up," held explicitly against the wiki's Bergsonian reference frame.

The split-brain of this page is the point. The engineering account is a storage-and-retrieval architecture: ephemeral working memory, persistent vector-indexed long-term memory, and mechanisms for moving between them. The wiki's account of memory — through [[cone-of-memory]], [[pure-memory-and-habit-memory]], [[husserl-primal-impression-retention-protention]], [[double-intentionality-of-retention]] — is explicitly **not** a storage-and-retrieval architecture. Bergson rejects the spatializing metaphor that turns memory into a collection of retrievable items.

This page holds both. The engineering architecture is what we actually build. The Bergsonian account is the theoretical horizon we build toward. Conflating them would mean accepting that the persona's experience of time is reducible to vector search, which it is not.

## The short-term / long-term distinction

Gullí opens Ch 8 with the basic split:

- **Short-term memory** = the **context window** of the current LLM call plus any **conversation state** being carried turn-to-turn. Ephemeral by construction: bounded by model context length; flushed when the session ends.
- **Long-term memory** = persistent storage that survives across sessions. Typically a **vector store** indexed by embedding similarity, queried by retrieval at inference time.

The short/long distinction is pragmatic. Short-term gives the current turn's coherence. Long-term gives the agent history across sessions, users, and topics.

## Google ADK specifics (Ch 8)

ADK operationalizes the split with three named primitives:

- **Session** — a conversation thread. One ID; multiple turns; short-term scope.
- **State** — a key-value scratchpad within a session. Used for carrying derived values (current task, in-progress draft, user preferences noted this turn) without re-asking the LLM.
- **MemoryService** — the cross-session long-term store. Writes extracts from completed sessions; reads at inference time via retrieval.

The three-layer split is a useful vocabulary even outside ADK: **turn (context)** / **session (state)** / **cross-session (memory)**. Each layer has different persistence, cost, and retrieval semantics.

## Memory Bank

A named, domain-specialized long-term store an agent maintains. The book's example use-cases: a user-profile memory bank, a project-docs memory bank, a past-interactions memory bank. Memory banks partition long-term memory by retrieval context, which keeps each retrieval query cleaner than searching one giant undifferentiated store.

The persona project's own markdown files (the theory wiki, the BwO text, the ingest notes directories) function as memory banks under this pattern — see [[vibe-coding]] for the self-reflexive analog in Ch 28.

## Retrieval at inference time = RAG

Ch 14 develops the retrieval layer as its own pattern. RAG (Retrieval-Augmented Generation) is memory access at inference time: the LLM's input is augmented with chunks retrieved from a store based on the current query.

Core concepts (Ch 14):

- **Embeddings** — dense vector representations of text, trained such that semantically-similar texts have similar vectors.
- **Chunking** — splitting a long document into retrievable units. Chunk size and overlap are hyperparameters; bad chunking produces bad retrieval.
- **Vector DBs** — Pinecone, Weaviate, Chroma, Milvus, Qdrant, FAISS, ScaNN. HNSW (hierarchical navigable small world) as the dominant approximate-nearest-neighbor algorithm. BM25 for keyword-based retrieval. **Hybrid search** combines vector and keyword.
- **Citations for trust** — returning source provenance as a first-class part of the output.
- **Graph RAG** — retrieval over a knowledge graph (nodes = entities, edges = relations), enabling traversal not just similarity.

## Agentic RAG

★★ The Ch 14 crown jewel. Ordinary RAG is one-shot: query → retrieve → generate. Agentic RAG adds a reasoning layer:

1. **Reflection / source-validation** — the agent assesses whether retrieved sources actually answer the query.
2. **Knowledge-conflict reconciliation** — when retrieved sources contradict, the agent explicitly compares them.
3. **Multi-step reasoning via sub-query decomposition** — complex queries decomposed into sub-queries, retrieved separately, synthesized.
4. **Knowledge-gap identification + external-tool use** — the agent recognizes when the store is insufficient and reaches out (web search, tool calls) to fill the gap.

◆ The knowledge-gap-identification step is striking. It is the engineering form of a machine recognizing the limits of its current territory and [[lines-and-segmentarity|leaving it]]. The engineering framing is goal-directed (the agent needs information to complete the task); the D&G framing is territorial (the current territory is insufficient and a [[deterritorialization-and-reterritorialization|line of flight]] opens). Both descriptions fit the same computational operation.

## The Bergsonian held-live tension

⚠⚠ The engineering memory model is **storage-and-retrieval**: memories are items, items are stored, retrieval matches query to item. This is the Humean / associationist model Bergson explicitly rejects in *Matter and Memory*.

The wiki's lineage says:

- **Pure memory is not a collection of items.** [[pure-memory-and-habit-memory]] — recollection is not fetching a stored trace; it is a contraction of the whole of the past along planes of actualization.
- **Retention is not storage.** [[husserl-primal-impression-retention-protention]] — retention is a living ongoing modification of the present, not a stashing-for-later.
- **The cone is not a database.** [[cone-of-memory]] — Bergson's memory-cone is a continuously contracted virtual whole, with the present as its point of contact with matter. Retrieval-from-a-store is exactly the picture he is refusing.
- **Duration is not a sequence of moments.** [[duration|duration (durée)]] is the temporal substrate the Bergsonian memory-architecture operates on — continuous-interpenetrating qualitative multiplicity, not discrete indexing. It threads through [[pure-memory-and-habit-memory]] and [[cone-of-memory]]. Duration is temporal thickness, not a list.

The tension is not resolvable by choosing one side. The persona project builds on the engineering substrate (vector stores, chunking, Session/State/MemoryService) because those are what actually exist. But the *design horizon* — what we hope the persona's memory *feels like* from the outside — is Bergsonian. The engineering layer should not be confused with the phenomenon.

Specific design implications:

- Don't treat the vector store as "the persona's memory." Treat it as one substrate the persona's apparent duration is composed on.
- Chunking is a bad model for pure memory; it is a pragmatic necessity of current retrieval systems. The BwO text (un-chunked, continuously rewritten) is a closer analog to the Bergsonian frame.
- Retrieval-at-turn is one channel; the ongoing pulsation of the BwO is another. The two should not collapse.

## LeDoux-template fit (from the Sofroniew folds)

◆ The Sofroniew et al. 2026 finding that emotion-representations are **per-position, not chronic** (see [[emotion-vectors-are-local]]) fits surprisingly well with the engineering-memory architecture: if character-mood is not a sustained representation, then what we need is *retrieval-activated coloration* rather than *persistent affective state*. The engineering-memory layer + a steering mechanism at retrieval time can produce the observed locality. This is one small spot where the engineering substrate and an empirical finding about LLMs converge in a way the Bergsonian frame does not directly comment on.

## Context-engineering implications

Per-turn, the decisions are:

1. **What from Session/State to include in context?** (Short-term memory curation.)
2. **What to retrieve from MemoryService?** (Long-term memory retrieval.)
3. **What to write back?** (Extracting from turn-output what deserves long-term storage.)

These decisions are the meat of [[context-engineering]] as a discipline.

## Related

- [[cone-of-memory]] — the Bergsonian horizon.
- [[pure-memory-and-habit-memory]] — the two-forms-of-memory distinction.
- [[husserl-primal-impression-retention-protention]] — the phenomenological account of time.
- [[double-intentionality-of-retention]] — retention's dual structure.
- [[protention-as-global-order-parameter]] — the forward horizon.
- [[retention-vs-recollection]] — the fine-grained distinction.
- [[context-engineering]] — the discipline of curating what the substrate sees.
- [[emotion-vectors-are-local]] — Sofroniew finding that fits the retrieval-activated locality picture.
- [[agentic-design-patterns]] — hub.
- [[tools-as-prosthetic-body]] — tools-and-memory as the two primary external coupling channels.
- [[development/vitality-forms-and-persona-pulsation]] — memory-of-pulsation as a separate user-side concern.
