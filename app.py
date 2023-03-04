# -*- coding: utf-8 -*-

import json
import os
import uvicorn

from functools import lru_cache
from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse

from config import DefaultConfig
from exceptions.exceptions import ExampleError
from schema.schema import (InputPost, OutputPost, InputGet, OutputGet)
from somerandomclass.simpleprinter import SimplePrinter

app = FastAPI()


@lru_cache()
def get_config():
    """Caching config values for faster loading across all the sessions."""
    return DefaultConfig()


# Routes
@app.get("/")
async def _index():
    return JSONResponse(content="FastAPI Template V1")


@app.get("/api/v1/example", response_model=OutputGet)
async def _example_get(input_get: InputGet = Depends(InputGet)):
    """An example to show usage of response_model and request_model in GET method"""
    try:
        print(input_get.UID)

        return {
            "UID": input_get.UID
        }
    except ExampleError as e:
        raise HTTPException(status_code=404, detail="Example Error")


@app.post("/api/v1/example", response_model=OutputPost)
async def _example_post(input_post: InputPost):
    """An example to show usage of response_model and request_model in POST method"""
    try:
        print(input_post.UID)

        return {
            "UID": input_post.UID
        }
    except ExampleError as e:
        raise HTTPException(status_code=404, detail="Example Error")


@app.post("/api/v1/backgroundtask", response_model=OutputPost)
async def _example_backgroundtask_post(input_post: InputPost,
                                       background_tasks: BackgroundTasks,
                                       app_config: DefaultConfig = Depends(get_config)):
    """An example to show usage of FastAPI background_tasks, FastAPI Depends function(+ lru_cache)"""
    try:
        sp = SimplePrinter(
            app_config=app_config
        )

        background_tasks.add_task(sp.print_n_times,
                                  msg=input_post.UID,
                                  n=4)

        return {
            "UID": input_post.UID
        }
    except ExampleError as e:
        raise HTTPException(status_code=404, detail="Example Error")


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=7010)
