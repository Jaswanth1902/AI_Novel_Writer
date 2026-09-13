# Security Policy — AI Novel Writer & Engine

## 🛡️ Supported Versions

The following versions of **AI Novel Writer / AI Novel Engine** receive security updates and maintenance:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| < 2.0.0 | :x:                |

---

## 🔒 Security Architecture & Privacy Principles

AI Novel Writer is designed from first principles to be **local-first, privacy-preserving, and air-gapped**:

1. **Zero Cloud Telemetry**: The engine runs 100% locally. No narrative briefs, character dossiers, scene contracts, or manuscript chapters are ever transmitted to third-party telemetry servers.
2. **Private Manuscript Protection**: All generated outputs (`output/chapters/`, `output/pipeline_logs/`, and story databases) are strictly `.gitignore`'d by default to ensure private manuscripts are never accidentally committed to public version control.
3. **Deterministic SQLite Storage**: Narrative state and author craft graphs utilize standard Python `sqlite3` with Write-Ahead Logging (WAL). No arbitrary code execution or unpickling is permitted during state persistence.
4. **Clean Dependency Footprint**: The core engine depends only on verified, audited packages (`pyyaml`, `rich`) without heavy unverified neural wrappers.

---

## 🚨 Reporting a Vulnerability

We take the security and intellectual property privacy of our users seriously. If you discover a security vulnerability or sensitive data leakage risk:

1. **Do NOT open a public GitHub issue.**
2. Send an email directly to the maintainer: **`jaswanthreddy1537@gmail.com`**.
3. Include:
   - A clear description of the vulnerability.
   - Steps or proof-of-concept scripts to reproduce the issue.
   - The potential impact on manuscript privacy, state integrity, or local systems.
4. You will receive an initial response within **48 hours**, followed by status updates as the patch is prepared and verified.

Thank you for helping keep AI Novel Writer safe, private, and dependable for creators everywhere!
