class KVStore:
    def __init__(self):
        self.store = {}

    def set(self, key, value):
        self.store[key] = value
        return 
    
    def get(self, key):
        return self.store[key]
    
    def delete(self, key):
        self.store.pop(key, None)
        return
    
    def show(self):
        return self.store.copy()
    
    def exists(self, key):
        return key in self.store
        