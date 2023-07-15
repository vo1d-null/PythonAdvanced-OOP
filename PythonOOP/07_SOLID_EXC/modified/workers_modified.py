from abc import ABC, abstractmethod


class DefaultWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...


class Worker(DefaultWorker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(DefaultWorker):
    @staticmethod
    def work():
        print("I work very hard!!!")


class RobotWorker(DefaultWorker):
    @staticmethod
    def work():
        print("Initialization.Beep...Beep...Meow...")
        print('Maximum efficiency protocol activated.Starting work...')


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, DefaultWorker):
            raise AssertionError(f'`worker` must be of type {DefaultWorker}')

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
robot_worker = RobotWorker()
try:
    manager.set_worker(super_worker)  # manager.set_worker(robot_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
