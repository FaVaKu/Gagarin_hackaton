from datetime import datetime
import aiohttp



async def validate(date_text):
    try:
        datetime.strptime(date_text, "%d.%m.%Y")
    except ValueError:
        return False
    else:
        return True
            
            

class MemoryCode():
    
    @classmethod
    async def get_access_token(self, email: str, password: str) -> dict:
        async with aiohttp.ClientSession(headers={'Accept': 'application/json', 'Content-Type': 'application/json;charset=UTF-8'}) as session:
            async with session.post(
                url = 'https://mc.dev.rand.agency/api/v1/get-access-token',
                params={
                    'email': email,
                    'password': password,
                    'device': 'ellipsis_bot'
                }
            ) as response:
                resp_data = await response.json()
        return resp_data
