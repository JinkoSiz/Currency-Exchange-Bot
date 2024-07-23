import aiohttp
import xml.etree.ElementTree as ET
import redis

REDIS_HOST = 'redis'
REDIS_PORT = 6379
CBR_URL = "https://www.cbr.ru/scripts/XML_daily.asp"

async def fetch_currency_rates():
    async with aiohttp.ClientSession() as session:
        async with session.get(CBR_URL) as response:
            xml_data = await response.text()
            return xml_data

def parse_and_store(xml_data):
    root = ET.fromstring(xml_data)
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    for valute in root.findall('Valute'):
        char_code = valute.find('CharCode').text
        value = valute.find('Value').text.replace(',', '.')
        r.set(char_code, value)

async def main():
    xml_data = await fetch_currency_rates()
    parse_and_store(xml_data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
