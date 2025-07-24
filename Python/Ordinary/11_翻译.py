# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   11_翻译 |User    Pfolg
# 2024/7/27   22:26
from translate import Translator


def translate(text, sources, target):
    translator = Translator(from_lang=sources, to_lang=target)  # from_lang='en',
    outText = translator.translate(text)


languageDict = {"英语": "en",
                "中文": "zh",
                "繁体中文": "zh-TW",
                "日语": "ja",
                "韩语": "ko",
                "法语": "fr",
                "西班牙语": "es",
                "意大利语": "it",
                "德语": "de",
                "土耳其语": "tr",
                "俄语": "ru",
                "葡萄牙语": "pt",
                "越南语": "vi",
                "印尼语": "id",
                "泰语": "th",
                "马来语": "ms",
                "阿拉伯语": "ar",
                "印地语": "hi"}

t = "Do you love me"
translator = Translator(from_lang="en",to_lang="zh")  # from_lang='en',
outText = translator.translate(t)
print(outText)
