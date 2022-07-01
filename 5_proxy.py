import pykka
import time


class HeavyComputer(pykka.ThreadingActor):

    def compute_heavy_simple(self, message):
        time.sleep(1)
        return f"simple {message}"

    def compute_heavy_complex(self):
        time.sleep(2)
        return "complex"


computer = HeavyComputer.start().proxy()

fut_simple: pykka.Future = computer.compute_heavy_simple("message")
fut_complex: pykka.Future = computer.compute_heavy_complex()

print(pykka.get_all([fut_simple, fut_complex]))

pykka.ActorRegistry.stop_all()
