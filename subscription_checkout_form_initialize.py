# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

address = {
    'contactName': 'Jane Doe',
    'city': 'Istanbul',
    'country': 'Turkey',
    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'zipCode': '34732'
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'pricingPlanReferenceCode': '8a8eaa5b-a2b0-4d88-a6d4-877d69ddd0ab',
    'subscriptionInitialStatus': 'ACTIVE',
    "callbackUrl": "https://www.merchant.com/callback",
    "customer": {
        'name': 'Adı',
        'surname': 'Soyadı',
        'email': 'test@iyzipay.com',
        'gsmNumber': '+905555555555',
        'identityNumber': 11111113333,
        'shippingAddress': address,
        'billingAddress': address,
    }

}

checkout_form_initialize = iyzipay.SubscriptionCheckoutForm().create(request, options)

print(checkout_form_initialize.read().decode('utf-8'))
