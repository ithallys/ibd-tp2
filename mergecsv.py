import glob

import pandas as pd

interesting_files = glob.glob(r"G:\My Drive\UFMG\UFMG 2023.2\IBD\TP2\TP2_CoberturaVacinacao_Municipio\habitantes_ano\*.csv")
df = pd.concat((pd.read_csv(f, header = 0) for f in interesting_files))
df.to_csv(r"G:\My Drive\UFMG\UFMG 2023.2\IBD\TP2\TP2_CoberturaVacinacao_Municipio\habitantes_ano\merged.csv")