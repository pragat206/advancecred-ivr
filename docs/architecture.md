# Enterprise AI-Powered IVR Architecture (FastAPI + Twilio)

## 1) Core Product Modules
- **Identity & Access (RBAC):** Admin, Human Agent, AI Agent service-accounts.
- **Lead Management:** Bulk import, deduplication, assignment rules (human vs AI pool), lifecycle statuses.
- **Call Orchestration:** Twilio telephony abstraction for outbound, inbound, conference bridge, and warm transfer.
- **Conversation Intelligence:** Live transcription, disposition extraction, sentiment, objection tagging, conversion scoring.
- **Analytics & Dashboards:** Daily calls, connection %, conversion %, AHT, agent productivity, funnel views.
- **Compliance & Security:** PII encryption, audit logs, retention controls, role-level transcript visibility.

## 2) Recommended High-Level Architecture
1. **FastAPI API Gateway** (authn/authz, admin APIs, agent APIs, webhook ingestion).
2. **Task Workers (Celery + Redis)** for bulk import, async dial jobs, transcript post-processing.
3. **PostgreSQL** for transactional entities (users, leads, calls, assignments, outcomes).
4. **Object Storage (S3/GCS compatible)** for call recordings and large transcript artifacts.
5. **Twilio Voice** for PSTN call routing, number provisioning, and transfer mechanics.
6. **AI Runtime Service** for STT/TTS/LLM loop and policy enforcement.
7. **BI/Observability Layer** (Metabase/Grafana + OpenTelemetry + structured logs).

## 3) AI Voice Agent Design
- **Realtime Loop:** Twilio Media Streams -> STT -> LLM policy engine -> TTS -> Twilio stream.
- **Concurrency:** One orchestrator worker can manage multiple calls via async event loops; horizontally auto-scale by queue depth.
- **Policy Controls:** Admin-configurable goals, forbidden claims, language, escalation criteria, transfer triggers.
- **Human Transfer:** Query real-time availability service, reserve target agent, then warm-transfer via conference bridge.
- **Outcome Capture:** Extract lead intent, objections, budget/timeline, callback window, and final disposition.

## 4) India-Fit Model Guidance (Cost vs Quality)
- **OpenAI path (good default):** `gpt-4o-mini-transcribe` + `gpt-4o-mini-tts` + policy LLM.
- **Budget fallback:**
  - STT: Deepgram Nova-2 or Whisper large-v3 hosted.
  - TTS: ElevenLabs / Azure Neural (Indian English + Hindi quality check).
  - LLM: Mixtral/Llama 3.1 via managed endpoint for lower per-minute cost.
- **Language Strategy:** Start with English + Hindi + Hinglish prompts; evaluate WER by accent/region.

## 5) Security Baseline
- SSO (SAML/OIDC) for enterprise tenants.
- Per-tenant data isolation and scoped JWT claims.
- AES-256 encryption at rest and TLS 1.2+ in transit.
- Immutable audit logs for transcript access and lead edits.
- Consent and DND checks before dialing.

## 6) Suggested Frontend UX Standards
- Clean enterprise UI with square-corner controls and high-contrast typography.
- Minimal dashboard cards (Today calls, Connected, Converted, Avg duration, Revenue proxy).
- Dense but readable tables: lead owner, status, last call, next action, quick comments.
- Role-specific nav: Admin (global), Human Agent (my queue), AI Ops (agent configs).

## 7) Clarifications Needed Before Build
1. Single company deployment or multi-tenant SaaS?
2. Expected concurrent call volume (peak) for AI and human separately?
3. Mandatory CRM integrations (Salesforce/HubSpot/Zoho)?
4. Regulatory expectations: call recording consent wording and retention period?
5. Preferred deployment region/cloud (India data residency constraints)?
