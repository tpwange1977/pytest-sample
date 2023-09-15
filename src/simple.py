# main.py

from fastapi import FastAPI
import requests, uvicorn
from fastapi.responses import PlainTextResponse
from fastapi import Request, Response
app = FastAPI()


@app.get('/metrics')
def hello(a):

    headers=[]
    a = a + "1"
    b=0
    b = b + 1
    response = requests.get("http://aaa.bbb.ccc", headers={})
    print(response.status_code)

    return response

def main():
    #uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
    uvicorn.run(app="simple:app", host="127.0.0.1", port=5000, reload=True)

if __name__ == "__main__":
    main()






