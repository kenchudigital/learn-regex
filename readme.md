### Content
- [Introduction](#Introduction)
- [Get_Started](#Get_Started)
- [Function](#Function)
- [Flags](#Flags)
- [Regex](#Regex)

***

### Introduction

Regex 簡單來說，利用 pattern 從 string 指定特定字句。為了做到「指定」這個動作，需要 Regex 這種表達方式

例如我要從 string 找出所有數字:

<pre>
string = "some digits: 888"
pattern = re.compile(r"<a href="learn-regex">\d"</a>>)     # \d 是任何數字的表達
re.findall(pattern, string)      # 利用表達式找到 string 內的數字
</pre>

<pre>
Answer: ['8', '8', '8']
</pre>
Documentation: https://docs.python.org/3/library/re.html

測試工具: https://regex101.com/

***

### Get_Started

初學者設定 pattern 時會常用:

<pre>
pattern = re.compile(<a href="learn-regex">r"</a>\d<a href="learn-regex">"</a>)
</pre>

<a href="learn-regex">r""</a> 是指 raw string，令一些特姝字符以最原始的 string 表達，例如 <a href="learn-regex">"\n"</a> 會變為隔行。

另外是以上的寫法是多餘的，因為在運行 function 時，便會自動執行 <a href="learn-regex">pattern = re.complie()</a> 了。

***

### Function

Python <a>re</a> 可以利用不同的 function 得到指定的字符。

#1 <a>re.match( ).group( )</a> -> string
<pre>
假設：pattern = r"\d", string = 12345
re.match(pattern, string).group()  //1
re.match(pattern, string).group(0) //1
re.match(pattern, string).group(1) //2
# re.match( ) 結果為 re.Match object
</pre>

***

#2 <a>re.findall( )</a> -> list
<pre>
假設：pattern = r"\d", string = 12345
re.findall(pattern, string) // [1, 2, 3, 4, 5]
</pre>

***

#3 <a>re.finditer( )</a> -> iterator 

<pre>
假設：pattern = r"\d", string = 12345
a = re.finditer(pattern, string)
[i.group() for i in a] // [1, 2, 3, 4, 5]
# 是把 re.Match object 以 iterator 形式表示
</pre>

***

#4 <a>re.search( ).group( )</a> -> string  

<pre>
假設：pattern = r"\d", string = 12345
re.search(pattern, string).group() // 1
# 與 re.group( ) 非常相似
</pre>

<a>re.match</a> vs <a>re.search</a>
<pre>
# 分別在於 re.search 是匹配整個 string, re.match 只匹配開頭。
string = "go to school"
pattern = r"school"
print(re.search(pattern, string)) //re.Match object
print(re.match(pattern, string))  //None
</pre>

***

#5 <a>re.split( )</a>
<pre>
pattern = r","
string = "1,2,3,4,5"
re.split(pattern, string)             // ['1', '2', '3', '4', '5']
re.split(pattern, string, maxsplit=1) // ['1', '2,3,4,5']
</pre>

***

#6 <a>re.sub( )</a> similar to <a>str.replace( )</a>
<pre>
pattern = r","
string = "1,2,3,4,5"
repl = "-"
re.sub(pattern, repl, string)           // 1-2-3-4-5
re.sub(pattern, repl, string, count=1)  // 1-2345
</pre>

***

### Flags

<table>
<tr>
<th>#</th>
<th>flags</th>
<th>full_flags</th>
<th>descriptions</th>
</tr>
<tr>
<td>1</td>
<td>re.I</td>
<td>re.IGNORECASE</td>
<td> 忽略大小寫 </td>
</tr>
<tr>
<td>2</td>
<td>re.M</td>
<td>MULTILINE</td>
<td> 多行模式，pattern'^'、'$' 變為多行的 </td>
</tr>
<tr>
<td>3</td>
<td>re.S</td>
<td>DOTALL</td>
<td> 例子：re.findall(&lt;p&gt;.*&lt;/p&gt;", string, re.DOTALL) </td>
</tr>
<tr>
<td>4</td>
<td>re.L</td>
<td>LOCALE</td>
<td> 使預定字符類 \w \W \b \B \s \S 取決於當前區域設定  </td>
</tr>
<tr>
<td>5</td>
<td>re.U</td>
<td>UNICODE</td>
<td> re.U(UNICODE): 使預定字符類 \w \W \b \B \s \S \d \D 取決於unicode定義的字符屬性  </td>
</tr>
<tr>
<td>6</td>
<td>re.X</td>
<td>VERBOSE</td>
<td> 詳細模式。這個模式下正則表達式可以是多行，忽略空白字符，並可以加入註釋 </td>
</tr>
</table>

***

### Regex

以下是一些常用的 Regex 及例子：

檢整網址:
https://blog.hsdn.net/1391.html
<pre>
pattern = r'/^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$/’
</pre>

https://5xruby.tw/posts/15min-regular-expression

