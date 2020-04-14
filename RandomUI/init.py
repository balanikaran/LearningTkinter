import time
import concurrent.futures


class InitializeApp:
    def initialize(self):
        print("This is some actual work going on...")
        time.sleep(5)
        print("some heavy work complete...")
        return True

    @classmethod
    def start(cls):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(cls.initialize, cls)
            returned_value = future.result()
            return returned_value
