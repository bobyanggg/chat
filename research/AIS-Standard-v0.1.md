# Agentic Identity & Security Standard
  ## AIS v0.1 — Full Specification

  ---

  | | |
  |---|---|
  | **Version** | 0.1 |
  | **Status** | Living Standard |
  | **Issuer** | 5thnode Ltd |
  | **Published** | February 27, 2026 |
  | **Total Requirements** | 23 |
  | **Registry** | https://5thnode.com/standards/ais |
  | **API** | https://5thnode.com/api/ais/requirements |
  | **Contact** | tom@5thnode.com |

  ---

  ## Introduction

  The Agentic Identity & Security (AIS) Standard defines security requirements for autonomous agents operating in Web3 and crypto environments. As AI agents gain the ability to execute financial transactions, interact with smart contracts, and operate with increasing autonomy, the absence of a structured security framework creates systemic risk.

  AIS establishes 23 requirements across 7 categories, covering the full agent lifecycle: from principal identity and credential integrity, through capability governance and behavioral standards, to environmental safety and governance controls.

  AIS is a **living standard** — requirements are maintained and extended through community proposals at https://5thnode.com/standards/ais.

  ---

  ## Severity Scale

  | Level | Meaning |
  |-------|---------|
  | 🔴 Critical | Must be implemented before any consequential agent deployment |
  | 🟠 High | Required for production environments |
  | 🟡 Medium | Strongly recommended; required at higher trust tiers |
  | 🟢 Low | Best practice; apply where feasible |

  ---

  ## Summary of All 23 Requirements

  | Code | Name | Severity | Category |
  |------|------|----------|----------|
  | **AIS-001** | Principal Identity Verification | 🔴 Critical | Principal & Authorization |
| **AIS-002** | Tiered Authorization Model | 🔴 Critical | Principal & Authorization |
| **AIS-003** | Sanctions & Exclusion Screening | 🔴 Critical | Principal & Authorization |
| **AIS-004** | Agent Identity Anchor | 🔴 Critical | Credential Integrity |
| **AIS-005** | Tamper-Evident Credentials | 🔴 Critical | Credential Integrity |
| **AIS-006** | Replay & Session Hijacking Prevention | 🟠 High | Credential Integrity |
| **AIS-007** | Credential Revocation | 🔴 Critical | Credential Integrity |
| **AIS-008** | Prompt Injection Defense | 🔴 Critical | Instruction Integrity |
| **AIS-009** | Context Poisoning Resistance | 🟠 High | Instruction Integrity |
| **AIS-010** | Credential Leakage Prevention | 🟠 High | Instruction Integrity |
| **AIS-011** | Explicit Capability Declaration | 🔴 Critical | Capability Governance |
| **AIS-012** | Compute Budget Enforcement | 🟠 High | Capability Governance |
| **AIS-013** | Policy Commitment & Drift Detection | 🟠 High | Capability Governance |
| **AIS-014** | Behavioral History Record | 🟡 Medium | Behavioral & Reputation |
| **AIS-015** | Failure Behavior Standards | 🟠 High | Behavioral & Reputation |
| **AIS-016** | Data Feed Integrity | 🔴 Critical | Environmental Security |
| **AIS-017** | Execution Environment Attestation | 🟡 Medium | Environmental Security |
| **AIS-018** | Cascading Failure Prevention | 🟠 High | Environmental Security |
| **AIS-019** | Complete Audit Trail | 🔴 Critical | Governance & Control |
| **AIS-020** | Emergency Halt & Recovery | 🔴 Critical | Governance & Control |
| **AIS-021** | Multi-Signature Governance for High-Stakes Agents | 🟠 High | Governance & Control |
| **AIS-022** | Provenance Chain Integrity | 🟠 High | Governance & Control |
| **AIS-023** | Pre-Execution Verification Proof | 🔴 Critical | Governance & Control |

  ---

  ---

# Principal & Authorization

*Requirements ensuring every agent is traceable to a verified, screened human or organizational principal with appropriately tiered access rights.*

**3 requirements** — 3 Critical

---

## AIS-001 — Principal Identity Verification

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Every agent must be traceable to a verified human or organizational principal. The principal's identity must be confirmed before the agent is permitted to take consequential actions.

### Threats Addressed

- Bad actor deploying agents to manipulate or attack systems
- Sybil attacks using many agents from unverified principals
- Sanctioned entity accessing regulated environments via agent proxies

### Verification Methods

- KYC verification via approved identity provider
- Sanctions screening against OFAC SDN, UN, and EU consolidated lists
- Principal signature required on agent manifest at instantiation
- Verification tier recorded in on-chain registry

### Implementation Notes

Use tiered verification proportional to stake level. Low-stakes participation requires only wallet + email (Tier 1). High-stakes or institutional access requires full KYC with liveness detection (Tier 3-4).

---

## AIS-002 — Tiered Authorization Model

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 👥 Principal-Level

### Definition

Agent capabilities and stake access must be gated by the principal's verified identity tier. Higher-consequence actions require deeper principal verification.

### Threats Addressed

- Privilege escalation through weak identity assertions
- High-value manipulation by unverified principals
- Regulatory exposure from unverified high-stakes participants

### Verification Methods

- Stake limits enforced per tier at Arena entry
- Capability set checked against principal tier on every manifest validation
- Tier upgrade requires re-verification through KYC partner

### Implementation Notes

Tier 0 (observer): wallet only. Tier 1 (light participant): email + wallet. Tier 2 (competitor): KYC Lite. Tier 3 (operator): full KYC + AML. Tier 4 (league operator): organizational KYC + AML.

---

## AIS-003 — Sanctions & Exclusion Screening

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 👥 Principal-Level

### Definition

Principal identities and associated wallets must be screened against active sanctions lists before registration and at the start of each new activity period.

### Threats Addressed

- Sanctioned entities accessing financial activity via agent proxies
- Regulatory violations from unknowing facilitation of prohibited actors
- Reputational risk from association with bad actors

### Verification Methods

- Automated screening against OFAC SDN, UN, EU consolidated lists
- Re-screening at season registration and major stake events
- Wallet address screening via Chainalysis KYT or TRM Labs
- Custom platform exclusion list for prior violations

### Implementation Notes

Screening via partner API. Do not store screening results — only the pass/fail status and timestamp.

---

# Credential Integrity

*Requirements ensuring agent credentials are cryptographically anchored, tamper-evident, replay-resistant, and revocable.*

**4 requirements** — 3 Critical, 1 High

---

## AIS-004 — Agent Identity Anchor

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

At instantiation, every agent must commit a signed manifest to the AIS on-chain registry establishing identity anchor: a cryptographic binding between the agent's keypair, its principal, its declared capabilities, and its initial policy state.

### Threats Addressed

- Agent impersonation — fake agents claiming to be legitimate ones
- Unauthorized agent deployment by compromised or rogue principals
- Identity disputes with no cryptographic ground truth

### Verification Methods

- Manifest present in AIS Registry and queryable by any counterparty
- Both agent and principal signatures valid against registered public keys
- Manifest fields complete: agent_id, principal_id, principal_tier, capability_set, policy_hash, model_hash, context_seed_hash, deployment_time

### Implementation Notes

Near-term: Ed25519 keypairs with on-chain manifest storage. Medium-term: upgrade to ZK proofs so agents can prove manifest properties without revealing contents.

---

## AIS-005 — Tamper-Evident Credentials

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Agent credentials must be structured so that any modification after instantiation is immediately detectable. A modified agent must fail credential verification.

### Threats Addressed

- Post-deployment agent modification by malicious principals
- Credential compromise via key theft enabling agent replacement
- Silent behavioral modification that bypasses identity checks

### Verification Methods

- Current agent state hash verifiable against manifest's policy_hash and model_hash
- Any deviation from committed hashes triggers credential invalidation
- Model version hash re-verified at season registration boundaries

### Implementation Notes

Store model_hash and policy_hash at instantiation. Re-hash and verify at each Arena entry.

---

## AIS-006 — Replay & Session Hijacking Prevention

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Every signed agent action must be scoped to prevent reuse. Captured signatures from previous sessions must be cryptographically invalid in new contexts.

### Threats Addressed

- Replay attacks using captured signatures from previous sessions
- Session hijacking via intercepted ephemeral credentials
- Cross-match signature reuse attacks

### Verification Methods

- Every signed action includes: nonce, current block hash, match ID, gate ID, expiry timestamp
- Verifier rejects any action where nonce has been seen before
- Actions expire after match window closes

### Implementation Notes

Maintain a nonce registry per agent. Nonces are cheap to store and check.

---

## AIS-007 — Credential Revocation

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Principals must be able to revoke agent credentials at any time. Revoked agents must be immediately unable to enter new commitments.

### Threats Addressed

- Compromised agents continuing to act after breach discovery
- No kill switch for autonomous agents causing harm
- Delayed human intervention in runaway agent behavior

### Verification Methods

- Revocation status queryable in real-time from AIS Registry
- Revocation timestamp recorded on-chain and immutable
- Principal signature required to initiate revocation

### Implementation Notes

Revocation should take effect within one block confirmation. Implement emergency revocation path for platform administrators.

---

# Instruction Integrity

*Requirements protecting agent decision-making from injection, poisoning, and credential leakage.*

**3 requirements** — 1 Critical, 2 High

---

## AIS-008 — Prompt Injection Defense

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Agents must detect and halt on unauthorized instruction injection. When a foreign instruction is inserted into an agent's context, the agent must refuse to execute and emit a verifiable alert.

### Threats Addressed

- Prompt injection attacks via malicious inputs
- Adversarial prompt crafting that alters agent behavior
- Third-party content hijacking agent decision-making

### Verification Methods

- Context integrity proof present at each decision checkpoint
- Unauthorized delta in context hash triggers halt and alert
- Post-match audit can replay full context chain with proof verification

### Implementation Notes

At each decision step, hash the full context window. Compare the delta to expected authorized inputs. Any unauthorized delta is flagged.

---

## AIS-009 — Context Poisoning Resistance

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Agents must validate the integrity of background data and environmental context. Manipulated telemetry, false market data, or spoofed state must be detectable.

### Threats Addressed

- Oracle/data feed manipulation causing incorrect agent decisions
- Sensor and telemetry spoofing
- False state fed to gain competitive advantage

### Verification Methods

- All environmental inputs signed by certified data source
- Data source whitelist enforced
- Anomaly detection flags statistically implausible inputs

### Implementation Notes

Maintain a whitelist of approved data sources. Require all data feeds to be signed by the source's registered keypair.

---

## AIS-010 — Credential Leakage Prevention

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Agent secrets — private keys, API credentials, authentication tokens — must never appear in reasoning context, logs, tool outputs, or any observable surface.

### Threats Addressed

- Credential leakage via prompt engineering contexts
- Secrets embedded in logs or tool outputs
- Key exposure through agent reasoning traces

### Verification Methods

- Static analysis of agent context for credential patterns
- Runtime scanning of context window for known secret patterns
- Secrets never stored in agent memory — always retrieved from secure vault at use time

### Implementation Notes

Implement a secrets scanner as part of the context integrity proof generation. Use a secrets vault for runtime credential retrieval.

---

# Capability Governance

*Requirements bounding agent capabilities to declared, minimal, verifiable scopes with enforced compute and policy constraints.*

**3 requirements** — 1 Critical, 2 High

---

## AIS-011 — Explicit Capability Declaration

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Every agent must declare a minimal, explicit capability set at instantiation. Broad or undeclared access is prohibited.

### Threats Addressed

- Over-privileged agents with excessive blast radius
- Unauthorized external calls
- Cross-protocol dependency exploitation

### Verification Methods

- Capability set present and signed in agent manifest
- Out-of-bounds action attempts logged and flagged
- Capability set cannot be changed without re-issuance of signed manifest

### Implementation Notes

Capability set must specify: max_stake_per_match, allowed_arena_types, allowed_augmentations, external_calls whitelist, wallet_ops, duration_limit, memory_limit.

---

## AIS-012 — Compute Budget Enforcement

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Agent compute resources must be bounded and enforced. All agents in a match must operate under identical, verified resource constraints.

### Threats Addressed

- Compute dominance undermining skill-based competition
- Resource exhaustion attacks via runaway agent loops
- Timing attacks using superior compute

### Verification Methods

- Compute budget set per Arena type and enforced by verifier
- Step counter enforced — agent halts if step limit reached
- Duration limit enforced by match clock

### Implementation Notes

Treat compute like weight classes in sport — a fairness constraint. Enforce via time limits and step counters.

---

## AIS-013 — Policy Commitment & Drift Detection

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

An agent's operating policy must be committed at instantiation and verified to remain unchanged. Policy drift must be detectable.

### Threats Addressed

- Model drift from baseline behavior over time
- Feedback loop exploitation by continuously learning agents
- Unpredictable reasoning divergence

### Verification Methods

- Policy hash committed in manifest and re-verified at each season boundary
- Behavioral metrics compared against declared policy type
- Re-verification required after any model update

### Implementation Notes

Policy hash covers declared operating parameters — not model weights. Include: optimization objective, risk tolerance class, prohibited action types.

---

# Behavioral & Reputation

*Requirements establishing verifiable behavioral history and predictable failure standards.*

**2 requirements** — 1 High, 1 Medium

---

## AIS-014 — Behavioral History Record

> 🟡 **Severity: Medium** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Every agent must accumulate a verifiable behavioral history through its Spectacle Profile. Agents with no behavioral history are treated as unknowns.

### Threats Addressed

- Unknown agents gaining high-stakes access
- Sybil attacks via fresh agents that discard history
- Counterparty risk from agents with undisclosed failure modes

### Verification Methods

- Spectacle Profile linked to agent identity via AIS Registry
- Match history and completion rate publicly queryable
- History immutable — cannot be deleted without full credential re-issuance

### Implementation Notes

Behavioral history includes: match completion rate, challenge acceptance patterns, failure behavior, policy adherence events.

---

## AIS-015 — Failure Behavior Standards

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

When an agent fails, its failure behavior must be clean and predictable. Stakes must resolve correctly even when the agent fails.

### Threats Addressed

- Funds locked in unresolvable escrow
- Counterparty left in undefined state
- Cascading failures from hung agent states

### Verification Methods

- Failure mode documentation in agent manifest
- Escrow contract includes timeout resolution
- Failure events recorded in Spectacle Profile

### Implementation Notes

Require every agent to declare its failure mode at registration. Escrow contracts must include automatic timeout resolution.

---

# Environmental Security

*Requirements ensuring agent data inputs, execution environments, and external interactions are safe and bounded.*

**3 requirements** — 1 Critical, 1 High, 1 Medium

---

## AIS-016 — Data Feed Integrity

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

External data sources feeding agent decision-making must be signed by verified providers and checked before use.

### Threats Addressed

- Oracle/data feed manipulation
- Automated liquidations triggered by manipulated price feeds
- Governance bots voting on malicious proposals

### Verification Methods

- All data sources on certified provider list
- Data signed by provider keypair and verified
- Statistical anomaly check against recent baseline

### Implementation Notes

Publish a certified data provider list per Arena type. Implement a simple anomaly detector for data deviations.

---

## AIS-017 — Execution Environment Attestation

> 🟡 **Severity: Medium** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Where possible, agents should provide proof that they ran in an authorized, unmodified execution environment.

### Threats Addressed

- Infrastructure-level compromise bypassing all software security
- Hidden environmental advantages
- Side-channel attacks via shared infrastructure

### Verification Methods

- TEE attestation report verifiable by counterparties
- Network isolation enforced
- Time integrity verified via blockchain timestamps

### Implementation Notes

Full TEE attestation is Phase 3. Near-term: checkpoint system's signed state emissions make manipulations detectable.

---

## AIS-018 — Cascading Failure Prevention

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Agent actions must be scoped to prevent triggering unintended cascades in connected systems.

### Threats Addressed

- Cascading failures across connected protocols
- Self-executing threshold triggers creating chain reactions
- Cross-protocol dependencies amplifying failures

### Verification Methods

- External call whitelist limits what can be triggered
- Gate-sequential execution prevents simultaneous multi-system commitment
- Circuit breakers at Arena level halt further action on anomaly

### Implementation Notes

Require agents to declare all external protocols. Block undeclared cross-protocol calls. Implement action rate limiter per match window.

---

# Governance & Control

*Requirements establishing audit trails, emergency controls, multi-signature governance, provenance integrity, and pre-execution verification.*

**5 requirements** — 3 Critical, 2 High

---

## AIS-019 — Complete Audit Trail

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Every consequential agent action must be recorded in a complete, immutable, human-readable audit trail.

### Threats Addressed

- No audit trail for agent decisions under dispute
- Opaque decision logic with no debugging path
- Regulatory requirement for decision explainability

### Verification Methods

- Checkpoint emitted at every gate transition
- Context integrity proof attached to each checkpoint
- Full decision replay available to authorized parties

### Implementation Notes

Include: timestamp, agent state hash, action taken, resources consumed, gate outcome, and context proof reference. Retain for minimum two full seasons.

---

## AIS-020 — Emergency Halt & Recovery

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Every agent deployment must include a defined emergency halt mechanism operable by the principal, the platform, or both.

### Threats Addressed

- No kill switch for runaway autonomous agents
- Delayed human intervention enabling continued harm
- Inability to stop compromised agents mid-match

### Verification Methods

- Halt mechanism defined and tested before deployment
- Platform-level emergency halt available
- Halt takes effect within one block confirmation

### Implementation Notes

Two halt levels: (1) Principal halt — agent stops new commitments but completes current match. (2) Platform emergency halt — immediate cessation.

---

## AIS-021 — Multi-Signature Governance for High-Stakes Agents

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Agents operating at Tier 3 or above must require multi-signature authorization for registration, capability changes, and high-value action approvals.

### Threats Addressed

- Single key compromise giving full control of high-value agent
- Rogue insider deploying high-stakes agent without oversight
- Inadequate governance for institutional-scale autonomous activity

### Verification Methods

- Tier 3+ manifests require M-of-N principal signatures
- Capability changes require full multi-sig re-issuance
- High-value action thresholds trigger approval requirement

### Implementation Notes

Require 2-of-3 multi-sig for Tier 3, 3-of-5 for Tier 4. Use Gnosis Safe or equivalent as the principal signing entity.

---

## AIS-022 — Provenance Chain Integrity

> 🟠 **Severity: High** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

The complete chain from agent action back to authorizing human or organization must be cryptographically traceable. Every delegation must be recorded.

### Threats Addressed

- Authority laundering through deep agent delegation chains
- Regulatory accountability gaps in multi-agent systems
- Bad actor hiding behind legitimate-looking intermediate agents

### Verification Methods

- Principal chain recorded in manifest with each delegation step signed
- Maximum delegation depth enforced (recommended: 3 levels)
- Terminal principal must be verified human or organization

### Implementation Notes

Agent-to-agent delegation is permitted but bounded. Maximum depth of 3 to prevent accountability laundering.

---

## AIS-023 — Pre-Execution Verification Proof

> 🔴 **Severity: Critical** &nbsp;|&nbsp; 🤖 Agent-Specific

### Definition

Before executing a consequential blockchain transaction, an agent must obtain a verifiable proof that its identity, credentials, capabilities, and execution context satisfy the AIS Standard. This proof confirms that the transaction passed security verification prior to execution.

### Threats Addressed

- Autonomous agents executing malicious or unsafe transactions
- Compromised agents acting outside declared capability bounds
- Unverifiable transaction origin in agent-driven systems
- Lack of pre-execution validation in autonomous financial activity

### Verification Methods

- Agent identity anchor verified against AIS registry
- Credential integrity verified (policy_hash, model_hash)
- Capability set permits intended action
- Execution environment attested
- Transaction simulation completed
- Risk policy evaluation passed

### Implementation Notes

Proofs may be implemented using lightweight signatures or zero-knowledge proofs. Proofs should be inexpensive to generate and verify. Proof may optionally be attached to the transaction metadata. Protocols may choose to require proof verification before accepting transactions. Proof structure must include: agent_id, manifest_hash, verification_timestamp, verification_nonce, transaction_hash, policy_result, synapse_signature.

---

# Appendix

## Community Proposals

The AIS Standard accepts community proposals for new requirements or amendments to existing ones. Proposals are reviewed by the 5thnode standards team and may be incorporated into future versions.

To submit a proposal, visit https://5thnode.com/standards/ais and use the proposal submission form (engagement portal authentication required).

## Machine-Readable Format

All 23 requirements are available as a JSON array at:

```
https://5thnode.com/api/ais/requirements
```

The AIS registry well-known endpoint is available at:

```
https://5thnode.com/.well-known/ais-registry.json
```

## Verification Services

| Service | Type | Endpoint |
|---------|------|----------|
| Greenlight | Security Scan | https://greenlightagent.com/v1/scans |

---

*AIS Standard v0.1 — Published by 5thnode Ltd — https://5thnode.com*
