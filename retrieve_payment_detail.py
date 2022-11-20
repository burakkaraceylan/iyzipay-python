import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'paymentConversationId': 'c9ae835b-2060-428a-94c7-1181cbd5f3f7'
}
report = iyzipay.RetrievePaymentDetails().retrieve(request, options)
print(report.read().decode('utf-8'))
