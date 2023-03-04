from typing import Union, Dict, List
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


# Models
# Schemas for POST Method

class InputPost(BaseModel):
    UID: str = Field(description="UID")

class OutputPost(BaseModel):
    UID: str = Field(description="UID")


# Schemas for GET Method
# - need to wrap with dataclass in order to OpenAPI compatibility
@dataclass
class InputGet:
    UID: str = Query(default=...,
                     description="UID")

@dataclass
class OutputGet:
    UID: str = Query(default=...,
                     description="UID")
