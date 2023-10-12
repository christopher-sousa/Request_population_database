from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError 
import datetime
from processing.generate_data import merchants, transactions, addresses, get_social_data, affiliation, get_banck_account, terminals
from credentials import DATABASE_URL
from tables.entity import Base, Merchants, Transactions, Address, SocialData, Terminals, BackAccount, Affiliation, TransactionsInstallmet

def Main():
    select = int(input('Selecione uma das opções:\
                   \nGet all data (1)\
                   \nGet data from the last 2 days(2)\n:'))
    message = 'Making the request for all data!'
    dateEnd = ''
    dateStart = ''
    if(select == 2):
        current_time = datetime.datetime.now()
        dateEnd = current_time.strftime('%Y-%m-%d')
        last_day = current_time - datetime.timedelta(days=2)
        dateStart = last_day.strftime('%Y-%m-%d')
        message = 'Requesting data from the last 2 days!'

    print(f"\n---------- {message} ----------\n")

    print("---------- Request data! ----------")
    # Request data in Rs Solution
    merchants_df = merchants(dateStart,dateEnd)
    [transactions_df, installments_df] = transactions(dateStart,dateEnd)
    terminals_df = terminals(dateStart, dateEnd)

    address_df = addresses(merchants_df)
    social_data_df = get_social_data(merchants_df)
    affiliations_df = affiliation(merchants_df)
    bank_account_df = get_banck_account(merchants_df)

    # Opening connection with the bank
    engine = create_engine(DATABASE_URL)

    # Creating tables
    Base.metadata.create_all(engine)

    print("---------- Connect bank! ----------")
    Session = sessionmaker(bind=engine)
    session = Session()

    print("---------- persistent data in the database! ----------")
    # Loop through DataFrame records and insert them with conflict checking
    for index, row in merchants_df.iterrows():
        try:
            merchant = Merchants(**row.to_dict())
            session.add(merchant)
            session.commit()
        except IntegrityError as e:
            print("Error adding: ", e)
            session.rollback()  # Rollback transaction in case of integrity conflict

    for index, row in terminals_df.iterrows():
        try:
            # Get merchant of related merchant using idClient
            # WIP There are no known users in the API
            # idClient = row['id_client']
            # merchant = session.query(Merchants).filter_by(id_client=idClient).first()
            # if merchant:
            terminals_data = row.to_dict()
            # WIP There are no known transactions in the API
            # terminals_data['id_merchant'] = merchant.id
            transaction = Terminals(**terminals_data)
            session.add(transaction)
            session.commit()
        except IntegrityError as e:
            print("Error adding: ", e)
            session.rollback()  # Rollback transaction in case of integrity conflict


    for index, row in transactions_df.iterrows():
        try:
            # Get merchant of related merchant using idClient
            idClient = row['id_client']
            merchant = session.query(Merchants).filter_by(id_client=idClient).first()
            if merchant:
                # Create a new transaction instance
                transaction_data = row.to_dict()
                transaction_data['id_merchant'] = merchant.id
                transaction_data['document_id'] = merchant.document_id
                del transaction_data['id_client'] # Removing client id
                transaction = Transactions(**transaction_data)
                session.add(transaction)
                session.commit()
        except IntegrityError as e:
            print("Error adding: ", e)
            session.rollback()  # Rollback transaction in case of integrity conflict

    for index, row in installments_df.iterrows():
        try:
            # Get transaction of related merchant using id_transaction
            idTransaction = row['id_transaction']
            transaction = session.query(Transactions).filter_by(id_transaction=idTransaction).first()
            if transaction:
                # Create a new TransactionsInstallmet instance
                installment_data = row.to_dict()
                installment_data['id_transaction'] = transaction.id
                installment = TransactionsInstallmet(**installment_data)
                session.add(installment)
                session.commit()
        except IntegrityError as e:
            print("Error adding: ", e)
            session.rollback()  # Rollback transaction in case of integrity conflict

    for index, row in address_df.iterrows():
        try:
            # Get merchant of related merchant using idClient
            idClient = row['id_client']
            merchant = session.query(Merchants).filter_by(id_client=idClient).first()
            if merchant:
                # Create a new Address instance
                address_data = row.to_dict()
                address_data['id_merchant'] = str(merchant.id)
                address_data['document_id'] = merchant.document_id
                del address_data['id_client']
                address = Address(**address_data)
                session.add(address)
                session.commit()
        except IntegrityError as e:
            print("Error adding: ", e)
            session.rollback()  # Rollback transaction in case of integrity conflict

    for index, row in social_data_df.iterrows():
        try:
            # Get merchant of related merchant using idClient
            idClient = row['id_client']
            merchant = session.query(Merchants).filter_by(id_client=idClient).first()
            if merchant:
                # Create a new SocialData instance
                social_data = row.to_dict()
                social_data['id_merchant'] = merchant.id
                del social_data['id_client']
                data = SocialData(**social_data)
                session.add(data)
                session.commit()
        except IntegrityError as e:
            print("Error adding: ", e)
            session.rollback()  # Rollback transaction in case of integrity conflict

    for index, row in affiliations_df.iterrows():
        try:
            # Get merchant of related merchant using idClient
            idClient = row['id_client']
            merchant = session.query(Merchants).filter_by(id_client=idClient).first()
            if merchant:
                # Create a new Affiliation instance
                affiliation_data = row.to_dict()
                affiliation_data['id_merchant'] = merchant.id
                del affiliation_data['id_client']
                data = Affiliation(**affiliation_data)
                session.add(data)
                session.commit()
        except IntegrityError as e:
            print("Error adding: ", e)
            session.rollback()  # Rollback transaction in case of integrity conflict

    for index, row in bank_account_df.iterrows():
        try:
            # Get merchant of related merchant using idClient
            idClient = row['id_client']
            merchant = session.query(Merchants).filter_by(id_client=idClient).first()
            if merchant:
                # Create a new BackAccount instance
                banck_account = row.to_dict()
                banck_account['id_merchant'] = merchant.id
                del banck_account['id_client']
                data = BackAccount(**banck_account)
                session.add(data)
                session.commit()
        except IntegrityError as e:
            print("Error adding: ", e)
            session.rollback()  # Rollback transaction in case of integrity conflict


    # Feche a conexão
    session.close()
    print("\n---------- The end! ----------\n")