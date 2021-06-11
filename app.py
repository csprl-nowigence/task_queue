"""Implements fastapi producer app."""

from fastapi import FastAPI
from pydantic import BaseModel

from worker import add
from worker2 import sub
# from bgt_task import add, sub


# Create the FastAPI app
app = FastAPI()


# Use pydantic to keep track of the input request payload
class Numbers(BaseModel):
    x: float
    y: float


@app.post('/add')
async def enqueue_add(numbers: Numbers):
    # We use celery delay method in order to enqueue the task with the given parameters
    add.delay(numbers.x, numbers.y)
    return "task added"


@app.post('/sub')
async def enqueue_sub(numbers: Numbers):
    # We use celery delay method in order to enqueue the task with the given parameters
    sub.delay(numbers.x, numbers.y)
    return "task added"
