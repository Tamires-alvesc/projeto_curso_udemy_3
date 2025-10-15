#!/usr/bin/env python3
"""
Script para gerar tokens JWT secretos
"""
import secrets

def gerar_token():
    """Gera um token seguro para JWT"""
    token = secrets.token_urlsafe(32)
    print(f"Token gerado: {token}")
    return token

if __name__ == "__main__":
    gerar_token()
