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

The DOCX §3.1 presents primitives as short machine-speed conversations (Identity, Principal, Delegated Authority, Mission, Intent, Limitations, Evidence, History, Freshness). The live site and Edition 1.x material enumerate a fuller **fourteen-primitive** set (P01–P14) that also includes Root of Trust, Policy/Compliance, Environment/Integrity, Transaction Artifacts, and Trust Session ([5thnode SPA](https://5thnode.com/), accessed 2026-08-18, confidence: Medium). Treat the 14-item list as the fuller vocabulary and the DOCX §3.1 list as the condensed narrative; Control Authority is called out separately as a first-class addition from 1.2.

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

## Technology Landscape

### Overview of Approaches

The agent stack is splitting into complementary layers, and Runtime Trust 2.0 explicitly wants to sit in the *admission / operational assurance* gap rather than replace communication or payment rails. Parallel landscape research ([Agent trust landscape](bc-0b39003c-89cc-5a51-b0aa-e72537e3f796)) and the primary paper agree on that layering. According to the [A2A Protocol site](https://a2a-protocol.org/latest/) (accessed 2026-08-18, confidence: High — Primary), Agent2Agent is an open standard for communication among opaque agents (Google → Linux Foundation; IBM ACP later merged into A2A). MCP, donated to the Agentic AI Foundation, standardizes agent-to-tool access and continues to harden enterprise authorization (e.g. EMA / ID-JAG in the 2026-07-28 MCP spec). SPIFFE/SPIRE supplies workload identity; OpenID [CAEP 1.0](https://openid.net/specs/openid-caep-1_0-final.html) (Final Spec, Aug/Sep 2025) supplies continuous session/device/credential signals — the closest mainstream “continuous assurance” bus, but not an agent operational-contract or fleet-integrity architecture.

On the payment axis, [Google AP2](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol) (accessed 2026-08-18, confidence: High — Primary) addresses agent payment authorization via signed Mandates, with an A2A x402 extension for crypto; [x402](https://x402.org/wp-content/uploads/sites/10/2026/06/x402-whitepaper.pdf) handles HTTP 402 stablecoin settlement. Parallel work also includes IETF [Agent Identity Protocol](https://datatracker.ietf.org/doc/html/draft-singla-agent-identity-protocol) drafts and a NIST NCCoE Feb 2026 concept paper on software/AI agent identity ([NIST CSRC](https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd), accessed 2026-08-18, confidence: High). Those harden identification and delegation; they do not jointly specify Runtime Trust’s enrollment → expiring certificate → drift-monitoring → Fleet Integrity loop.

Greenlight, operated by 5thnode, markets itself as a multi-chain crypto security scanner and AIS-aligned pre-action check API returning Ed25519-signed findings (not proceed/stop verdicts), and as a reference “Agentic Runtime Trust Engine” with an ARTP console ([Greenlight AI](https://greenlightagent.com/), accessed 2026-08-18, confidence: Medium — Primary vendor site). Smoke tests in this research pass confirmed live scan/pre-action APIs ([AIS and integration deep dive](bc-72fe63e4-9253-587f-849b-cd5ff4f7f866); [5thnode implementation signals](bc-4f3d1c93-7d32-5311-bad1-70f40f73239b)). That positions Greenlight as an *evidence provider / engine instance* inside the architecture — consistent with 2.0’s architecture-vs-product split, though brand overlap with Coherence remains high.

### Performance and Benchmarks

No independent latency, throughput, or scale benchmarks for Coherence Operational Trust Monitoring, Fleet Integrity reconciliation, or ARTP handshakes were found in public third-party sources during this research pass. The architecture text asserts handshakes should complete “within the latency envelope of the downstream protocol” ([5thnode SPA / Edition 1.x material](https://5thnode.com/research/runtime-trust), accessed 2026-08-18, confidence: Low for performance — marketing/architecture prose only). **Gap:** no published p50/p99 measurements, fleet sizes, or drift false-positive rates.

### Community Health and Maturity

Public maturity signals are early and largely first-party ([5thnode implementation signals](bc-4f3d1c93-7d32-5311-bad1-70f40f73239b)). **Greenlight** is the strongest shipping signal: live Agent API, OpenAPI, well-known manifest, signed findings verified in this pass — still beta/free, aggregator-backed, no independent reviews found. **Coherence** “live/finished” claims remain founder-asserted (LinkedIn / Pragma branding); no public reproducible certificate console or starred product repo was found (`EtherDotBlue/runtime-trust` reported empty). **Spectacle** site exists with BETA/SOON arenas; production sport unverified. AIS is a company living standard (23 requirements on-site; LinkedIn still says 22), not multi-org adoption.

Research Edition 1.x was announced publicly by Tom Lindeman around July 2026 ([LinkedIn post](https://www.linkedin.com/posts/thomaslindeman_autonomousai-autonomousagents-agenticai-activity-7485674703529889792-SB1Y), accessed 2026-08-18, confidence: Medium). Edition 2.0 DOCX last-modified 2026-08-15. A Runtime Trust Working Group is advertised with global kickoff **August 28, 2026** ([5thnode SPA](https://5thnode.com/research/working-group), accessed 2026-08-18, confidence: Medium — first-party); as of 2026-08-18 no public agenda/invite materials beyond site copy were found.

Lindeman’s motivational figure tracks IDC-linked forecasts: Microsoft-sponsored IDC Info Snapshot #US53361825 (May 2025) popularized as **1.3B agents by 2028**, while an [IDC blog](https://www.idc.com/resource-center/blog/agent-adoption-the-it-industrys-next-great-inflection-point/) projects **>1B by 2029**. 5thnode marketing mixes both lines. Treat as directional industry rhetoric.

Org context: 5thnode marketing says Singapore Ltd / founded 2021; ACRA-linked records show **5THNODE PTE. LTD.** (UEN 201537775R) live since **2015** — likely rename/repurpose. Author background (long Microsoft tenure; ConsenSys Diligence / MythX; Runtime Verification CSO) is well supported for Diligence/MythX and consistent but thinner for RV ([SCSA MythX spotlight](https://www.smartcontractsecurityalliance.com/articles/member-spotlight-mythx), accessed 2026-08-18, confidence: High for Diligence/MythX).

### Integration and Compatibility

**Companion document mapping (5thnode family):**

| Layer | Artifact | Role |
| --- | --- | --- |
| Architecture | Runtime Trust 2.0 | Primitives, flows, axes, outcomes |
| Passport format | APS v0.1 | Declaration + signed claim + discovery + lifecycle |
| Security requirements | AIS v0.1 | 23 requirements for Web3/crypto agents |
| Ops platform | Coherence | Reference monitoring / fleet / certificates |
| Pre-action evidence | Greenlight | Signed findings / ARTP engine demo |

APS defines a deliberately small passport (`identity`, `operator`, `authority`, `scope`, `refusals`) discoverable at `/.well-known/aps-passport.json`, with Ed25519 signed claims that attest *observation*, honest expiry, and UNKNOWN for undeclared fields ([APS Standard v0.1](https://5thnode.com/api/research/aps/download), accessed 2026-08-18, confidence: Medium — Primary). AIS is broader and more Web3-specific: 23 requirements across Principal & Authorization, Credential Integrity, Instruction Integrity, Capability Governance, Behavioral & Reputation, Environmental Security, and Governance & Control, published February 27, 2026 ([AIS Standard v0.1](https://5thnode.com/api/research/ais/download), accessed 2026-08-18, confidence: Medium — Primary). Several AIS items map cleanly onto Runtime Trust concerns (explicit capability declaration AIS-011, policy/drift AIS-013, behavioral history AIS-014, audit trail AIS-019, pre-execution verification AIS-023), while others (prompt injection AIS-008, sanctions screening AIS-003) sit in adjacent security domains the architecture says it does not replace.

Handshake step 6 explicitly hands certificates into A2A, MCP, x402, wallet, or chain transactions — a peer-handoff model rather than a protocol fork. Integration research ([AIS and integration deep dive](bc-72fe63e4-9253-587f-849b-cd5ff4f7f866)) found **no public wire bindings** (A2A Agent Card fields, MCP tool schemas, AP2 mandate extensions, or x402 header maps) beyond architectural prose and Greenlight demos — so handoff remains a design claim, not proven interop. AIS maps strongly onto Principal/Credential/Capability/Governance primitives and weakly onto Instruction Integrity (prompt injection), which RTA correctly parks outside its job. Greenlight ≈ evidence input toward AIS-023 (pre-execution verification), not the full AIS proof object; MCP/LangChain integrations remain **Planned**.

## Comparative Analysis

### Top Options Head-to-Head

**5thnode APS vs other “Agent Passport” efforts (naming collision).** Parallel research ([APS naming collision](bc-ae5f9b46-f2ee-506f-830a-7b4c3d972b2b)) confirms at least two independent “APS” protocols plus adjacent products. 5thnode’s Agent Passport **Standard** (five-field operational contract + `coherence_passport` observation claim at `/.well-known/aps-passport.json`) is unrelated to Tymofii Pidlisnyi / AEOESS’s Agent Passport **System** ([draft-pidlisnyi-aps-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/), [agent-passport.org](https://agent-passport.org/), accessed 2026-08-18, confidence: High — Primary): self-signed identity passports, seven-facet monotonic delegation, intent/decision/receipt chain, MCP/OAuth bindings. That IETF draft is an **individual submission**, not working-group consensus; an AAIF project proposal was declined ([AAIF #14](https://github.com/aaif/project-proposals/issues/14), accessed 2026-08-18, confidence: High). Additional name collisions raise risk further: [cezexPL/agent-passport-standard](https://github.com/cezexPL/agent-passport-standard) also expands APS as “Standard” with a different DID/receipt model; [Cubitrek Agent Passport](https://cubitrek.com/agent-passport) uses a near path `/.well-known/agent-passport.json`; Workday “Agent Passport” is an enterprise product name. **Developer confusion risk is High.**

**Runtime Trust vs continuous Zero Trust / continuous authorization.** [NIST SP 800-207](https://doi.org/10.6028/nist.sp.800-207) and ISCM/ongoing-authorization guidance share the rejection of one-shot implicit trust, but their unit of continuity is enterprise access/session posture and AO risk cadence — not agent operational-contract drift or Fleet Integrity ([continuous assurance paradigms](bc-8f9f84b1-1747-54db-a04f-010da78c4f2b)). Complementary input plane, not a substitute.

**SAFE-Matter™ and related present-state admissibility work.** [SAFE-Matter Reference Runtime Architecture](https://doi.org/10.5281/zenodo.20116375) (accessed 2026-08-18, confidence: High on self-claims, Low on independent evaluation — unreviewed Zenodo) is the closest conceptual peer: capability ≠ admissibility; execution authority only while present-state evidence remains provable. Classical aerospace RTA ([ASTM F3269](https://www.astm.org/f3269-21.html)) is an orthogonal *safety-filter* plane. Continuous attestation ([MITRE CRA](https://www.mitre.org/news-insights/publication/framework-continuous-remote-attestation)) strengthens the evidence substrate but does not define Approval Required. **Conflict:** some “cryptographic runtime governance” framings celebrate *autonomous* drift remediation; that collides with Edition 2.0’s no-automatic-drift-approval rule unless limited to fail-closed halt/quarantine.

### Decision Matrix

| Option | What it decides | Continuity model | Openness signal | Lock-in risk | Notes |
| --- | --- | --- | --- | --- | --- |
| Runtime Trust 2.0 + APS/AIS | Admission facts + ops assurance vocabulary | Handshake + monitoring + drift review | Research editions + drafts on 5thnode | Medium if Coherence is only engine | Vendor-neutral claim; reference impl is 5thnode |
| A2A | Agent collaboration / tasks | Session/task lifecycle | Linux Foundation, multi-vendor | Lower for messaging | Does not certify operational contract drift |
| MCP | Tool/data access | Connection/session | Broad ecosystem | Tool-server coupling | Peer handoff target |
| x402 | Pay-per-request settlement | Per-request 402 challenge | Open protocol / Coinbase origin | Rail/facilitator choices | Peer handoff target |
| IETF/agent-passport.org APS | Identity, attenuated authority, receipts | Per-action policy chain | Individual I-D + OSS (AAIF declined) | Protocol choice | **Different APS** than 5thnode |
| Cubitrek / cezexPL passports | Business or DID passport variants | Per their specs | Early OSS/drafts | Path/schema choice | More name/path collisions |
| SAFE-Matter / admissibility cluster | Present-state execution legitimacy | Continuous recomputation at reliance | Zenodo/self-pub (mostly unreviewed) | Domain framing | Closest thesis peer; different domain |
| NIST ZTA / ISCM-OA | Access & ongoing AO authorization | Continual / cadenced reevaluation | Established federal standards | Enterprise IAM coupling | Complementary access plane |
| Classical RTA (ASTM F3269) | Bound untrusted controllers | Monitor → recovery switch | Established aerospace | Safety-path dependence | Complementary physical-safety plane |
| Greenlight | Crypto pre-action findings | Per-scan signed evidence | Public API docs | Vendor evidence provider | Reference Runtime Trust Engine (first-party) |

### Migration and Lock-in Risks

If you adopt only the *vocabulary* (primitives, UNKNOWN, Approval Required, two unblended axes), migration cost is mostly conceptual. If you enroll fleets into Coherence-specific certificates, well-known paths, and claim `kind: coherence_passport` (as in APS v0.1 example), switching engines later requires claim/format translation. APS text asserts “no product owns” the standard, but the draft is extracted from the shipped Coherence implementation ([APS v0.1](https://5thnode.com/api/research/aps/download), accessed 2026-08-18, confidence: Medium) — an honesty tension worth tracking as the working group forms.

## Implementation Considerations

### Recommended Architecture Patterns

From the paper’s own contracts, a minimal honest deployment looks like: publish receiver requirements → enroll agents via read-only discovery + human-completed UNKNOWN gaps → snapshot baseline → issue short-lived per-action certificates → monitor baseline vs observed → human approve or investigate drift → preserve append-only evidence → optionally run Fleet Integrity as a separate signed phase. Keep reputation and admission scores in receiver policy, not in the passport.

### Common Pitfalls and Gotchas

Treating a successful handshake as durable authorization contradicts Edition 2.0’s core claim. Inferring undeclared fields instead of UNKNOWN pads passports and breaks the honesty model. Merging Runtime Trust and Fleet Integrity into one score hides structural failure. Auto-approving drift removes the human accountability the architecture depends on. Confusing 5thnode APS with IETF Agent Passport System will send implementers to the wrong schemas. Expecting Greenlight’s signed findings to be a policy verdict violates Greenlight’s own “findings, not proceed/stop” stance ([greenlightagent.com](https://greenlightagent.com/), accessed 2026-08-18, confidence: Medium).

### Security and Compliance

AIS provides a Web3-oriented requirements checklist with Critical items spanning principal KYC/sanctions, credential integrity, prompt-injection defense, capability declaration, audit trail, emergency halt, and pre-execution verification proof ([AIS v0.1](https://5thnode.com/api/research/ais/download), accessed 2026-08-18, confidence: Medium). No SOC 2 / ISO / third-party audit artifacts for Coherence or Greenlight were located in this pass (**Gap**). Greenlight’s privacy copy claims it does not store personal information or transaction history ([Greenlight](https://greenlightagent.com/), accessed 2026-08-18, confidence: Low for compliance — self-asserted).

---

## Key Findings

According to [Runtime Trust Architecture Research Edition 2.0](https://5thnode.com/api/research/runtime-trust-2/download) (accessed 2026-08-18, confidence: Medium), the paper’s core move is philosophical as much as technical: a pre-action handshake is necessary but insufficient, because agents keep changing after admission. Edition 2.0 therefore re-centers the architecture on continuous operational assurance — baseline versus observed contract comparison, human-gated drift approval, and independently signed Runtime Trust / Fleet Integrity certificate phases that must never be mashed into one score.

The document family split is load-bearing. APS Draft v0.1 defines a small portable operational contract and observation claim ([APS download](https://5thnode.com/api/research/aps/download), accessed 2026-08-18, confidence: Medium); AIS v0.1 supplies a 23-requirement Web3 agent security checklist ([AIS download](https://5thnode.com/api/research/ais/download), accessed 2026-08-18, confidence: Medium); Coherence and Greenlight are positioned as reference implementation and reference engine. This suggests readers should evaluate the architecture’s contracts separately from 5thnode product readiness.

Adjacent industry protocols mostly solve different jobs. [A2A](https://a2a-protocol.org/latest/) and MCP move messages and tool calls; [x402](https://x402.org/wp-content/uploads/sites/10/2026/06/x402-whitepaper.pdf) moves money. Runtime Trust claims the missing admission/assurance peer layer. That layering story is coherent on paper; independent multi-vendor adoption of 5thnode’s specific primitives, well-known paths, and certificates was not evidenced in this pass.

A practical hazard is branding collision: 5thnode’s APS is not the IETF / [agent-passport.org](https://agent-passport.org/) Agent Passport System ([draft-pidlisnyi-aps-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/), accessed 2026-08-18, confidence: High). Both use “APS” and Ed25519 passports for agentic systems; schemas and problem statements diverge. Anyone implementing from a web search alone can easily wire the wrong stack.

Evidence for shipping scale remains first-party. Greenlight’s public Agent API and well-known manifest are live vendor signals ([greenlightagent.com](https://greenlightagent.com/), accessed 2026-08-18, confidence: Medium). Coherence “shipping” is asserted by the paper and site without independent customer case studies located here. The Runtime Trust Working Group kickoff is scheduled for 2026-08-28 — after this report’s date — so governance maturity is prospective rather than demonstrated.

## Strategic Recommendations

1. **Read 2.0 as an operational-trust checklist, not a product buy.** Adopt the honesty rules first: UNKNOWN over inference, expiring certificates, unblended axes, human-gated baseline advancement. Evidence: [Runtime Trust 2.0 DOCX](https://5thnode.com/api/research/runtime-trust-2/download).
2. **Map peer protocols explicitly in your architecture diagram.** Put A2A/MCP/x402/IAM beside Runtime Trust with labeled handoffs at certificate consume time, so teams do not try to stretch one protocol into another’s job. Evidence: paper §11; [A2A](https://a2a-protocol.org/latest/); [x402 whitepaper](https://x402.org/wp-content/uploads/sites/10/2026/06/x402-whitepaper.pdf).
3. **Namespace-check any “APS” dependency.** If you need attenuated delegation receipts and MCP policy chains, evaluate IETF/agent-passport.org APS separately from 5thnode’s operational-contract passport. Evidence: [draft-pidlisnyi-aps-03](https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/03/); [5thnode APS](https://5thnode.com/api/research/aps/download).
4. **If evaluating Coherence/Greenlight commercially, demand measurable ops metrics.** Ask for handshake latency envelopes, drift false-positive rates, fleet sizes in production, and third-party assurance. Current public material does not provide them (confidence: Low on performance claims).
5. **Track the Aug 28, 2026 working group** for multi-party governance of vocabulary and registry rules — the open questions in §12 (lineage, registry emergency revocation, drift-review economics) are where standards work either becomes real or stays essay. Evidence: [working group page](https://5thnode.com/research/working-group).

## Risks and Uncertainties

- **Data gaps:** No independent Coherence benchmarks, customer references, or compliance attestations found; no public Trust Certificate → A2A/MCP/AP2/x402 wire adapters; Aug 28 WG materials not yet public.
- **Low-confidence claims:** Billion-agent IDC figures vary (1.0B vs 1.3B; 2028 vs 2029) across secondary citations; Coherence “shipping” is Medium/self-asserted; treat as motivational context.
- **Unresolved conflicts:** Site/1.x materials emphasize fourteen primitives and ARTP naming; the 2.0 DOCX compresses primitives and elevates monitoring — not contradictory, but implementers need a single normative checklist. “Continuous” means different control loops in NIST ISCM vs present-state admissibility architectures. Autonomous drift remediation (some CRG framings) conflicts with Approval Required unless strictly fail-closed.
- **Domain risks:** Human-gated drift review may not scale without batching economics (paper’s own open question); first-party reference implementations can quietly become de facto standards despite vendor-neutral language; APS/Agent Passport naming now spans Standard vs System vs Cubitrek/cezexPL/Workday product names — integration error risk is High.

## Next Steps

- Attend or monitor the Runtime Trust Working Group kickoff (2026-08-28) and inspect the promised public repository.
- Diff Edition 1.2 vs 2.0 DOCX side-by-side for ARTP / primitive enumeration deltas if building a conformance suite.
- Prototype a minimal APS well-known passport + UNKNOWN coverage scan against one internal agent before buying platform software.
- Separately spike IETF Agent Passport System if you need cryptographic delegation receipts rather than operational-contract monitoring.
- Re-run this research within 30 days if acting on competitive or governance assumptions — the standards surface is moving quickly.

