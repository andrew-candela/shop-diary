from shop_diary.diary import lambda_handler
from shop_diary.lib.torque import exact_result


def create_test_event(size):
    return {
        'request': {
            'type': 'IntentRequest',
            'requestId': 'amzn1.echo-api.request.requestUUID',
            'locale': 'en-US',
            'timestamp': '2021-04-25T22:20:15Z',
            'intent': {
                'name': 'torque_specs',
                'confirmationStatus': 'NONE',
                'slots': {
                    'bolt_size': {
                        'name': 'bolt_size',
                        'value': f'{size}',
                        'confirmationStatus': 'NONE',
                        'source': 'USER'
                    }
                }
            },
            'dialogState': 'COMPLETED'
        }
    }


def test_lambda_handler():
    bolt_size = 10
    output = lambda_handler(create_test_event(bolt_size), {})
    print(output['response']['outputSpeech'])
    assert output['response']['outputSpeech']['ssml'] == \
        f"<speak>{exact_result.format(size=bolt_size, spec=55)}</speak>"


if __name__ == "__main__":
    test_lambda_handler()
