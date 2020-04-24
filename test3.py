from keycloak import KeycloakAdmin

keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                               username='admin',
                               password='admin',
                               realm_name="master",
                               client_secret_key="client-secret",
                               verify=True)

