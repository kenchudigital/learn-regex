### Content
- [Introduction](#Introduction)
- [Get_Started](#Get_Started)
- [Function](#Function)
- [Flags](#Flags)
- [Regex](#Regex)
- [Example](#Example)

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
<td> 忽略大小寫。 </td>
</tr>
<tr>
<td>2</td>
<td>re.M</td>
<td>MULTILINE</td>
<td> 多行模式，pattern'^'、'$' 變為多行的。 </td>
</tr>
<tr>
<td>3</td>
<td>re.S</td>
<td>DOTALL</td>
<td> 可以把隔行變為 \n 去 search。 </td>
</tr>
</table>

***

### Regex

Triple dots and space:
<pre>
string = "... something"
re.findall('\d+', string) // ['123']
</pre>

常用 re 字符：

1. [...] 只要出現在括號內都 match
<pre>
string = "112233"
pattern1 = "[123]" //re.findall result: ['1', '1', '2', '2', '3', '3']
pattern2 = "[123]" //re.findall result: ['12']

[a-z]  - > 所有細階字母
[A-Z]  - > 所有大階字母
[0-9]  - > 所有數字
[^0-9] - > 除了數字
</pre>

2. 位置上的 match (^ $)
<pre>
string = "abc"
^ 例子
pattern1 = "^a" // ^例子re.search result: a
$ 例子
pattern2 = "c$" // re.search result: c
</pre>

3. ^ vs \A and $ vs \Z
<pre>
when you only need to match the start of a string regardless of any modifiers, use \A.
差別在於 \A 及 \Z 不受 multi-line mode 影響

re.search('^abc', 'firstline\nabc', re.M)  
>> abc
re.search('\Aabc', 'firstline\nabc', re.M) 
>> 
</pre>

4. 數量上的 match
<table>
<tr>
<th> symbol </th>
<th> description </th>
</tr>
<tr>
<td> * </td>
<td> 大過等於 0 個 </td>
</tr>
<tr>
<td> + </td>
<td> 大過 0 個 </td>
</tr>
<tr>
<td> ？ </td>
<td> 0 或 1 個 </td>
</tr>
<tr>
<td> {n} </td>
<td> n 個 </td>
</tr>
<tr>
<td> {n,} </td>
<td> 大過等於 n 個 </td>
</tr>
<tr>
<td> {n, m} </td>
<td> n 到 m 個 </td>
</tr>
</table>
<pre>
re.search('abcd?', 'abcd').group() 
>> abcd
re.search('abcd?', 'abc').group() 
>> abc
re.findall('abcd{2,4}', 'abcdddddabcdd')
>> ['abcdddd', 'abcdd']
條件是 abcdd, abcddd, abcdddd，結果以重覆最多的顯示
</pre>

5. 組合及 or
<pre>
or 用法：
re.search('a|b', 'a').group()
>> a
re.findall('a|b', 'ab')
>> ['a', 'b']

組合 (...) 用法：
re.search('(abc){2}', 'aabbccabcabc').group()
>> 'abcabc'
</pre>

5. 組合特姝用法：
- (?:re...) - 當不需要中間的值時用，例如：
<pre>
re.findall('(\d+)(?:abc)(\d+)', '123abc456abc888abc999')
>> [('123', '456'), ('888', '999')]
# list of tuple
</pre>
- a(?=\d) - a 後面一定要係數字
- a(?!=\d) - a 後面一定唔係數字
- (?<=\d)a - a 前面一定係數字
- (?<!\d)a - a 前面不能是數字

6. 其他特別字符
<pre>
\f (換頁), \n (換行), \r (Enter鍵), \t (Tab鍵), \\ (\)
</pre>

7. 提示
> 盡可能 match 較少的字，例如：.*? ， ? ，可以令結果不會重覆
<pre>
re.search('go{2,4}?','good')
// goo
re.search('go{2,4}?','goooood')
// goooo
</pre>

### Example
網址：
<pre>
‘/^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$/’
</pre>

