from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from core.database import Base


class AuditMixin(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    created_at = Column(
        DateTime(),
        default=datetime.now()
    )
    updated_at = Column(
        DateTime(),
        default=datetime.now(),
        onupdate=datetime.now()
    )

    def __repr__(self):
        return f"{self.__class__.__name__}-{self.id}"
