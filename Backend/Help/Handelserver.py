from Backend.Help.app_packet import AppHeader, Kind, Status_code
from Backend.Help.gabai import Gabai
from Backend.Help.synagogue import Nosah, City, Synagogue


def process_request(request: AppHeader):
    import server
    the_synagogue_list = server.getSynagogues()
    the_gabi_list = server.getGabais()

    if request.kind == Kind.REQUEST_LOGIN.value:
        the_data_got = request.data.decode().split(',')
        try:
            id_to_check = int(the_data_got[0])
        except:
            id_to_check = 0
        the_gabai = the_gabi_list.get_by_id(id_to_check)
        if the_gabai is None:
            return AppHeader(Status_code.WRONG_ID.value, Kind.RESPONSE.value, Nosah.NULL.value,
                             City.NULL.value, b'')
        else:
            if the_gabai.password == the_data_got[1]:
                return AppHeader(Status_code.CORRECT_LOGIN.value, Kind.RESPONSE.value, Nosah.NULL.value,
                                 City.NULL.value, str(the_gabai).encode())
            else:
                return AppHeader(Status_code.WRONG_PASSWORD.value, Kind.RESPONSE.value, Nosah.NULL.value,
                                 City.NULL.value, b'')

    elif request.kind == Kind.REQUEST_BY_QUERY.value:
        temp = the_synagogue_list.get_by_name_and_nosah_and_city(request.data.decode(), request.nosah, request.city)
        if temp is None:
            return AppHeader(Status_code.NOT_FOUND.value, Kind.RESPONSE.value, Nosah.NULL.value,
                             City.NULL.value, b'')
        else:
            return AppHeader(Status_code.OK.value, Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value,
                             bytes(temp))

    elif request.kind == Kind.REQUEST_SYNG_BY_ID.value:
        the_data_got = request.data.decode()
        try:
            the_data_got = int(the_data_got)
            temp = the_synagogue_list.get_by_id(the_data_got)
        except:
            temp = None
        if temp is None:
            return AppHeader(Status_code.NOT_FOUND.value, Kind.RESPONSE.value, Nosah.NULL.value,
                             City.NULL.value, b'')
        else:
            return AppHeader(Status_code.OK.value, Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value,
                             temp.toJSON().encode())

    elif request.kind == Kind.SET_SYNAGOGUE.value:
        syng = Synagogue.fromJSON(request.data.decode())
        ans = the_synagogue_list.edit(syng, the_gabi_list.get_by_id(syng.gabai.gabai_id))
        the_synagogue_list.write_json()
        the_gabi_list.write_json()

        return AppHeader(Status_code.OK.value, Kind.RESPONSE.value, Nosah.NULL.value,
                         City.NULL.value, str(ans).encode())

    elif request.kind == Kind.SET_GABAI.value:
        gabai = Gabai.fromJSON(request.data.decode())
        ans = the_gabi_list.edit(gabai, the_synagogue_list)
        the_gabi_list.write_json()

        return AppHeader(Status_code.OK.value, Kind.RESPONSE.value, Nosah.NULL.value,
                         City.NULL.value, str(ans).encode())

    elif request.kind == Kind.REQUEST_ALL_GABAI.value:
        ids = []
        for gabai_to_send in the_gabi_list.gabai_list:
            ids.append(gabai_to_send.gabai_id)
        return AppHeader(Status_code.OK.value, Kind.RESPONSE.value, Nosah.NULL.value,
                         City.NULL.value, bytes(ids))

    elif request.kind == Kind.REQUEST_GABAI_BY_ID.value:
        the_data_got = request.data.decode()
        try:
            the_data_got = int(the_data_got)
            temp = the_gabi_list.get_by_id(the_data_got)
        except:
            temp = None
        if temp is None:
            return AppHeader(Status_code.NOT_FOUND.value, Kind.RESPONSE.value, Nosah.NULL.value,
                             City.NULL.value, b'')
        else:
            return AppHeader(Status_code.OK.value, Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value,
                             temp.toJSON().encode())
