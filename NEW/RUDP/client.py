from RUDPclient import RUDPclient
from api import AppHeader, Kind
from synagogue import Nosah, City


if __name__ == '__main__':
    # big_data = ""
    # for i in range(20000000):
    #     big_data += str(i) + "\n"
    server_address = ("127.0.0.1", 9879)
    connection = RUDPclient(server_address)
    connection.connect()

    connection.sendData(AppHeader(None, Kind.REQUEST_LOGIN.value, Nosah.NULL.value, City.NULL.value, "idsadddddd,paqeradsasdss".encode())
                        .pack())
    connection.sendData(AppHeader(None, Kind.REQUEST_SYNG_BY_ID.value, Nosah.NULL.value, City.NULL.value, "qweasdssssssssssssssadafvcexqead".encode())
                        .pack())


    #
    # connection.sendTo()
    # connection.recevFrom()
    #
    # connection.sendTo()
    # connection.recevFrom()

    connection.close()
