from abc import ABC, abstractmethod

class AbstractStructure(ABC):
    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def add(self):
        pass

class Hash(AbstractStructure):
    data = {}
    def get(self, key):
        data[key]
    
    def add(self, key, value):
        data[key] = value

class Queue(AbstractStructure):
    data = []

    def get(self):
        data[0]
    
    def add(self, key, vaue):
        data[len(data)-1] = value


class BankRow:
    
    def __init__(self, store_users):
        if not isinstance(store_users, AbstractStructure):
            raise ValueError("Store isn't suported")
        self.users = store_users

    def next_user(self, turn):
        return self.users.get(turn)

    def settle_users(self, turn, user):
        self.users.add(turn, user)

BankRow(Queue())