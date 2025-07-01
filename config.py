from gc import enable


BASE_PATH = 'http://data.fixer.io/api/latest?access_key='
API_KEY = '1efae8c05a77a3bafc8754fbd12e43f2'

url = BASE_PATH + API_KEY

EMAIL_RECEIVER = "test@example.com"
# rules = {
#     'archive': True,
#     'send_mail': True,
#     # preferred default is None
#     # 'preferred': None
#     'preferred': ['BTC', 'IRR', "IQD", "USD", "CAD", "AED"]
# }

rules = {
    "archive": True,
    "email": {
        "receiver": 'example@gmail.com',
        "enable": True,
        "preferred": ["BTC", "IRR", "IQD", "USD", "CAD", "AED"],
    },
    "notification": {
        "enable": True,
        "receiver": '09107731631',
        "preferred": {
            'BTC': {'min': 0.000101, 'max': 0.000109},
            'IRR': {'min': 49430.900000, 'max': 49430.107521},
            }
        
    }
}