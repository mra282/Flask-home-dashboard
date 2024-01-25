import requests

class HomeAssistantService:
    def __init__(self, url, token):
        self.url = url
        self.headers = {
            'Authorization': f'Bearer {token}',
            'content-type': 'application/json',
        }

    def get_state(self, entity_id):
        response = requests.get(
            f'{self.url}/api/states/{entity_id}',
            headers=self.headers
        )
        return response.json()

    def set_state(self, entity_id, new_state):
        response = requests.post(
            f'{self.url}/api/states/{entity_id}',
            headers=self.headers,
            json={'state': new_state}
        )
        return response.json()