import xlrd
import sys
from utils import get_config

if len(sys.argv) != 2:
    print("Usage : python3 get_surperformer_players.py surperform_percent")
    #quit()

# prct = int(sys.argv[1])/100 + 1
prct = 1.35
conf = get_config("/mnt/c/Users/perig.cosseckerloch/test/conf/config.json")

l10_worksheet = xlrd.open_workbook(conf.get('L10_FILE_PATH')).sheet_by_index(0)
d_l10 = {}
for i in range(2, l10_worksheet.nrows):
    d_l10[l10_worksheet.cell_value(i, 1).lower()]=float(l10_worksheet.cell_value(i, 3))

previsions_l10_worksheet = xlrd.open_workbook(conf.get('PREVISION_FILE_PATH')).sheet_by_index(0)
d_predicted = {}
for i in range(1, previsions_l10_worksheet.nrows):
    d_predicted[previsions_l10_worksheet.cell_value(i, 0).lower()]={
        "score":previsions_l10_worksheet.cell_value(i, 22),
        "match":'{}-{}'.format(previsions_l10_worksheet.cell_value(i, 1), previsions_l10_worksheet.cell_value(i, 2))
    }

d_final={}
for key, value in d_l10.items():
    if d_predicted.get(key):
        d_final[key]={
            "l10":value,
            "Predicted":d_predicted.get(key)
        }

surperformers={}
for key, value in d_final.items():
    if value.get("Predicted") and value.get("l10") and prct*value["l10"]<value["Predicted"].get("score") and value["l10"]>10:
        surperformers[key]={
            "l10":value.get("l10"),
            "Predicted": d_predicted.get(key).get('score'),
            "Match": d_predicted.get(key).get('match')
        }

print("Here are the surperformers players having a prediction {} percent above their l10 :\n{}".format(prct, surperformers))