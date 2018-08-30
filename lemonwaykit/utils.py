# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging

from pysimplesoap.client import SoapClient, SimpleXMLElement

from .exceptions import LemonWayInvalidParameterError, LemonWayApiMethodError
from .constants import VALID_LEMONWAY_METHOD_PARAMETERS

logger = logging.getLogger("lemonwaykit")

"""
Updated at 06 April '16
"""


class LemonWayKit(object):

    def __init__(self, environment="test", wl_login="society", wl_pass="123456", wallet_ip="", wallet_ua="",
                 language="fr", timeout=30, direct_kit_css=None, dev=True):
        self._environment = environment
        self._wl_login = wl_login
        self._wl_pass = wl_pass
        self._language = language
        self._wallet_ip = wallet_ip
        self._wallet_ua = wallet_ua

        self._timeout = timeout
        self._soap_ns = "soap12env"
        self._namespace = "Service_mb"
        self._action = "%s/" % self._namespace

        self._direct_kit_css = direct_kit_css

        self._direct_kit_domain = 'https://sandbox-api.lemonway.fr' if dev else 'https://ws.lemonway.fr'
        self._direct_kit_url = "%s/mb/%s/%s/directkit/service.asmx" % (
            self._direct_kit_domain, self._environment, "dev" if dev else "prod"
        )

        # print("direct_kit_url : %s"%self._direct_kit_url)
        self._web_kit_url = self.get_web_kit_url(dev)
        # print("web_kit_url : %s"%self._web_kit_url)
        self._client = SoapClient(
            location=self._direct_kit_url,
            cache=None,
            timeout=self._timeout,
            soap_ns=self._soap_ns,
            action=self._action,
            namespace=self._namespace,
            trace=False
        )
        print 'lmk ', locals()
        # print("self._client : %s"%self._client)

    def get_web_kit_url(self, dev):
        from django.conf import settings
        domain = getattr(settings, 'LEMONWAY_WEB_KIT_DOMAIN', 'https://m.lemonway.fr')
        url = "{domain}/{enviroment}/{dev}/".format(
            domain=domain,
            enviroment=self._environment,
            dev=("dev" if dev else "prod")
        )
        return url

    def fast_pay(self, version="1.2", **kwargs):
        return self._make_request('FastPay', version, **kwargs)

    #####################
    #####################
    ###  DIRECT KIT #####
    #####################
    #####################

    #######
    ## MANAGE WALLETS
    #########
    def register_wallet(self, version="1.1", **kwargs):
        return self._make_request('RegisterWallet', version, **kwargs)

    def get_wallet_details(self, version="1.8", **kwargs):
        """http://documentation.lemonway.fr/api-en/directkit/manage-wallets/getwalletdetails-getting-detailed-wallet-data
        @UPDATED FROM 1.7 --> New :CARDS List of cards linked to the wallet"""
        return self._make_request('GetWalletDetails', version, **kwargs)

    def update_wallet_details(self, version="1.0", **kwargs):
        return self._make_request('UpdateWalletDetails', version, **kwargs)

    def upload_file(self, version="1.1", **kwargs):
        return self._make_request('UploadFile', version, **kwargs)

    def get_kyc_status(self, version="1.5", **kwargs):
        return self._make_request('GetKycStatus', version, **kwargs)

    def update_wallet_status(self, version="1.0", **kwargs):
        return self._make_request('UpdateWalletStatus', version, **kwargs)

    def get_balances(self, version="1.0", **kwargs):
        return self._make_request('GetBalances', version, **kwargs)

    def get_wallet_trans_history(self, version="1.8", **kwargs):
        #@TODO update to 2.0
        return self._make_request('GetWalletTransHistory', version, **kwargs)

    ###############
    #### MONEY IN :Credit a wallet
    #############

    #### MONEY IN : By Card

    def money_in_web_init(self, version="1.2", **kwargs):
        #@TODO update to 1.3
        return self._make_request('MoneyInWebInit', version, **kwargs)

    def money_in(self, version="1.1", **kwargs):
        return self._make_request('MoneyIn', version, **kwargs)

    def money_in_3d_init(self, version="1.1", **kwargs):
        #NOT USED
        return self._make_request('MoneyIn3DInit', version, **kwargs)

    def money_in_3d_authenticate(self, version="1.0", **kwargs):
        return self._make_request('MoneyIn3DAuthenticate', version, **kwargs)

    def money_in_3d_confirm(self, version="1.1", **kwargs):
        return self._make_request('MoneyIn3DConfirm', version, **kwargs)

    def register_card(self, version="1.2", **kwargs):
        return self._make_request('RegisterCard', version, **kwargs)

    def unregister_card(self, version="1.0", **kwargs):
        return self._make_request('UnregisterCard', version, **kwargs)

    def money_in_with_card_id(self, version="1.1", **kwargs):
        return self._make_request('MoneyInWithCardId', version, **kwargs)

    def money_in_validate(self, version="1.0", **kwargs):
        return self._make_request('MoneyInValidate', version, **kwargs)

    #### MONEY IN : By Bank wire (SCT, Sepa Credit Transfer

    def get_money_in_iban_details(self, version="1.4", **kwargs):
        return self._make_request('GetMoneyInIBANDetails', version, **kwargs)

    #### MONEY IN : By cheque

    def money_in_cheque_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInChequeInit', version, **kwargs)

    def get_money_in_cheque_details(self, version="1.9", **kwargs):
        return self._make_request('GetMoneyInChequeDetails', version, **kwargs)

    #### MONEY IN : By Sepa Direct Debit (SDD)

    def register_sdd_mandate(self, version="1.0", **kwargs):
        return self._make_request('RegisterSddMandate', version, **kwargs)

    def unregister_sdd_mandate(self, version="1.0", **kwargs):
        return self._make_request('UnregisterSddMandate', version, **kwargs)

    def sign_document_init(self, version="1.0", **kwargs):
        return self._make_request('SignDocumentInit', version, **kwargs)

    def money_in_sdd_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInSddInit', version, **kwargs)

    def get_money_in_sdd(self, version="1.0", **kwargs):
        return self._make_request('GetMoneyInSdd', version, **kwargs)

    #### MONEY IN : By iDEAL

    def money_in_deal_confirm(self, version="1.0", **kwargs):
        return self._make_request('MoneyInIDealConfirm', version, **kwargs)

    def money_in_deal_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInIDealInit', version, **kwargs)

    #### MONEY IN : By SOFORT
    """
    #@TODO Implement it
    def money_in_sofort_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInSofortInit', version, **kwargs)
    """

    #### MONEY IN : By Neosurf

    def money_in_neosurf(self, version="1.0", **kwargs):
        # You need a specific contract in order to use this functionality. Please contact us.
        return self._make_request('MoneyInNeosurf', version, **kwargs)

    #### MONEY IN : ----

    def get_money_in_trans_details(self, version="1.8", **kwargs):
        #@TODO update to 1.8 da 1.6
        return self._make_request('GetMoneyInTransDetails', version, **kwargs)

    #### MONEY IN : By MB WAY/Multibanco/Payshop (Portuguese payment methods)

    """
    #@TODO Implement these
    def money_in_mbway_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInMbwayInit', version, **kwargs)
    def money_in_multibanco_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInMultibancoInit', version, **kwargs)
    def money_in_payshop_init_(self, version="1.0", **kwargs):
        return self._make_request('MoneyInPayshopInit', version, **kwargs)
    """

    ###############
    #### MONEY OUT : debit a wallet (and credit a bank account)
    #############

    def register_iban(self, version="1.1", **kwargs):
        return self._make_request('RegisterIBAN', version, **kwargs)

    def money_out(self, version="1.3", **kwargs):
        #http://documentation.lemonway.fr/api-en/directkit/money-out-debit-a-wallet-and-credit-a-bank-account/moneyout-external-fund-transfer-from-a-wallet-to-a-bank
        return self._make_request('MoneyOut', version, **kwargs)

    def get_money_out_trans_details(self, version="1.4", **kwargs):
        return self._make_request('GetMoneyOutTransDetails', version, **kwargs)

    ##################
    ##### P2P : transfer between wallets
    #############

    def get_payment_details(self, version="1.0", **kwargs):
        # looking for payments between wallets
        return self._make_request('GetPaymentDetails', version, **kwargs)

    def send_payment(self, version="1.0", **kwargs):
        # ON-US payment between Wallets
        return self._make_request('SendPayment', version, **kwargs)

    ######################
    ####### Other Functions
    ###############

    def refund_money_in(self, version="1.2", **kwargs):
        return self._make_request('RefundMoneyIn', version, **kwargs)

    def get_chargebacks(self, version="1.8", **kwargs):
        # get list of chargebacks from a given date
        return self._make_request('GetChargebacks', version, **kwargs)

    def create_vcc(self, version="1.0", **kwargs):
        # generating a Virtual Credit Card
        return self._make_request('CreateVCC', version, **kwargs)

    def get_wizpay_ads(self, version="1.0", **kwargs):
        # get offers and ads list of Wizypay’s affiliate merchants
        return self._make_request('GetWizypayAds', version, **kwargs)

    #####################
    #####################
    ###  WEB KIT ########
    #####################
    #####################

    def create_money_in_web_url(self, token, template_name=None, web_kit_url=None):
        # Finalize card payment, indirect mode
        # http://documentation.lemonway.fr/api-en/webkit/finalize-card-payment-indirect-mode
        if not web_kit_url:
            url = "%s?moneyInToken=%s&lang=%s" % (self._web_kit_url, token, self._language)
        else:
            url = "%s?moneyInToken=%s&lang=%s" % (web_kit_url, token, self._language)
        # ATOS v1 contracts
        if self._direct_kit_css:
            url = "%s&p=%s" % (url, self._direct_kit_css)
        # ATOS v2 contracts
        if template_name:
            url = "%s&tpl=%s" % (url, template_name)
        return url

    #####################
    #####################
    ###  ??????? ########
    #####################
    #####################

    def create_gift_code_amazon(self, version="1.0", **kwargs):
        # @TODO Not found in Documentation
        return self._make_request('CreateGiftCodeAmazon', version, **kwargs)

    @staticmethod
    def _parse_response(method, res):
        try:
            res_text = str(getattr(getattr(res, "%sResponse" % method), "%sResult" % method))
            res_xml = SimpleXMLElement(res_text)
        except Exception as ex:
            logger.exception("LWKIT Exception")
            return None

        if res_xml.get_name() == 'E':
            logger.error("LWKIT Error %s : %s " % (int(res_xml.Code), str(res_xml.Msg)))
            raise LemonWayApiMethodError(int(res_xml.Code), str(res_xml.Msg), int(res_xml.Prio))

        return res_xml

    def _make_request(self, method, version, **kwargs):
        params = {}
        for key in kwargs:
            print("key %s and value %s (type : %s) for LW method : %s"%(key, kwargs.get(key), type(kwargs.get(key)), method))
            if key not in VALID_LEMONWAY_METHOD_PARAMETERS.get(method):
                raise LemonWayInvalidParameterError()
            params.update({key: kwargs.get(key)})

        params.update({
            'version': version,
            'wlLogin': self._wl_login,
            'wlPass': self._wl_pass,
            'language': self._language,
            'walletIp': self._wallet_ip,
            'walletUa': self._wallet_ua
        })
        print("LWKIT call to method %s with params : %s for environment '%s'  direct_kit : %s"%(method,str(params),self._environment), self._direct_kit_url)
        res = getattr(self._client, method)(**params)
        print("res : %s" % str(res.as_xml))
        return LemonWayKit._parse_response(method, res)
