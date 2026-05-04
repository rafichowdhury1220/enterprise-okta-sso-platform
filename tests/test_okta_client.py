import pytest

from app.okta_client import OktaClient, OktaConfig


@pytest.fixture
def config() -> OktaConfig:
    return OktaConfig(
        org_url="https://example.okta.com",
        client_id="client-id",
        client_secret="client-secret",
        redirect_uri="https://localhost/callback",
    )


def test_generate_authorization_url(config: OktaConfig) -> None:
    okta = OktaClient(config)
    url = okta.generate_authorization_url(state="test-state")

    assert "/oauth2/default/v1/authorize" in url
    assert "client_id=client-id" in url
    assert "redirect_uri=https%3A%2F%2Flocalhost%2Fcallback" in url
    assert "state=test-state" in url
