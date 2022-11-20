import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'paymentId': '6e55f05b-bdcc-4399-ab31-9b87c00c6337',
    # 'paymentConversationId': '123456789'
}

payment = iyzipay.Payment().retrieve(request, options)

print(payment.read().decode('utf-8'))
