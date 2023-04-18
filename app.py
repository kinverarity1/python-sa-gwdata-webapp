from datetime import datetime, timedelta

from fastapi import Depends, Request, FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

import pandas as pd
import numpy as np

import sa_gwdata as gd


app = FastAPI(debug=True)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/app/well/{dh_no}")
def well(request: Request, dh_no: int):
    summ = gd.wells_summary([dh_no])
    return templates.TemplateResponse(
        "well.html",
        context={
            "request": request,
            "title": summ.unit_hyphen.iloc[0],
            "summary_table": summ.T.to_html(),
        },
    )


@app.get("/app/identify/{input}")
def identify(request: Request, input: str):
    wells = gd.find_wells(input)
    return RedirectResponse(f"/app/well/{wells[0].dh_no}")