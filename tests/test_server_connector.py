import Socket.server_connector as connector
import fake_server as server

server.main() #création du serveur fictif pour pytest

host = '127.0.0.1'
port = 3333
message = {"request": "subscribe", "port": 4000, "name": "Redbull"}

def test_init():

    monkeypatch.setattr(connector.Client, "subscribe", lambda self: None)

    client = connector.Client(host, port, message)

    assert client.port == port
    assert client.host == host
    assert client.message == message

def test_subscribe():

    try:

        monkeypatch.setattr(connector.Client, "connect_game", lambda self: None)
        connector.Client(host, port, message)
    
    except Exception:

        assert False, 'La connection na pas fonctionné'