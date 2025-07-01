import requests
import json

from config import url, rules
from mail import send_smtp_email
from notification import send_msg

def get_rates():
    """
    send a get requests to the fixer.io api and get live rates
    :return: request.Response instance
    """
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    """
    get filename and rates, save them to the specific directory
    :param filename:
    :param rates:
    :return: None
    """
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    """
    get timestamp and rates, check if there is preferred rates and
    then send email through smtp
    :param timestamp:
    :param rates:
    :return:
    """
    subject = f'{timestamp} rates'

    if rules['email']['preferred'] is not None:
        tmp = dict()
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp

    text = json.dumps(rates)

    send_smtp_email(subject, text)


def check_notify_rules(rates):
    '''
    check if the rates are in the preferred range and if user defined  
    :param rates:
    :return: msg(string)
    '''
    preferred = rules['notification']['preferred']
    msg = ''
    for exc in preferred.keys():
        min_val = float(preferred[exc]['min'])
        max_val = float(preferred[exc]['max'])

        if rates[exc] <= min_val:
            msg += f'{exc} is below the minimum value {rates[exc]}\n'
        if rates[exc] >= max_val:
            msg += f'{exc} is above the maximum value {rates[exc]}\n'
    print(msg)
    return msg
 
def send_notification(msg):
    send_msg(msg)
    


if __name__ == "__main__":
    res = get_rates()

    if rules['archive']:
        archive(res['timestamp'], res['rates'])

    if rules['email']['enable']:
        send_mail(res['timestamp'], res['rates'])

    if rules['notification']['enable']:
        notification_msg = check_notify_rules(res['rates'])
        if notification_msg:
            send_notification(notification_msg)