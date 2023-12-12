from web_crawler import web_crawler
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
async def get_apartments(request: Request):
    wc = web_crawler.WebCrawler()
    wc.fetch_web_data('https://www.sreality.cz/en/search/for-sale/apartments', 500)
    apartments = wc.get_all_apartments()
    return templates.TemplateResponse('index.html', {'request': request, 'apartments':apartments,'num_apartments':len(apartments)})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
