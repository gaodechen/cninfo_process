"""
    downloads:
    公开招股书（招股说明书/招股意向书）
    《年度报告》 16 17 18
"""
import requests
import random
import time
import urllib

download_path = 'http://static.cninfo.com.cn/'
saving_path = './pdf/'

User_Agent = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"
]


headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5",
           'Host': 'www.cninfo.com.cn',
           'Origin': 'http://www.cninfo.com.cn',
           'Referer': 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice',
           'X-Requested-With': 'XMLHttpRequest'
           }




# 深市 年度报告
def szseAnnual(page, stock):
    query_path = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers['User-Agent'] = random.choice(User_Agent)  # 定义User_Agent
    query = {'pageNum': page,  # 页码
             'pageSize': 30,
             'tabName': 'fulltext',
             'column': 'szse',  # 深交所
             'stock': stock,
             'searchkey': '',
             'secid': '',
             'plate': 'sz',
             'category': 'category_ndbg_szsh;',  # 年度报告
             'trade': '',
             'seDate': '2016-01-01+~+2019-4-26'  # 时间区间
             }

    namelist = requests.post(query_path, headers=headers, data=query)
    return namelist.json()['announcements']


# 沪市 年度报告
def sseAnnual(page, stock):
    query_path = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers['User-Agent'] = random.choice(User_Agent)  # 定义User_Agent
    query = {'pageNum': page,  # 页码
             'pageSize': 30,
             'tabName': 'fulltext',
             'column': 'sse',
             'stock': stock,
             'searchkey': '',
             'secid': '',
             'plate': 'sh',
             'category': 'category_ndbg_szsh;',  # 年度报告
             'trade': '',
             'seDate': '2016-01-01+~+2019-4-26'  # 时间区间
             }

    namelist = requests.post(query_path, headers=headers, data=query)
    return namelist.json()['announcements']  # json中的年度报告信息


# 深市 招股
def szseStock(page, stock):
    query_path = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers['User-Agent'] = random.choice(User_Agent)  # 定义User_Agent
    query = {'pageNum': page,  # 页码
             'pageSize': 30,
             'tabName': 'fulltext',
             'column': 'szse',
             'stock': stock,
             'searchkey': '招股',
             'secid': '',
             'plate': 'sz',
             'category': '',
             'trade': '',
             'seDate': '2001-01-01+~+2019-4-26'  # 时间区间
             }

    namelist = requests.post(query_path, headers=headers, data=query)
    return namelist.json()['announcements']  # json中的年度报告信息


# 沪市 招股
def sseStock(page, stock):
    query_path = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers['User-Agent'] = random.choice(User_Agent)  # 定义User_Agent
    query = {'pageNum': page,  # 页码
             'pageSize': 30,
             'tabName': 'fulltext',
             'column': 'sse',
             'stock': stock,
             'searchkey': '招股',
             'secid': '',
             'plate': 'sh',
             'category': '',
             'trade': '',
             'seDate': '2001-01-01+~+2019-4-26'  # 时间区间
             }

    namelist = requests.post(query_path, headers=headers, data=query)
    return namelist.json()['announcements']  # json中的年度报告信息


# download PDF
def Download(single_page):
    if single_page is None:
        return

    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5",
               'Host': 'www.cninfo.com.cn',
               'Origin': 'http://www.cninfo.com.cn'
               }

    for i in single_page:
        allowed_list = [
            '2018年年度报告（更新后）',
            '2018年年度报告',
            '2017年年度报告（更新后）',
            '2017年年度报告',
            '2016年年度报告（更新后）',
            '2016年年度报告',
        ]
        allowed_list_2 = [
            '招股书',
            '招股说明书',
            '招股意向书',
        ]
        title = i['announcementTitle']
        allowed = title in allowed_list
        if '确认意见' in title:
            return
        for item in allowed_list_2:
            if item in title:
                allowed = True
                break
        if allowed:
            download = download_path + i["adjunctUrl"]
            name = i["secCode"] + '_' + i['secName'] + '_' + i['announcementTitle'] + '.pdf'
            if '*' in name:
                name = name.replace('*', '')
            file_path = saving_path + name
            time.sleep(random.random() * 2)

            headers['User-Agent'] = random.choice(User_Agent)
            r = requests.get(download)

            f = open(file_path, "wb")
            f.write(r.content)
            f.close()
        else:
            continue


# given page_number & stock number
def Run(page_number, stock):
    try:
        annual_report = szseAnnual(page_number, stock)
        stock_report = szseStock(page_number, stock)
        annual_report_ = sseAnnual(page_number, stock)
        stock_report_ = sseStock(page_number, stock)
    except:
        print(page_number, 'page error, retrying')
        try:
            annual_report = szseAnnual(page_number, stock)
        except:
            print(page_number, 'page error')
    Download(annual_report)
    Download(stock_report)
    Download(annual_report_)
    Download(stock_report_)


with open('company_id.txt') as file:
    lines = file.readlines()
    for line in lines:
        stock = line
        Run(1, line)
        print(line, "done")
