# -*- coding: utf-8 -*-
import codecs
import os
import re
import sys
from .insert_to_db import insert_2snt_into_db_table
from bs4 import BeautifulSoup
from .config_wv import LDC2002T01_loc, ch_loc, en_loc, en_sub, chinese_train_file, english_train_file, german_train_file

#
# load all LDC2002T01 paired ch-en sentences into Database
#
def load_ldc_into_database(ldc = LDC2002T01_loc, ch_loc = ch_loc, en_loc = en_loc, en_sub = en_sub):
    """
    table ldc2002t01: id | fname | en_sub | seg_id  | ch_snt | en_snt | ch_ldg | ch_sdg | en_ldg | en_sdg
    :param ldc:
    :param ch_loc:
    :param en_loc:
    :param en_sub:
    :return:
    """
    ch_path = os.path.join(LDC2002T01_loc, ch_loc)
    en_path = os.path.join(LDC2002T01_loc, en_loc, en_sub)
    ch_files = [f for f in os.listdir(ch_path) if re.match(r'.*\.sgm', f)]
    en_files = [f for f in os.listdir(en_path) if re.match(r'.*\.sgm', f)]
    if len(ch_files) != len(en_files):
        print('paired directories contain different number of files')
        return
    else:
        n = 0
        for fname in ch_files:
            ch_fname = os.path.join(ch_path, fname)
            en_fname = os.path.join(en_path, fname)
            try:
                ch_seg_lst = get_ldc_in_soup(ch_fname, lan = 'ch').find_all('seg')
                en_seg_lst = get_ldc_in_soup(en_fname, lan = 'en').find_all('seg')
                for i in range(len(ch_seg_lst)):
                    n += 1
                    ch_txt = ch_seg_lst[i].get_text().strip()
                    en_txt = en_seg_lst[i].get_text().strip()
                    print(fname, en_sub, i, ch_txt, en_txt, '\n')
                    insert_2snt_into_db_table(db='language_graph', dbuser='postgres', table='ldc2002t01',
                                              id=n, fname=fname, en_sub=en_sub, seg_id = i, ch_snt=ch_txt, en_snt=en_txt)
            except OSError as err:
                print("OS error: {0}".format(err))
            except:
                print("Unexpected error:", sys.exc_info()[0])


#
# read LDC2002T01 chinese file
#
def get_ldc_in_soup(fname, lan='ch'):
    """
    :param fname: must be the full file name wit path
    :param lan: 'ch' or 'en'
    :return: soup object
    """
    if lan == 'ch':
        fhd = codecs.open(fname, 'rb', encoding='gb2312')
        ch_txt = fhd.read()
        soup = BeautifulSoup(ch_txt, 'html.parser')
        return soup
    elif lan == 'en':
        fhd = open(fname, 'rb')
        en_txt = fhd.read()
        soup = BeautifulSoup(en_txt, 'html.parser')
        return soup
    else:
        print('Usage: lan="ch" or "en"')
        return


def read_train_file(fname, encode='utf-8'):
    """

    :param fname:
    :param encode:
    :return:
    """
    fhandle = codecs.open(fname, "r", encode)
    for line in fhandle.readlines():
        line = line.strip('\n')
        bbid = ''
        snt = ''
        lst = line.split(' ')
        if len(lst) < 3:
            bbid = lst[0]+' '+lst[1]
        elif ':' in lst[1]:
            bbid = lst[0]+' '+lst[1]
            snt = ' '.join(lst[2:])
        else:
            print('**', lst)
        print(bbid, snt)


def test_reading_train_files():
    read_train_file(chinese_train_file, encode="gb2312")
    read_train_file(german_train_file, encode='ISO-8859-1')
    read_train_file(english_train_file)