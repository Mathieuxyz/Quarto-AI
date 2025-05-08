import Socket.server_connector as connector

from unittest.mock import MagicMock

def test_initalization(): #working fine

    host = '127.0.0.0'
    port = 3333
    message = 'message de test'
    client = connector.Client(host, port, message)

    assert client.host == host
    assert client.port == port
    assert client.message == message

def test_response_treatment_ping(): #working fine

    host = '127.0.0.0'
    port = 3333
    message = 'message de test'
    client = connector.Client(host, port, message)
    
    client.message_sender = MagicMock()

    request = {"request": "ping"}
    client.response_treatment(request)

    client.message_sender.assert_called_once_with({"response": "pong"})


def test_response_treatment_play():
    host = '127.0.0.0'
    port = 3333
    message = 'message de test'
    client = connector.Client(host, port, message)

    client.message_sender = MagicMock()

    request = {"request": "play", "state": {"players": ["LUR", "FKY"],"current": 0,"board": [null,"BDEC",null,"SDFP",null,null,null,null,null,"SLFC",null,null,"BLFP","BLEC",null,null], "piece": "BLEP"}}
    client.response_treatment(request)

    client.message_sender.assert_called_once_with({"response": "move", "move": any, "message": "La calotte de tes morts"})
    assert isinstance(args[0]['move'], dict)

