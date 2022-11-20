# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'referenceCode': '8a8eaa5b-a2b0-4d88-a6d4-877d69ddd0ab'
}

report = iyzipay.SubscriptionPlan().retrieve(request, options)
print(report.read().decode('utf-8'))
