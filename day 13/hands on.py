import threading
import time

def task(name, delay):
    for i in range(3):
        print(f"Task {name}: Step {i+1}")
        time.sleep(delay)


thread1 = threading.Thread(target=task, args=("A", 1))
thread2 = threading.Thread(target=task, args=("B", 2))


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All tasks completed!")
