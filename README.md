# Enterprise Okta SSO Platform — IAM Solution Architect Demo

This project is a polished proof-of-concept for an enterprise Okta SSO platform, designed to showcase both IAM engineering and solution architecture skills.

It is intended for recruiters and hiring managers who want to see:
- architecture thinking for internal app SSO
- identity lifecycle and access policy design
- Okta OIDC integration workflows
- security, compliance, and enterprise readiness

## Why this project stands out

- Demonstrates a clear business problem: internal employees need one login for HR, DevOps, Finance, and Analytics apps.
- Shows architecture-level decisions: identity provider, access model, authentication flow, and migration planning.
- Highlights IAM engineering capabilities: provisioning, policy design, secure token handling, and audit controls.
- Includes a runnable Python demo and unit test to prove technical execution.

## What it demonstrates

- Enterprise Okta OIDC SSO flow generation
- Token exchange and session management patterns
- Identity lifecycle and role-based access governance
- Solution architecture mapping of business requirements to IAM design
- Compliance-focused security control thinking for internal applications

## Skills showcased

- Okta identity platform design
- OIDC / OAuth2 integration
- IAM policy modeling and least-privilege enforcement
- Solution architecture for enterprise internal apps
- Python implementation and test-driven design

## Project structure

- `app/okta_client.py` — Okta integration helper, authorization URL builder, token exchange, userinfo retrieval
- `app/iam_architect.py` — IAM Engineer and Solution Architect capability modeling, business mapping, and migration planning
- `app/main.py` — Demo runner that prints the enterprise architecture story and Okta workflow
- `tests/test_okta_client.py` — Unit test validating Okta authorization URL generation

## How to run

1. Create a Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the demo:

```bash
python app/main.py
```

3. Run tests:

```bash
pytest
```

## Recruiter summary

This repository is a strong example of a candidate who can design and articulate enterprise IAM solutions with Okta, while also delivering a clean, runnable implementation in Python.
