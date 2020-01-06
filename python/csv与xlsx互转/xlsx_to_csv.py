# encoding: utf-8
import pandas as pd
import sys
  

def xlsx_to_csv(xlsx_file, csv_file):
    """
    csv 文件 \t 分隔，编码方式 utf-8
    """
    data_xls = pd.read_excel(xlsx_file)
    data_xls.to_csv(csv_file, sep="\t", encoding="utf-8")

  
if __name__ == '__main__':
	xlsx_file = sys.argv[1].strip()
	csv_file = sys.argv[2].strip()
    xlsx_to_csv(xlsx_file, csv_file)