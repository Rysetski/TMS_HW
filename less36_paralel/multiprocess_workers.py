import multiprocessing as mp
from datetime import datetime
import os
from random import random


def worker(name: str, queue, semaphore, logs_queue):
    logs_queue.put(f"{name}: Запущен. PID: {os.getpid()}")

    try:
        while True:
            item = queue.get()
            logs_queue.put(f"{name}: Получено сообщение: type: {type(item)}, value: {item}")

            # time.sleep(5 * random() + 1)

            if random() < -0.1:
                raise Exception("Ошибка при обработке задачи")

            logs_queue.put(f"{name}: Отработал {item}")

    except KeyboardInterrupt:
        return
    except Exception as e:
        logs_queue.put(f"{name}: Ошибка: {e}")
        return

    finally:
        try:
            semaphore.release()
            logs_queue.put(f"{name}: Завершил работу")
        except Exception:
            pass


def logger(log_queue):
    print("Logger started")
    with open("log.txt", "w", encoding="utf-8") as f:
        try:
            while True:
                now = datetime.now()
                text = now.strftime("%Y-%m-%d %H:%M:%S") + " | " + log_queue.get()

                f.write(text + "\n")
                print(text)
        except KeyboardInterrupt:
            return


def worker_spawner(semaphore, work_queue, logs_queue):
    logs_queue.put("Worker spawner started")
    worker_num = 1
    while True:
        semaphore.acquire()
        mp.Process(target=worker, args=(f"Worker-{worker_num}", work_queue, semaphore, logs_queue)).start()
        worker_num += 1


def queue_gen(work_queue, logs_queue):
    logs_queue.put("Queue generator started")
    for i in range(100):
        work_queue.put(
            {
                "id": i,
                "created_at": datetime.now(),
            }
        )


if __name__ == '__main__':
    manager = mp.Manager()
    work_queue = manager.Queue()
    logs_queue = manager.Queue()
    semaphore = manager.Semaphore(3)

    spawner = mp.Process(target=worker_spawner, args=(semaphore, work_queue, logs_queue))
    spawner.start()

    generator = mp.Process(target=queue_gen, args=(work_queue, logs_queue))
    generator.start()

    logger_process = mp.Process(target=logger, args=(logs_queue,))
    logger_process.start()

    try:
        generator.join()
        logger_process.join()
        spawner.join()
    except KeyboardInterrupt:
        generator.terminate()
        logger_process.terminate()
        spawner.terminate()
        print("Exit")
