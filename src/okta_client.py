from dataclasses import dataclass
from typing import Dict, Optional
from urllib.parse import urlencode

import requests
from authlib.jose import jwt


@dataclass
class OktaConfig:
    org_url: str
    client_id: str
    client_secret: str
    redirect_uri: str
    authorization_server: str = "default"
    scopes: str = "openid profile email"


class OktaClient:
    def __init__(self, config: OktaConfig) -> None:
        self.config = config

    def generate_authorization_url(self, state: Optional[str] = None) -> str:
        params = {
            "client_id": self.config.client_id,
            "response_type": "code",
            "scope": self.config.scopes,
            "redirect_uri": self.config.redirect_uri,
            "state": state or "iam-okta-architect-demo",
        }
        url = f"{self.config.org_url}/oauth2/{self.config.authorization_server}/v1/authorize?{urlencode(params)}"
        return url

    def exchange_code_for_tokens(self, code: str) -> Dict[str, str]:
        token_url = f"{self.config.org_url}/oauth2/{self.config.authorization_server}/v1/token"
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.config.redirect_uri,
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
        }
        response = requests.post(token_url, data=data)
        response.raise_for_status()
        return response.json()

    def refresh_access_token(self, refresh_token: str) -> Dict[str, str]:
        token_url = f"{self.config.org_url}/oauth2/{self.config.authorization_server}/v1/token"
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
        }
        response = requests.post(token_url, data=data)
        response.raise_for_status()
        return response.json()

    def validate_id_token(self, id_token: str, jwks: Dict) -> Dict:
        # In a full solution, use Okta JWKS keys and audience validation.
        claims = jwt.decode(id_token, jwks)
        claims.validate()
        return claims

    def get_user_info(self, access_token: str) -> Dict[str, str]:
        userinfo_url = f"{self.config.org_url}/oauth2/{self.config.authorization_server}/v1/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(userinfo_url, headers=headers)
        response.raise_for_status()
        return response.json()
