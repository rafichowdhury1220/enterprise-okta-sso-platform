from dataclasses import dataclass
from typing import List, Dict


@dataclass
class IAMEngineer:
    name: str
    primary_focus: str = "Identity lifecycle and access enforcement"

    def design_identity_lifecycle(self) -> str:
        return (
            "Designing lifecycle workflows for user provisioning, deprovisioning, "
            "role-based access, and attribute-driven access control."
        )

    def define_access_policies(self) -> List[Dict[str, str]]:
        return [
            {"policy": "Least privilege", "description": "Grant only required access."},
            {"policy": "Separation of duties", "description": "Separate approval and access paths."},
            {"policy": "Just-in-time access", "description": "Use timebound access for sensitive operations."},
        ]

    def implement_sso_architecture(self) -> str:
        return (
            "Implementing Okta SSO with OIDC across internal apps, central session management, "
            "and secure token exchange for downstream services."
        )

    def audit_security_controls(self) -> Dict[str, bool]:
        return {
            "MFA_enabled": True,
            "Session_timeout_policy": True,
            "Token_replay_protection": True,
        }


@dataclass
class SolutionArchitect:
    name: str
    product_goals: str = "Align identity platform with business requirements"

    def map_business_requirements(self) -> List[str]:
        return [
            "Single sign-on across HR, DevOps, Finance, Analytics",
            "Standardized access model for internal apps",
            "Strong authentication and compliance reporting",
        ]

    def define_reference_architecture(self) -> Dict[str, str]:
        return {
            "Identity Provider": "Okta",
            "Authentication": "OIDC / SAML for internal apps",
            "Access Management": "Role-based and group-based policies",
            "Monitoring": "Audit events and real-time access logs",
        }

    def plan_migration(self) -> str:
        return (
            "Plan includes application discovery, Okta app onboarding, user directory sync, "
            "role model definition, and phased rollout with pilot groups."
        )

    def articulate_solution_value(self) -> str:
        return (
            "Establishing a scalable identity foundation that reduces risk, improves user experience, "
            "and enables enterprise internal application access with one login."
        )
