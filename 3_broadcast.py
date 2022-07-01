import pykka
from typing import Any


class HookActor(pykka.ThreadingActor):
    pass


class HookActorFirst(HookActor):

    def on_receive(self, message: Any) -> Any:
        print(f"hook {message} first")


class HookActorSecond(HookActor):

    def on_receive(self, message: Any) -> Any:
        print(f"hook {message} second")


actor_first_ref = HookActorFirst.start()
HookActorSecond.start()

pykka.ActorRegistry.broadcast("my message", target_class=HookActor)

pykka.ActorRegistry.stop_all()
