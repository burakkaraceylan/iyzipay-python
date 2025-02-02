# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'subscriptionReferenceCode': '8d614e87-0b10-4112-98c3-14b201c23f28',
}

report = iyzipay.Subscriptions().retrieve(request, options)
print(report.read().decode('utf-8'))
