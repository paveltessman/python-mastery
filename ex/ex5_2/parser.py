import time
import threading
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor


def parse_line(line: str) -> tuple[str, str] | None:
    parts = line.split("=")

    if len(parts) != 2:
        return None
        # raise ValueError("opa")

    return (parts[0], parts[1])


if __name__ == "__main__":
    parse_line("email=guido@python.org")


def worker(x, y):
    print("About to work")
    time.sleep(5)
    print("done, what a day")
    return x + y


def do_work(x, y, fut):
    fut.set_result(worker(x, y))


if __name__ == "__main__":
    pool = ThreadPoolExecutor()
    fut = pool.submit(worker, 2, 3)
