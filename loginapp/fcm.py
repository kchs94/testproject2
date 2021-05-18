def sendFcm(userId):
    with open('user_id.txt', 'wb+') as destination:
        for chunk in userId.chunks():
            destination.write(chunk)
