# Enterprise Okta SSO Platform Overview

## Business challenge

A large organization has multiple internal applications with separate access controls:
- HR portal
- DevOps dashboard
- Finance app
- Analytics portal

Employees must be able to sign in once and access all approved internal applications without repeated authentication.

## Solution

This project models an enterprise identity solution using Okta as the identity provider and OIDC as the primary authentication flow.

Key solution elements:
- Single sign-on for internal web applications
- Centralized authentication using Okta
- Role-based and group-based access policies
- Identity lifecycle governance for onboarding, role changes, and deprovisioning
- Security controls for MFA, session timeout, and token management

## Architecture summary

- Identity provider: Okta
- Protocol: OpenID Connect (OIDC)
- Access model: role-based and group-based policies
- Session management: centralized session and token refresh
- Compliance: audit logging, authentication policy enforcement, and least-privilege access

## Recruiter-friendly value

This repository demonstrates both technical execution and architectural thinking:
- Practical Python code for Okta integration
- Business-driven IAM solution design
- Clear separation between IAM engineering and solution architecture responsibilities
- Focus on enterprise internal application readiness and stakeholder alignment

## File structure

- `app/okta_client.py` — Okta integration helpers
- `app/iam_architect.py` — IAM engineer and solution architect capability modeling
- `app/main.py` — Demo runner with narrative output
- `README.md` — recruiter-facing project overview and usage
- `tests/test_okta_client.py` — test coverage for core integration logic
