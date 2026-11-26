from collections import deque

tasks = deque()


def countdown(n):
    while n > 0:
        print("T-minus", n)
        yield
        n -= 1


def countup(n):
    x = 0
    while x < n:
        print("up we go", x)
        yield
        x += 1


def run():
    while tasks:
        task = tasks.popleft()
        try:
            task.send(None)
            tasks.append(task)
        except StopIteration:
            print("task done")


if __name__ == "__main__":
    tasks.append(countdown(10))
    tasks.append(countdown(5))
    tasks.append(countup(20))
    run()
