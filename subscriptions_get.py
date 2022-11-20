# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'page': 1,
    'count': 10,
    'subscriptionReferenceCode': '55a85da1-9b83-41a3-9fed-d270456da8ae'
}

report = iyzipay.Subscriptions().get(request, options)
print(report.read().decode('utf-8'))
