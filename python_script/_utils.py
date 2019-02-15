#!/usr/bin/env python3
import os
import re

def check_folder(path):
    """
    检查的文件夹是否存在，如果不存在则新建

    --
    :param path: 

    """
    if not os.path.exists(path):
        os.mkdir(path)   
    return True

def find_all_file(rootdir='', **kw):
    """
    遍历文件列表

    --
    :param rootpath: "THIS_FOLDER" 绝对路径,默认为文件当前路径

    :param suffix_filter: ['XLSX'] 文件后缀筛选,需要的文件后缀

    :param name_filter: [''] 文件名关键字筛选，含有关键字的文件不会被返回
    :returns: ["",""] 绝对文件路径
    """

    files_dir = os.listdir(rootdir)
    __files = []
    suffix_filter = kw['suffix_filter'] if 'suffix_filter' in kw.keys() else [
        'xls', 'xlsx', 'xlsm']
    name_fileter = kw['name_filter'] if 'name_filter' in kw.keys() else []
    for i in range(0, len(files_dir)):

        path = os.path.join(rootdir, files_dir[i])
        if os.path.isdir(path):
            __files.extend(find_all_file(path, suffix_filter=suffix_filter))
        if os.path.isfile(path):
            # 过滤文件名
            for each in name_fileter:
                if each in os.path.splitext(files_dir[i])[0]:
                    continue
            if os.path.splitext(path)[1][1:] in suffix_filter:
                # os.remove(path)
                if os.path.splitext(files_dir[i])[0].find('~') == 0:
                    continue
                __files.append(path)
    return __files

def get_url_list(*args,**kwargs):
    '''
    把url构建成list \n
    --
    :param url: url 链接 \n
    :returns: list 返回的列表

    http://www.xinhuanet.com/travel \n
    [com,xinhuanet,www,travel]
    '''
    from urllib import parse
    url=args[0]
    url_list=[]
    url=parse.urlparse(url)
    url_list.extend(reversed(url[1].split('.')))
    
    for url in url[2].split('/'):
        if url!='':
            url_list.append(url)
    return url_list
def isurl(url=None):
    """ 
    判断是否是url

    --
    :param url: None 默认为空

    :returns: Bool 是返回True,否者返回False
    """
    if url == None:
        return False
    pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')    # 匹配模式
    strs = re.findall(pattern, str(url))
    if strs:
        if url == strs[0]:
            return True
    else:
        return False
    pass

def cut_filename(path):
    """
    传入绝对路径文件名

    --

    :param path: str 绝对路径

    :returns: str 绝对路径

    :returns: str 文件名

    :returns: str 文件后缀
    """
    path = os.path.split(path)
    cut = os.path.splitext(path[1])
    return (path[0], cut[0], cut[1])

def cut_url(url):
    """
    切分url
    
    --
    :param url:url
    :return []
    """

def html_filter(input_text):
    """
    正则去除html标签
    
    --
    :param input_text: str 输入html文本

    :returns: str 去除html标签文本
    """
    import re
    return re.sub('<\/?[\s\S]*?(?:".*")*>','',input_text)

def _filter_tags(htmlstr):
    """
    正则去除HTML标签

    --
    :param htmlstr:
    :return:
    """
    def _replaceCharEntity(htmlstr):
        """
        :param htmlstr:HTML字符串
        :function:过滤HTML中的标签
        """
        CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                        'lt': '<', '60': '<',
                        'gt': '>', '62': '>',
                        'amp': '&', '38': '&',
                        'quot': '"', '34': '"', }

        re_charEntity = re.compile(r'&#?(?P<name>\w+);')
        sz = re_charEntity.search(htmlstr)
        while sz:
            entity = sz.group()  # entity全称，如>
            key = sz.group('name')  # 去除&;后entity,如>为gt
            try:
                htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
                sz = re_charEntity.search(htmlstr)
            except KeyError:
                # 以空串代替
                htmlstr = re_charEntity.sub('', htmlstr, 1)
                sz = re_charEntity.search(htmlstr)
        return htmlstr
    def _repalce(s, re_exp, repl_string):
        return re_exp.sub(repl_string,s)        
    def cleaning_data(strs):
        strs=str(strs).replace('<p>&nbsp; &nbsp; &nbsp; &nbsp;','').replace('</p><p><br></p>','').replace('<br>','').replace('</p>','').replace('<p>','').replace('       ','').replace('[图片]','').strip()
        strs=_filter_tags(strs)
        return _replaceCharEntity(strs)

    # CDATA
    re_cdata = re.compile('//<!\
    CDATA\[[ >]∗ //\
    CDATA\[[ >]∗ //\
    \] > ',re.I)
    
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    # Script
    
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
    # style
    
    re_br = re.compile('<br\s*?/?>')
    # 换行
    
    re_h = re.compile('</?\w+[^>]*>')
    # HTML标签
    
    re_comment = re.compile('<!--[^>]*-->')
    # HTML注释
    
    s = re_cdata.sub('', htmlstr)
    # 去掉CDATA
    
    s = re_script.sub('', s)  # 去掉SCRIPT
    
    s = re_style.sub('', s)
    # 去掉style
    
    s = re_br.sub('\n', s)
    # 将br转换为换行
    
    s = re_h.sub('', s)  # 去掉HTML 标签
    
    s = re_comment.sub('', s)
    # 去掉HTML注释
    
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = _replaceCharEntity(s)  # 替换实体
    return s

def word_count(*args,**kwargs):
    """词频统计,大->小"""
    try:
        import jieba
    except:
        return ()
    content_count={}
    content_cut=jieba.lcut(args[0])
    for word in content_cut:
        if word not in content_count:
            content_count[word]=1
        else:
            content_count[word]+=1
    content_count=sorted(content_count.items(),key=lambda x:x[1],reverse=True)
    return content_count