
from fastapi import FastAPI, HTTPException
import fibonacci
from poker import poker

app = FastAPI()

@app.get("/fibonacci/{i}")
def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be non-negative.")
    if n > 1000:
        raise HTTPException(status_code=400, detail="n is too large. Max is 1000.")

    result = fibonacci.fibonacci(n)
    return {"n": n, "fibonacci": result}

@app.post("/poker/")
def best_poker_hand(hands: list[str]):
    result = poker.best_hand(hands)
    return {"best hand: ", result}

