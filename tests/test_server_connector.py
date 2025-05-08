import Socket.server_connector as connector

def test_initalization():

    port = '127.0.0.0'
    host = 3333
    message = 'message de test'
    client = connector.Client(port, host, message)

    assert client.port == port
    assert client.host == host
    assert client.message == message

def test_response_treatment_ping():

    client = connector.Client()
    request = {"request": "ping"}
    client.response_treatment(request)

    client.message_sender.assert_called_once_with({"response": "pong"})


def test_response_treatment_play():
    client = connector.Client()
    request = {"request": "play"}
    client.response_treatment(request)

    client.message_sender.assert_called_once_with({"response": "move", "move": set(), "message": "La calotte de tes morts"})


