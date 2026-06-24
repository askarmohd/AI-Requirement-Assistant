from pathlib import Path
from uuid import uuid4

from app.core.constants import DOCUMENT_STORAGE_PATH
from app.services.storage.base import StorageService


class LocalStorageService(StorageService):

    def save_file(
        self,
        file_name: str,
        content: bytes
    ) -> str:

        storage_dir = Path(
            DOCUMENT_STORAGE_PATH
        )

        storage_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        unique_name = (
            f"{uuid4()}_{file_name}"
        )

        file_path = (
            storage_dir / unique_name
        )

        file_path.write_bytes(content)

        return str(file_path)

    def delete_file(
        self,
        file_path: str
    ) -> None:

        path = Path(file_path)

        if path.exists():
            path.unlink()