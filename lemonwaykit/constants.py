# -*- coding: utf-8 -*-
VALID_LEMONWAY_METHOD_PARAMETERS = {
    'FastPay': [
        "clientMail", "clientTitle", "clientFirstName", "clientLastName", "cardType", "cardNumber", "cardCrypto",
        "cardDate", "creditWallet", "amount", "message", "autoCommission", "registerCard"
    ],
    'RegisterWallet': [
        "wallet", "clientName", "clientMail", "clientTitle", "clientFirstName", "clientLastName", "street",
        "postCode", "city", "ctry", "birthdate", "phoneNumber", "mobileNumber", "isCompany", "companyName",
        "companyWebsite", "companyDescription", "companyIdentificationNumber", "idDebtor", "nationality",
        "birthcity", "birthcountry", "isOneTimeCustomer"
    ],
    'UpdateWalletDetails': [
        "wallet", "newEmail", "newTitle", "newFirstName", "newLastName", "newStreet", "newPostCode", "newCity",
        "newCtry", "newIp", "newPhoneNumber", "newMobileNumber", "newBirthDate", "newIsCompany", "newCompanyName",
        "newCompanyWebsite", "newCompanyDescription", "newCompanyIdentificationNumber", "newIsDebtor",
        "newNationality", "newBirthcity", "newBirthcountry"
    ],
    'UpdateWalletStatus': [
        "wallet", "newStatus"
    ],
    'GetWalletDetails': [
        "wallet", "email"
    ],
    'MoneyIn': [
        "wallet", "cardType", "cardNumber", "cardCrypto", "cardDate", "amountTot", "amountCom", "comment",
        "autoCommission", "isPreAuth", "wkToken", "specialConfig"
    ],
    'MoneyIn3DInit': [
        "wallet", "amountTot", "amountCom", "comment", "wkToken", "cardType", "cardNumber", "cardCode", "cardDate",
        "autoCommission", "returnUrl", "specialConfig"
    ],
    'MoneyIn3DConfirm': [
        "transactionId", "MD", "PaRes", "cardType", "cardNumber", "cardCode", "cardDate", "isPreAuth",
        "specialConfig"
    ],
    'MoneyInWebInit': [
        "wallet", "amountTot", "amountCom", "comment", "useRegisteredCard", "wkToken", "returnUrl", "cancelUrl",
        "errorUrl", "autoCommission", "registerCard"
    ],
    'RegisterCard': [
        "wallet", "cardType", "cardNumber", "cardCode", "cardDate", "specialConfig"
    ],
    'UnregisterCard': [
        "wallet", "cardId"
    ],
    'MoneyInWithCardId': [
        "wallet", "cardId", "amountTot", "amountCom", "message", "autoCommission", "isPreAuth", "specialConfig"
    ],
    'MoneyInValidate': [
        "transactionId", "specialConfig"
    ],
    'SendPayment': [
        "debitWallet", "creditWallet", "amount", "message", "scheduledDate", "privateData"
    ],
    'RegisterIBAN': [
        "wallet", "holder", "bic", "iban", "dom1", "dom2"
    ],
    'MoneyOut': [
        "wallet", "amountTot", "amountCom", "message", "ibanId", "autoCommission"
    ],
    'GetPaymentDetails': [
        "transactionId", "transactionComment", "privateData"
    ],
    'GetMoneyInTransDetails': [
        "transactionId", "transactionComment", "transactionMerchantToken"
    ],
    'GetMoneyOutTransDetails': [
        "transactionId", "transactionComment"
    ],
    'UploadFile': [
        "wallet", "fileName", "type", "buffer", "sddMandateId"
    ],
    'GetKycStatus': [
        "updateDate"
    ],
    'GetMoneyInIBANDetails': [
        "updateDate"
    ],
    'RefundMoneyIn': [
        "transactionId", "amountToRefund", "comment"
    ],
    'GetBalances': [
        "updateDate"
    ],
    'MoneyIn3DAuthenticate': [
        "transactionId", "MD", "PaRes", "cardType", "cardNumber", "cardCode", "cardDate"
    ],
    'CreateGiftCodeAmazon': [
        "debitWallet", "amountAGCOD"
    ],
    'MoneyInIDealInit': [
        "wallet", "amountTot", "amountCom", "issuerId", "comment", "returnUrl", "autoCommission"
    ],
    'MoneyInIDealConfirm': [
        "transactionId"
    ],
    'RegisterSddMandate': [
        "wallet", "holder", "bic", "iban", "isRecurring", "street", "postCode", "city", "country"
    ],
    'UnregisterSddMandate': [
        "wallet", "sddMandateId"
    ],
    'MoneyInSddInit': [
        "wallet", "amountTot", "amountCom", "comment", "autoCommission", "sddMandateId", "collectionDate"
    ],
    'GetMoneyInSdd': [
        "updateDate"
    ],
    'GetMoneyInChequeDetails': [
        "updateDate"
    ],
    'GetWalletTransHistory': [
        "wallet"
    ],
    'GetChargebacks': [
        "updateDate"
    ],
    'MoneyInChequeInit': [
        "wallet", "amountTot", "amountCom", "comment", "autoCommission"
    ],
    'SignDocumentInit': [
        "wallet", "mobileNumber", "documentId", "documentType", "returnUrl", "errorUrl"
    ],
    'CreateVCC': [
        "debitWallet", "amountVCC"
    ],
    'MoneyInNeosurf': [
        "wallet", "amountTot", "amountCom", "comment", "idTicket", "isNeocode", "wkToken"
    ],
    'GetWizypayAds': [

    ],
}

#http://documentation.lemonway.fr/api-en/annex/status-and-types/iban-status
LEMONWAY_IBAN_STATUS_WAITING_FOR_LW_VERIFICATION = 4
LEMONWAY_IBAN_STATUS_ACTIVATED = 5
LEMONWAY_IBAN_STATUS_DEACTIVATED = 8
LEMONWAY_IBAN_STATUS_REJECTED = 9
"""LEMONWAY_IBAN_STATUSES = [
    LEMONWAY_IBAN_STATUS_WAITING_FOR_LW_VERIFICATION,
    LEMONWAY_IBAN_STATUS_ACTIVATED,
    LEMONWAY_IBAN_STATUS_DEACTIVATED,
    LEMONWAY_IBAN_STATUS_REJECTED,
]"""
LEMONWAY_IBAN_STATUS_DICT = {
    str(LEMONWAY_IBAN_STATUS_WAITING_FOR_LW_VERIFICATION):'4 - LEMONWAY_IBAN_STATUS_WAITING_FOR_LW_VERIFICATION',
    str(LEMONWAY_IBAN_STATUS_ACTIVATED):'5 - LEMONWAY_IBAN_STATUS_ACTIVATED',
    str(LEMONWAY_IBAN_STATUS_DEACTIVATED):'8 - LEMONWAY_IBAN_STATUS_DEACTIVATED',
    str(LEMONWAY_IBAN_STATUS_REJECTED):'9 - LEMONWAY_IBAN_STATUS_REJECTED',
}
LEMONWAY_IBAN_STATUSES = [int(x) for x in LEMONWAY_IBAN_STATUS_DICT.iterkeys()]

#http://documentation.lemonway.fr/api-en/annex/status-and-types/kyc-document-types
LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_ID = 0
LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_ADDRESS = 1
LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_IBAN = 2
LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_REGISTRY_COMMERCE_NUMBER_FOR_ENTERPRICE_ONLY = 7
LEMONWAY_KYC_DOCUMENT_TYPE_OTHER_DOCUMENTS = range(11,21)
LEMONWAY_KYC_DOCUMENT_TYPE_SDD_MANDATE = 21
"""LEMONWAY_KYC_DOCUMENT_TYPES = [
    LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_ID,
    LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_ADDRESS,
    LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_IBAN,
    LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_REGISTRY_COMMERCE_NUMBER_FOR_ENTERPRICE_ONLY,
    LEMONWAY_KYC_DOCUMENT_TYPE_SDD_MANDATE
]"""
LEMONWAY_KYC_DOCUMENT_TYPES_DICT = {
    str(LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_ID):'0 - LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_ID',
    str(LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_ADDRESS):'1 - LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_ADDRESS',
    str(LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_IBAN):'2 - LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_IBAN',
    str(LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_REGISTRY_COMMERCE_NUMBER_FOR_ENTERPRICE_ONLY):'7 - LEMONWAY_KYC_DOCUMENT_TYPE_PROOF_OF_REGISTRY_COMMERCE_NUMBER_FOR_ENTERPRICE_ONLY',
    str(LEMONWAY_KYC_DOCUMENT_TYPE_SDD_MANDATE):'21 - LEMONWAY_KYC_DOCUMENT_TYPE_SDD_MANDATE'
}
for x in LEMONWAY_KYC_DOCUMENT_TYPE_OTHER_DOCUMENTS:
    #LEMONWAY_KYC_DOCUMENT_TYPES.append(x)
    LEMONWAY_KYC_DOCUMENT_TYPES_DICT.update({str(x):'%s - LEMONWAY_KYC_DOCUMENT_TYPE_OTHER_DOCUMENTS'%str(x)})
LEMONWAY_KYC_DOCUMENT_TYPES = [int(x) for x in LEMONWAY_KYC_DOCUMENT_TYPES_DICT.iterkeys()]


#http://documentation.lemonway.fr/api-en/annex/status-and-types/kyc-document-status
LEMONWAY_KYC_DOCUMENT_STATUS_HOLD = 0 # waiting for another document
LEMONWAY_KYC_DOCUMENT_STATUS_NOT_VERIFIED_YET = 1
LEMONWAY_KYC_DOCUMENT_STATUS_ACCEPTED = 2
LEMONWAY_KYC_DOCUMENT_STATUS_NOT_ACCEPTED = 3
LEMONWAY_KYC_DOCUMENT_STATUS_REPLACED_WITH_ANOTHER_DOCUMENT = 4
LEMONWAY_KYC_DOCUMENT_STATUS_EXPIRED = 5
LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_TYPE = 6
LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_NAME = 7
"""LEMONWAY_KYC_DOCUMENT_STATUSES = [
    LEMONWAY_KYC_DOCUMENT_STATUS_HOLD,
    LEMONWAY_KYC_DOCUMENT_STATUS_NOT_VERIFIED_YET,
    LEMONWAY_KYC_DOCUMENT_STATUS_ACCEPTED,
    LEMONWAY_KYC_DOCUMENT_STATUS_NOT_ACCEPTED,
    LEMONWAY_KYC_DOCUMENT_STATUS_REPLACED_WITH_ANOTHER_DOCUMENT,
    LEMONWAY_KYC_DOCUMENT_STATUS_EXPIRED,
    LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_TYPE,
    LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_NAME
]"""
LEMONWAY_KYC_DOCUMENT_SEEN_STATUSES = [
    #LEMONWAY_KYC_DOCUMENT_STATUS_HOLD,
    #LEMONWAY_KYC_DOCUMENT_STATUS_NOT_VERIFIED_YET,
    str(LEMONWAY_KYC_DOCUMENT_STATUS_ACCEPTED),
    str(LEMONWAY_KYC_DOCUMENT_STATUS_NOT_ACCEPTED),
    str(LEMONWAY_KYC_DOCUMENT_STATUS_REPLACED_WITH_ANOTHER_DOCUMENT),
    str(LEMONWAY_KYC_DOCUMENT_STATUS_EXPIRED),
    str(LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_TYPE),
    str(LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_NAME)
]
LEMONWAY_KYC_DOCUMENT_STATUSES_DICT = {
    str(LEMONWAY_KYC_DOCUMENT_STATUS_HOLD):  '0 - LEMONWAY_KYC_DOCUMENT_STATUS_HOLD',
    str(LEMONWAY_KYC_DOCUMENT_STATUS_NOT_VERIFIED_YET):  '1 - LEMONWAY_KYC_DOCUMENT_STATUS_NOT_VERIFIED_YET',
    str(LEMONWAY_KYC_DOCUMENT_STATUS_ACCEPTED):  '2 - LEMONWAY_KYC_DOCUMENT_STATUS_ACCEPTED',
    str(LEMONWAY_KYC_DOCUMENT_STATUS_NOT_ACCEPTED):  '3 - LEMONWAY_KYC_DOCUMENT_STATUS_NOT_ACCEPTED',
    str(LEMONWAY_KYC_DOCUMENT_STATUS_REPLACED_WITH_ANOTHER_DOCUMENT):  '4 - LEMONWAY_KYC_DOCUMENT_STATUS_REPLACED_WITH_ANOTHER_DOCUMENT',
    str(LEMONWAY_KYC_DOCUMENT_STATUS_EXPIRED):  '5 - LEMONWAY_KYC_DOCUMENT_STATUS_EXPIRED',
    str(LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_TYPE):  '6 - LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_TYPE',
    str(LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_NAME): '7 - LEMONWAY_KYC_DOCUMENT_STATUS_WRONG_NAME',
}
LEMONWAY_KYC_DOCUMENT_STATUSES = [int(x) for x in LEMONWAY_KYC_DOCUMENT_STATUSES_DICT.iterkeys()]


#http://documentation.lemonway.fr/api-en/annex/status-and-types/wallet-status
LEMONWAY_SDD_MANDATE_STATUS_NOT_VALIDATED = 0
LEMONWAY_SDD_MANDATE_STATUS_USABLE_WITH_6_DAYS_DELAY = 5 #can be used, actual debit will happen after 6 working days
LEMONWAY_SDD_MANDATE_STATUS_USABLE_WITH_3_DAYS_DELAY = 6 #can be used, actual debit will happen after 3 working days
LEMONWAY_SDD_MANDATE_STATUS_DEACTIVATED = 8
LEMONWAY_SDD_MANDATE_STATUS_REJECTED = 9
"""LEMONWAY_SDD_MANDATE_STATUSES = [
    LEMONWAY_SDD_MANDATE_STATUS_NOT_VALIDATED,
    LEMONWAY_SDD_MANDATE_STATUS_USABLE_WITH_6_DAYS_DELAY,
    LEMONWAY_SDD_MANDATE_STATUS_USABLE_WITH_3_DAYS_DELAY,
    LEMONWAY_SDD_MANDATE_STATUS_DEACTIVATED,
    LEMONWAY_SDD_MANDATE_STATUS_REJECTED
]"""
LEMONWAY_SDD_MANDATE_STATUSES_DICT = {
    str(LEMONWAY_SDD_MANDATE_STATUS_NOT_VALIDATED):  '0 - LEMONWAY_SDD_MANDATE_STATUS_NOT_VALIDATED',
    str(LEMONWAY_SDD_MANDATE_STATUS_USABLE_WITH_6_DAYS_DELAY):  '5 - LEMONWAY_SDD_MANDATE_STATUS_USABLE_WITH_6_DAYS_DELAY',
    str(LEMONWAY_SDD_MANDATE_STATUS_USABLE_WITH_3_DAYS_DELAY):  '6 - LEMONWAY_SDD_MANDATE_STATUS_USABLE_WITH_3_DAYS_DELAY',
    str(LEMONWAY_SDD_MANDATE_STATUS_DEACTIVATED):  '8 - LEMONWAY_SDD_MANDATE_STATUS_DEACTIVATED',
    str(LEMONWAY_SDD_MANDATE_STATUS_REJECTED):  '9 - LEMONWAY_SDD_MANDATE_STATUS_REJECTED',
}
LEMONWAY_SDD_MANDATE_STATUSES = [int(x) for x in LEMONWAY_SDD_MANDATE_STATUSES_DICT.iterkeys()]


LEMONWAY_WALLET_STATUS_REGISTERED_KYC_INCOMPLETE = 2
LEMONWAY_WALLET_STATUS_REGISTERED_KYC_REJECTED = 3
LEMONWAY_WALLET_STATUS_REGISTERED_KYC_1 = 5
LEMONWAY_WALLET_STATUS_REGISTERED_KYC_2 = 6
LEMONWAY_WALLET_STATUS_REGISTERED_KYC_3 = 7 #may or may not be used depending on your business
LEMONWAY_WALLET_STATUS_REGISTERED_KYC_EXPIRED = 8
LEMONWAY_WALLET_STATUS_BLOCKED = 9
LEMONWAY_WALLET_STATUS_CLOSED = 12
LEMONWAY_WALLET_STATUS_REGISTERED_KYC_BETWEEN_2_AND_3 = 13 #may or may not be used depending on your business
LEMONWAY_WALLET_STATUS_ONE_TIME_CUSTOMER = 14 #may or may not be used depending on your business
LEMONWAY_WALLET_STATUS_SPECIAL_WALLET_FOR_CROWDLENDING = 15 #may or may not be used depending on your business
"""LEMONWAY_WALLET_STATUSES = [
    LEMONWAY_WALLET_STATUS_REGISTERED_KYC_INCOMPLETE,
    LEMONWAY_WALLET_STATUS_REGISTERED_KYC_REJECTED,
    LEMONWAY_WALLET_STATUS_REGISTERED_KYC_1,
    LEMONWAY_WALLET_STATUS_REGISTERED_KYC_2,
    LEMONWAY_WALLET_STATUS_REGISTERED_KYC_3,
    LEMONWAY_WALLET_STATUS_REGISTERED_KYC_EXPIRED,
    LEMONWAY_WALLET_STATUS_BLOCKED,
    LEMONWAY_WALLET_STATUS_CLOSED,
    LEMONWAY_WALLET_STATUS_REGISTERED_KYC_BETWEEN_2_AND_3,
    LEMONWAY_WALLET_STATUS_ONE_TIME_CUSTOMER,
    LEMONWAY_WALLET_STATUS_SPECIAL_WALLET_FOR_CROWDLENDING
]"""
LEMONWAY_WALLET_STATUSES_DICT = {
    str(LEMONWAY_WALLET_STATUS_REGISTERED_KYC_INCOMPLETE):  '2 - REGISTERED_KYC_INCOMPLETE',
    str(LEMONWAY_WALLET_STATUS_REGISTERED_KYC_REJECTED):  '3 - REGISTERED_KYC_REJECTED',
    str(LEMONWAY_WALLET_STATUS_REGISTERED_KYC_1):  '5 - REGISTERED_KYC_1',
    str(LEMONWAY_WALLET_STATUS_REGISTERED_KYC_2):  '6 - REGISTERED_KYC_2',
    str(LEMONWAY_WALLET_STATUS_REGISTERED_KYC_3):  '7 - REGISTERED_KYC_3',
    str(LEMONWAY_WALLET_STATUS_REGISTERED_KYC_EXPIRED):  '8 - REGISTERED_KYC_EXPIRED',
    str(LEMONWAY_WALLET_STATUS_BLOCKED):  '9 - BLOCKED',
    str(LEMONWAY_WALLET_STATUS_CLOSED): '12 - CLOSED',
    str(LEMONWAY_WALLET_STATUS_REGISTERED_KYC_BETWEEN_2_AND_3): '13 - REGISTERED_KYC_BETWEEN_2_AND_3',
    str(LEMONWAY_WALLET_STATUS_ONE_TIME_CUSTOMER): '14 - ONE_TIME_CUSTOMER',
    str(LEMONWAY_WALLET_STATUS_SPECIAL_WALLET_FOR_CROWDLENDING): '15 - SPECIAL_WALLET_FOR_CROWDLENDING',
}
LEMONWAY_WALLET_STATUSES = [int(x) for x in LEMONWAY_WALLET_STATUSES_DICT.iterkeys()]



#http://documentation.lemonway.fr/display/EN/GetMoneyInTransDetails%3A+looking+for+a+money-in
LEMONWAY_MONEYIN_STATUS_SUCCESS = 3
LEMONWAY_MONEYIN_STATUS_ERROR = 4
LEMONWAY_MONEYIN_STATUS_WAITING_FOR_FINALIZATION = 0
LEMONWAY_MONEYIN_STATUS_RESERVATION_SUCCESS_AWAITING_VALIDATION = 16
"""LEMONWAY_MONEYIN_STATUSES = [
    LEMONWAY_MONEYIN_STATUS_SUCCESS,
    LEMONWAY_MONEYIN_STATUS_ERROR,
    LEMONWAY_MONEYIN_STATUS_WAITING_FOR_FINALIZATION,
    LEMONWAY_MONEYIN_STATUS_RESERVATION_SUCCESS_AWAITING_VALIDATION,
]"""
LEMONWAY_MONEYIN_STATUSES_DICT = {
    str(LEMONWAY_MONEYIN_STATUS_SUCCESS):'3 - LEMONWAY_MONEYIN_STATUS_SUCCESS',
    str(LEMONWAY_MONEYIN_STATUS_ERROR):'4 - LEMONWAY_MONEYIN_STATUS_ERROR',
    str(LEMONWAY_MONEYIN_STATUS_WAITING_FOR_FINALIZATION):'0 - LEMONWAY_MONEYIN_STATUS_WAITING_FOR_FINALIZATION',
    str(LEMONWAY_MONEYIN_STATUS_RESERVATION_SUCCESS_AWAITING_VALIDATION):'16 - LEMONWAY_MONEYIN_STATUS_RESERVATION_SUCCESS_AWAITING_VALIDATION',
}
LEMONWAY_MONEYIN_STATUSES = [int(x) for x in LEMONWAY_MONEYIN_STATUSES_DICT.iterkeys()]


LEMONWAY_P2P_PAYMENT_STATUS_DELAYED = 0
LEMONWAY_P2P_PAYMENT_STATUS_SUCCESS = 3
LEMONWAY_P2P_PAYMENT_STATUSES_DICT = {
    str(LEMONWAY_P2P_PAYMENT_STATUS_DELAYED):'0 - LEMONWAY_P2P_PAYMENT_STATUS_DELAYED',
    str(LEMONWAY_P2P_PAYMENT_STATUS_SUCCESS):'3 - LEMONWAY_P2P_PAYMENT_STATUS_SUCCESS',
}
LEMONWAY_P2P_PAYMENT_STATUSES = [int(x) for x in LEMONWAY_P2P_PAYMENT_STATUSES_DICT.iterkeys()]


#########
### ATOS
###########
"""
The format of the code depend on the method used for card payment:
MoneyIn, MoneyInWebInit, RegisterCard, MoneyInWithCardId: xx-yy-zz
MoneyIn3DInit: dd
MoneyIn3DConfirm : xx-yy-zz-dd 
xx : general code 
yy : control made by our partners
zz: code returned by the card owner's bank
dd: code linked to 3DS
"""
LEMONWAY_ATOS_ERRORS = {
    'xx': { #general code 
        '03': 'Configuration issue (please contact LW support)',
        '05': 'Autorisation refusée',
        '12': 'Invalid transaction',
        '14': 'Invalid card information',
        '17': 'Cancelled by user',
        '34': 'Fraud suspected',
        '54': 'Card expired',
        '63': 'Transaction stopped',
        '75': 'Not authenticated on 3D Secure platform or max number of attempts',
        '90': 'Temporarily unavailable',
        '99': 'Temporarily unavailable'
    },
    'yy': { #control made by our partners
        '00': 'No issue',
        '02': 'More than 5 payments with the same card in 48 hours',
        '03': 'Blacklisted card',
        '05': 'Could not determine card country (only if you asked for a card country filter)',
        '06': 'Card country not allowed',
        '07': 'e Carte Bleue detected',
        '08': 'Card country not allowed',
        '13': 'Could not determine card country',
        '17': '3D error',
        '99': 'Technical error'
    },
    'zz': { #code returned by the card owner's bank
        '04': 'Fraud suspected',
        '05': 'Do not honor',
        '12': 'Invalid transaction',
        '13': 'Invalid card',
        '14': 'Numéro de porteur invalide',
        '15': 'Unknown card',
        '33': 'Card expired',
        '34': 'Fraud suspected',
        '41': 'Lost card',
        '43': 'Stolen card',
        '51': 'Insufficient funds',
        '54': 'Card expired',
        '56': 'Unknown card',
        '57': 'Client not allowed',
        '58': 'Operation not allowed',
        '59': 'Fraud suspicion',
        '61': 'Amount not allowed',
        '63': 'Not allowed',
        '68': 'No response',
        '90': 'Service temporarily unavailable',
        '91': 'Could not reach card issuer',
        '96': 'Temporarily unavailable',
        '97': 'Temporarily unavailable',
        '98': 'Temporarily unavailable',
        '99': 'Temporarily unavailable'
    },
    'dd': { #code linked to 3DS
        '01': 'Not enrolled',
        '02': 'ACS technical issue',
        '03': 'Configuration issue (please contact LW support)',
        '10': 'Cannot get information from the card owner\'s bank',
        '12': 'Invalid transaction',
        '55': 'Not authenticated',
        '81': 'Internal error',
        '85': 'Server unreachable',
        '94': 'Technical error while the user was authenticating',
        '95': 'ACS message error',
        '96': 'ACS message error',
        '97': 'Paramètres transmis invalides',
        '98': 'Technical error while the user was authenticating',
        '99': 'Technical error'
    }
}


LEMONWAY_DIRECTKIT_ERRORS= {
    '1' : 'Internal Error',
    '100' : 'Limit amount reached (if the error is raised during a payment between 2 wallets, the limit has been reached by the sending wallet)',
    '101' : 'Limit amount reached (if the error is raised during a payment between 2 wallets, the limit has been reached by the receiving wallet)',
    '105' : 'WHITE BRAND not recognized',
    '110' : 'Insufficient credit',
    '119' : 'Card information format incorrect',
    '124' : 'Unknown error returned by the payment gateway (ATOS, iDEAL, SOFORT...)',
    '137' : 'Wallet type not allowed',
    '138' : 'Unavailable functionality (depends on your contract)',
    '143' : 'Transaction not found. If searching for a transaction : please fill in one of the search field If validating a transaction : transaction does not exist or status does not allow validation',
    '146' : 'Incorrect wallet status',
    '147' : 'Wallet not found',
    '151' : 'Amount not allowed (higher than refundable amount, or lower than 0.50€ for a card payment, not allowed according to your contract, or too high. Please contact support)',
    '152' : 'Wallet ID already exists',
    '167' : 'Wallet blocked for security reason',
    '170' : 'Invalid operation returned by the payment gateway (ATOS, iDEAL, SOFORT...)',
    '171' : 'Operation refused by the payment gateway (ATOS, iDEAL, SOFORT...)',
    '172' : 'Internal error in the payment gateway (ATOS, iDEAL, SOFORT…)',
    '188' : 'Incorrect amount format',
    '190' : 'Internal error in the card payment processing (VISA, MASTERCARD)',
    '204' : 'Email already used',
    '209' : 'Fraud suspicion from the payment gateway (ATOS, iDEAL, SOFORT…)',
    '212' : 'Bad card data format',
    '215' : 'No approved IBAN found for this wallet',
    '219' : 'Card ID not found',
    '221' : 'Bad IBAN data format',
    '234' : 'Bad input data',
    '235' : 'File too big or wrong format',
    '236' : 'IP in input parameter is blacklisted',
    '237' : 'Email is blacklisted',
    '238' : 'IBAN is blacklisted',
    '241' : 'A document of same type is already pending review by LW\'s KYC services',
    '242' : 'Wrong BIC/SWIFT code format',
    '243' : 'Type of document does not exist',
    '244' : 'SDD mandate not found',
    '245' : 'SDD mandate invalid',
    '246' : 'SDD mandate currently already in use for a direct debit',
    '247' : 'Wrong date format',
    '248' : 'Wrong IP format',
    '249' : 'Mobile number mandatory for electronic signature',
    '250' : 'Type mandatory',
    '251' : 'Address mandatory',
    '252' : 'Wrong first or last name format',
}