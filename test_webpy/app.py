import web
import sys

# path_ = "/home/nb/webapps/tfty/test_webpy/test_webpy/"
# if path_ not in sys.path:
#     sys.path.append(path_)

urls = (
    "/resp_200/?", "Resp200",
    "/resp_500/?", "Resp500",
    "/resp_json/?", "RespJson",

    "/no_html_start/?", "NoHtmlStart",
    "/no_html_end/?", "NoHtmlEnd",
    "/no_head_start/?", "NoHeadStart",
    "/no_head_end/?", "NoHeadEnd",
    "/no_title_start/?", "NoTitleStart",
    "/no_title_end/?", "NoTitleEnd",
    "/no_head_start_title_start/?", "NoHeadStartTitleStart",
    "/no_head_start_title_end/?", "NoHeadStartTitleEnd",
    "/no_head/?", "NoHead",
    "/no_title/?", "NoTitle",
    "/no_head_end_title_start/?", "NoHeadEndTitleStart",
    "/no_head_end_title_end/?", "NoHeadEndTitleEnd",
    "/no_head_start_title/?", "NoHeadStartTitle",
    "/no_head_title_start/?", "NoHeadTitleStart",
    "/no_head_end_title/?", "NoHeadEndTitle",

    "/html_start_has_attr/?", "HtmlStartHasAttr",
    "/html_end_has_attr/?", "HtmlEndHasAttr",
    "/html_has_attr_lang_en/?", "HtmlHasAttrLangEN",
    "/html_has_attr_lang_zh/?", "HtmlHasAttrLangZH",
    "/head_start_has_attr/?", "HeadStartHasAttr",
    "/head_end_has_attr/?", "HeadEndHasAttr",
    "/title_start_has_attr/?", "TitleStartHasAttr",
    "/title_end_has_attr/?", "TitleEndHasAttr",
    "/head_start_title_start_has_attr/?", "HeadStartTitleStartHasAttr",
    "/head_start_title_end_has_attr/?", "HeadStartTitleEndHasAttr",
    "/head_end_title_start_has_attr/?", "HeadEndTitleStartHasAttr",
    "/head_end_title_end_has_attr/?", "HeadEndTitleEndHasAttr",

    "/befor_head_start_has_head_note/?", "BeforHeadStartHasHeadNote",
    "/befor_title_start_has_head_note/?", "BeforTitleStartHasHeadNote",
    "/befor_title_end_has_head_note/?", "BeforTitleEndHasHeadNote",
    "/befor_head_end_has_head_note/?", "BeforHeadEndHasHeadNote",
    "/after_head_end_has_head_note/?", "AfterHeadEndHasHeadNote",
    "/befor_head_start_has_title_note/?", "BeforHeadStartHasTitleNote",
    "/befor_title_start_has_title_note/?", "BeforTitleStartHasTitleNote",
    "/befor_title_end_has_title_note/?", "BeforTitleEndHasTitleNote",
    "/befor_head_end_has_title_note/?", "BeforHeadEndHasTitleNote",
    "/after_head_end_has_title_note/?", "AfterHeadEndHasTitleNote",

    "/title_has_special_char/?", "TitleHasSpecialChar",
    "/head_has_special_char/?", "HeadHasSpecialChar",
    "/html_has_special_char/?", "HtmlHasSpecialChar",
    "/size_gt_64k/?", "SizeGt64k",
)


t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates/', globals=t_globals)
app = web.application(urls, globals())

class Resp200:

    def GET(self):
        return render.resp_200()


class Resp500:

    def GET(self):
        a = 1 / 0
        return render.resp_200()


class RespJson:

    def GET(self):
        return {
            "status": "ok"
        }


class NoHtmlStart:

    def GET(self):
        return render.no_html_start()


class NoHtmlEnd:

    def GET(self):
        return render.no_html_end()


class NoHeadStart:

    def GET(self):
        return render.no_head_start()


class NoHeadEnd:

    def GET(self):
        return render.no_head_end()


class NoTitleStart:

    def GET(self):
        return render.no_title_start()


class NoTitleEnd:

    def GET(self):
        return render.no_title_end()


class NoHeadStartTitleStart:

    def GET(self):
        return render.no_head_start_title_start()


class NoHeadStartTitleEnd:

    def GET(self):
        return render.no_head_start_title_end()


class NoHead:

    def GET(self):
        return render.no_head()


class NoTitle:

    def GET(self):
        return render.no_title()


class NoHeadEndTitleStart:

    def GET(self):
        return render.no_head_end_title_start()


class NoHeadEndTitleEnd:

    def GET(self):
        return render.no_head_end_title_end()


class NoHeadStartTitle:

    def GET(self):
        return render.no_head_start_title()


class NoHeadTitleStart:

    def GET(self):
        return render.no_head_title_start()


class NoHeadEndTitle:

    def GET(self):
        return render.no_head_end_title()


class HtmlStartHasAttr:

    def GET(self):
        return render.html_start_has_attr()


class HtmlEndHasAttr:

    def GET(self):
        return render.html_end_has_attr()


class HtmlHasAttrLangEN:

    def GET(self):
        return render.html_has_attr_lang_en()


class HtmlHasAttrLangZH:

    def GET(self):
        return render.html_has_attr_lang_zh()


class HeadStartHasAttr:

    def GET(self):
        return render.head_start_has_attr()


class HeadEndHasAttr:

    def GET(self):
        return render.head_end_has_attr()


class TitleStartHasAttr:

    def GET(self):
        return render.title_start_has_attr()


class TitleEndHasAttr:

    def GET(self):
        return render.title_end_has_attr()


class HeadStartTitleStartHasAttr:

    def GET(self):
        return render.head_start_title_start_has_attr()


class HeadStartTitleEndHasAttr:

    def GET(self):
        return render.head_start_title_end_has_attr()


class HeadEndTitleStartHasAttr:

    def GET(self):
        return render.head_end_title_start_has_attr()


class HeadEndTitleEndHasAttr:

    def GET(self):
        return render.head_end_title_end_has_attr()


class BeforHeadStartHasHeadNote:

    def GET(self):
        return render.befor_head_start_has_head_note()


class BeforTitleStartHasHeadNote:

    def GET(self):
        return render.befor_title_start_has_head_note()


class BeforTitleEndHasHeadNote:

    def GET(self):
        return render.befor_title_end_has_head_note()


class BeforHeadEndHasHeadNote:

    def GET(self):
        return render.befor_head_end_has_head_note()


class AfterHeadEndHasHeadNote:

    def GET(self):
        return render.after_head_end_has_head_note()


class BeforHeadStartHasTitleNote:

    def GET(self):
        return render.befor_head_start_has_title_note()


class BeforTitleStartHasTitleNote:

    def GET(self):
        return render.befor_title_start_has_title_note()


class BeforTitleEndHasTitleNote:

    def GET(self):
        return render.befor_title_end_has_title_note()


class BeforHeadEndHasTitleNote:

    def GET(self):
        return render.befor_head_end_has_title_note()


class AfterHeadEndHasTitleNote:

    def GET(self):
        return render.after_head_end_has_title_note()


class TitleHasSpecialChar:

    def GET(self):
        return render.title_has_special_char()


class HeadHasSpecialChar:

    def GET(self):
        return render.head_has_special_char()


class HtmlHasSpecialChar:

    def GET(self):
        return render.html_has_special_char()


class SizeGt64k:

    def GET(self):
        return render.size_gt_64k()

application = app.wsgifunc()

