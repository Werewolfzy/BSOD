#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Werewolfzy

import sys
import getopt
import pandas as pd
import numpy as np
import os



def usage():
    print(
"""
usage: python [{0}] ... [-i input_file | -o out_file]  ...
参数说明:
-i     : 输入文件名字
-o     : 数据保存名字
-h     : 帮助信息
""".format(sys.argv[0]))

def main():

    opts,args = getopt.getopt(sys.argv[1:],"hi:o:")
    input_file = ""
    out_file = "result.txt"


    for op,value in opts:
        if op == '-i':
            input_file = value
        elif op == "-o":
            out_file = value
        else:
            usage()
            sys.exit()
            return


    # print(genotype_file,phenotype_file,significant_snp,freq_cutoff,parent_info,out_file)


    # print(df)

    data = pd.read_csv(input_file, encoding="gbk", sep="\t", header=None)
    data2 = data[1].str.split('_', expand=True)
    data3 = data.drop([0], axis=1).join(data2[0])
    data3[0].replace('[a-z]', '', regex=True, inplace=True)
    select_cols = [0, 1, 2, 3]
    data4 = data3[select_cols]
    data4.to_csv(out_file, sep='\t', header=0, index=False)


    print('程序运行结束，请查看结果文件')



if __name__ == '__main__':
    main()













