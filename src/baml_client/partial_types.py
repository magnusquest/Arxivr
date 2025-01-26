###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import baml_py
from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import Dict, List, Optional, Union, Literal

from . import types
from .types import Checked, Check

###############################################################################
#
#  These types are used for streaming, for when an instance of a type
#  is still being built up and any of its fields is not yet fully available.
#
###############################################################################


class Email(BaseModel):
    subject: Optional[str] = None
    body: Optional[str] = None
    from_address: Optional[str] = None

class MyUserMessage(BaseModel):
    role: Optional[Union[Optional[Literal["user"]], Optional[Literal["assistant"]]]] = None
    content: Optional[str] = None

class OrderInfo(BaseModel):
    order_status: Optional[Union[Optional[Literal["ORDERED"]], Optional[Literal["SHIPPED"]], Optional[Literal["DELIVERED"]], Optional[Literal["CANCELLED"]]]] = None
    tracking_number: Optional[str] = None
    estimated_arrival_date: Optional[str] = None

class ProductSearch(BaseModel):
    query: Optional[str] = None
    maxPrice: Optional[float] = None
    category: Optional[str] = None

class Response(BaseModel):
    category: Optional[types.Category] = None
    priority: Optional[str] = None
    message: Optional[str] = None
    internal_notes: Optional[str] = None

class Resume(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    experience: List[Optional[str]]
    skills: List[Optional[str]]

class ScheduleAppointment(BaseModel):
    customerName: Optional[str] = None
    serviceType: Optional[str] = None
    preferredDate: Optional[str] = None
    duration: Optional[int] = None
