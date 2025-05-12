import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Socket.server_connector as connector

from unittest.mock import MagicMock, ANY

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
    # Set up the fake client
    host = '127.0.0.1'
    port = 3333
    message = 'dummy message'
    client = connector.Client(host, port, message)

    # Mock the message sender
    client.message_sender = MagicMock()

    # Prepare a normal request
    null = None
    request = {
        "request": "play",
        "state": {
            "players": ["LUR", "FKY"],
            "current": 0,
            "board": [null, "BDEC", null, null, null, null, null, null,
                      null, null, null, null, null, null, null, null],
            "piece": "BLEP"
        }
    }

    # Test normal behavior (no crash, move is generated)
    client.response_treatment(request)

    client.message_sender.assert_called_once_with({
        "response": "move",
        "move": ANY,  # We don't know exactly what move will be, it's dynamic
        "message": "Carotte"
    })


