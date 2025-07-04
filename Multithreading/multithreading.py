import threading
import time

def walk(first):
    time.sleep(8)
    print(f"you finish walking  {first} ")

def run():
    time.sleep(2)
    print("you finish running")

def take_out_the_thrash():
    time.sleep(5)
    print("you finish taking out the thrash")

chore1 = threading.Thread(target=walk, args=("mike"))
chore1.start()

chore2 = threading.Thread(target=run)
chore2.start()

chore3 = threading.Thread(target=take_out_the_thrash)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("you finished the chores")