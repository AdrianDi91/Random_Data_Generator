import time
import threading
import random

class Functions:
    def __init__(self):
        self.is_generating = False

    def gen_data(self):                #https://www.influxdata.com/blog/how-convert-timestamp-to-datetime-in-python/
         
        x_data = []
        y_data = []       
         
        start_time = time.time()
        actual_time = 0
        while self.is_generating and actual_time < 15:
            x_number = random.randint(1, 100)
            x_data.append(x_number)
            end_time = time.time()
            actual_time = end_time - start_time
            y_data.append(actual_time)
            print(x_data[-1], y_data[-1])
            time.sleep(5) 
    
            print(x_data, y_data)
    
    def start_generation(self):
        self.is_generating = True
        self.gen_thread = threading.Thread(target=self.gen_data)
        self.gen_thread.start()

    def stop_generation(self):
        if self.is_generating:
            self.is_generating = False
            if self.gen_thread:
                self.gen_thread.join(timeout=0.1)
                if self.gen_thread.is_alive():
                    print("Forcing thread termination")
                    self.gen_thread._stop()