import requests
import json



# URL de l'API Kibana
kibana_url = 'http://localhost:5601'  

headers = {
    'kbn-xsrf': 'true',
    'Content-Type': 'application/json'
    
}
with open('Dashboard/export.json', 'r') as file:
    dashboard_data = json.load(file)

# URL pour importer le dashboard
url = f'{kibana_url}/api/kibana/dashboards/import'



# Faire la requête POST pour importer le dashboard
response = requests.post(url, headers=headers, data=json.dumps(dashboard_data))

# Vérifier le statut de la réponse
if response.status_code == 200:
    print("Dashboard importé avec succès !")
else:
    print("Erreur lors de l'importation du dashboard :", response.content.decode())
