#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import Response
from flask import Blueprint
from flask import render_template

block_code_blueprint = Blueprint(__name__, __name__)


@block_code_blueprint.route("/resp_200/")
def resp_200():
    return render_template("resp_200.html")


@block_code_blueprint.route("/resp_500/")
def resp_500():
    num = 1 / 0
    return "hello"


@block_code_blueprint.route("/resp_json/")
def resp_json():
    rt = {
        "name": "tom",
        "age": 18
    }
    return Response(json.dumps(rt),  mimetype='application/json')


@block_code_blueprint.route("/no_html_start/")
def no_html_start():
    return render_template("no_html_start.html")


@block_code_blueprint.route("/no_html_end/")
def no_html_end():
    return render_template("no_html_end.html")


@block_code_blueprint.route("/no_head_start/")
def no_head_start():
    return render_template("no_head_start.html")


@block_code_blueprint.route("/no_head_end/")
def no_head_end():
    return render_template("no_head_end.html")


@block_code_blueprint.route("/no_title_start/")
def no_title_start():
    return render_template("no_title_start.html")


@block_code_blueprint.route("/no_title_end/")
def no_title_end():
    return render_template("no_title_end.html")


@block_code_blueprint.route("/no_head_start_title_start/")
def no_head_start_title_start():
    return render_template("no_head_start_title_start.html")


@block_code_blueprint.route("/no_head_start_title_end/")
def no_head_start_title_end():
    return render_template("no_head_start_title_end.html")


@block_code_blueprint.route("/no_head/")
def no_head():
    return render_template("no_head.html")


@block_code_blueprint.route("/no_title/")
def no_title():
    return render_template("no_title.html")


@block_code_blueprint.route("/no_head_end_title_start/")
def no_head_end_title_start():
    return render_template("no_head_end_title_start.html")


@block_code_blueprint.route("/no_head_end_title_end/")
def no_head_end_title_end():
    return render_template("no_head_end_title_end.html")


@block_code_blueprint.route("/no_head_start_title/")
def no_head_start_title():
    return render_template("no_head_start_title.html")


@block_code_blueprint.route("/no_head_title_start/")
def no_head_title_start():
    return render_template("no_head_title_start.html")


@block_code_blueprint.route("/no_head_end_title/")
def no_head_end_title():
    return render_template("no_head_end_title.html")


@block_code_blueprint.route("/html_start_has_attr/")
def html_start_has_attr():
    return render_template("html_start_has_attr.html")


@block_code_blueprint.route("/html_end_has_attr/")
def html_end_has_attr():
    return render_template("html_end_has_attr.html")


@block_code_blueprint.route("/html_has_attr_lang_en/")
def html_has_attr_lang_en():
    return render_template("html_has_attr_lang_en.html")


@block_code_blueprint.route("/html_has_attr_lang_zh/")
def html_has_attr_lang_zh():
    return render_template("html_has_attr_lang_zh.html")


@block_code_blueprint.route("/head_start_has_attr/")
def head_start_has_attr():
    return render_template("head_start_has_attr.html")


@block_code_blueprint.route("/head_end_has_attr/")
def head_end_has_attr():
    return render_template("head_end_has_attr.html")


@block_code_blueprint.route("/title_start_has_attr/")
def title_start_has_attr():
    return render_template("title_start_has_attr.html")


@block_code_blueprint.route("/title_end_has_attr/")
def title_end_has_attr():
    return render_template("title_end_has_attr.html")


@block_code_blueprint.route("/head_start_title_start_has_attr/")
def head_start_title_start_has_attr():
    return render_template("head_start_title_start_has_attr.html")


@block_code_blueprint.route("/head_start_title_end_has_attr/")
def head_start_title_end_has_attr():
    return render_template("head_start_title_end_has_attr.html")


@block_code_blueprint.route("/head_end_title_start_has_attr/")
def head_end_title_start_has_attr():
    return render_template("head_end_title_start_has_attr.html")


@block_code_blueprint.route("/head_end_title_end_has_attr/")
def head_end_title_end_has_attr():
    return render_template("head_end_title_end_has_attr.html")


@block_code_blueprint.route("/befor_head_start_has_head_note/")
def befor_head_start_has_head_note():
    return render_template("befor_head_start_has_head_note.html")


@block_code_blueprint.route("/befor_title_start_has_head_note/")
def befor_title_start_has_head_note():
    return render_template("befor_title_start_has_head_note.html")


@block_code_blueprint.route("/befor_title_end_has_head_note/")
def befor_title_end_has_head_note():
    return render_template("befor_title_end_has_head_note.html")


@block_code_blueprint.route("/befor_head_end_has_head_note/")
def befor_head_end_has_head_note():
    return render_template("befor_head_end_has_head_note.html")


@block_code_blueprint.route("/after_head_end_has_head_note/")
def after_head_end_has_head_note():
    return render_template("after_head_end_has_head_note.html")


@block_code_blueprint.route("/befor_head_start_has_title_note/")
def befor_head_start_has_title_note():
    return render_template("befor_head_start_has_title_note.html")


@block_code_blueprint.route("/befor_title_start_has_title_note/")
def befor_title_start_has_title_note():
    return render_template("befor_title_start_has_title_note.html")


@block_code_blueprint.route("/befor_title_end_has_title_note/")
def befor_title_end_has_title_note():
    return render_template("befor_title_end_has_title_note.html")


@block_code_blueprint.route("/befor_head_end_has_title_note/")
def befor_head_end_has_title_note():
    return render_template("befor_head_end_has_title_note.html")


@block_code_blueprint.route("/after_head_end_has_title_note/")
def after_head_end_has_title_note():
    return render_template("after_head_end_has_title_note.html")


@block_code_blueprint.route("/title_has_special_char/")
def title_has_special_char():
    return render_template("title_has_special_char.html")


@block_code_blueprint.route("/head_has_special_char/")
def head_has_special_char():
    return render_template("head_has_special_char.html")


@block_code_blueprint.route("/html_has_special_char/")
def html_has_special_char():
    return render_template("html_has_special_char.html")


@block_code_blueprint.route("/size_gt_64k/")
def size_gt_64k():
    return render_template("size_gt_64k.html")
