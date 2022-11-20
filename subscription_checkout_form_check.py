# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}


request = {
    'token': 'token',
}

checkout_form_initialize = iyzipay.SubscriptionCheckoutForm().get(request, options)

print(checkout_form_initialize.read().decode('utf-8'))
