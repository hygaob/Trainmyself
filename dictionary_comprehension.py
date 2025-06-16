#Python 字典推導式
#dictionary=
#{key: expression for key , value in iterable}

#運算
#華氏列表
cities_in_F={'LA':80,'New York':65,'Chicago':50,"Miami":90}
#轉換攝氏
cities_in_C={key:(value-32)*5/9 for key,value in cities_in_F.items()}
print(cities_in_F)
print(f"{cities_in_C}")

#ex2 條件判斷
weather = {'台北':"大晴天","台中":"大晴天","宜蘭":"下雨","台東":"下雨"}
sunnuy_weather={key:value for key,value in weather.items() if value =="大晴天"}
print(sunnuy_weather)

#ex3 條件判斷+函式

cities_in_F={'LA':80,'New York':65,'Chicago':50,"Miami":90}


def check_temp(value):
    if value >=70:
        return  "熱"
    elif 40<= value:
        return "溫暖"
    else:
        return '冷'
description_cities={key:check_temp(value) for key, value in cities_in_F.items()}
print(description_cities)




