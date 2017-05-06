import  matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba.analyse
# 添加词典
jieba.add_word("侯亮平",100,"n")
jieba.add_word("亮平",100,"n")
jieba.add_word("赵东来",100,"n")
jieba.add_word("陈岩石",100,"n")
jieba.add_word("高老师",100,"n")
jieba.add_word("沙瑞金",100,"n")
jieba.add_word("季昌明",100,"n")
jieba.add_word("陆亦可",100,"n")
jieba.add_word("郑西坡",100,"n")
jieba.add_word("山水集团",100,"n")
jieba.add_word("大风厂",100,"n")

jieba.analyse.set_stop_words('novel_stopwords.txt')
#打开小说
text = open('novel_LM.txt','r',encoding = 'utf-8').read()
#分析权重
tags = jieba.analyse.extract_tags(text,topK=200,withWeight=False)
text = " ".join(tags)
word_jieba = jieba.cut(text,cut_all=False)
word_split = " ".join(word_jieba)
print(word_split)
#my_wordclud = WordCloud(max_words=100,width = 1600,height=800).generate(word_split)
#绘制云图
backgroud_Image = plt.imread('novel_pic.jpg')
my_wordcloud = WordCloud(
            background_color='white',    # 设置背景颜色
            mask = backgroud_Image,          # 设置背景图片
            max_words = 200,            # 设置最大现实的字数
            stopwords=STOPWORDS,        # 设置停用词
            font_path = 'simkai.ttf',   # 设置字体格式，如不设置显示不了中文
            max_font_size = 100,            # 设置字体最大值
            random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
            scale=1
                ).generate(word_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

