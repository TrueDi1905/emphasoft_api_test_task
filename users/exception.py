from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return response
    if response.status_code == 403:
        return Response({'ошибка': 'Нельзя редактировать чужой аккаунт!'})
    if response.status_code == 401:
        return Response({'ошибка': 'Зарегистрируйтесь пожалуйста!'})
    return response
