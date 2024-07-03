from abc import ABC, abstractmethod


class ConnectDB(ABC):

    @abstractmethod
    def connection(self):
        pass
