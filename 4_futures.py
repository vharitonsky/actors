import pykka
import time
from typing import Any


class FutureActor(pykka.ThreadingActor):

    def on_receive(self, message: Any) -> Any:
        time.sleep(1)
        print(f"{message} is done")
        return f"result of {message}"


actor_one = FutureActor.start()
actor_two = FutureActor.start()

fut1, fut2 = (
    actor_one.ask("compute 1", block=False),
    actor_two.ask("compute 2", block=False)
)
time.sleep(1)
print(f"{fut1.get()} {fut2.get()}")
fut = actor_one.ask("compute 3", block=False)


def get_fut(res):
    print(f"in hook {res}")

fut.set_get_hook(lambda res: print(f"got me {res}"))

fut.get()
pykka.ActorRegistry.stop_all()
