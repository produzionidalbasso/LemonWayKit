from __future__ import unicode_literals

VALID_LEMONAY_METHOD_PARAMETERS = {
    'FastPay': [
        "clientMail", "clientTitle", "clientFirstName", "clientLastName", "cardType", "cardNumber", "cardCrypto",
        "cardDate", "creditWallet", "amount", "message", "autoCommission", "registerCard"
    ],
    'RegisterWallet': [
        "wallet", "clientName", "clientMail", "clientTitle", "clientFirstName", "clientLastName", "street",
        "postCode", "city", "ctry", "birthdate", "phoneNumber", "mobileNumber", "isCompany", "companyName",
        "companyWebsite", "companyDescription", "companyIdentificationNumber", "idDebtor", "nationality",
        "birthcity", "birthcountry"
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
        "errorUrl", "autoCommission"
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
