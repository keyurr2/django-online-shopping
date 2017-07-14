from django.shortcuts import render
from .models import ProductDetails, Tag
import paypalrestsdk
from django.http import JsonResponse
import json 
# Create your views here.
def index(request):

    products = ProductDetails.objects.all().order_by('-published_on')

    # if user need to filter products otherwise list all products
    
    if request.method == "POST":
        
        # Filter criteria
        search_query = request.POST.get("search_query", None)
        min_price = request.POST.get("min_price", None)
        max_price = request.POST.get("max_price", None)
        rating = request.POST.get("rating", None)
        tag = request.POST.get("tag", None)
    
        if search_query:
            products = ProductDetails.objects.filter(name__contains = search_query)
        if min_price:
            products = products.filter(price__gte = min_price)
        if max_price:
            products = products.filter(price__lte = max_price)
        if rating and rating != "-":
            products = products.filter(ratings = rating)
        if tag and tag != "-":
            products = products.filter(Tags__in = [tag])

    context = {
        'title':'list of products', 
        'products' : products,
        'rating' : ProductDetails.RATING_CHOICE,
        'tags' : Tag.objects.all()
    }
    return render(request, 'shop/list.html', context)


def create_payment(request):
    paypalrestsdk.configure({
        "mode": "sandbox", # sandbox or live
        "client_id": "EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM",
        "client_secret": "EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM" })
    payment_method = request.POST.get('payment_method', 'paypal')
    if payment_method == 'paypal' : 
        # Payment
        # A Payment Resource; create one using
        # the above types and intent as 'sale'
        payment = paypalrestsdk.Payment({
            "intent": "sale",

            # Payer
            # A resource representing a Payer that funds a payment
            # Payment Method as 'paypal'
            "payer": {
                "payment_method": "paypal"},

            # Redirect URLs
            "redirect_urls": {
                "return_url": "http://localhost:8000/execute-payment",
                "cancel_url": "http://localhost:8000/"},

            # Transaction
            # A transaction defines the contract of a
            # payment - what is the payment for and who
            # is fulfilling it.
            "transactions": [{

                # ItemList
                "item_list": {
                    "items": [{
                        "name": "item",
                        "sku": "item",
                        "price": "1.00",
                        "currency": "USD",
                        "quantity": 1}]},

                # Amount
                # Let's you specify a payment amount.
                "amount": {
                    "total": "1.00",
                    "currency": "USD"},
                "description": "This is the payment transaction description."}]})

        # Create Payment and return status
        if payment.create():            
            print("Payment[%s] created successfully" % (payment.id))
            # print(payment)
            # Redirect the user to given approval url
            for link in payment.links:
                if link.rel == "approval_url":
                    approval_url = str(link.href)
                    print("Redirect for approval: %s" % (approval_url))
            return JsonResponse({'status' : 'success', 'approval_url' : approval_url})
        else:
            print("Error while creating payment:")          
            return JsonResponse({'status' : 'failed', 'error' : payment.error})
    elif payment_method == 'credit_card':
        # Payment
        # A Payment Resource; create one using
        # the above types and intent as 'sale'
        payment = paypalrestsdk.Payment({        
            "intent": "sale",

            # Payer
            # A resource representing a Payer that funds a payment
            # Use the List of `FundingInstrument` and the Payment Method
            # as 'credit_card'
            "payer": {
                "payment_method": "credit_card",

                # FundingInstrument
                # A resource representing a Payeer's funding instrument.
                # Use a Payer ID (A unique identifier of the payer generated
                # and provided by the facilitator. This is required when
                # creating or using a tokenized funding instrument)
                # and the `CreditCardDetails`
                "funding_instruments": [{

                    # CreditCard
                    # A resource representing a credit card that can be
                    # used to fund a payment.
                    "credit_card": {
                        "type": "visa",
                        "number": "4417119669820331",
                        "expire_month": "11",
                        "expire_year": "2018",
                        "cvv2": "874",
                        "first_name": "Joe",
                        "last_name": "Shopper",

                        # Address
                        # Base Address used as shipping or billing
                        # address in a payment. [Optional]
                        "billing_address": {
                            "line1": "52 N Main ST",
                            "city": "Johnstown",
                            "state": "OH",
                            "postal_code": "43210",
                            "country_code": "US"}}}]},
            # Transaction
            # A transaction defines the contract of a
            # payment - what is the payment for and who
            # is fulfilling it.
            "transactions": [{

                # ItemList
                "item_list": {
                    "items": [{
                        "name": "item",
                        "sku": "item",
                        "price": "1.00",
                        "currency": "USD",
                        "quantity": 1}]},

                # Amount
                # Let's you specify a payment amount.
                "amount": {
                    "total": "1.00",
                    "currency": "USD"},
                "description": "This is the payment transaction description."}]})

        # Create Payment and return status( True or False )
        if payment.create():
            print("Payment[%s] created successfully" % (payment.id))
            return JsonResponse({'status' : 'success', 'payment' : 'Payment created successfully for ID : '+payment.id})
        else:
            # Display Error message
            print("Error while creating payment:")
            # print(payment.error)
            return JsonResponse({'status' : 'failed', 'error' : payment.error})

## Id of Payment, Payer's ID once we have visited the URL provide while creating payment 
def execute_payment(request):
    # ID of the payment. This ID is provided when creating payment.
    # http://localhost:8000/execute-payment?paymentId=PAY-9V4804912B855184VLFUK2QY&token=EC-2VJ23511L14767440&PayerID=K5PYYZ4395SVQ
    paypalrestsdk.configure({
        "mode": "sandbox", # sandbox or live
        "client_id": "EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM",
        "client_secret": "EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM" })    
    paymentId = str(request.GET.get('paymentId', None))
    PayerID = str(request.GET.get('PayerID', None))

    payment = paypalrestsdk.Payment.find(paymentId)

    if payment.execute({"payer_id": PayerID}): # return True or False
        print("Payment[%s] execute successfully" % (payment.id))
        return JsonResponse({'status' : 'success', 'payment' : 'Payment successfully executed for ID : '+ payment.id})
    else :      
        return JsonResponse({'status' : 'failed', 'error' : payment.error})