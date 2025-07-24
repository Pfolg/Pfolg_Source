import jieba
from wordcloud import WordCloud

# 读取数据
with open('shuju.txt', 'r', encoding='utf-8') as file:
    s = file.read()

#中文分词
list1 = jieba.lcut(s)
# 排除词
# stopword=[]
txt = ''.join(list1)
# 绘制
wordcloud = WordCloud(background_color='#26FFF6', font_path='msyh.ttc', stopwords=None,
                      width=800, height=600)

# 由txt生成词云图
wordcloud.generate(txt)
wordcloud.to_file('小学数学公式词云图.png')
