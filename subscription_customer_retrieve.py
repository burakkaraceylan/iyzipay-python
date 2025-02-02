# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '8138',
    'customerReferenceCode': '0fce1fe6-db69-4909-b514-03ec5d31b781',
}

report = iyzipay.SubscriptionCustomer().retrieve(request, options)
print(report.read().decode('utf-8'))
