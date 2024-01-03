# core imports
import logging
import time
import hashlib

# django imports
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# 3rd party imports
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers  # , status
from rest_framework.decorators import permission_classes, api_view

# simpris imports
from ...models.models import Account


logger = logging.getLogger(__name__)


# serializer for accounts
class APIAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('accountname', 'authenticationid', 'authenticationid2', 'authenticationid3', 'membershiptypeid', 'membershiprenewaldate',
                  'firstname', 'lastname', 'phone', 'email', 'createddate', 'createdby', 'updatedate', 'updatedby')


@permission_classes((AllowAny, ))
@csrf_exempt
def auto(request):

    logger.info('------------------------------')
    logger.info('FastSpring notification start')

    logger.info('Start auto processing')

    security_data = request.POST.get('security_data') or None
    security_hash = request.POST.get('security_hash') or None

    if security_data == None or security_hash == None:
        logger.info('Fastspring - Input data empty')
        logger.error('Fastspring - Account AUTO Input data empty')
        raise ValueError('Subscription API post with bad data')

    logger.info('Input data: ' + security_data)
    logger.info('Input security hash: ' + security_hash)

    privatekey = '6fe948252c91a91cde78e889d5e7d0eb'

    security_data_unicode = security_data.encode('utf-8')
    security_hash_unicode = security_hash.encode('utf-8')
    privatekey_unicode = privatekey.encode('utf-8')

    logger.info('Past encoding commands')

    against = ' against '
    logger.info('After against string creation')
    against_unicode = against.encode('utf-8')

    logger.info('Ready for compare...')
    combined_security_unicode_str = str(hashlib.md5(security_data_unicode + privatekey_unicode))
    combined_security_unicode = hashlib.md5(security_data_unicode + privatekey_unicode)
    logger.info('Combined_security_unicode: ' + combined_security_unicode_str)
    if combined_security_unicode != security_hash_unicode:
        md5Error = str(hashlib.md5(security_data_unicode + privatekey_unicode + against_unicode + security_hash_unicode))
        logging.error('FastSpring notification mismatch failure: ' + md5Error)
    #    response = {'Error': 500}
    #    return Response(response)

    logger.info('Hashed data received OK')

    order_id = request.POST.get('SubscriptionReference') or None
    first_name = request.POST.get('subscription.customer.firstName') or None
    last_name = request.POST.get('subscription.customer.lastName') or None
    country = request.POST.get('AddressCountry') or None
    company = request.POST.get('subscription.customer.companyName') or None
    phone = request.POST.get('subscription.customer.phone') or None
    email = request.POST.get('subscription.customer.email') or None
    customer_reference = request.POST.get('SubscriptionReference') or None
    product = request.POST.get('subscription.productName') or None
    referrer = request.POST.get('SubscriptionReferrer') or None

    logger.info('Data processed into variables')

    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')

    if product == 'Simpris-Medium':
        membershiptypeid = 30
    elif product == 'Simpris-Micro':
        membershiptypeid = 10
    elif product == 'Simpris-Large':
        membershiptypeid = 40
    elif product == 'Simpris-Small':
        membershiptypeid = 20
    elif product == 'Simpris-Corporate':
        membershiptypeid = 50
    else:
        membershiptypeid = 10

    logger.info('Order ID: ' + str(order_id))
    logger.info('First name: ' + str(first_name))
    logger.info('Last name: ' + str(last_name))
    logger.info('Country: ' + str(country))
    logger.info('Company: ' + str(company))
    logger.info('Phone: ' + str(phone))
    logger.info('Email: ' + str(email))
    logger.info('Customer reference: ' + str(customer_reference))
    logger.info('Product: ' + str(product))
    logger.info('Referrer: ' + str(referrer))

    if referrer != None:
        account_id = referrer[0:referrer.index("-")]
        logger.info('Account: ' + account_id)
    else:
        account_id = None

    logger.info('Account: ' + str(account_id))

    account_serializer = APIAccountSerializer(data={'accountid': account_id,
                                                    'accountname': 'DUMMY',
                                                    'authenticationid': order_id,
                                                    'authenticationid2': customer_reference,
                                                    'authenticationid3': product,
                                                    'membershiptypeid': membershiptypeid,
                                                    'membershiprenewaldate': updated_date,
                                                    'firstname': first_name,
                                                    'lastname': last_name,
                                                    'phone': phone,
                                                    'email': email,
                                                    'updatedate': updated_date,
                                                    'updatedby': 0,
                                                    'createddate': updated_date,
                                                    'createdby': 0})

    logger.info('Serializer loaded')

    if account_serializer.is_valid():

        logger.info('Serializer OK')
        acc = Account.objects.get(accountid=account_id)
        acc.authenticationid = order_id
        acc.authenticationid2 = customer_reference
        acc.authenticationid3 = product
        acc.membershiptypeid = membershiptypeid
        acc.membershiprenewaldate = updated_date
        acc.updatedby = 0
        acc.updatedate = updated_date
        # acc.createdby = acc.createdby
        # acc.createddate = acc.createddate
        acc.save(
            update_fields=['authenticationid', 'authenticationid2', 'authenticationid3', 'membershiptypeid', 'membershiprenewaldate',
                           'updatedate', 'updatedby'])

        logger.info('dB update OK')
        # response = {account_id}
        # return Response(account_id, status=200, template_name=None, headers=None, content_type=None)
        # return Response(account_id, status=status.HTTP_200_OK)
        return HttpResponse()
    else:
        logger.info("Serializer Error")
        raise serializers.ValidationError(account_serializer.errors)
