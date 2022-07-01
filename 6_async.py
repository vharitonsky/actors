import time
from typing import Any

import pykka
from asyncio import get_event_loop, sleep


async def process(fut):
    print(await fut)
    print('xxx')


class AsyncAct(pykka.ThreadingActor):

    def on_receive(self, message: Any) -> Any:
        time.sleep(3)
        return 'y'

act = AsyncAct.start()

get_event_loop().run_until_complete(process(act.ask(None, block=False)))
