import os

ChBibleRaw = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "hgb.txt")
EnBibleRaw = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "bbe.txt")
DeBibleRaw = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "Martin_Luther_Uebersetzung_1912.txt")

ChBibleCsv = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "hgb.csv")
EnBibleCsv = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "bbe.csv")
DeBibleCsv = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "Martin_Luther_Uebersetzung_1912.csv")

DeBibleLst = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "Martin_Luther_Uebersetzung_1912.lst")
DeBibleLDG = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "Martin_Luther_Uebersetzung_1912.ldg")

ChBiblePickle = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "hgb.pickle")
EnBiblePickle = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "bbe.pickle")
DeBiblePickle = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "Martin_Luther_Uebersetzung_1912.pickle")

EnBibleWords = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "bbeWords.txt")

ChSntSeparators = ["。", "？","！", "；"]
EnSntSeparators = [ "\.", "\?","!", ";", ":"]


#
# following are raw bible files
#
chinese_train_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", 'hgb.txt')
english_train_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", 'bbe.txt')
german_train_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data",
                                 'Martin_Luther_Uebersetzung_1912.txt')

#
# following are LDC2002T01 en-ch training files
# chinese txt encoded in gb2312
#
LDC2002T01_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "mt_chinese_v1")
ch_loc = 'source'
en_loc = 'translation'
en_sub_loc = 't[a|b][0-9]'
en_sub = 'ta0'