###Python练习题第 0011题
https://github.com/Yixiaohan/show-me-the-code
*用 Python 写一个爬图片的程序，爬这个链接里的日本妹子图片 :-)*
http://tieba.baidu.com/p/2166231880

如果html是这样子的话：
```html
<img...>...</img>
<img...>...</img>
<img...>...</img>
```

用BeautifulSoup是没问题的，可是！贴吧里上传的图片，html是下面这样的，用BeautifulSoup的话会死的很惨，结果超出想象！
所以果断用正则非贪婪模式找到所有节点之后，再用BS拎出每个图片的链接。
```html
<img...><img...><img...></img></img></img>
```

###知识点Get
####Python整型和字符串的转换
int -> str: str(int_value)
str -> int: int(str_value)
####正则非贪婪模式和贪婪模式
http://deerchao.net/tutorials/regex/regex.htm
