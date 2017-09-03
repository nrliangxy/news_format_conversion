# -*- encoding: utf-8 -*-
import os
import re
import arrow
path1 = '/home/liangxiaoyong/Downloads/11'
path2 = '/home/lxy/Downloads/financial-news-dataset-master/20061020_20131126_bloomberg_news'

def export_file(path):
    """
    :param path:
    :return: json_news
    """
    file = open(path,'r')
    all_lines = file.readlines()
    file.close()
    name = ''
    result = {'data_type': 'news', 'source_categories': ['investment']}
    try:
        authors = all_lines[1].lstrip('-- ')
        authors1 = re.sub(r'\[.*?\]','',authors)
    except IndexError:
        return
    if all_lines[0].strip() == '--' or all_lines[2].lstrip('-- ')[:2] != '20' :
        return
    else:
        if 'B y' in authors1:
            n1 = authors1.lstrip('-- B y   ')
            no_space_list = [re.sub(r'\s{1}?', '', i) for i in n1.split("   ")]
            for i in no_space_list:
                name += i
                name += ' '
            result["authors"] = [name.strip()]
        else:
            result["authors"] = [authors1]
        post_ts = arrow.get(all_lines[2].lstrip('-- ')).to('local').timestamp
        if all_lines[0]:
            result["title"] = all_lines[0].lstrip('-- ')
        if all_lines[2]:
            #result["post_ts"] = all_lines[2].lstrip('-- ')
            result["post_ts"] = post_ts
        if all_lines[3]:
            result["url"] = all_lines[3].lstrip('-- ')
        return result

def start(start_path):
    for path,d,filelist in os.walk(start_path):
        for filename in filelist:
            direct = os.path.join(path,filename)
            #print(direct)
            try:
                print(export_file(direct))
            except UnicodeDecodeError:
                pass
if __name__ == '__main__':
    start(path2)


