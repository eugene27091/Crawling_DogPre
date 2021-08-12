import pandas as pd

# data1 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_01.csv') # 파일 경로 지정
# data2 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_02.csv')
# data3 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_03.csv')
# data4 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_04.csv')
# data5 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_05.csv')
# data6 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_06.csv')

data7 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_07.csv') # 파일 경로 지정
data8 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_08.csv')
data9 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_09.csv')
data10 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_10.csv')
data11 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_11.csv')
data12 = pd.read_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang/Coupang_12.csv')

data7.columns = ['item_no','item_name','item_function','star_rating','review_name','review_day','review_total'] #컬럼 명 지정
data8.columns = ['item_no','item_name','item_function','star_rating','review_name','review_day','review_total']
data9.columns = ['item_no','item_name','item_function','star_rating','review_name','review_day','review_total']
data10.columns = ['item_no','item_name','item_function','star_rating','review_name','review_day','review_total']
data11.columns = ['item_no','item_name','item_function','star_rating','review_name','review_day','review_total']
data12.columns = ['item_no','item_name','item_function','star_rating','review_name','review_day','review_total']


# data2['item_no'] = data1['item_no']+60
# data3['item_no'] = data9['item_no']+120
# data10['item_no'] = data10['item_no']+180
# data11['item_no'] = data11['item_no']+240
# data12['item_no'] = data12['item_no']+300


data7['item_no'] = data8['item_no']+360
data8['item_no'] = data8['item_no']+420
data9['item_no'] = data9['item_no']+480
data10['item_no'] = data10['item_no']+540
data11['item_no'] = data11['item_no']+600
data12['item_no'] = data12['item_no']+660


# data13['item_no'] = data13['item_no']+720
# data14['item_no'] = data14['item_no']+780
# data15['item_no'] = data15['item_no']+840
# data16['item_no'] = data16['item_no']+900
# data17['item_no'] = data17['item_no']+960


data7_8 = data7.append(data8, ignore_index=True)   #합치는 코드
data7_9 = data7_8.append(data9, ignore_index=True)
data7_10 = data7_9.append(data10, ignore_index=True)
data7_11 = data7_10.append(data11, ignore_index=True)
data7_12 = data7_11.append(data12, ignore_index=True)



data7_12.to_csv('C:/Users/EUGENE/PycharmProjects/ExcelMerge/Coupang_page_7_12.csv', encoding='utf-8-sig') # 파일 출력 위치 지정


