from Backend.RUDP.RUDPclient import RUDPclient
from Backend.Help.app_packet import AppHeader, Kind, Status_code
from Backend.Help.synagogue import Nosah, City


def send_login(connection: RUDPclient, mId, password):
    request = AppHeader(0, Kind.REQUEST_LOGIN.value, Nosah.NULL, City.NULL,
                        (mId + ',' + password).encode())

    response = connection.sendData(request)
    if response is None:
        return None
    return response


def send_request_all_gabai(connection: RUDPclient):
    request = AppHeader(0, Kind.REQUEST_ALL_GABAI.value, Nosah.NULL.value, City.NULL.value, b'')
    response = connection.sendData(request)

    if response.status_code == Status_code.NOT_FOUND.value:
        return None
    return send_request_gabai_by_id(connection, list(response.data))


def send_edit_syng(connection, syng):
    request = AppHeader(0, Kind.SET_SYNAGOGUE.value, Nosah.NULL, City.NULL, str(syng).encode())
    response = connection.sendData(request)
    return response.data.decode()


def send_edit_gabai(connection, gabai):
    request = AppHeader(0, Kind.SET_GABAI.value, Nosah.NULL, City.NULL, str(gabai).encode())
    response = connection.sendData(request)
    return response.data.decode()


def send_by_query(connection: RUDPclient, name, nosah, city):
    request = AppHeader(0, Kind.REQUEST_BY_QUERY.value, nosah, city, name.encode())
    response = connection.sendData(request)

    if response.status_code == Status_code.NOT_FOUND.value:
        return None
    return send_request_syng_by_id(connection, list(response.data))


def send_request_syng_by_id(connection: RUDPclient, ids):
    recv_syng = []
    for id_to_send in ids:
        replay = AppHeader(0, Kind.REQUEST_SYNG_BY_ID.value, Nosah.NULL, City.NULL,
                           str(id_to_send).encode())
        replay = connection.sendData(replay)
        if replay.status_code == Status_code.OK.value:
            recv_syng.append(replay)
    if len(recv_syng) <= 0:
        return None
    return recv_syng


def send_request_gabai_by_id(connection, ids):
    recv_gabai = []
    for id_to_send in ids:
        replay = AppHeader(0, Kind.REQUEST_GABAI_BY_ID.value, Nosah.NULL, City.NULL,
                           str(id_to_send).encode())
        replay = connection.sendData(replay)
        if replay.status_code == Status_code.OK.value:
            recv_gabai.append(replay)
    if len(recv_gabai) <= 0:
        return None
    return recv_gabai
