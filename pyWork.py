import pandas as pd
df = pd.read_csv(r'C:\Users\1568925.ZONE1-SCBNET\Downloads\WB_Non_Derv_final_201712.csv')


df['source_sys'] = df['Contract.Reference'].apply(lambda x: get_sys_name(x) )
" df['bcrs_matching_key'] = df.apply(lambda row: find_bcrs_matching_key(row), axis = 1) "
" df['bcrs_matching_key'] = df.apply(find_bcrs_matching_key(row), axis = 1) "
df['bcrs_matching_key'] = df.apply(set_bcrs_matching_key, axis = 1)


df.to_csv(r'C:\Users\1568925.ZONE1-SCBNET\Downloads\new.csv')

" df[12:13]['bcrs_matching_key'] "
