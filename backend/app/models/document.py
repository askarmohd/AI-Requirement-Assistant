from sqlalchemy import BigInteger, Enum, String,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID as PythonUUID
from app.models.base import BaseModel
from app.models.enums import DocumentStatus


class Document(BaseModel):
    __tablename__ = "documents"

    file_name: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    uploaded_by_id: Mapped[PythonUUID] = mapped_column(
    ForeignKey("users.id"),
    nullable=False,
    index=True
)
    file_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )

    storage_path: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    status: Mapped[DocumentStatus] = mapped_column(
        Enum(
            DocumentStatus,
            name="document_status_enum"
        ),
        nullable=False,
        default=DocumentStatus.UPLOADED,
        index=True
    )