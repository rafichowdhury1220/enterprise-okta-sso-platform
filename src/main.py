from app.iam_architect import IAMEngineer, SolutionArchitect
from app.okta_client import OktaClient, OktaConfig


def print_enterprise_scenario() -> None:
    print("=== Enterprise Okta SSO Platform ===")
    print(
        "Objective: Enable one-login access for HR, DevOps, Finance, and Analytics internal applications "
        "using Okta as the centralized identity provider."
    )
    print("Key business outcomes: improved user experience, stronger security, and consistent access controls.\n")


def demo_okta_integration() -> None:
    config = OktaConfig(
        org_url="https://example.okta.com",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri="https://localhost/callback",
    )
    okta = OktaClient(config)
    authorization_url = okta.generate_authorization_url(state="enterprise-okta-demo")

    print("--- Okta SSO Workflow ---")
    print("1. User attempts to access an internal application.")
    print("2. Application redirects to Okta for authentication.")
    print("3. Okta issues an authorization code and tokens for the app.")
    print(f"4. Example authorization URL: {authorization_url}\n")
    print("This demonstrates how the runtime Okta flow is generated for enterprise app onboarding.")
    print("It connects identity design to a concrete OIDC authorization step.\n")


def demo_iam_and_solution_architecture() -> None:
    engineer = IAMEngineer(name="Ayesha")
    architect = SolutionArchitect(name="Ravi")

    print("--- IAM Engineering ---")
    print("Identity lifecycle narrative:")
    print(f"- {engineer.design_identity_lifecycle()}")
    print("Access policy framework:")
    for policy in engineer.define_access_policies():
        print(f"- {policy['policy']}: {policy['description']}")
    print("Security checks and controls:")
    for name, enabled in engineer.audit_security_controls().items():
        print(f"- {name}: {'enabled' if enabled else 'disabled'}")
    print("\n")

    print("--- Solution Architecture ---")
    print("Business requirements addressed:")
    for requirement in architect.map_business_requirements():
        print(f"- {requirement}")
    print("Reference architecture components:")
    for layer, detail in architect.define_reference_architecture().items():
        print(f"- {layer}: {detail}")
    print(f"\nMigration approach: {architect.plan_migration()}")
    print(f"Value proposition: {architect.articulate_solution_value()}")


def main() -> None:
    print_enterprise_scenario()
    demo_okta_integration()
    print("\n")
    demo_iam_and_solution_architecture()


if __name__ == "__main__":
    main()
