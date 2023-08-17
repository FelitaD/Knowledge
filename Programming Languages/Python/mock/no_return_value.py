

class HelloTest(object):
    def foo(self, msg):
        MSG = msg.upper()
        self.bar(MSG)

    def bar(self, MSG):
        print(MSG)

