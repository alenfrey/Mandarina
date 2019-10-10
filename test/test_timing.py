from mandarina.timing import *
import unittest


class TimingTest(unittest.TestCase):
    def test(self):
        pass

    def test_create_dir_if_doesnt_exist(self):
        def fn(*s):
            print(s)

        run_function_every_n_seconds_thread(fn, ["tick", "tock"], 1.0)


    def test_run_function_after_n_seconds(self):
        def fn(*s):
            print(s)

        run_function_after_n_seconds_thread(fn, ["tock", "tock"], 1.0)
        time.sleep(10)