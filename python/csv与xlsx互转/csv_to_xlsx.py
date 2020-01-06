# encoding: utf-8
import pandas as pd
import sys
  

def csv_to_xlsx(cvs_file, xlsx_file):
    """
    csv 文件 \t 分隔，编码方式 utf-8
    """
	csv = pd.read_csv(csv_file, sep='\t', encoding='utf-8')
	csv.to_excel(xlsx_file, sheet_name='data')

  
if __name__ == '__main__':
	csv_file = sys.argv[1].strip()
	xlsx_file = sys.argv[2].strip()
	csv_to_xlsx(csv_file, xlsx_file)