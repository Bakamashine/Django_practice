from django.core.paginator import Paginator
from django.http import HttpRequest


def new_paginator(req: HttpRequest, model, count = 6):
    paginator = Paginator(model, count)
    if "page" in req.GET:
        page_num = req.GET["page"]
    else:
        page_num = 1
    return paginator.get_page(page_num)