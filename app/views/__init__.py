#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:28:14 2019

@author: anran
"""
from app import flask_app as app
from flask import request
import json
from datetime import datetime


@app.route("/heartbeat")
def heartbeat():
    return json.dumps(
        {
            "status": True,
            "service": "Homework01",
            "datetime": f"{datetime.now()}"
        }
    )


@app.route("/sum", methods=['POST'])
def sum():
    form = request.form
    print(form)
    x = form.get("x")
    y = form.get("y")

    x = int(x)
    y = int(y)

    print(x)
    print(y)

    results = {
        "result": x + y
    }

    return json.dumps(results)

@app.route("/minimum", methods=['POST'])
def minimum():
    form = request.form
    print(form)
    value = form.get('value')
    
    value = list(value)
    
    print(value)
    
    results = {
            "result": min(value)
    }
    
    return json.dumps(results)


@app.route("/product", methods=['POST'])
def product():
    form = request.form
    print(form)
    value = form.get('value')
    
    value = list(value)
    
    print(value)
    
    if value == []:
        results = {
                "result": 0
                }
    else:
        r = 1
        for i in range(len(value)):
            r = r*value[i]
        results = {
            "result": r
            }
    
    return json.dumps(results)


@app.before_first_request
def load_app():
    print("Loading App Before First Request")

