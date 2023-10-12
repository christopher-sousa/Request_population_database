from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Merchants(Base):
  __tablename__ = 'batch_merchants_rs'
  id = Column(Integer, primary_key=True)
  id_client = Column(String, unique=True)
  corporate_name = Column(String)
  name = Column(String)
  status = Column(String)
  email = Column(String)
  document_id = Column(String, unique=True)
  type_merchant = Column(String)
  created = Column(String)
  batch_transactions_rs = relationship("Transactions", back_populates="batch_merchants_rs")
  batch_merchants_address_rs = relationship("Address", back_populates="batch_merchants_rs")
  batch_merchants_social_data_rs = relationship("SocialData", back_populates="batch_merchants_rs")
  batch_merchants_affiliation_rs = relationship("Affiliation", back_populates="batch_merchants_rs")
  batch_merchants_bank_account_rs = relationship("BackAccount", back_populates="batch_merchants_rs")

class Terminals(Base):
  __tablename__ = 'batch_terminals_rs'
  id = Column(Integer, primary_key=True)
  # id_merchant = Column(Integer, ForeignKey('merchants.id'))
  id_client = Column(String)
  id_terminal  = Column(String, unique=True)
  serial = Column(String)
  status = Column(String)
  identification_code = Column(String)
  # transactions = relationship("Transactions", back_populates="terminals")

class Transactions(Base):
  __tablename__ = 'batch_transactions_rs'
  id = Column(Integer, primary_key=True)
  id_merchant = Column(Integer, ForeignKey('batch_merchants_rs.id'))
  id_transaction  = Column(String, unique=True)
  id_terminal = Column(String)
  # id_terminal = Column(String, ForeignKey('terminals.id_terminal'))
  name = Column(String)
  status = Column(String)
  brand = Column(String)
  installments = Column(Integer)
  created = Column(String)
  document_id = Column(String)
  batch_merchants_rs = relationship("Merchants", back_populates="batch_transactions_rs")
  batch_transactions_installment_rs = relationship("TransactionsInstallmet", back_populates="batch_transactions_rs")
  # terminals = relationship("Terminals", back_populates="transactions")

class TransactionsInstallmet(Base):
  __tablename__ = 'batch_transactions_installment_rs'
  id = Column(Integer, primary_key=True)
  id_transaction = Column(Integer, ForeignKey('batch_transactions_rs.id'))
  id_installment = Column(String, unique=True)
  status  = Column(String)
  installment = Column(Integer)
  date_antecipation = Column(String)
  date_payment = Column(String)
  date_due = Column(String)
  amount_gross = Column(String)
  amount_anticipation = Column(String)
  amount_resale = Column(String)
  batch_transactions_rs = relationship("Transactions", back_populates="batch_transactions_installment_rs")

class Address(Base):
  __tablename__ = 'batch_merchants_address_rs'
  id = Column(Integer, primary_key=True)
  id_merchant = Column(Integer, ForeignKey('batch_merchants_rs.id'))
  id_city  = Column(String)
  id_country = Column(String)
  document_id = Column(String)
  address = Column(String)
  number = Column(Integer)
  complement = Column(String)
  neighborhood = Column(String)
  reference = Column(String)
  type_address = Column(String)
  zipcode = Column(String)
  batch_merchants_rs = relationship("Merchants", back_populates="batch_merchants_address_rs")

class SocialData(Base):
  __tablename__ = 'batch_merchants_social_data_rs'
  id = Column(Integer, primary_key=True)
  id_merchant = Column(Integer, ForeignKey('batch_merchants_rs.id'))
  name  = Column(String)
  document_id = Column(String)
  birthday = Column(String)
  percentage = Column(Integer)
  batch_merchants_rs = relationship("Merchants", back_populates="batch_merchants_social_data_rs")

class Affiliation(Base):
  __tablename__ = 'batch_merchants_affiliation_rs'
  id = Column(Integer, primary_key=True)
  id_merchant = Column(Integer, ForeignKey('batch_merchants_rs.id'))
  id_filliation = Column(String, unique=True)
  automatic_anticipation  = Column(String)
  code_activation_terminal = Column(String)
  status = Column(String)
  batch_merchants_rs = relationship("Merchants", back_populates="batch_merchants_affiliation_rs")

class BackAccount(Base):
  __tablename__ = 'batch_merchants_bank_account_rs'
  id = Column(Integer, primary_key=True)
  id_merchant = Column(Integer, ForeignKey('batch_merchants_rs.id'))
  bank  = Column(String)
  holder = Column(String)
  agency = Column(String)
  account = Column(String)
  document_id = Column(String)
  status = Column(String)
  inactivation_at = Column(String)
  agency_digit = Column(String)
  account_digit = Column(String)
  account_type = Column(String)
  batch_merchants_rs = relationship("Merchants", back_populates="batch_merchants_bank_account_rs")