from api_rs.api import get_client_data, get_transaction_data, get_client_data_address, get_client_social_data, get_transaction_terminals, get_client_data_affiliation, get_client_data_bankaccount
from processing.formart import format_address, format_transactions, format_merchants, format_social_data, format_terminals, format_affiliations, format_bank_account, format_installments_transactions
from processing.data_transform import create_dataframe

def merchants(dataStart:str, dataEnd:str):
  clientes_data = get_client_data(dataStart, dataEnd) # Get client data
  clientes_df = create_dataframe(format_merchants(clientes_data)) # Transforming the client object list into a dataframe
  return clientes_df

def transactions(dataStart:str, dataEnd:str):
  transaction_data = get_transaction_data(dataStart, dataEnd) # Get transactions data
  installments_df = installments(transaction_data) # Get installments data
  transactions_df = create_dataframe(format_transactions(transaction_data)) # Transforming the transactions object list into a dataframe
  return transactions_df, installments_df

def terminals(dataStart:str, dataEnd:str):
  terminals_data = get_transaction_terminals(dataStart, dataEnd) # Get terminals data
  terminals_df = create_dataframe(format_terminals(terminals_data)) # Transforming the terminals object list into a dataframe
  return terminals_df

def addresses(merchant):
  address_data = []
  for index, row in merchant.iterrows():
    addres = get_client_data_address(row.id_client) # Get addrress data usning merchant.id_client
    for addr in addres:
        addr['idParticipant'] = row.id_client
    address_data.extend(addres)
  address_df = create_dataframe(format_address(address_data)) # Transforming the addrress object list into a dataframe
  return address_df

def get_social_data(merchant):
  social_data = []
  for index, row in merchant.iterrows():
    list_social_data = get_client_social_data(row.id_client) # Get social data data usning merchant.id_client
    
    for data in list_social_data:
        data['idParticipant'] = row.id_client

    social_data.extend(list_social_data)
  social_data_df = create_dataframe(format_social_data(social_data)) # Transforming the social data object list into a dataframe
  return social_data_df

def affiliation(merchant):
  affiliation_data = []
  for index, row in merchant.iterrows():
    affiliations = get_client_data_affiliation(row.id_client) # Get social data data usning merchant.id_client
    for affiliation in affiliations:
        affiliation['idParticipant'] = row.id_client
    affiliation_data.extend(affiliations)
  affiliation_data_df = create_dataframe(format_affiliations(affiliation_data)) # Transforming the social data object list into a dataframe
  return affiliation_data_df

def get_banck_account(merchant):
  banck_account_data = []
  for index, row in merchant.iterrows():
    banck_accounts = get_client_data_bankaccount(row.id_client) # Get social data data usning merchant.id_client
    for account in banck_accounts:
        account['idParticipant'] = row.id_client
    banck_account_data.extend(banck_accounts)
  banck_account_df = create_dataframe(format_bank_account(banck_account_data)) # Transforming the social data object list into a dataframe
  return banck_account_df

def installments(transactions):
  transactions_installments = []
  for transation in transactions:
    id_transaction = transation['idTransaction']
    list_installments = transation['titles']
    for installments in list_installments:
        installments['idTransaction'] = id_transaction
    transactions_installments.extend(list_installments)
  transacoes_installments_df = create_dataframe(format_installments_transactions(transactions_installments)) # Transforming the installments object list into a dataframe
  return transacoes_installments_df