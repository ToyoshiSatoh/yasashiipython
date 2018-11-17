year_str = input('あなたの生まれた年を西暦4桁で入力してください。: ')
year = int(year_str) # 西暦を数値に変換する
# 干支の順番（0-11の範囲）を西暦から計算する
number_of_eto = (year + 8) % 12
print ('あなたの干支の順番は',number_of_eto,'番です。')
