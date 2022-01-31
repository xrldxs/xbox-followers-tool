import asyncio
import aiohttp
import colorama
import time
import os
from colorama import Fore
from time import sleep
from sys import platform
from os import system, _exit

os.system("cls & title xbox followers tool made by mkay")

class Follow_Bot:
    def __init__(self):
        self.users = self.collect_tokens()
        self.followed = 0
        self.failed = 0
        self.target = ''


    async def follow_target(self, token) -> None:
        session = aiohttp.ClientSession()

        async with session.put(f"https://social.xboxlive.com/users/me/people/gt({self.target})", headers={ "Authorization": token, "X-XBL-Contract-Version": "2" }) as follow_request:
            if follow_request.status in [200, 201, 202, 204]: 
                self.followed += 1 

            else:
                self.failed += 1             

            print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] GAMERTAG: [{self.target}] | FOLLOWED: [{self.followed}] | ERRORS: [{self.failed}]", end='\r', flush=True)
        await session.close()   
 

    @staticmethod
    def collect_tokens() -> None:
        with open("tokens.txt", "r") as token_file:
            return [token.strip() for token in token_file]

    
    async def initialise(self) -> None:
        os.system("cls & title xbox followers tool made by mkay")

        if len(open('tokens.txt', 'r').readlines()) > 0:
            print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] You successfully loaded your tokens, NO TOKENS: [{len(open('tokens.txt', 'r').readlines())}] \n")
        else:
            print(f'[{Fore.RED}ERROR{Fore.RESET}] Please make sure you have placed your tokens in the tokens.txt file.');_exit(0)

        self.target = input(f"[{Fore.YELLOW}INPUT{Fore.RESET}] GAMERTAG: ");print('')
        time.sleep(3)
        os.system("cls & title xbox followers tool made by mkay")
        await self.start()


    async def start(self):
        await asyncio.gather(*[self.follow_target(user) for user in self.users])
        print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] GAMERTAG: [{self.target}] | FOLLOWED: [{self.followed}] | ERRORS: [{self.failed}]", flush=True)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Follow_Bot().initialise())