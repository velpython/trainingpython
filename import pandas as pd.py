class Logger:
    def __init__(self):
        self.set = self.Set(self)

    def show_logger(self):
        print("This is show logger")
        self.set.show_set()


    class Set:
        def __init__(self, logger):
            self.logger = logger

        def show_set(self):
            print("This is show set")
            
        def parent_call(self):
            self.logger.show_logger()

        def self_call(self):
            self.show_set()


logger = Logger()

logger.show_logger()
logger.set.show_set()
logger.set.parent_call()
logger.set.self_call()