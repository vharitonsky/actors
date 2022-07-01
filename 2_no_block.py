from typing import Any

import pykka
import time


class HeavyComputer(pykka.ThreadingActor):

    def on_receive(self, message: Any) -> Any:
        time.sleep(2)
        print(message)


actor_ref = HeavyComputer.start()
actor_ref.tell("compute 1")
actor_ref.tell("compute 2")
actor_ref.tell("compute 3")
print('continue')
actor_ref.stop()
