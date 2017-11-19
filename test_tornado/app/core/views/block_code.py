#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from core.views.base import BaseHandler


class Resp200(BaseHandler):
    def get(self):
        self.render("resp_200.html")


class Resp500(BaseHandler):
    def get(self):
        num = 1 / 0
        self.write("hello")


class RespJson(BaseHandler):
    def get(self):
        rt = {
            "name": "tom",
            "age": 18
        }
        self.write(json.dumps(rt))


class NoHtmlStart(BaseHandler):
    def get(self):
        self.render("no_html_start.html")


class NoHtmlEnd(BaseHandler):
    def get(self):
        self.render("no_html_end.html")


class NoHeadStart(BaseHandler):
    def get(self):
        self.render("no_head_start.html")


class NoHeadEnd(BaseHandler):
    def get(self):
        self.render("no_head_end.html")


class NoTitleStart(BaseHandler):
    def get(self):
        self.render("no_title_start.html")


class NoTitleEnd(BaseHandler):
    def get(self):
        self.render("no_title_end.html")


class NoHeadStartTitleStart(BaseHandler):
    def get(self):
        self.render("no_head_start_title_start.html")


class NoHeadStartTitleEnd(BaseHandler):
    def get(self):
        self.render("no_head_start_title_end.html")


class NoHead(BaseHandler):
    def get(self):
        self.render("no_head.html")


class NoTitle(BaseHandler):
    def get(self):
        self.render("no_title.html")


class NoHeadEndTitleStart(BaseHandler):
    def get(self):
        self.render("no_head_end_title_start.html")


class NoHeadEndTitleEnd(BaseHandler):
    def get(self):
        self.render("no_head_end_title_end.html")


class NoHeadStartTitle(BaseHandler):
    def get(self):
        self.render("no_head_start_title.html")


class NoHeadTitleStart(BaseHandler):
    def get(self):
        self.render("no_head_title_start.html")


class NoHeadEndTitle(BaseHandler):
    def get(self):
        self.render("no_head_end_title.html")


class HtmlStartHasAttr(BaseHandler):
    def get(self):
        self.render("html_start_has_attr.html")


class HtmlEndHasAttr(BaseHandler):
    def get(self):
        self.render("html_end_has_attr.html")


class HtmlHasAttrLangEN(BaseHandler):
    def get(self):
        self.render("html_has_attr_lang_en.html")


class HtmlHasAttrLangZH(BaseHandler):
    def get(self):
        self.render("html_has_attr_lang_zh.html")


class HeadStartHasAttr(BaseHandler):
    def get(self):
        self.render("head_start_has_attr.html")


class HeadEndHasAttr(BaseHandler):
    def get(self):
        self.render("head_end_has_attr.html")


class TitleStartHasAttr(BaseHandler):
    def get(self):
        self.render("title_start_has_attr.html")


class TitleEndHasAttr(BaseHandler):
    def get(self):
        self.render("title_end_has_attr.html")


class HeadStartTitleStartHasAttr(BaseHandler):
    def get(self):
        self.render("head_start_title_start_has_attr.html")


class HeadStartTitleEndHasAttr(BaseHandler):
    def get(self):
        self.render("head_start_title_end_has_attr.html")


class HeadEndTitleStartHasAttr(BaseHandler):
    def get(self):
        self.render("head_end_title_start_has_attr.html")


class HeadEndTitleEndHasAttr(BaseHandler):
    def get(self):
        self.render("head_end_title_end_has_attr.html")


class BeforHeadStartHasHeadNote(BaseHandler):
    def get(self):
        self.render("befor_head_start_has_head_note.html")


class BeforTitleStartHasHeadNote(BaseHandler):
    def get(self):
        self.render("befor_title_start_has_head_note.html")


class BeforTitleEndHasHeadNote(BaseHandler):
    def get(self):
        self.render("befor_title_end_has_head_note.html")


class BeforHeadEndHasHeadNote(BaseHandler):
    def get(self):
        self.render("befor_head_end_has_head_note.html")


class AfterHeadEndHasHeadNote(BaseHandler):
    def get(self):
        self.render("after_head_end_has_head_note.html")


class BeforHeadStartHasTitleNote(BaseHandler):
    def get(self):
        self.render("befor_head_start_has_title_note.html")


class BeforTitleStartHasTitleNote(BaseHandler):
    def get(self):
        self.render("befor_title_start_has_title_note.html")


class BeforTitleEndHasTitleNote(BaseHandler):
    def get(self):
        self.render("befor_title_end_has_title_note.html")


class BeforHeadEndHasTitleNote(BaseHandler):
    def get(self):
        self.render("befor_head_end_has_title_note.html")


class AfterHeadEndHasTitleNote(BaseHandler):
    def get(self):
        self.render("after_head_end_has_title_note.html")


class TitleHasSpecialChar(BaseHandler):
    def get(self):
        self.render("title_has_special_char.html")


class HeadHasSpecialChar(BaseHandler):
    def get(self):
        self.render("head_has_special_char.html")


class HtmlHasSpecialChar(BaseHandler):
    def get(self):
        self.render("html_has_special_char.html")


class SizeGt64k(BaseHandler):
    def get(self):
        self.render("size_gt_64k.html")
