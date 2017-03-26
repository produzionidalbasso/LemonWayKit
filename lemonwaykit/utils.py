from __future__ import unicode_literals
import sys

from xml.parsers.expat import ExpatError
from pysimplesoap.client import SoapClient, SimpleXMLElement
from .exceptions import InvalidParameterError, ApiMethodError
from .constants import VALID_LEMONAY_METHOD_PARAMETERS

if sys.version > '3':
    unicode = str


class LemonWayKit:
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

        self._direct_kit_url = "https://ws.lemonway.fr/mb/%s/%s/directkit/service.asmx" % (
            self._environment, "dev" if dev else "prod"
        )
        self._web_kit_url = "https://webkit.lemonway.fr/mb/%s/%s/" % (
            self._environment, "dev" if dev else "prod"
        )

        self._client = SoapClient(
            location=self._direct_kit_url,
            cache=None,
            timeout=self._timeout,
            soap_ns=self._soap_ns,
            action=self._action,
            namespace=self._namespace,
            trace=False
        )

    def fast_pay(self, version="1.2", **kwargs):
        return self._make_request('FastPay', version, **kwargs)

    def register_wallet(self, version="1.1", **kwargs):
        return self._make_request('RegisterWallet', version, **kwargs)

    def update_wallet_details(self, version="1.0", **kwargs):
        return self._make_request('UpdateWalletDetails', version, **kwargs)

    def update_wallet_status(self, version="1.0", **kwargs):
        return self._make_request('UpdateWalletStatus', version, **kwargs)

    def get_wallet_details(self, version="1.7", **kwargs):
        return self._make_request('GetWalletDetails', version, **kwargs)

    def money_in(self, version="1.1", **kwargs):
        return self._make_request('MoneyIn', version, **kwargs)

    def money_in_3d_init(self, version="1.1", **kwargs):
        return self._make_request('MoneyIn3DInit', version, **kwargs)

    def money_in_3d_confirm(self, version="1.1", **kwargs):
        return self._make_request('MoneyIn3DConfirm', version, **kwargs)

    def money_in_web_init(self, version="1.2", **kwargs):
        return self._make_request('MoneyInWebInit', version, **kwargs)

    def register_card(self, version="1.2", **kwargs):
        return self._make_request('RegisterCard', version, **kwargs)

    def unregister_card(self, version="1.0", **kwargs):
        return self._make_request('UnregisterCard', version, **kwargs)

    def money_in_with_card_id(self, version="1.1", **kwargs):
        return self._make_request('MoneyInWithCardId', version, **kwargs)

    def money_in_validate(self, version="1.0", **kwargs):
        return self._make_request('MoneyInValidate', version, **kwargs)

    def send_payment(self, version="1.0", **kwargs):
        return self._make_request('SendPayment', version, **kwargs)

    def register_iban(self, version="1.1", **kwargs):
        return self._make_request('RegisterIBAN', version, **kwargs)

    def money_out(self, version="1.3", **kwargs):
        return self._make_request('MoneyOut', version, **kwargs)

    def get_payment_details(self, version="1.0", **kwargs):
        return self._make_request('GetPaymentDetails', version, **kwargs)

    def get_money_in_trans_details(self, version="1.6", **kwargs):
        return self._make_request('GetMoneyInTransDetails', version, **kwargs)

    def get_money_out_trans_details(self, version="1.4", **kwargs):
        return self._make_request('GetMoneyOutTransDetails', version, **kwargs)

    def upload_file(self, version="1.1", **kwargs):
        return self._make_request('UploadFile', version, **kwargs)

    def get_kyc_status(self, version="1.5", **kwargs):
        return self._make_request('GetKycStatus', version, **kwargs)

    def get_money_in_iban_details(self, version="1.4", **kwargs):
        return self._make_request('GetMoneyInIBANDetails', version, **kwargs)

    def refund_money_in(self, version="1.2", **kwargs):
        return self._make_request('RefundMoneyIn', version, **kwargs)

    def get_balances(self, version="1.0", **kwargs):
        return self._make_request('GetBalances', version, **kwargs)

    def money_in_3d_authenticate(self, version="1.0", **kwargs):
        return self._make_request('MoneyIn3DAuthenticate', version, **kwargs)

    def create_gift_code_amazon(self, version="1.0", **kwargs):
        return self._make_request('CreateGiftCodeAmazon', version, **kwargs)

    def money_in_deal_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInIDealInit', version, **kwargs)

    def money_in_deal_confirm(self, version="1.0", **kwargs):
        return self._make_request('MoneyInIDealConfirm', version, **kwargs)

    def register_sdd_mandate(self, version="1.0", **kwargs):
        return self._make_request('RegisterSddMandate', version, **kwargs)

    def unregister_sdd_mandate(self, version="1.0", **kwargs):
        return self._make_request('UnregisterSddMandate', version, **kwargs)

    def money_in_sdd_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInSddInit', version, **kwargs)

    def get_money_in_sdd(self, version="1.0", **kwargs):
        return self._make_request('GetMoneyInSdd', version, **kwargs)

    def get_money_in_cheque_details(self, version="1.9", **kwargs):
        return self._make_request('GetMoneyInChequeDetails', version, **kwargs)

    def get_wallet_trans_history(self, version="1.8", **kwargs):
        return self._make_request('GetWalletTransHistory', version, **kwargs)

    def get_chargebacks(self, version="1.8", **kwargs):
        return self._make_request('GetChargebacks', version, **kwargs)

    def money_in_cheque_init(self, version="1.0", **kwargs):
        return self._make_request('MoneyInChequeInit', version, **kwargs)

    def sign_document_init(self, version="1.0", **kwargs):
        return self._make_request('SignDocumentInit', version, **kwargs)

    def create_vcc(self, version="1.0", **kwargs):
        return self._make_request('CreateVCC', version, **kwargs)

    def money_in_neosurf(self, version="1.0", **kwargs):
        return self._make_request('MoneyInNeosurf', version, **kwargs)

    def get_wizpay_ads(self, version="1.0", **kwargs):
        return self._make_request('GetWizypayAds', version, **kwargs)

    def create_money_in_web_url(self, token):
        url = "%s?moneyInToken=%s&lang=%s" % (self._web_kit_url, token, self._language)
        if self._direct_kit_css:
            url = "%s&p=%s" % (url, self._direct_kit_css)
        return url

    @staticmethod
    def _parse_response(method, res):
        try:
            res_text = str(getattr(getattr(res, "%sResponse" % method), "%sResult" % method))
            res_xml = SimpleXMLElement(res_text)
        except AttributeError:
            return None
        except ExpatError:
            return None

        if res_xml.get_name() == 'E':
            code = int(res_xml.Code)
            message = unicode(res_xml.Msg)
            raise ApiMethodError(code, message)

        return res_xml

    def _make_request(self, method, version, **kwargs):
        params = {}

        for key in kwargs:
            if key not in VALID_LEMONAY_METHOD_PARAMETERS.get(method):
                raise InvalidParameterError()
            params.update({key: kwargs.get(key)})

        params.update({
            'version': version,
            'wlLogin': self._wl_login,
            'wlPass': self._wl_pass,
            'language': self._language,
            'walletIp': self._wallet_ip,
            'walletUa': self._wallet_ua
        })

        res = getattr(self._client, method)(**params)
        return LemonWayKit._parse_response(method, res)
