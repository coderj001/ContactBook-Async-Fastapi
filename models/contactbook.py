from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from database import Base


class AuditMixin(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

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


class Sample(AuditMixin):
    __tablename__ = "Sample"

    username = Column(String(), server_default='', nullable=False)
