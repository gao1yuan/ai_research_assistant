import json

class Memory:
    def __init__(self):
        self.memory_store = {}

    def save(self, key: str, value: str):
        self.memory_store[key] = value
        self._save_to_file()

    def load(self, key: str) -> str:
        return self.memory_store.get(key, "")

    def _save_to_file(self):
        with open('data/notes.json', 'w') as file:
            json.dump(self.memory_store, file)