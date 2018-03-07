def map_request(centerx, centery, sp1, sp2):
    import requests, sys
    map_request = "http://static-maps.yandex.ru/1.x/?l=sat&ll={},{}&spn={},{}&l=map".format(str(centerx), str(centery), str(sp1), str(sp2))
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    return response.content