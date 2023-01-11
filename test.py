from locust import HttpUser, task, between, TaskSet


class NestedBehavior(TaskSet):
    @task
    def inner_task(self):
        print("inner task")

    def on_stop(self):
        self.interrupt()


class MainBehavior(TaskSet):
    tasks = [NestedBehavior]

    @task
    def main_task(self):
        print("main task")


class LocustUser(HttpUser):
    host = "127.0.0.1:8080"
    tasks = [MainBehavior]
    wait_time = between(1, 4)
