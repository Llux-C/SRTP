#读取数据
import pandas as pd
import math
import numpy as np
import glob,os

empty = pd.read_csv(r'./data/empty.csv')
loc_file = pd.read_csv("./data/site_list.csv")
site_list = loc_file['监测点编码']
site_list = site_list.tolist()

# 用于将角度转换为弧度
def ConvertDegreesToRadians(degrees):
    return degrees * math.pi / 180


# 用于将弧度转换为角度
def ConvertRadiansToDegrees(radian):
    return radian * 180.0 / math.pi


# 用于计算HverSin的值（用于进行经纬度与距离转化的一种数学公式，详情参考wiki）
def HaverSin(theta):
    v = math.sin(theta / 2)
    return v * v


# 用于计算两个用经纬度表示的地点之间的‘实际’距离,单位为km（公里）
def Distance(lat1, lon1, lat2, lon2):
    lat1 = ConvertDegreesToRadians(lat1)
    lon1 = ConvertDegreesToRadians(lon1)
    lat2 = ConvertDegreesToRadians(lat2)
    lon2 = ConvertDegreesToRadians(lon2)
    # 计算经纬度的差值
    vLon = math.fabs(lon1 - lon2)
    vLat = math.fabs(lat1 - lat2)
    # 计算距离相关数值
    EARTH_RADIUS = 6371.0
    h = HaverSin(vLat) + math.cos(lat1) * math.cos(lat2) * HaverSin(vLon)
    return 2 * EARTH_RADIUS * math.asin(math.sqrt(h))



def cal_dist(loc1, loc2):
    a = site_list.loc[site_list['监测点编码'] == loc1]['纬度'].iloc[0]
    b = site_list.loc[site_list['监测点编码'] == loc1]['经度'].iloc[0]
    c = site_list.loc[site_list['监测点编码'] == loc2]['纬度'].iloc[0]
    d = site_list.loc[site_list['监测点编码'] == loc2]['经度'].iloc[0]
    return Distance(a, b, c, d)


# IDW
# 不能整行为空
# 输入需要填补的监测点编号以及时间点
def IDW(df, hour, loc, alpha, city_site):
    count = 0
    sum = 0
    dist_sum = 0
    for i in range(len(city_site)):
        if not (pd.isnull(df.at[hour, city_site[i]])) and city_site[i] != loc:
            sum = sum + df.at[hour, city_site[i]] * pow(cal_dist(loc, city_site[i]), (-alpha))
            dist_sum = dist_sum + pow(cal_dist(loc, city_site[i]), (-alpha))
    #print(sum / dist_sum)
    return (sum / dist_sum)


# SES
def SES(df, hour, loc, beta):
    nume = 0
    deno = 0
    for i in range(24):
        if not (pd.isnull(df.at[i, loc])) and i != hour:
            # print(df.at[i,loc])
            nume = nume + df.at[i, loc] * beta * pow(1 - beta, abs(hour - i))
            deno = deno + beta * pow(1 - beta, abs(hour - i))
    #print(nume)
    #print(deno)
    #print(nume / deno)
    return (nume / deno)


# UCF
def sim_s(df, loc1, loc2, hour, omega):
    start = hour - (omega - 1) / 2
    end = hour + (omega - 1) / 2
    if start < 0:
        start = 0
    if end > 23:
        end = 23
    sum = 0
    count = 0

    for i in range(int(start), int(end + 1)):
        if not (pd.isnull(df.at[i, loc1])) and not (pd.isnull(df.at[i, loc2])):
            # print(df.at[i,loc1],',',df.at[i,loc2])
            sum = sum + pow(abs(df.at[i, loc1] - df.at[i, loc2]), 2)
            count = count + 1

    return (pow(sum / count, -1 / 2))


def UCF(df, hour, loc, omega, city_site):
    length = len(city_site)
    sum = 0
    nume = 0
    deno = 0
    for i in range(length):
        if city_site[i] != loc and not pd.isnull(df.at[hour, city_site[i]]):
            sim = sim_s(df, loc, city_site[i], hour, omega)
            #print(df.at[hour, city_site[i]], ',', sim)
            nume = nume + df.at[hour, city_site[i]] * sim
            deno = deno + sim
    #print(nume / deno)
    return (nume / deno)


def sim_icf(df, h1, h2, city_site):
    length = len(city_site)
    sum = 0
    NS = 0
    for i in range(length):
        if not (pd.isnull(df.at[h1, city_site[i]])) and not (pd.isnull(df.at[h2, city_site[i]])):
            sum = sum + pow(abs(df.at[h1, city_site[i]] - df.at[h2, city_site[i]]), 2)
            NS = NS + 1
    return (pow(sum / NS, -1 / 2))


def ICF(df, hour, loc, omega, city_site):
    start = hour - (omega - 1) / 2
    end = hour + (omega - 1) / 2
    if start < 0:
        start = 0
    if end > 23:
        end = 23
    nume = 0
    deno = 0
    for i in range(int(start), int(end)):
        if i != hour and not (pd.isnull(df.at[i, loc])):
            sim = sim_icf(df, i, hour, city_site)
            nume = nume + df.at[i, loc] * sim
            deno = deno + sim
    #print(nume / deno)
    return (nume / deno)


def find_miss(df, j, city_site):
    block_missing = bool(0)
    exist_missing = bool(0)
    miss_item = []
    start = 0
    end = 24
    for i in range(int(start), int(end)):
        if not pd.isnull(df.at[i, city_site[j]]):
            continue
        if not exist_missing:
            exist_missing = bool(1)
        miss_item.append(i)
    if len(miss_item) == 24:
        block_missing = bool(1)
    return (exist_missing, block_missing, miss_item)


def FMV(df, omega, alpha, beta, city_site):
    length = len(city_site)
    # print(length)
    # print(df)
    miss_items = []
    # miss_block只表示在某一个时间戳情况下city_site的所有值均为NAN,在这里用miss_block来表示特定时间点（24）小时中，哪些时间戳出现了block_missing
    miss_block = [bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), \
                  bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), \
                  bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0)]
    miss_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(length):
        miss_items.append(find_miss(df, i, city_site))
        length2 = len(miss_items[i][2])
        for m in range(length2):
            miss_count[miss_items[i][2][m]] = miss_count[miss_items[i][2][m]] + 1
            if i == length - 1 and miss_count[miss_items[i][2][m]] == length:
                miss_block[miss_items[i][2][m]] = bool(1)
    for i in range(length):
        length2 = len(miss_items[i][2])
        for m in range(length2):
            if not miss_items[i][1] and not miss_block[miss_items[i][2][m]]:  # 表示只是普通的缺失，而不是block_missing
                val1 = ICF(df, miss_items[i][2][m], city_site[i], omega, city_site)
                val2 = UCF(df, miss_items[i][2][m], city_site[i], omega, city_site)
                #print(val1)
                #print(val2)
                mean = (val1 + val2) / 2
                #print("mean:%f" % (mean))
                df.at[miss_items[i][2][m], city_site[i]] = mean
            if miss_items[i][1] or miss_block[miss_items[i][2][m]]:  # 如果发生一个地点所有时间戳都没有数据则发生block_missing
                val1 = 0
                val2 = 0
                count = 0
                if miss_items[i][1]:
                    val1 = IDW(df, miss_items[i][2][m], city_site[i], alpha, city_site)
                    count = count + 1
                if miss_block[miss_items[i][2][m]]:
                    val2 = SES(df, miss_items[i][2][m], city_site[i], beta)
                    count = count + 1
                val = (val1 + val2) / count
                #print("val:%f" % (val))
                df.at[miss_items[i][2][m], city_site[i]] = val
    for i in range(length):
        length2 = len(miss_items[i][2])
        for m in range(length2):
            if miss_items[i][1] or miss_block[miss_items[i][2][m]]:
                val1 = ICF(df, miss_items[i][2][m], city_site[i], omega, city_site)
                val2 = UCF(df, miss_items[i][2][m], city_site[i], omega, city_site)
                mean = (val1 + val2) / 2
                df.at[miss_items[i][2][m], city_site[i]] = mean
    # print(miss_items)
    # print(df)
    print('success')
    return df


#dfff = FMV(data_final, 7, 4, 0.85, city_site)

#dfff.to_json('a.json')
