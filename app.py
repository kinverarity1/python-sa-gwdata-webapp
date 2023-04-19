from datetime import datetime, timedelta

from fastapi import Depends, Request, FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

import pandas as pd
import numpy as np

import sa_gwdata as gd

import logging

logger = logging.getLogger(__name__)


app = FastAPI(debug=True)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/app/well/{dh_no}")
def well(request: Request, dh_no: int):
    summ = gd.wells_summary([dh_no])
    well_summary = summ.iloc[0].to_dict()
    well = gd.Well(
        dh_no=well_summary["dh_no"],
        obs_no=well_summary["obs_no"],
        unit_no=well_summary["unit_long"],
    )
    context = {
        "request": request,
        "title": well.title,
        "summary_table": summ.T.to_html(),
    }
    context.update(well_summary)
    return templates.TemplateResponse(
        "well.html",
        context=context,
    )


@app.get("/app/identify/{input}")
def identify(request: Request, input: str):
    wells = gd.find_wells(input)
    return RedirectResponse(f"/app/well/{wells[0].dh_no}")
