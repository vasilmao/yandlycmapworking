def geocode_request(**kwargs):
    import requests
    x = 'https://geocode-maps.yandex.ru/1.x/'
    if kwargs:
        x += '?'
        for i in kwargs.keys():
            x += i + '=' + str(kwargs[i])
            x += '&'
    x = x[:-1]
    resp = requests.get(x)
    print(resp.text)
    return resp.json()

def find_coords(s):
    x = geocode_request(geocode=s, format='json')['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    a = list(map(float, x['boundedBy']['Envelope']['lowerCorner'].split()))
    center = list(map(float, x['Point']['pos'].split()))
    sp1 = center[0] - a[0]
    sp2 = center[1] - a[1]
    return center + [sp1, sp2]