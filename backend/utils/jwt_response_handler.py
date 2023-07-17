from backend.accounts.serializers import BlogUserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'status': 20000,
        "data": {
            "token": token,
            # "user": BlogUserSerializer(user).data
        }
    }
