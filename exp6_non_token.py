import random
import threading
import time


class RAProcess:
    def __init__(self, pid, total):
        self.pid = pid
        self.total = total
        self.timestamp = 0
        self.reply_count = 0
        self.requesting = False
        self.deferred = []

    def request_cs(self):
        self.requesting = True
        self.timestamp = time.time()
        self.reply_count = 0
        print(f"Process {self.pid} requesting CS at time {self.timestamp}")

        for p in processes:
            if p.pid != self.pid:
                p.receive_request(self.pid, self.timestamp)

    def receive_request(self, pid, timestamp):
        if (not self.requesting) or (timestamp < self.timestamp) or (
            timestamp == self.timestamp and pid < self.pid
        ):
            processes[pid].receive_reply()
        else:
            self.deferred.append(pid)

    def receive_reply(self):
        self.reply_count += 1
        if self.reply_count == self.total - 1:
            self.enter_cs()

    def enter_cs(self):
        print(f"Process {self.pid} ENTERED Critical Section")
        time.sleep(2)
        print(f"Process {self.pid} EXITING Critical Section")
        self.requesting = False

        for pid in self.deferred:
            processes[pid].receive_reply()
        self.deferred = []


if __name__ == "__main__":
    n = 3
    processes = [RAProcess(i, n) for i in range(n)]

    def generate_requests():
        while True:
            time.sleep(random.randint(3, 6))
            p = random.choice(processes)
            if not p.requesting:
                p.request_cs()

    threading.Thread(target=generate_requests, daemon=True).start()

    print(f"Simulation running for 20 seconds with {n} processes...")
    time.sleep(20)
    print("Simulation finished.")

# Pip command for this file:
# python -m pip install --upgrade pip
# Note: This script uses only Python standard-library modules.
