import logging, datetime, pytz
# import stripe

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from ...library.user_context import UserContextFull

logger = logging.getLogger(__name__)

# Create your views here.
@login_required
def upgrade(request):
    
    logger.info('account upgrade')    
            
    userContext = UserContextFull(request)
    now = timezone.now()
    userContextSubID = "{}-{}-{}{}{}{}{}".format(userContext.clientID, userContext.id, now.day, now.hour, now.minute, now.second, now.microsecond)
    context_dict = {'client': userContextSubID, 'usercontext': userContext, 'subscription_url': settings.BASE_URL_SUBSCRIPTION}
    return render(request, "simpris/account/upgrade.html", context_dict)

# NOTE this is for Stripe Gateway only
# def subscribe(request):
#     user_context = UserContextFull(request)
#
#     # check if customer already on stripe
#
#     # if customer not on stripe create customer and set plan in one call
#
#     # Set your secret key: remember to change this to your live secret key in production
#     # See your keys here https://dashboard.stripe.com/account/apikeys
#     stripe.api_key = settings.PGK
#
#     plan_in = request.POST.get('plan')
#     account_id = request.POST.get('account')
#
#     # Get customer details
#     account = Account.objects.get(account=account_id, clientid=user_context.clientID)
#
#
#     # Get the credit card details submitted by the form
#     token = request.POST['stripeToken']
#
#     # Create a Customer
#     customer = stripe.Customer.create(
#       source=token,
#       plan=plan_in,
#       email="payinguser@example.com"
#     )
#
#     # save customer
#     account.authenticationid = 'stripe'
#     account.authenticationid2 = customer.stripe_id


# def unsubscribe(request):
#     # unsubscribe
#     stripe.api_key = settings.PGK
#
#     customer = stripe.Customer.retrieve("cus_3R1W8PG2DmsmM9")
#     customer.subscriptions.retrieve("sub_3R3PlB2YlJe84a").delete()
