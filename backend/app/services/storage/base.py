from abc import ABC, abstractmethod


class StorageService(ABC):

    @abstractmethod
    def save_file(
        self,
        file_name: str,
        content: bytes
    ) -> str:
        pass

    @abstractmethod
    def delete_file(
        self,
        file_path: str
    ) -> None:
        pass