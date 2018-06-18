import requests
from maltego import MaltegoEntity, MaltegoTransform


def trx_getstastuscode(data):
    trx = MaltegoTransform()
    website = data.Value
    url = 'http://{0}'.format(website)
    try:
        r = requests.get(url)
        trx.addEntity('maltego.Phrase', str(r.status_code))
    except:
        trx.addUIMessage(
            'Whoops, that doesn\'t look like a valid website address')
    return trx.returnOutput()
