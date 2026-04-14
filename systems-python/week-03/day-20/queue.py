class TaskQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None


class Worker:
    def process(self, task):
        print("Processing task:", task["id"], task["type"])

        if task["type"] == "email":
            return True
        return False


queue = TaskQueue()

task1 = {
    "id": 1,
    "type": "email",
    "payload": {"to": "user@test.com"},
    "priority": 1,
    "retry_count": 0
}

task2 = {
    "id": 2,
    "type": "sms",
    "payload": {"to": "+233000000000"},
    "priority": 1,
    "retry_count": 0
}

queue.enqueue(task1)
queue.enqueue(task2)

worker = Worker()

class TaskQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None


class Worker:
    def process(self, task):
        print("Processing task:", task["id"], task["type"])

        # simulate success/failure
        if task["type"] == "email":
            return True
        return False


# create queue
queue = TaskQueue()

# tasks
task1 = {
    "id": 1,
    "type": "email",
    "payload": {"to": "user@test.com"},
    "priority": 1,
    "retry_count": 0
}

task2 = {
    "id": 2,
    "type": "sms",
    "payload": {"to": "+233000000000"},
    "priority": 1,
    "retry_count": 0
}

# add tasks
queue.enqueue(task1)
queue.enqueue(task2)

# create worker
worker = Worker()

# process tasks
while True:
    task = queue.dequeue()

    if not task:
        break

    success = worker.process(task)

    if success:
        print("Task completed:", task["id"])
    else:
        task["retry_count"] += 1
        print("Task failed:", task["id"], "Retry:", task["retry_count"])

        if task["retry_count"] < 3:
            queue.enqueue(task)
        else:
            print("Task moved to dead letter queue:", task["id"])