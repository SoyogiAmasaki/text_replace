#!/usr/bin/env python
import os
import pandas as pd
import textfile as tf

class RuleTbl():
    hasExisted = False
    tblData = 0
    row = 0

    def read_src_file(self, file_path):
        ext = os.path.splitext(file_path)
        if ext[1] == '.csv':
            self.hasExisted = True
            self.tblData = pd.read_csv(file_path)
        elif ext[1] == '.xlsx':
            self.hasExisted = True
            self.tblData = pd.read_excel(file_path, index_col=0)
        else:
            self.hasExisted = False
            self.tblData = 0
            return
        self.row = len(self.tblData)

def replace_txt(rule_file_path, src_txt_file_path, target_str):
    rule_tbl = RuleTbl()
    rule_tbl.read_src_file(rule_file_path)
    if rule_tbl.hasExisted:
        target_data = ""
        with open(src_txt_file_path, encoding='utf-8') as src_file:
            target_data = src_file.read()
        col_num = rule_tbl.tblData.columns.get_loc(target_str)
        for num in range(rule_tbl.row):
            target_data = target_data.replace(rule_tbl.tblData.iloc[num, 0], rule_tbl.tblData.iloc[num, col_num])
        return target_data

def read_col_title(rule_file_path):
    rule_tbl = RuleTbl()
    rule_tbl.read_src_file(rule_file_path)
    if rule_tbl.hasExisted:
        replacelist = rule_tbl.tblData.columns.values
        return replacelist.tolist()
    return "NoData"