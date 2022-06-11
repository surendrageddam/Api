from fastapi import FastAPI
from Scraper.scraping import Scraper


app = FastAPI()


@app.get("/get")
async def run(url: str):
    return{"price": Scraper().scrape(url)}
