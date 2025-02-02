# @Time    : 2021/07/04
# @Author  : Naunter
# @Page    : https://github.com/Naunters
# @Page    : https://github.com/BDO-CnHope/bdocn_client

from time_template import time_template
from shutil import copy2

def loc_tw(dir):
    time_template()
    print("loc_lang.py >>> def loc_tw(dir)")

    fromloc = dir + r'/ads/languagedata_en.loc'
    toloc = dir + r'/ads/languagedata_tw.loc'

    print("loc_lang.py >>> def loc_tw(dir): copy "+fromloc+" to "+toloc)
    copy2(fromloc,toloc)

def loc_pt(dir):
    time_template()
    print("loc_lang.py >>> def loc_pt(dir)")

    fromloc = dir + r'/ads/languagedata_en.loc'
    toloc = dir + r'/ads/languagedata_pt.loc'

    print("loc_lang.py >>> def loc_pt(dir): copy "+fromloc+" to "+toloc)
    copy2(fromloc,toloc)

def loc_jp(dir):
    time_template()
    print("loc_lang.py >>> def loc_jp(dir)")

    fromloc = dir + r'/ads/languagedata_en.loc'
    toloc = dir + r'/ads/languagedata_jp.loc'

    print("loc_lang.py >>> def loc_jp(dir): copy "+fromloc+" to "+toloc)
    copy2(fromloc,toloc)

def loc_ru(dir):
    time_template()
    print("loc_lang.py >>> def loc_ru(dir)")

    fromloc = dir + r'/ads/languagedata_en.loc'
    toloc = dir + r'/ads/languagedata_ru.loc'

    print("loc_lang.py >>> def loc_ru(dir): copy "+fromloc+" to "+toloc)
    copy2(fromloc,toloc)

def loc_fr(dir):
    time_template()
    print("loc_lang.py >>> def loc_fr(dir)")

    fromloc = dir + r'/ads/languagedata_en.loc'
    toloc = dir + r'/ads/languagedata_fr.loc'

    print("loc_lang.py >>> def loc_fr(dir): copy "+fromloc+" to "+toloc)
    copy2(fromloc,toloc)