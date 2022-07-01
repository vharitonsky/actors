import pykka


class Greeter(pykka.ThreadingActor):
    def __init__(self, greeting='Hi there!'):
        super().__init__()
        self.greeting = greeting

    def on_receive(self, message):
        print(self.greeting)


actor_ref = Greeter.start(greeting='Hi you!')
actor_ref2 = Greeter.start(greeting='Hi you!')
answer = actor_ref.ask('Hi?')
answer2 = actor_ref2.ask('Hi?')

