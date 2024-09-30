from fastapi import FastAPI

app = FastAPI()

richest_people_list = {
    "Elon Musk": "280 Billion USD",
    "Jeff Bezzos": "240 Billion USD",
    "Bill Gates": "380 Billion USD",
}

@app.get("/richest-people")
def richest_people():
    return richest_people_list