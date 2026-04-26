class BullyElection:
    def __init__(self, processes):
        self.processes = processes
        self.alive = {p: True for p in processes}
        self.coordinator = max(processes)

    def crash(self, pid):
        self.alive[pid] = False
        print(f"Process {pid} crashed.")

    def start_election(self, pid):
        print(f"\nProcess {pid} starts election")

        higher = [p for p in self.processes if p > pid and self.alive[p]]

        if not higher:
            self.coordinator = pid
            print(f"Process {pid} becomes new Coordinator")
        else:
            print(f"Process {pid} sends Election to {higher}")
            new_leader = max(higher)
            self.start_election(new_leader)

    def show_coordinator(self):
        print("Current Coordinator:", self.coordinator)


class RingElection:
    def __init__(self, processes):
        self.processes = processes
        self.alive = {p: True for p in processes}
        self.coordinator = max(processes)

    def crash(self, pid):
        self.alive[pid] = False
        print(f"Process {pid} crashed.")

    def start_election(self, starter):
        print(f"\nProcess {starter} starts election")

        active_list = []
        n = len(self.processes)
        index = self.processes.index(starter)

        for i in range(n):
            pid = self.processes[(index + i) % n]
            if self.alive[pid]:
                active_list.append(pid)

        print("Active Processes:", active_list)

        new_leader = max(active_list)
        self.coordinator = new_leader

        print(f"Process {new_leader} elected as Coordinator")

    def show_coordinator(self):
        print("Current Coordinator:", self.coordinator)


if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5]
    bully = BullyElection(processes)

    print("Bully Election Algorithm Simulation")
    bully.show_coordinator()

    bully.crash(5)
    bully.start_election(2)

    bully.show_coordinator()

    processes = [1, 2, 3, 4]
    ring = RingElection(processes)

    print("-----------------------------------------------")
    print("\nRing Election Algorithm Simulation")
    ring.show_coordinator()

    ring.crash(4)
    ring.start_election(2)

    ring.show_coordinator()

# Pip command for this file:
# python -m pip install --upgrade pip
# Note: This script uses only Python standard-library modules.
