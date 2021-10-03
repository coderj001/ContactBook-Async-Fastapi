from sqlalchemy import Column, String

from models.base import AuditMixin


class ContactBook(AuditMixin):
    __tablename__ = "contactbook"

    name = Column(String(), server_default='', nullable=False)
    emal_address = Column(String(), unique=True, nullable=False)
