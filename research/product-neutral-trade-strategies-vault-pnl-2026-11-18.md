---
topic: "Neutral.trade Strategies — mid-deposit vault PnL accounting"
type: "product"
goals: "Explain how Neutral Strategies vaults attribute profit/loss to a depositor who joins mid-period; verify or refute the formula profit = (exit_vault_balance - entry_vault_balance) * (my_deposit / total_deposit); document the actual share/NAV formula, fees, and mid-deposit edge cases."
date: "2026-11-18"
methodology: "Parallel web research via sub-agents. Citations inline per references/citations.md. Confidence levels: High / Medium / Low. Primary focus on official Neutral docs, app UI copy, contracts/SDK if public, and comparable DeFi vault share patterns when Neutral docs are thin."
---

# Research Report — Neutral.trade Strategies Vault PnL (Mid-Deposit)

> **Type:** product (+ technical vault accounting) | **Date:** 2026-11-18 | **Constraints:** Focus on https://www.neutral.trade/strategies; answer the user's proposed PnL formula; English/Chinese sources OK
>
> **Assumptions:** type=product with technical deep-dive on deposit share accounting; scope=Neutral Strategies vaults (not the broader Neutral product suite unless needed for context); horizon=docs and on-chain behavior as of 2026-11-18; goals=(1) product overview of Strategies, (2) exact depositor PnL / share math for mid-period joins, (3) fees/lockups that change realized PnL, (4) confidence-flagged gaps if contracts/docs do not disclose the formula.
>
> **Goals:**
> - Describe what Neutral Strategies vaults are and how deposits/withdrawals work
> - Verify whether `profit = (exit_vault_balance - entry_vault_balance) * (my_deposit / total_deposit)` is correct
> - If not, state the actual formula (shares, NAV, PPS, high-water mark, etc.) with sources
> - Note fees, lockups, and mid-deposit dilution effects

---

## Product Overview

### Target Audience

Neutral Trade positions Neutral Strategies as on-chain access to hedge-fund-style systematic strategies for capital allocators who historically faced high minimums and slow redemptions. Official docs state the thesis as “Hedge fund strategies. On-chain. For everyone,” and contrast traditional access (often large minimums, venue-by-venue onboarding, monthly/quarterly redemptions) with a wallet deposit into an audited vault and weekly or twice-weekly redemptions on most vaults. Most strategy vaults start at 100 USDC. [Neutral Trade Introduction](https://docs.neutral.trade/) (accessed 2026-11-18, confidence: High) — **Primary**.

Docs split intent by product surface: start with Autopilot for one managed position, or select individual strategies to build a mix. Autopilot is framed for users who do not want to pick and rebalance strategies; RWA vaults target longer-horizon allocators with higher minimums (50,000 USDC for Multi-Asset Volatility Arbitrage); NT Earn is the conservative no-fee USDC lending optimizer. The platform is also two-sided: curators raise on-chain capital, and builders can earn a share of management fees. Products are not intended for users in the United States, Mainland China, Hong Kong, sanctioned, or other restricted jurisdictions. [Neutral Autopilot](https://docs.neutral.trade/for-capital-allocators/neutral-autopilot); [Regional Availability](https://docs.neutral.trade/legal/regional-availability); [Strategies page](https://www.neutral.trade/strategies) (accessed 2026-11-18, confidence: High) — **Primary**.

### Feature Surface

On [https://www.neutral.trade/strategies](https://www.neutral.trade/strategies), users see Neutral Autopilot (auto-compounded, USDC-denominated) plus curated strategy tables with trailing APY, TVL, redemption, and network/asset. Availability is listed for Solana, Ethereum, and Monad. The core loop is: connect wallet → submit deposit request → receive vault shares when the batch processes → hold while share price tracks strategy NAV → request withdrawal or switch vaults on the published schedule → receive USDC as shares are burned. Deposit requests cannot be cancelled; while a deposit is pending you may add more but cannot withdraw until it processes. After processing, “you receive vault shares representing your proportional ownership of the vault’s total assets,” and “Your share price moves with the strategy’s performance from this point forward.” [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); [Strategies](https://www.neutral.trade/strategies) (accessed 2026-11-18, confidence: High) — **Primary**.

Autopilot on Solana: deposits daily; redemptions weekly; 1% management fee (VIP can reduce), no Autopilot performance fee, 0.3% withdrawal fee, 100 USDC minimum. Individual strategy vaults generally share the 1% management fee but add performance fees (often 20–35%) and sit on once-weekly or twice-weekly redemption schedules. Ethereum/Monad Autopilot paths use Accountable Vaults with terms shown in-app; docs lag the live Monad surface. [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period); [Neutral Autopilot](https://docs.neutral.trade/for-capital-allocators/neutral-autopilot) (accessed 2026-11-18, confidence: High) — **Primary**.

### Pricing and Packaging

Neutral Strategy Vaults charge up to three on-chain fees: management, performance (where applicable), and withdrawal, shown in each vault’s Details view. On Solana vaults as of documented 12 October 2026 settings, base management fee is 1% annual (charged in vault shares over elapsed time), except NT Earn (no fees). Performance fees, when present, range 20%–35% of new profit above a personal high-water mark. Withdrawal fees are typically 0.3% (0.5% on CTA - Systematic Alpha). Minimum deposits are generally 100 USDC. VIP discounts on Autopilot can cut management fee to 0.90% / 0.80% / 0.70%; performance fees are not discounted. [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (accessed 2026-11-18, confidence: High) — **Primary**.

From 12 October 2026, most vaults follow fixed weekly redemption schedules with cutoffs at 00:00 UTC. Until settlement, capital stays exposed to share-price moves; the value shown at request time is an estimate. [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period); [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work) (accessed 2026-11-18, confidence: High) — **Primary**.

FAQ copy sometimes simplifies to “two fees” and “no lock,” while primary Fees/How They Work docs list three fees and note some vaults/exceptions with different lock or redemption terms. Prefer Fees + How They Work for accounting; treat FAQ as simplified marketing. [FAQ](https://www.neutral.trade/faq) vs [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (accessed 2026-11-18).

### Technology and Architecture

Neutral Strategy Vaults are share-accounted pooled vehicles. A deposit is requested, then batched/netted by a keeper and processed into vault shares at the then-current NAV / price per share (PPS). Shares record proportional ownership; value thereafter tracks PPS. Daily NAV combines on-chain assets with externally reported venue equity via a permissioned keeper. Price updates are bounded, rate-limited, and applied while deposits/withdrawals are paused. Measured vault yield is PPS change: `return = (PPS_end - PPS_start) / PPS_start`. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); [Vault Protections](https://docs.neutral.trade/neutral-strategy-vaults/vault-protections); [Trailing APY and APR Calculations](https://docs.neutral.trade/additional-info/apy-and-apr-calculations) (accessed 2026-11-18, confidence: High) — **Primary**.

### Integrations and Ecosystem

Integrator surface is the v2 REST API at `https://api.neutral.trade`, with OpenAPI at `https://api.neutral.trade/openapi.json`. Key reads for PnL math: share-price (`GET /v2/vault/{id}/share-price`), daily snapshots (`closePps`, `closeTotalShares`, `closeTvlToken`), user balance (`shares`, `pps`, `value`, `netDeposits`, `hwmPerShare`), interest-earned (method `value-delta-minus-net-flows`), and simulate-deposit/withdraw previews. OpenAPI simulate-deposit example: `amount=100`, fee 25 bps → `netAmount=99.75`, `currentPps=1.2` → `expectedShares=83.125` (= 99.75 / 1.2). Spec states fee/share calcs use exact integer program semantics; final shares can differ if PPS moves before netting. [Vault & User Data](https://docs.neutral.trade/developers/vault-and-user-data); [API Conventions](https://docs.neutral.trade/developers/api-conventions); [OpenAPI](https://api.neutral.trade/openapi.json) (accessed 2026-11-18, confidence: High) — **Primary**.

## Vault Deposit / PnL Accounting (Primary Question)

### User-Proposed Formula Check

**Verdict: the proposed formula is not correct.**

The user proposed:

```text
profit = (vault_balance_at_exit - vault_balance_at_entry) * (my_deposit / total_deposit)
```

According to Neutral’s official docs, ownership is vault **shares** whose **price per share (PPS / NAV)** moves with strategy performance from the moment shares are issued forward—not a static fraction of raw vault TVL. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); [Trailing APY and APR Calculations](https://docs.neutral.trade/additional-info/apy-and-apr-calculations) (accessed 2026-11-18, confidence: High) — **Primary**.

Why the proposed formula fails:

1. **Wrong numerator.** Vault balance (TVL) rises and falls with other users’ deposits and withdrawals, not only with strategy P&L. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); [Vault & User Data](https://docs.neutral.trade/developers/vault-and-user-data) (accessed 2026-11-18, confidence: High).
2. **Wrong ownership fraction.** On-chain claim is `user_shares / total_shares`, which changes whenever anyone mints or burns. `my_deposit / total_deposit` is not the accounting unit. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work) (accessed 2026-11-18, confidence: High).
3. **Wrong time basis.** Mid-deposit shares are priced at entry PPS; prior vault appreciation is already in that PPS and is not owed to the new depositor. Docs: share price moves with performance “from this point forward.” [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work) (accessed 2026-11-18, confidence: High).
4. **Ignores fees.** Deposit fee (if any), management fee in shares, performance fee vs personal HWM, and withdrawal fee all change take-home PnL. [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (accessed 2026-11-18, confidence: High).

### Documented Share / NAV Formula

Neutral does not print one consumer-facing closed-form “profit = …” equation, but the share/PPS model is consistent across How They Work, APY docs, curator infrastructure language (“shares are minted and redeemed at that NAV”), and OpenAPI simulate-deposit. Reconstruction confidence: **High** for gross share math; **Medium** for full fee-cascade integer order without reading program IDL. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); [Trailing APY and APR Calculations](https://docs.neutral.trade/additional-info/apy-and-apr-calculations); [OpenAPI](https://api.neutral.trade/openapi.json) (accessed 2026-11-18).

```text
# Pricing identity
PPS_t ≈ total_assets_t / total_shares_t

# At deposit processing / netting
fee_amount    = deposit_amount * deposit_fee_bps / 10_000   # if deposit fee applies
net_amount    = deposit_amount - fee_amount
shares_minted = net_amount / PPS_entry

# Mark-to-market while held
position_value_t = shares_held_t * PPS_t

# Gross hold P&L (single deposit, no top-ups; before exit fees / ignoring mgmt share burns)
gross_profit ≈ shares_minted * (PPS_exit - PPS_entry)
             = net_amount * (PPS_exit / PPS_entry - 1)

# Neutral API interest-earned method (handles mid-period flows)
earnings = Δ(position_value) − signed_net_flows

# Realized cash on full exit (schematic)
proceeds_net = shares_redeemed * PPS_settlement
               − withdrawal_fee
               − unpaid management / performance fees at settlement
realized_pnl = proceeds_net − cost_basis
```

Vault-level Trailing APR (not individual user PnL) is:

```text
return = (PPS_end - PPS_start) / PPS_start
APR    = return * (365 / days_in_window)
APY    = (1 + APR / 365) ^ 365 - 1
```

[Trailing APY and APR Calculations](https://docs.neutral.trade/additional-info/apy-and-apr-calculations) (accessed 2026-11-18, confidence: High) — **Primary**.

App “Balance” is current value of vault shares after charged fees; “Earnings” is profit after management and performance fees. [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (accessed 2026-11-18, confidence: High).

### Mid-Period Deposit Edge Cases

**Toy example** (0 deposit fee for clarity): vault TVL 1,000,000 USDC at PPS 1.10 → ~909,090.909 shares. User deposits 10,000 mid-way → ~9,090.909 shares. Later PPS = 1.21 (+10%). Correct gross profit = 9,090.909 × 1.21 − 10,000 = **1,000**.

If another user later deposits +500,000 at PPS 1.10 and the same +10% PPS move occurs, TVL exit ≈ 1,661,000. Wrong formula `(1,661,000 − 1,000,000) × (10,000 / 1,000,000) = 6,610` — far above the true 1,000 — because it attributes other capital’s appreciation and confuses flow-driven TVL with P&L. (Illustrative reconstruction from documented share model; confidence: High for qualitative failure mode.)

Other documented edges: pending deposits have no PPS exposure until keeper netting; preview shares can drift if PPS moves before netting; new deposits mint at current NAV so they do not dilute prior holders’ PPS and do not inherit pre-entry gains; a new deposit can adjust the account’s weighted entry basis / HWM per program rules; until redemption settlement the user remains PPS-exposed. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period); [API Conventions](https://docs.neutral.trade/developers/api-conventions) (accessed 2026-11-18, confidence: High).

### Fees, Lockups, and Realized PnL Adjustments

Headline Trailing APY is vault-level PPS history, not your personal path. Docs warn that your own result depends on entry date, personal HWM, and any VIP discount. Management fee continuously reduces share economics (~1%/year base). Performance fee only on new post-fee profit above wallet HWM. Withdrawal fee is a one-time haircut at settlement and is not in the Trailing APY net/gross definition (which references management and performance). Redemption delay keeps PnL open until settlement. [Trailing APY and APR Calculations](https://docs.neutral.trade/additional-info/apy-and-apr-calculations); [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (accessed 2026-11-18, confidence: High).

## User and Market Perception

### Review Summary

Independent public reviews are scarce relative to Neutral’s claimed scale. A thin Oct 2025 r/solana legitimacy thread (Low-tier) shows curiosity more than fee/timing anger. Primary Neutral docs remain the main explanation of deposit batching, fees, and share-price exposure until settlement. Quantstamp’s public audit acknowledged “No Slippage Tolerance for Withdrawals”: pricing at process time, not request time. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); Quantstamp certificate search via research pass (accessed 2026-11-18, confidence: Medium for audit detail) — **Primary/Established**.

### Changelog Highlights (last 12 months)

Jul–Oct 2026 product posts and docs emphasize portfolio P&L rebuilds, Autopilot launch, VIP fee discounts, fixed weekly redemption schedules from 12 Oct 2026, multi-network Autopilot, and additional audits. Messaging treats opaque settlement calendars and fee opacity as friction to remove. [Updated Vault Fees blog](https://www.neutral.trade/blog/updated-vault-fees-nt-points-july-2026); [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (accessed 2026-11-18, confidence: Medium–High).

### Community Health

Community is concentrated on Discord/Telegram/X with support ticketed in Discord. Public Reddit/Trustpilot discourse is thin; Discord internals were not scrapable. Perception of vault mechanics is therefore inferred largely from Primary Neutral docs rather than a thick body of user reviews. (Low confidence on grassroots sentiment.)

## Strategic Signals

### Competitive Positioning

Neutral uses the same share × NAV / PPS mental model as Yearn and ERC-4626: mid-period depositors mint shares at the then-current exchange rate, and subsequent PnL is share-price movement—not a special period-start reset. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); [OpenZeppelin ERC-4626](https://docs.openzeppelin.com/contracts/5.x/erc4626); [Yearn wallet integration](https://docs.yearn.fi/developers/wallet-integration) (accessed 2026-11-18, confidence: High). Neutral-specific twists: keeper-reported external venue NAV with bounded updates while deposits/withdrawals are paused; daily deposit/withdrawal batching; scheduled weekly redemptions with continued PPS exposure until settlement; **per-wallet** high-water mark (vs common vault-level ATH PPS); shares not yet transferable ERC-20 tokens. [Vault Protections](https://docs.neutral.trade/neutral-strategy-vaults/vault-protections); [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period); [API Conventions](https://docs.neutral.trade/developers/api-conventions) (accessed 2026-11-18, confidence: High).

### Adoption Signals

Neutral markets the vault as a substitute for traditional fund subscriptions (low USDC minimums, on-chain share ledgers, weekly redemptions) and sells the same NAV/share stack to curators as shared fund-admin infrastructure. [Introduction](https://docs.neutral.trade/); [Infrastructure for Trading Firms](https://docs.neutral.trade/curators/infrastructure-for-trading-firms) (accessed 2026-11-18, confidence: High).

### Risk Signals

Security docs cite four public Solana vault audits (Halborn, Quantstamp, Offside Labs, Adevar). Quantstamp engaged share-supply / HWM fee accounting and recorded findings that were marked fixed or acknowledged. Residual risk for mid-depositors is less “opaque period PnL math” and more valuation trust (keeper external NAV), pending-deposit lockout until batch processing, non-cancellable requests, and mark-to-market exposure through redemption lag. Non-Solana vaults use separate contracts outside the Solana audit table. [Security](https://docs.neutral.trade/neutral-strategy-vaults/security); [Quantstamp Neutral Trade report](https://certificate.quantstamp.com/full/neutral-trade/52a6403b-648c-4ea6-be5e-c8b525acc9b7/index.html) (accessed 2026-11-18, confidence: High).

## Deep Dive — HWM and Realized PnL Estimation

Docs define HWM as the wallet’s highest **post-fee** position value; a new deposit “can adjust the account’s weighted entry basis according to the vault program rules,” but **no closed-form reweight formula is published**. [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (accessed 2026-11-18, confidence: High for definition; Low for mid-deposit algebra).

SDK `@neutral-trade/sdk` mirrors on-chain fee charge order: management fee shares first from elapsed time, then performance fee shares if PPS > HWM, capped so perf cannot consume shares already taken by management; withdrawal fee applies at redemption. Builder rebate splits charged management fee only and does not raise user cost. (SDK mirror; confidence: Medium–High for Solana ntbundle.)

Practical estimators for a mid-life deposit then full exit:

```text
# Prefer Neutral API semantics
gross_earnings ≈ Δ(position_value) − signed_net_flows

# App "Earnings" while still in vault (after charged mgmt/perf; before withdrawal fee)
earnings ≈ balance − net_deposits   # after unpaid fee estimate if using API net

# Realized cash PnL after all fees
realized_pnl = cash_received_at_settlement − sum(wallet_deposits)
```

Do not use vault Trailing APY as personal PnL. Until settlement, redemption values remain estimates. Exact mid-deposit HWM blend remains a documented gap; Quantstamp test logs are circumstantial evidence of fee crystallization then HWM ≈ current PPS, not a Neutral-authored spec. [Vault & User Data](https://docs.neutral.trade/developers/vault-and-user-data); [Trailing APY and APR Calculations](https://docs.neutral.trade/additional-info/apy-and-apr-calculations) (accessed 2026-11-18).

---

## Key Findings

1. **The user’s proposed formula is wrong.** Neutral attributes ownership via vault **shares** minted at processing-time **PPS/NAV**, not via `(Δ vault balance) × (my deposit / total deposit)`. TVL deltas mix strategy P&L with other users’ flows, so that fraction over- or under-attributes profit. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); [Trailing APY and APR Calculations](https://docs.neutral.trade/additional-info/apy-and-apr-calculations) (accessed 2026-11-18, confidence: High).

2. **Correct gross mental model for a single mid-period deposit:** `shares = net_deposit / PPS_entry`, then `gross_profit ≈ shares × (PPS_exit − PPS_entry)` (equivalently `net_deposit × (PPS_exit/PPS_entry − 1)`). Performance only accrues **from share issue forward**. [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work); OpenAPI `simulate-deposit` example ([OpenAPI](https://api.neutral.trade/openapi.json)) (accessed 2026-11-18, confidence: High).

3. **With deposits/withdrawals mid-hold, use flow-adjusted earnings:** Neutral’s API defines interest earned as `Δ(position_value) − signed_net_flows`. [Vault & User Data](https://docs.neutral.trade/developers/vault-and-user-data); OpenAPI (accessed 2026-11-18, confidence: High).

4. **Realized take-home is lower than gross share PnL** because of management fee (share drag), performance fee above personal HWM on some vaults, and withdrawal fee at settlement; you also stay PPS-exposed until redemption settles. [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (accessed 2026-11-18, confidence: High).

5. **This is standard DeFi vault accounting** (Yearn / ERC-4626 family) with Neutral twists: batched netting, external venue NAV via keeper, weekly redemption schedules, per-wallet HWM, non-transferable shares today. [OpenZeppelin ERC-4626](https://docs.openzeppelin.com/contracts/5.x/erc4626); [Vault Protections](https://docs.neutral.trade/neutral-strategy-vaults/vault-protections) (accessed 2026-11-18, confidence: High).

## Strategic Recommendations

1. **Use share × PPS, not vault-balance share** — When estimating mid-join PnL, record `PPS_entry` (or use `simulate-deposit` / post-process share count) and mark `shares × PPS_now`. Evidence: [How They Work](https://docs.neutral.trade/neutral-strategy-vaults/how-they-work), [APY docs](https://docs.neutral.trade/additional-info/apy-and-apr-calculations).

2. **Treat app Balance / Earnings as the fee-aware truth** — Prefer UI Earnings or API `interest-earned` / `balance − netDeposits` over DIY Trailing APY. Evidence: [Fees](https://docs.neutral.trade/additional-info/fees-+-redemption-period), [Vault & User Data](https://docs.neutral.trade/developers/vault-and-user-data).

3. **Budget for redemption lag** — Request-time value is an estimate; settlement can be days to ~two weeks depending on schedule. Evidence: [Fees + Redemption Period](https://docs.neutral.trade/additional-info/fees-+-redemption-period).

4. **If topping up the same wallet, expect HWM/basis adjustment** — Do not assume a simple average without checking post-deposit `hwmPerShare`; program rules are not fully public. Evidence: [Fees](https://docs.neutral.trade/additional-info/fees-+-redemption-period) (Low confidence on exact algebra).

5. **Read vault Details before deposit** — Fee tables and Autopilot network terms can differ from FAQ/marketing; Details view wins when they conflict. Evidence: [Fees](https://docs.neutral.trade/additional-info/fees-+-redemption-period).

## Risks and Uncertainties

- Data gaps: no single Neutral page prints `shares = net_deposit / PPS` as a formal equation; reconstructed from multiple Primary pages + OpenAPI (still High confidence).
- Mid-deposit weighted entry / HWM update algebra is **not published** (Low confidence on exact reweight).
- Full on-chain fee-cascade integer rounding without IDL/source remains Medium confidence (SDK mirror helps).
- FAQ vs Fees/How They Work conflicts on lock language and Autopilot performance fee.
- Trailing APY net methodology vs wallet-specific HWM is not fully specified for aggregate vault metrics.
- Research snapshot as of 2026-11-18; fee schedules and redemption rules can change—re-verify Details before acting.

## Next Steps

- Optional: call authenticated Neutral API `simulate-deposit` + user `balance`/`interest-earned` on a real vault to validate share mint math live.
- If top-up HWM algebra matters for tax/accounting, ask Neutral support/Discord for program-rule clarification or inspect `ntbundle` IDL/`process_deposit`.
- Decisions this research enables: reject the vault-balance-delta formula; use share×PPS (± fees) for mid-join profit estimates.
- PDF export available on request (Step 6).

---

## Disclaimer

Research reflects a snapshot in time (2026-11-18). Web content and on-chain fee settings change. For volatile topics (fees, redemption, NAV), re-run within 30 days or verify key claims in the vault Details view and docs before depositing. This is not financial advice.
