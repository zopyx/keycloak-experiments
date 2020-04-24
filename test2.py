
from keycloak.realm import KeycloakRealm


realm = KeycloakRealm(server_url='http://localhost:8080', realm_name='test')
print(realm)

oidc_client = realm.open_id_connect(client_id='admin',
                                    client_secret='admin')
print(oidc_client)
import pdb; pdb.set_trace() 
