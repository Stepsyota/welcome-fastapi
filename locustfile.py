from locust import HttpUser, task
import random


# class AsyncUser(HttpUser):
#     @task(1)
#     def async_get_movie(self):
#         id = random.randint(1, 5)
#         self.client.get(f"/slow/{id}")


# class SyncUser(HttpUser):
#     @task(1)
#     def sync_get_movie(self):
#         id = random.randint(1, 5)
#         self.client.get(f"/sync-slow/{id}")

class LogUser(HttpUser):
    @task(1)
    def get_movie_with_logs(self):
        id = random.randint(1, 5)
        self.client.get(f"/movies/{id}")
