def format_transactions(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id_transaction': response['idTransaction'],
                'id_terminal': response['idTerminal'],
                'id_client': response['idClient'],
                'name': response['nameClient'] or 'null',
                'status': response['status'],
                'brand': response['brand'],
                'installments': response['installmentsTotal'],
                # TODO 'amount': response['titles'] # Pensar em uma lógica para amount 
                'created': response['date']['created'],
            }
            result_list.append(obj)
    return result_list

def format_installments_transactions(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id_transaction': response['idTransaction'],
                'id_installment': response['idTitle'],
                'status': response['status'],
                'installment': response['installment'],
                'date_antecipation': response['date']['anticipation'] or 'null',
                'date_payment': response['date']['payment'] or 'null',
                'date_due': response['date']['due'] or '',
                'amount_gross': response['amount']['gross'] or 'null',
                'amount_anticipation': response['amount']['anticipation'] or 'null',
                'amount_resale': response['amount']['resale'] or 'null',
            }
            result_list.append(obj)
    return result_list

def format_merchants(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id_client': response['id'],
                'corporate_name': response['nameSocialReason'],
                'name': response['nameFantasy'] or 'null',
                'status': response['status'],
                'email': response['login'],
                'document_id': response['document'],
                'type_merchant': response['type'],
                'created': response['createdAt'],
            }
            result_list.append(obj)
    return result_list

def format_address(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id_client': response['idParticipant'],
                'id_city': response['idCity'] or 'null',
                'id_country': response['idCountry'] or 'null',
                'address': response['address'],
                'number': response['number'] or 'null',
                'complement': response['complement'] or 'null',
                'neighborhood': response['neighborhood'] or 'null',
                'reference': response['reference'] or 'null',
                'type_address': response['type'] or 'null',
                'zipcode': response['zipCode'] ,
            }
            result_list.append(obj)
    return result_list

def format_social_data(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id_client': response['idParticipant'],
                'name': response['name'] or 'null',
                'document_id': response['cpf'],
                'birthday': response['birthday'] or 'null',
                'percentage': response['percentage'] or 'null',
            }
            result_list.append(obj)
    return result_list

def format_terminals(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id_client': response['idParticipant'],
                'id_terminal': response['id'],
                'serial': response['serial'],
                'status': response['status'],
                'identification_code': response['identificationCode'] or 'null',
            }
            result_list.append(obj)
    return result_list

def format_affiliations(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id_client': response['idParticipant'],
                'id_filliation': response['id'],
                'automatic_anticipation': response['automaticAnticipation'],
                'code_activation_terminal': response['codeActivationTerminal'] or 'null' ,
                'status': response['status'],
            }
            result_list.append(obj)
    return result_list

def format_bank_account(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id_client': response['idParticipant'],
                'bank': response['bank'],
                'holder': response['holder'] or 'null' ,
                'agency': response['agency'],
                'account': response['account'],
                'document_id': response['cpfcnpj'] or 'null',
                'status': response['status'],
                'inactivation_at': response['inactivationAt'] or 'null',
                'agency_digit': response['agencyDigit'] or 'null',
                'account_digit': response['accountDigit'] or 'null',
                'account_type': response['status'],
            }
            result_list.append(obj)
    return result_list