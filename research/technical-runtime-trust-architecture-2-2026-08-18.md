---
topic: "Runtime Trust Architecture Research Edition 2.0 (5thnode)"
type: "technical"
goals: "Walk through https://5thnode.com/research/runtime-trust-2; explain the architecture's thesis, primitives, flows, and 2.0 revisions; situate it among adjacent agent-identity and runtime-assurance work; flag naming collisions and evidence gaps."
date: "2026-08-18"
methodology: "Primary source: downloaded Research Edition 2.0 DOCX from 5thnode download API, plus APS/AIS companion specs. Parallel web research via sub-agents for landscape, related architectures, and implementation signals. Citations inline per references/citations.md. Confidence levels: High / Medium / Low."
---

# Research Report — Runtime Trust Architecture (Research Edition 2.0)

> **Type:** technical | **Date:** 2026-08-18 | **Constraints:** Focused walkthrough of the published paper and its immediate document family; not a full market TAM study.
>
> **Assumptions:** type=technical; primary object=`https://5thnode.com/research/runtime-trust-2` (Research Edition 2.0, August 2026, Tom Lindeman / 5thnode Ltd); goals=explain the paper section-by-section, clarify what changed from 1.x, map peer protocols, and assess how much is architecture vs shipping product.
>
> **Goals:**
> - Produce a readable walkthrough of Research Edition 2.0
> - Separate architecture claims from Coherence/Greenlight product claims
> - Place the work next to A2A/MCP/payments/identity peers and naming-colliding "Agent Passport" efforts
> - Surface open questions, risks, and what an implementer should do next

---

## Source Note

The public page at [5thnode Research Edition 2.0](https://5thnode.com/research/runtime-trust-2) is a client-rendered SPA. The authoritative downloadable artifact is the DOCX served by [the paper download API](https://5thnode.com/api/research/runtime-trust-2/download) (`Runtime_Trust_Architecture_Research_Edition_2.0.docx`, last-modified 2026-08-15 per response headers). Companion downloads: [APS Standard v0.1](https://5thnode.com/api/research/aps/download) and [AIS Standard v0.1](https://5thnode.com/api/research/ais/download). A local plaintext extract of the DOCX is saved at `research/runtime-trust-2-source-extract.txt`.

---

## Paper Walkthrough — Research Edition 2.0

### What this paper is trying to answer

According to [Runtime Trust Architecture Research Edition 2.0](https://5thnode.com/api/research/runtime-trust-2/download) (accessed 2026-08-18, confidence: Medium — primary author document), autonomous agents are moving from advisory tools into actors that pay, trade, contract, access records, and change infrastructure. Open standards make that agency practical; they do not decide whether a receiving bank, marketplace, hospital system, or peer agent should accept a consequential request. The paper’s thesis is that **runtime trust is the peer infrastructure layer for that admission decision** — what must be exchanged, verified, and preserved before consequential action, and across the actions that follow.

The author’s framing, also echoed on the company site and in [Tom Lindeman’s LinkedIn announcement of the first public Research Edition](https://www.linkedin.com/posts/thomaslindeman_autonomousai-autonomousagents-agenticai-activity-7485674703529889792-SB1Y) (accessed 2026-08-18, confidence: Medium), is deliberately not about model capability, token economics, or AGI timelines. It is about the handshake and ongoing assurance between independently developed systems.

### Version note — what 2.0 actually changes

Research Edition 2.0 is presented as a **major architectural revision**, not an incremental edit of 1.2. Three shifts dominate the version note in the DOCX ([primary download](https://5thnode.com/api/research/runtime-trust-2/download), accessed 2026-08-18, confidence: Medium):

1. **Runtime Trust is architecture, not product.** Coherence (by 5thnode) is demoted to *reference implementation* language. The architecture is claimed vendor-neutral.
2. **Trust is continuous, not one-shot.** Edition 1.x centered on the pre-action handshake. Operating experience allegedly showed that a handshake only establishes trust at a moment; agents keep operating, prompts and models change, scopes drift. The central claim of 2.0: *“Trust is not established once. Trust is continuously re-established through operational assurance.”*
3. **The document family splits.** The Agent Passport moves out into its own **APS (Agent Passport Standard)** draft. This paper references APS rather than redefining Passport structure.

Carried forward from 1.2: Control Authority as a first-class primitive, Approval Required as a protocol outcome, and the two-phase Fleet Trust Certificate.

### Section 1 — From handshake to operations

Section 1 reframes the original bilateral question (“what must initiator present / receiver verify before one consequential action?”) as still foundational but incomplete. The new claim is that a trust architecture unable to say whether past verifications still hold is “an audit of history, not an assurance of operation.”

It introduces **two complementary verification axes** that must not be blended into one score:

| Axis | Orientation | Question |
| --- | --- | --- |
| **Runtime Trust** | Vertical / per-agent | May this agent act? Is it still what it declared, with the authority it claimed, within the bounds it accepted? |
| **Fleet Integrity** | Horizontal / fleet-wide | Have global inconsistencies emerged across agents that are each individually trusted? Do declared views still compose into one consistent picture? |

An agent can hold a clean passport inside a structurally broken fleet, and the reverse can also be true. The paper treats that as a feature of honest reporting, not a defect.

### Section 2 — Definition, scope, and document family

**Definition (paraphrased from primary):** Runtime Trust is the architecture governing what autonomous systems exchange, verify, and preserve before consequential action — and across the actions that follow. It defines vocabulary (primitives), flows (discovery, enrollment, handshake, monitoring), axes (Runtime Trust / Fleet Integrity), and outcomes (including Approval Required).

**Explicit non-goals:** it is not an identity system, reputation network, security scanner, or enforcement gateway. It does not replace prompt-injection detection, model scanners, IAM, or domain APIs. Facts, policy, and outcomes must stay separate: verifiable inputs feed receiver policy; history is factual; reputation is interpretation.

The **document family** as stated in the paper:

| Document | Defines | Status (per paper) |
| --- | --- | --- |
| Runtime Trust Architecture (this paper) | Primitives, flows, axes, outcomes | Research Edition 2.0 |
| APS — Agent Passport Standard | Passport declaration, signed claim, discovery, lifecycle | Draft v0.1 |
| AIS — Agent Identity & Security | Runtime interoperability rules | v0.1 (paper says published Feb 2026) |
| Coherence | Operational reference implementation | Shipping |

### Section 3 — Runtime Trust Primitives

A primitive is defined by **the question it answers**, not by serialization format. The same primitive may be a signed manifest, VC, public key, directory entry, smart-contract state, ZK proof, or trusted API response.

The primitive conversations listed in §3.1:

- **Identity** — who are you?
- **Principal** — who do you represent?
- **Delegated Authority** — what may you do?
- **Mission** — why are you operating?
- **Intent** — what are you doing now?
- **Limitations** — what boundaries apply?
- **Evidence** — what supports your claims?
- **History** — what verifiable events should I consider?
- **Freshness** — is this still true, and has this request already been used?

Lifetime split matters: stable claims live in the **Agent Passport (APS)**; request-specific material lives in a per-interaction **Runtime Trust Package**; derived outcomes (reputation, admission, price, priority) are **never primitives** — they are receiver-policy outputs.

**Control Authority (§3.2)** is the 1.2 addition retained in 2.0. Delegated Authority bounds what an agent may *do*; Control Authority names who may change what the agent *is* (model, prompts, tools, config, keys). The procurement-agent example separates Owner, Principal, Operator, and Control Authority as four parties that are frequently conflated. **UNKNOWN is a valid first-class resolution** — it maps to Approval Required rather than a fabricated pass or unsupported deny.

**Agent Passport (§3.3)** is by-reference to APS. Architecturally load-bearing properties: operational contract (not identity card); signed claim attests *observation*, not virtue; undeclared material stays UNKNOWN (a 50%-coverage passport is preferred to a padded one).

### Section 4 — Discovery and enrollment

Receivers publish trust requirements at discoverable, versioned locations (paper analogy: robots.txt / OpenAPI, but for consequential-interaction trust conditions). Discovery evolves from document-fetch into an **operator-guided enrollment flow**:

Operator supplies Agent URL → Discover Agent Card (well-known APS passport, then agent card, read-only) → Discover Fleet → Construct Passport → Coverage Scan (declared / not disclosed / unknown) → Operator completes missing declarations → Passport Established → Operational Assurance Enabled.

Design rules: discovery is read-only and bounded; coverage never manufactures certainty; humans complete missing declarations. On establishment, the declaration is snapshotted as the **baseline**. From then on the Passport is a contract under supervision, not a static document.

### Section 5 — The Runtime Trust Handshake

Handshake shape is unchanged from prior editions. Edition 2.0 points readers to Edition 1.2 for the full seven-step flow; the live site still surfaces that sequence as ([5thnode SPA content](https://5thnode.com/research/runtime-trust-2) / bundle, accessed 2026-08-18, confidence: Medium):

1. **DISCOVER** — retrieve the receiving system’s current requirement set  
2. **PREPARE** — assemble identity, authority, mission, intent, limits, history, evidence  
3. **PRESENT** — submit a signed, replay-protected Trust Package  
4. **VERIFY** — validate claims, issuers, freshness, evidence, and policy  
5. **CERTIFY** — issue a bounded Trust Certificate for this action and period  
6. **INTERACT** — consume the certificate in A2A, MCP, x402, wallet, or chain tx  
7. **RECORD** — preserve evidence, certificate, outcome, and resulting history  

What 2.0 changes is **standing**: handshake is the *entry* into operational trust, not the whole of it. Success yields a **bounded, scoped, expiring certificate** — never durable status. Expiry is treated as architectural honesty about how long a verification can be presumed to hold. The older Edition 1.x web material also names a proposed interoperability layer **ARTP (AI Runtime Trust Protocol)** for discovery, package presentation, challenge-response, certification, evidence, handoff, and revocation ([Edition 1.2 page / SPA](https://5thnode.com/research/runtime-trust), accessed 2026-08-18, confidence: Medium); Edition 2.0’s DOCX text de-emphasizes ARTP naming in favor of operational monitoring and the document-family split.

### Sections 6–7 — Operational Trust Monitoring and Drift

**Operational Trust Monitoring** continuously asks whether the enrolled contract should still be believed. It compares **baseline** (approved declaration snapshot; advanced only by explicit operator approval) vs **observed state** (discovery, re-observation, verified runs — never a model’s opinion about the agent). Drift raises deduplicated findings for human review. There is **no automatic approval path**.

Re-verification triggers include credential revocation, authority change, mission drift, delegation-depth change, model/prompt update (Control Authority event), stale state, conflicting interpretation, behavior inconsistency, certificate expiry, and fleet topology changes.

**Operational drift** is divergence between declared contract and observed state/behavior. Drift is **evidence, not verdict**, and not automatically malicious. Deterministic classes named in the paper: identity/operator change; scope/refusal change; behavior outside declared scope; stale observation. **Approval Required** routes UNKNOWN required claims to a human/policy gate. Because enrollment records topology, drift can queue a Fleet Integrity re-check for the drifted agent’s exposure neighborhood; missing topology is treated honestly rather than invented.

### Section 8 — Two axes, one honest certificate

The **Fleet Trust Certificate** wraps two independently produced, independently signed, independently expiring result areas (Runtime Trust phase + Fleet Integrity phase). Results are never merged into a single score. Each phase carries an explicit evaluation state (`evaluated` / `not_evaluated`); a phase never run is never synthesized as a pass. Multi-agent contention for a scarce resource remains the **receiver’s policy** problem — Runtime Trust supplies facts and hooks, not winners.

### Section 9 — Evidence and preservation

Evidence rules refined by implementation: append-only hash-chained records; broken chains reported at the break, never silently repaired; per-agent history as signed lifecycle chain (registration, vouches, renewals, drift, revision approvals); recording failures must not suppress findings; history is factual while reputation is derived; persist enough to explain/verify/update trust — **not** an unrestricted behavioral transcript.

### Section 10 — Coherence as reference implementation

Coherence maps architecture concepts to shipping vocabulary: Operational Trust Monitoring, Agent Assurance (per-agent axis + APS passports), Fleet Coherence (reconciliation kernel + six-class structural taxonomy), Operational Evidence, and sealed certificates. A concrete example in the paper: an invoicing agent declared for `invoices.write` / `ledger.read` with refusal of `payments.execute` is later observed writing outside scope → scope-drift finding → human approve-or-investigate. The paper insists the architecture requires the *contracts* (honest UNKNOWN, baseline vs observed, human-gated approval, append-only evidence, unblended axes), not Coherence internals.

### Sections 11–12 — Peers and open questions

Runtime Trust is positioned as a **peer architecture with explicit handoffs** to A2A (agent communication), MCP (tools/data), AP2 and x402 (payments), identity/IAM, and domain APIs — not a replacement for them.

Open questions carried for a working group include: universal vs domain-specific primitives; history without a behavioral dossier (selective disclosure / ZK over lifecycle chains); what persists across many actions once monitoring refreshes trust; adversarial multi-agent ordering; agent lineage for spawned agents; registry governance and emergency revocation; drift-review economics at fleet scale.

The site footer and paper also reference a [Runtime Trust Working Group kickoff](https://5thnode.com/research/working-group) dated Aug 28, 2026 ([5thnode site navigation](https://5thnode.com/), accessed 2026-08-18, confidence: Medium).

---

<!-- Steps 2–4 landscape findings appended below as sub-agents complete. -->

## Technology Landscape

### Overview of Approaches

_Pending research._

### Performance and Benchmarks

_Pending research._

### Community Health and Maturity

_Pending research._

### Integration and Compatibility

_Pending research._

## Comparative Analysis

### Top Options Head-to-Head

_Pending research._

### Decision Matrix

| Option | Performance | DX  | Community | Cost | Lock-in | Notes |
| ------ | ----------- | --- | --------- | ---- | ------- | ----- |
| _TBD_  |             |     |           |      |         |       |

### Migration and Lock-in Risks

_Pending research._

## Implementation Considerations

### Recommended Architecture Patterns

_Pending research._

### Common Pitfalls and Gotchas

_Pending research._

### Security and Compliance

_Pending research._

---

## Key Findings

_Populated at Step 5._

## Strategic Recommendations

_Populated at Step 5._

## Risks and Uncertainties

_Populated at Step 5._

## Next Steps

_Populated at Step 5._
