import time
import threading
from collections import deque
from typing import Callable, Any


class Buffr:
    max_capacity: int
    time_interval = float
    flush_func: Callable[[list], None]  #todo can we do ... in stead of None?
    buffer: deque[Any]
    lock: threading.Lock
    last_flush_time: float = None
    timer_thread: threading.Thread
    fifo:bool


    def __init__(self, max_capacity: int, time_interval: float, flush_func: Callable[[list], None], fifo:bool=True):
        self.max_capacity = max_capacity
        self.time_interval = time_interval
        self.flush_func = flush_func

        self.buffer = deque()
        self.lock = threading.Lock()
        self.last_flush_time = time.time()

        # Start a background thread for the timer
        self.timer_thread = threading.Thread(target=self._time_trigger, daemon=True)
        self.timer_thread.start()
        self.fifo = fifo


    def add(self, message: Any):
        with self.lock:
            self.buffer.append(message)
            if len(self.buffer) >= self.max_capacity:
                self.flush()

    def _time_trigger(self):
        while True:
            time.sleep(self.time_interval)
            with self.lock:
                if time.time() - self.last_flush_time >= self.time_interval:
                    self.flush()

    def flush(self):
        print("flushing")

        if self.buffer:
            messages = list(self.buffer)
            if not self.fifo:
                messages.reverse()
            self.buffer.clear()
            self.last_flush_time = time.time()
            self.flush_func(messages)

    def stop(self):
        if self.timer_thread.is_alive():
            self.timer_thread.join()
