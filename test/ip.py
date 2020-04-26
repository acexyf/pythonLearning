from gevent import monkey
monkey.patch_all()
from fake_useragent import UserAgent
import re, requests, time, gevent, json


# 随机获取ua
def gen_ua():
    ua = UserAgent()
    return ua.random


# 获取西刺高匿代理
def get_ip(url):
    headers = {'User-Agent': gen_ua()}
    html = requests.get(url, headers=headers).text
    time.sleep(1)
    pattern = r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,5}).*?高匿.*?(HTTPS?)'
    tds = re.findall(pattern, html, re.S)
    for td in tds:
        k = 'http' if td[2] == 'HTTP' else 'https'
        v = '{}:{}'.format(td[0], td[1])
        yield {k: v}


# 检测IP是否可用
def check_ip(ips):
    for ip in ips:
        try:
            r = requests.get('https://httpbin.org/ip', proxies=ip, timeout=3)
            r.raise_for_status()
            if '119.129' not in r.text:
                print(ip, '可用')
                ip_str = json.dumps(ip)
                with open('ip.txt', 'a', encoding='utf-8') as f:
                    f.write(ip_str + '\n')
            else:
                print(ip, '不可用')
                
        except:
            pass


# 主程序
def crawler(url):
    ips = get_ip(url)
    check_ip(ips)


if __name__ == '__main__':
    urls = [
        'https://www.xicidaili.com/nn/',
        'https://www.xicidaili.com/wn/',
        'https://www.xicidaili.com/wt/'
    ]
    url_list = [url+str(i+1) for url in urls for i in range(2)]
    tasks_list = [gevent.spawn(crawler, url) for url in url_list]
    gevent.joinall(tasks_list)