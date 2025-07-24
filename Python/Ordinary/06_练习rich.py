# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   06_练习rich |User    Pfolg
# 2024/7/10   20:30
url = ("https://blog.csdn.net/qq_43954124/article/details/112772262?ops_request_misc=%257B%2522request%255Fid%2522%253A"
       "%2522172061455316800188598725%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id"
       "=172061455316800188598725&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive"
       "~default-1-112772262-null-null.142^v100^pc_search_result_base1&utm_term=rich&spm=1018.2226.3001.4187")
from rich import print as rprint
from rich_console import console

rprint(locals())
input()
console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")
