import time

def start_timing():
    CNT = [time.time()] * 2
    print(CNT)
    def add_one():
        CNT[0] = CNT[1] - time.time()
        print(f"Time elapsed: {abs(CNT[0]):9.2f} seconds")
    return add_one

elapsed_time = start_timing()


time.sleep(1)
elapsed_time()

