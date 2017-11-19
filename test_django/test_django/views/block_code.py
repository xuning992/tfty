#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.shortcuts import render_to_response
from django.http import HttpResponse


def resp_200(request):
    return render_to_response("resp_200.html")


def resp_500(request):
    num = 1 / 0
    return HttpResponse("500")


def resp_json(request):
    rt = {
        "name": "tom",
        "age": 18
    }
    return HttpResponse(json.dumps(rt),  content_type='application/json')


def no_html_start(request):
    return render_to_response("no_html_start.html")


def no_html_end(request):
    return render_to_response("no_html_end.html")


def no_head_start(request):
    return render_to_response("no_head_start.html")


def no_head_end(request):
    return render_to_response("no_head_end.html")


def no_title_start(request):
    return render_to_response("no_title_start.html")


def no_title_end(request):
    return render_to_response("no_title_end.html")


def no_head_start_title_start(request):
    return render_to_response("no_head_start_title_start.html")


def no_head_start_title_end(request):
    return render_to_response("no_head_start_title_end.html")


def no_head(request):
    return render_to_response("no_head.html")


def no_title(request):
    return render_to_response("no_title.html")


def no_head_end_title_start(request):
    return render_to_response("no_head_end_title_start.html")


def no_head_end_title_end(request):
    return render_to_response("no_head_end_title_end.html")


def no_head_start_title(request):
    return render_to_response("no_head_start_title.html")


def no_head_title_start(request):
    return render_to_response("no_head_title_start.html")


def no_head_end_title(request):
    return render_to_response("no_head_end_title.html")


def html_start_has_attr(request):
    return render_to_response("html_start_has_attr.html")


def html_end_has_attr(request):
    return render_to_response("html_end_has_attr.html")


def html_has_attr_lang_en(request):
    return render_to_response("html_has_attr_lang_en.html")


def html_has_attr_lang_zh(request):
    return render_to_response("html_has_attr_lang_zh.html")


def head_start_has_attr(request):
    return render_to_response("head_start_has_attr.html")


def head_end_has_attr(request):
    return render_to_response("head_end_has_attr.html")


def title_start_has_attr(request):
    return render_to_response("title_start_has_attr.html")


def title_end_has_attr(request):
    return render_to_response("title_end_has_attr.html")


def head_start_title_start_has_attr(request):
    return render_to_response("head_start_title_start_has_attr.html")


def head_start_title_end_has_attr(request):
    return render_to_response("head_start_title_end_has_attr.html")


def head_end_title_start_has_attr(request):
    return render_to_response("head_end_title_start_has_attr.html")


def head_end_title_end_has_attr(request):
    return render_to_response("head_end_title_end_has_attr.html")


def befor_head_start_has_head_note(request):
    return render_to_response("befor_head_start_has_head_note.html")


def befor_title_start_has_head_note(request):
    return render_to_response("befor_title_start_has_head_note.html")


def befor_title_end_has_head_note(request):
    return render_to_response("befor_title_end_has_head_note.html")


def befor_head_end_has_head_note(request):
    return render_to_response("befor_head_end_has_head_note.html")


def after_head_end_has_head_note(request):
    return render_to_response("after_head_end_has_head_note.html")


def befor_head_start_has_title_note(request):
    return render_to_response("befor_head_start_has_title_note.html")


def befor_title_start_has_title_note(request):
    return render_to_response("befor_title_start_has_title_note.html")


def befor_title_end_has_title_note(request):
    return render_to_response("befor_title_end_has_title_note.html")


def befor_head_end_has_title_note(request):
    return render_to_response("befor_head_end_has_title_note.html")


def after_head_end_has_title_note(request):
    return render_to_response("after_head_end_has_title_note.html")


def title_has_special_char(request):
    return render_to_response("title_has_special_char.html")


def head_has_special_char(request):
    return render_to_response("head_has_special_char.html")


def html_has_special_char(request):
    return render_to_response("html_has_special_char.html")


def size_gt_64k(request):
    return render_to_response("size_gt_64k.html")
