# APS — Agent Passport Standard, v0.1 (Draft)

**Status:** Draft v0.1 · Extracted August 2026 from the shipped Coherence implementation and the Runtime Trust Architecture research line
**Maintainer:** 5thnode Ltd
**Relationship to other documents:** *Runtime Trust Architecture* defines the architecture. **APS defines the Agent Passport.** *AIS* defines runtime interoperability. *Coherence* is the operational reference implementation.

---

## 1. Purpose and scope

APS defines the **Agent Passport**: a portable declaration of an autonomous agent's operational contract, together with the signed claim format through which a verifier attests that it observed that declaration.

The Passport is an **operational contract, not an identity card**. Identity is one field. What the Passport captures is what the agent has declared about how it operates — so that a monitoring system can later compare declared against observed behavior and treat divergence as evidence.

APS deliberately does **not** define:

- how trust decisions are made (receiver policy — Runtime Trust Architecture),
- how fleets are verified collectively (Fleet Integrity — an implementation concern of engines such as Coherence),
- runtime interoperability rules (AIS),
- any universal trust score (explicitly rejected across the document family).

## 2. The Passport declaration

The canonical declaration is five fields:

```json
{
  "identity":  "string  — who or what is acting (required)",
  "operator":  "string  — who runs the agent day to day (required)",
  "authority": "string  — what the agent is authorized to decide or do (default: \"\")",
  "scope":     ["string — canonical reads and writes the agent declares (default: [])"],
  "refusals":  ["string — what the agent declares it will not do (default: [])"]
}
```

Normalization rules:

- `identity` and `operator` are required, non-empty strings.
- `scope` and `refusals` are sorted arrays; comparison of two declarations is order-insensitive.
- An absent field means **undeclared**, never "none". A verifier records undeclared material as UNKNOWN; it never manufactures certainty.

The declaration is intentionally small. Larger claim families (mission, limitations, control authority, environment attestations) are Runtime Trust Primitives that may be attached alongside the Passport; APS does not absorb them, it composes with them additively.

## 3. The signed Passport claim

A verifier that has observed a declaration may issue a signed claim:

```json
{
  "alg": "Ed25519",
  "claims": {
    "v": 1,
    "kind": "coherence_passport",
    "agent_id": "…",
    "tier": "sandboxed | operator | vouched",
    "passport": { "identity": "…", "operator": "…", "authority": "…", "scope": [], "refusals": [] },
    "issued_at": "ISO-8601",
    "expires_at": "ISO-8601",
    "nonce": "…"
  },
  "signature_b64": "…",
  "signer_public_key_b64": "…"
}
```

Semantics — these are the load-bearing rules:

1. **A claim attests observation, not virtue.** It means: *this verifier observed this declaration for this agent at this time.* It is not self-sovereign identity, not a structural-coherence result, and not a license for future action.
2. **Every served field lives inside the signature.** The signature covers the canonical JSON of `claims`; nothing outside it may be trusted.
3. **Expiry is honest.** Claims carry `expires_at` (reference implementation: 30 days for sandbox tier). An expired claim proves nothing current; verification rejects it (the reference implementation returns 403, not 401 — the credential is understood, it is simply no longer valid).
4. **Renewal preserves lineage.** Renewal re-observes the supplied declaration and preserves identity and drift baseline; a bounded grace window after expiry may permit renewal without re-enrollment.
5. **Tiers ride inside the claim.** Trust tier (e.g. `sandboxed` for self-registered agents) is a signed claim field, never an out-of-band assumption. Additional attestations extend additively; they never mutate the base claim.

## 4. Discovery

A Passport is discoverable at a well-known location on the agent's (or its operator's) origin:

```
GET /.well-known/aps-passport.json
```

- The document at that URL is the declaration of §2 (optionally accompanied by a signed claim of §3).
- A discovery client probes `aps-passport.json` first, then may fall back to other machine-readable descriptions (e.g. an A2A `agent-card.json`), classifying documents by shape: an APS document requires `identity`; malformed or unreachable documents are surfaced as failures, never inferred around.
- Verifiers publish their own signing material and endpoint map at their service's well-known manifest (reference: `/.well-known/agent-service.json`, including the Ed25519 public key, claim `kind`, expiry and renewal semantics).

Discovery is **read-only, bounded, and evidence-preserving**: HTTPS only, size- and time-capped, with private-address protection. What discovery finds is recorded as DECLARED or UNKNOWN — a 50% coverage result is honest and useful.

## 5. Passport lifecycle

```
Operator supplies Agent URL
  → Discover (aps-passport.json, then agent card)
  → Discover fleet (topology, overlap edges, if declared)
  → Construct Passport (declaration assembled from discovered material)
  → Coverage scan (each Runtime Trust primitive: declared / not_disclosed / unknown)
  → Operator completes missing declarations (human review; nothing fabricated)
  → Passport established (enrollment + activation; single-use activation token
     exchanged for the agent's credential and signed claim)
  → Operational assurance enabled (scheduled monitoring against the baseline)
```

On establishment, the declaration is snapshotted twice: as the **baseline** (what was declared) and as the initial **observed** state. From that point forward the Passport is a living contract:

- **Drift** is any divergence between baseline and observed declaration or behavior. Drift classes are deterministic (identity/operator change, scope or refusal change, behavior outside declared scope, stale observation). Drift is **not automatically malicious**: it produces evidence for human review.
- **Revision approval** is the only path that moves observed → baseline, and it is an explicit operator action (compare-and-swap protected, recorded as a signed lifecycle event). There is no automatic approval.
- **History** accumulates as a hash-linked, Ed25519-signed, append-only event chain: registration → vouches → renewals → drift incidents → revision approvals. Chain breaks are reported, never silently repaired.

## 6. Conformance

An implementation conforms to APS v0.1 if it:

1. serves or consumes the §2 declaration with the stated normalization and UNKNOWN semantics;
2. issues or verifies §3 claims with full-field signature coverage and honest expiry;
3. performs §4 discovery read-only and shape-classified, without inference on failure;
4. treats the §5 lifecycle rules as normative: baseline/observed separation, human-gated revision approval, and append-only reported-not-repaired history.

Anything beyond this — coverage scoring detail, drift scheduling, fleet-level verification, certificates — is implementation territory and belongs to the implementing system's own documentation.

---

*APS is maintained openly. Implementations, including Coherence, consume the standard as customers; no product owns it.*
