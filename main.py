from fastapi import FastAPI, Header , HTTPException


app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI"}

@app.get("/IsPrime/{num}")
def is_prime(num: int):

    if num>1:
        s=int(num/2)
        for i in range(2,s+1):
            if num%i==0:
                return {"changed": False, "msg": "No es primo"}
                break
        return {"changed": True, "msg": "Es primo"}
    else:
        return {"changed": False, "msg": "No es primo"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)