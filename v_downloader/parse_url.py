import re

def parse_url(txt_path='./url_addr.txt'):
    with open(txt_path, 'r') as f1:
        url_lst = f1.readlines()
        
    p_url_lst = [re.match(pattern=r'https://\S+', string=url).group() for url in url_lst]

    with open(txt_path[:-4] + '_parsed.txt', 'w') as f2:
        for url in p_url_lst:
            f2.write(url+'\n')
        