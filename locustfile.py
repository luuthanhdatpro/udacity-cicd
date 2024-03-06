from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    @task
    def predict(l):
        l.client.post("/predict", json = { "CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98} })
        l.client.get("/")
