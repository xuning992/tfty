from django.conf.urls import patterns, include, url
from django.contrib import admin
import django

from test_django.views.block_code import resp_200
from test_django.views.block_code import resp_500
from test_django.views.block_code import resp_json

from test_django.views.block_code import no_html_start
from test_django.views.block_code import no_html_end
from test_django.views.block_code import no_head_start
from test_django.views.block_code import no_head_end
from test_django.views.block_code import no_title_start
from test_django.views.block_code import no_title_end
from test_django.views.block_code import no_head_start_title_start
from test_django.views.block_code import no_head_start_title_end
from test_django.views.block_code import no_head
from test_django.views.block_code import no_title
from test_django.views.block_code import no_head_end_title_start
from test_django.views.block_code import no_head_end_title_end
from test_django.views.block_code import no_head_start_title
from test_django.views.block_code import no_head_title_start
from test_django.views.block_code import no_head_end_title

from test_django.views.block_code import html_start_has_attr
from test_django.views.block_code import html_end_has_attr
from test_django.views.block_code import html_has_attr_lang_en
from test_django.views.block_code import html_has_attr_lang_zh
from test_django.views.block_code import head_start_has_attr
from test_django.views.block_code import head_end_has_attr
from test_django.views.block_code import title_start_has_attr
from test_django.views.block_code import title_end_has_attr
from test_django.views.block_code import head_start_title_start_has_attr
from test_django.views.block_code import head_start_title_end_has_attr
from test_django.views.block_code import head_end_title_start_has_attr
from test_django.views.block_code import head_end_title_end_has_attr

from test_django.views.block_code import befor_head_start_has_head_note
from test_django.views.block_code import befor_title_start_has_head_note
from test_django.views.block_code import befor_title_end_has_head_note
from test_django.views.block_code import befor_head_end_has_head_note
from test_django.views.block_code import after_head_end_has_head_note
from test_django.views.block_code import befor_head_start_has_title_note
from test_django.views.block_code import befor_title_start_has_title_note
from test_django.views.block_code import befor_title_end_has_title_note
from test_django.views.block_code import befor_head_end_has_title_note
from test_django.views.block_code import after_head_end_has_title_note

from test_django.views.block_code import title_has_special_char
from test_django.views.block_code import head_has_special_char
from test_django.views.block_code import html_has_special_char
from test_django.views.block_code import size_gt_64k
from test_django.views.frame_django_test import test_template
from test_django.views.frame_django_test import func_view
from test_django.views.frame_django_test import ClassView
from test_django.views.ex_requests import requests_get

if str(django.get_version()) in ('1.4', '1.6'):
    from test_django.api import urls
else:
    pass

if str(django.get_version()) in ('1.6', '1.7.11'):
    from test_django.views.django_orm_test import db_insert
    from test_django.views.django_orm_test import db_delete
    from test_django.views.django_orm_test import db_update
    from test_django.views.django_orm_test import db_select
else:
    pass

if str(django.get_version()) in ('1.9'):
    from test_django.views.django_orm_test import db_insert
    from test_django.views.django_orm_test import db_delete
    from test_django.views.django_orm_test import db_update
    from test_django.views.django_orm_test import db_select
    from test_django.views.django_orm_test import db_transaction


print "DJANGO_VERSION***********************%s" % django.get_version()
if str(django.get_version()) == '1.9':
    urlpatterns = patterns(
        '',
        url(r'^admin/', include(admin.site.urls)),

        url(r'^resp_200/?$', resp_200),
        url(r'^resp_500/?$', resp_500),
        url(r'^resp_json/?$', resp_json),

        url(r'^no_html_start/?$', no_html_start),
        url(r'^no_html_end/?$', no_html_end),
        url(r'^no_head_start/?$', no_head_start),
        url(r'^no_head_end/?$', no_head_end),
        url(r'^no_title_start/?$', no_title_start),
        url(r'^no_title_end/?$', no_title_end),
        url(r'^no_head_start_title_start/?$', no_head_start_title_start),
        url(r'^no_head_start_title_end/?$', no_head_start_title_end),
        url(r'^no_head/?$', no_head),
        url(r'^no_title/?$', no_title),
        url(r'^no_head_end_title_start/?$', no_head_end_title_start),
        url(r'^no_head_end_title_end/?$', no_head_end_title_end),
        url(r'^no_head_start_title/?$', no_head_start_title),
        url(r'^no_head_title_start/?$', no_head_title_start),
        url(r'^no_head_end_title/?$', no_head_end_title),

        url(r'^html_start_has_attr/?$', html_start_has_attr),
        url(r'^html_end_has_attr/?$', html_end_has_attr),
        url(r'^html_has_attr_lang_en/?$', html_has_attr_lang_en),
        url(r'^html_has_attr_lang_zh/?$', html_has_attr_lang_zh),
        url(r'^head_start_has_attr/?$', head_start_has_attr),
        url(r'^head_end_has_attr/?$', head_end_has_attr),
        url(r'^title_start_has_attr/?$', title_start_has_attr),
        url(r'^title_end_has_attr/?$', title_end_has_attr),
        url(r'^head_start_title_start_has_attr/?$', head_start_title_start_has_attr),
        url(r'^head_start_title_end_has_attr/?$', head_start_title_end_has_attr),
        url(r'^head_end_title_start_has_attr/?$', head_end_title_start_has_attr),
        url(r'^head_end_title_end_has_attr/?$', head_end_title_end_has_attr),

        url(r'^befor_head_start_has_head_note/?$', befor_head_start_has_head_note),
        url(r'^befor_title_start_has_head_note/?$', befor_title_start_has_head_note),
        url(r'^befor_title_end_has_head_note/?$', befor_title_end_has_head_note),
        url(r'^befor_head_end_has_head_note/?$', befor_head_end_has_head_note),
        url(r'^after_head_end_has_head_note/?$', after_head_end_has_head_note),
        url(r'^befor_head_start_has_title_note/?$', befor_head_start_has_title_note),
        url(r'^befor_title_start_has_title_note/?$', befor_title_start_has_title_note),
        url(r'^befor_title_end_has_title_note/?$', befor_title_end_has_title_note),
        url(r'^befor_head_end_has_title_note/?$', befor_head_end_has_title_note),
        url(r'^after_head_end_has_title_note/?$', after_head_end_has_title_note),

        url(r'^title_has_special_char/?$', title_has_special_char),
        url(r'^head_has_special_char/?$', head_has_special_char),
        url(r'^html_has_special_char/?$', html_has_special_char),
        url(r'^size_gt_64k/?$', size_gt_64k),

        url(r'^requests_get/?$', requests_get),

        url(r'^db/insert/?$', db_insert),
        url(r'^db/delete/?$', db_delete),
        url(r'^db/update/?$', db_update),
        url(r'^db/select/?$', db_select),
        url(r'^db/transaction/?$', db_transaction),

        url(r'test/template/?$', test_template),
        url(r'test/func_view/?$', func_view),
        url(r'test/class_view/?$', ClassView.as_view())
    )

elif str(django.get_version()) == '1.7.11':
    urlpatterns = patterns(
        '',
        url(r'^admin/', include(admin.site.urls)),

        url(r'^resp_200/?$', resp_200),
        url(r'^resp_500/?$', resp_500),
        url(r'^resp_json/?$', resp_json),

        url(r'^no_html_start/?$', no_html_start),
        url(r'^no_html_end/?$', no_html_end),
        url(r'^no_head_start/?$', no_head_start),
        url(r'^no_head_end/?$', no_head_end),
        url(r'^no_title_start/?$', no_title_start),
        url(r'^no_title_end/?$', no_title_end),
        url(r'^no_head_start_title_start/?$', no_head_start_title_start),
        url(r'^no_head_start_title_end/?$', no_head_start_title_end),
        url(r'^no_head/?$', no_head),
        url(r'^no_title/?$', no_title),
        url(r'^no_head_end_title_start/?$', no_head_end_title_start),
        url(r'^no_head_end_title_end/?$', no_head_end_title_end),
        url(r'^no_head_start_title/?$', no_head_start_title),
        url(r'^no_head_title_start/?$', no_head_title_start),
        url(r'^no_head_end_title/?$', no_head_end_title),

        url(r'^html_start_has_attr/?$', html_start_has_attr),
        url(r'^html_end_has_attr/?$', html_end_has_attr),
        url(r'^html_has_attr_lang_en/?$', html_has_attr_lang_en),
        url(r'^html_has_attr_lang_zh/?$', html_has_attr_lang_zh),
        url(r'^head_start_has_attr/?$', head_start_has_attr),
        url(r'^head_end_has_attr/?$', head_end_has_attr),
        url(r'^title_start_has_attr/?$', title_start_has_attr),
        url(r'^title_end_has_attr/?$', title_end_has_attr),
        url(r'^head_start_title_start_has_attr/?$', head_start_title_start_has_attr),
        url(r'^head_start_title_end_has_attr/?$', head_start_title_end_has_attr),
        url(r'^head_end_title_start_has_attr/?$', head_end_title_start_has_attr),
        url(r'^head_end_title_end_has_attr/?$', head_end_title_end_has_attr),

        url(r'^befor_head_start_has_head_note/?$', befor_head_start_has_head_note),
        url(r'^befor_title_start_has_head_note/?$', befor_title_start_has_head_note),
        url(r'^befor_title_end_has_head_note/?$', befor_title_end_has_head_note),
        url(r'^befor_head_end_has_head_note/?$', befor_head_end_has_head_note),
        url(r'^after_head_end_has_head_note/?$', after_head_end_has_head_note),
        url(r'^befor_head_start_has_title_note/?$', befor_head_start_has_title_note),
        url(r'^befor_title_start_has_title_note/?$', befor_title_start_has_title_note),
        url(r'^befor_title_end_has_title_note/?$', befor_title_end_has_title_note),
        url(r'^befor_head_end_has_title_note/?$', befor_head_end_has_title_note),
        url(r'^after_head_end_has_title_note/?$', after_head_end_has_title_note),

        url(r'^title_has_special_char/?$', title_has_special_char),
        url(r'^head_has_special_char/?$', head_has_special_char),
        url(r'^html_has_special_char/?$', html_has_special_char),
        url(r'^size_gt_64k/?$', size_gt_64k),

        url(r'^requests_get/?$', requests_get),

        url(r'^db/insert/?$', db_insert),
        url(r'^db/delete/?$', db_delete),
        url(r'^db/update/?$', db_update),
        url(r'^db/select/?$', db_select),

        url(r'test/template/?$', test_template),
        url(r'test/func_view/?$', func_view),
        url(r'test/class_view/?$', ClassView.as_view())
    )


elif str(django.get_version()) == '1.6':
    urlpatterns = patterns(
        '',
        url(r'^api/', include(urls)),

        url(r'^admin/', include(admin.site.urls)),

        url(r'^resp_200/?$', resp_200),
        url(r'^resp_500/?$', resp_500),
        url(r'^resp_json/?$', resp_json),

        url(r'^no_html_start/?$', no_html_start),
        url(r'^no_html_end/?$', no_html_end),
        url(r'^no_head_start/?$', no_head_start),
        url(r'^no_head_end/?$', no_head_end),
        url(r'^no_title_start/?$', no_title_start),
        url(r'^no_title_end/?$', no_title_end),
        url(r'^no_head_start_title_start/?$', no_head_start_title_start),
        url(r'^no_head_start_title_end/?$', no_head_start_title_end),
        url(r'^no_head/?$', no_head),
        url(r'^no_title/?$', no_title),
        url(r'^no_head_end_title_start/?$', no_head_end_title_start),
        url(r'^no_head_end_title_end/?$', no_head_end_title_end),
        url(r'^no_head_start_title/?$', no_head_start_title),
        url(r'^no_head_title_start/?$', no_head_title_start),
        url(r'^no_head_end_title/?$', no_head_end_title),

        url(r'^html_start_has_attr/?$', html_start_has_attr),
        url(r'^html_end_has_attr/?$', html_end_has_attr),
        url(r'^html_has_attr_lang_en/?$', html_has_attr_lang_en),
        url(r'^html_has_attr_lang_zh/?$', html_has_attr_lang_zh),
        url(r'^head_start_has_attr/?$', head_start_has_attr),
        url(r'^head_end_has_attr/?$', head_end_has_attr),
        url(r'^title_start_has_attr/?$', title_start_has_attr),
        url(r'^title_end_has_attr/?$', title_end_has_attr),
        url(r'^head_start_title_start_has_attr/?$', head_start_title_start_has_attr),
        url(r'^head_start_title_end_has_attr/?$', head_start_title_end_has_attr),
        url(r'^head_end_title_start_has_attr/?$', head_end_title_start_has_attr),
        url(r'^head_end_title_end_has_attr/?$', head_end_title_end_has_attr),

        url(r'^befor_head_start_has_head_note/?$', befor_head_start_has_head_note),
        url(r'^befor_title_start_has_head_note/?$', befor_title_start_has_head_note),
        url(r'^befor_title_end_has_head_note/?$', befor_title_end_has_head_note),
        url(r'^befor_head_end_has_head_note/?$', befor_head_end_has_head_note),
        url(r'^after_head_end_has_head_note/?$', after_head_end_has_head_note),
        url(r'^befor_head_start_has_title_note/?$', befor_head_start_has_title_note),
        url(r'^befor_title_start_has_title_note/?$', befor_title_start_has_title_note),
        url(r'^befor_title_end_has_title_note/?$', befor_title_end_has_title_note),
        url(r'^befor_head_end_has_title_note/?$', befor_head_end_has_title_note),
        url(r'^after_head_end_has_title_note/?$', after_head_end_has_title_note),

        url(r'^title_has_special_char/?$', title_has_special_char),
        url(r'^head_has_special_char/?$', head_has_special_char),
        url(r'^html_has_special_char/?$', html_has_special_char),
        url(r'^size_gt_64k/?$', size_gt_64k),

        url(r'^requests_get/?$', requests_get),

        url(r'^db/insert/?$', db_insert),
        url(r'^db/delete/?$', db_delete),
        url(r'^db/update/?$', db_update),
        url(r'^db/select/?$', db_select),

        url(r'test/template/?$', test_template),
        url(r'test/func_view/?$', func_view),
        url(r'test/class_view/?$', ClassView.as_view())
    )
else:
    urlpatterns = patterns(
        '',
        url(r'^admin/', include(admin.site.urls)),

        url(r'^resp_200/?$', resp_200),
        url(r'^resp_500/?$', resp_500),
        url(r'^resp_json/?$', resp_json),

        url(r'^no_html_start/?$', no_html_start),
        url(r'^no_html_end/?$', no_html_end),
        url(r'^no_head_start/?$', no_head_start),
        url(r'^no_head_end/?$', no_head_end),
        url(r'^no_title_start/?$', no_title_start),
        url(r'^no_title_end/?$', no_title_end),
        url(r'^no_head_start_title_start/?$', no_head_start_title_start),
        url(r'^no_head_start_title_end/?$', no_head_start_title_end),
        url(r'^no_head/?$', no_head),
        url(r'^no_title/?$', no_title),
        url(r'^no_head_end_title_start/?$', no_head_end_title_start),
        url(r'^no_head_end_title_end/?$', no_head_end_title_end),
        url(r'^no_head_start_title/?$', no_head_start_title),
        url(r'^no_head_title_start/?$', no_head_title_start),
        url(r'^no_head_end_title/?$', no_head_end_title),

        url(r'^html_start_has_attr/?$', html_start_has_attr),
        url(r'^html_end_has_attr/?$', html_end_has_attr),
        url(r'^html_has_attr_lang_en/?$', html_has_attr_lang_en),
        url(r'^html_has_attr_lang_zh/?$', html_has_attr_lang_zh),
        url(r'^head_start_has_attr/?$', head_start_has_attr),
        url(r'^head_end_has_attr/?$', head_end_has_attr),
        url(r'^title_start_has_attr/?$', title_start_has_attr),
        url(r'^title_end_has_attr/?$', title_end_has_attr),
        url(r'^head_start_title_start_has_attr/?$', head_start_title_start_has_attr),
        url(r'^head_start_title_end_has_attr/?$', head_start_title_end_has_attr),
        url(r'^head_end_title_start_has_attr/?$', head_end_title_start_has_attr),
        url(r'^head_end_title_end_has_attr/?$', head_end_title_end_has_attr),

        url(r'^befor_head_start_has_head_note/?$', befor_head_start_has_head_note),
        url(r'^befor_title_start_has_head_note/?$', befor_title_start_has_head_note),
        url(r'^befor_title_end_has_head_note/?$', befor_title_end_has_head_note),
        url(r'^befor_head_end_has_head_note/?$', befor_head_end_has_head_note),
        url(r'^after_head_end_has_head_note/?$', after_head_end_has_head_note),
        url(r'^befor_head_start_has_title_note/?$', befor_head_start_has_title_note),
        url(r'^befor_title_start_has_title_note/?$', befor_title_start_has_title_note),
        url(r'^befor_title_end_has_title_note/?$', befor_title_end_has_title_note),
        url(r'^befor_head_end_has_title_note/?$', befor_head_end_has_title_note),
        url(r'^after_head_end_has_title_note/?$', after_head_end_has_title_note),

        url(r'^title_has_special_char/?$', title_has_special_char),
        url(r'^head_has_special_char/?$', head_has_special_char),
        url(r'^html_has_special_char/?$', html_has_special_char),
        url(r'^size_gt_64k/?$', size_gt_64k),

        url(r'^requests_get/?$', requests_get),

        url(r'test/template/?$', test_template),
        url(r'test/func_view/?$', func_view),
        url(r'test/class_view/?$', ClassView.as_view())
    )

