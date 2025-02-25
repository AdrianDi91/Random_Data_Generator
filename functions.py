import time
import threading
import random, logging
import pandas as pd

class Functions:
    def __init__(self):
        self.is_generating = False
        #self.pyqt = UI_MainWindow.setupUI.graphWidget.plot(self.x_data, self.y_data)
        self.x_data = [] #add
        self.y_data = [] #add

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename="RandomData.log", level=logging.INFO, filemode="a+",
                                format="%(asctime)s - %(levelname)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S')
        
        
    def gen_data(self):                #https://www.influxdata.com/blog/how-convert-timestamp-to-datetime-in-python/
         
        self.logger.info("Started Login")   
         
        start_time = time.time()
        actual_time = 0
        while self.is_generating and actual_time < 15:
            x_number = random.randint(1, 100)
            self.x_data.append(x_number)
            end_time = time.time()
            actual_time = end_time - start_time
            self.y_data.append(actual_time)
            print(self.x_data[-1], self.y_data[-1])
            #pg.plot(self.x_data, self.y_data)
            self.logger.info(f"Added {self.x_data[-1]} as random number after {self.y_data[-1]} secs ")
            time.sleep(5) 
        # print(self.x_data, self.y_data)
        
    
    def start_generation(self):
        self.is_generating = True
        self.gen_thread = threading.Thread(target=self.gen_data)
        self.gen_thread.start()
        #return self.x_data, self.y_data

    def stop_generation(self):
        if self.is_generating:
            self.is_generating = False
            if self.gen_thread:
                self.gen_thread.join(timeout=0.1)
                if self.gen_thread.is_alive():
                    print("Forcing thread termination")
                    self.gen_thread._stop()

    def get_data(self):
        return self.x_data.copy(), self.y_data.copy()

    def update_graph(self):
        return self.x_data, self.y_data

    def save_to_excel(self):
        data = {"x_data" : self.x_data,
                "y_data": self.y_data}
        print(data)
        df = pd.DataFrame(data)
        print(df)
        df.to_excel('random_data.xlsx', index=False)