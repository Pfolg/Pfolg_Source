# 定义本游戏使用的角色
define PaBo = Character(_("帕波"), color="#737d32")
define BuSi = Character(_("布斯"), color="#67c4c4")

# 定义图像时指定填充模式
image bg1 = "bg bg1.png"
image bg2 = "bg bg2.png"
image bde="badending1.png"
image noOne="noOneButRoom.png"
image dogLookFZ="dogLookFZ.png"
image dogEatFZ="dogEatFZ.png"
image catWorryDog="catworrydog.png"
image bch="beforeclearhome.png"
image ach1="afterclearhome1.png"
image ach2="afterclearhome2.png"
image washing="washing.png"
image dry="drybody.png"
image taw="thinkafterwash.png"
image rain="rain.png"
image avdrain="avoidrain.png"

# 此变量用于记录是否将视觉小说与书籍对比过
default book = False

# 游戏从这里开始
label start:
    # 首先播放背景音乐
    play music "親愛なるあの日々へ - 松本文紀.flac"

    # 森林里面有一个小木屋
    scene bg1:
        zoom 1.25  # 调整缩放比例直到填满屏幕
        xalign 0.5
        yalign 0.5
    with fade

    "小猫布斯和小狗帕波曾经住在一起，树林里有它们自己的小屋。"

    "它们试图像人一样，样样都自己干，然而却总是不如意。"
    
    # 木屋门前有小猫布斯和小狗帕波
    scene bg2:
        zoom 1.25
        xalign 0.5
        yalign 0.5
    with dissolve


    "它们只有一双笨拙的小爪子，小爪子怎么能像人一样的手一样啥都干呢？"

    "它们没去上过学，因为学校不是为动物办的。"

    # 展示小木屋内脏乱的地板和正在烦恼的两位主人公
    scene beforeclearhome:
        zoom 1.25
        xalign 0.5
        yalign 0.5
    with fade

    "小猫布斯和小狗帕波的小屋子，有时收拾得很干净，可常常是一团糟。"

    "有一天，它们注意到小屋的地板已经很脏了。"

    BuSi "帕波"


    menu:
        BuSi "地板很脏了，你说是吗？"


        "啊对对对，太脏了！":
            jump rightaway

        "哈？我什么都没看见！":
            jump badEnding

    return

label rightaway:
    with fade
    play music "Working - 松本文紀.mp3"

    BuSi "是的，太脏了，把我的爪子都弄脏了，555~"

    BuSi "我们得擦地板。"

    BuSi "人的地板可干净啦，因为，他们经常擦。"

    PaBo "怎么擦呢？"

    BuSi "这很容易，你去弄些水来，其余的我负责。"

    scene noOne:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    "帕波提水去了，布斯从包里拿出一块肥皂放到桌上，然后到里屋去了。"

    scene dogLookFZ:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    "帕波提水回来后，一眼看见桌上放着一块白色的东西。"

    menu:

        PaBo "哈哈！这东西闻上去真香，居然有四种味道！"

        "\"艾玛真香！(浅尝辄止)\"":
            jump eatFZ

        "忍住诱惑，等布斯回来。":
            jump clearHome 
    # 狗站在桌旁，一个装满水的水桶放在门边，狗好奇地看着肥皂，房间有点乱

label eatFZ:

    scene dogEatFZ:
        zoom 1.25
        xalign 0.5
        yalign 0.5
    with fade

    "说完帕波就一口塞在了嘴里咀嚼起来。"

    scene catWorryDog:
        zoom 1.25
        xalign 0.5
        yalign 0.5
    with dissolve

    "布斯进来了，听见帕波嘴里嚼着什么，满嘴泡沫，布斯吓坏了。"

    BuSi "Oh My God!"

    BuSi "你怎么了，一定是病了。"
    
    BuSi "瞧你满嘴的泡沫，到底怎么了？"

    PaBo "ε=(´ο｀*)))唉~"

    PaBo "我以为放在桌上的是奶酪或者饼干什么的，就吃了。"

    PaBo "我哪知道这玩意弄得我满嘴泡沫，还蛰得我真难受！"

    BuSi "红豆泥 + 八嘎 （你真是个大笨蛋）！"

    BuSi "那是块肥皂！肥皂怎么能吃呢？"

    PaBo "难怪这么多泡沫。"

    PaBo "哎哟，苦也！我的嘴啊！"

    BuSi "多喝些水就不痛了！"

    "帕波把桶里的水喝光了，嘴虽然不痛了，可还是还有许多泡沫。"

    "于是，它走出屋子，在草地上用力地擦完嘴后，再去提水。"

    "布斯只得用最后五分钱再去买块肥皂。"

    PaBo "我再也不吃那玩意儿了"

    jump clearHome

label clearHome:
    play music "ごきげん戦闘ロボ - 松本文紀.mp3"
    scene bch:
        zoom 1.25
        xalign 0.5
        yalign 0.5
    with fade


    PaBo "不过没有刷子，要怎么擦地板呢？"

    BuSi "我已想好了。"

    BuSi "你的毛正好可以打湿来擦地板！"

    PaBo "太好啦！"

    scene ach1:
        zoom 1.25
        xalign 0.5
        yalign 0.5
    with dissolve

    "布斯提着水桶，拿着肥皂，跪在地上，拖着帕波把地板全擦了一遍。"

    BuSi "用点儿什么干的东西把地板再擦一遍。"

    PaBo "我有办法！"

    PaBo "我浑身湿透了，你的毛又干又软，正好用来把地板擦干，我来擦！"

    scene ach2:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    "于是，帕波拖着布斯把地板全擦了一遍。"

    PaBo "喂，咱们去照照镜子！"

    "它们对镜子瞧了瞧。"

    BuSi "地板擦干净了，但我们可太脏了。"

    BuSi "这样可不行，别人会笑话我们的，我们得洗一洗。"

    PaBo "像人洗衣服一样，我们互相搓。"

    PaBo "你帮我洗，然后我再帮你洗。"

    scene washing:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    "它们在盆里放满水，然后用洗衣板用力地互相搓。"

    "帕波疼得一个劲喊轻点儿，它的双脚已经搓在一块了。"

    "很快轮到布斯了，帕波一把抓着它用力在洗衣板上搓呀、捏呀。"

    "疼得布斯苦苦求它，别把身上搓出个洞来。"

    "然后，它们互相拧干身上的水。"

    jump drybody

label drybody:
    scene taw:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade


    BuSi "咱们把自己晾出去。"

    "于是，它们拉起了晾衣绳。"

    scene dry:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    BuSi "你先把我吊在绳子上，我再把你挂上去！"

    "帕波举起布斯把它钩在绳子上——它们根本不需要衣钩，用爪子钩在绳子上就行了。"

    "布斯钩在绳子上后又倒吊过来把帕波提起来挂在绳子上。"

    "这会儿，它们悠闲地倒吊在衣绳上，太阳暖融融地照射着。"

    scene rain: 
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    "就在这时，下起了雨。"

    PaBo "哎呀！下雨了！晒什么太阳，快下去！"

    "它们赶紧跳下来，跑进小屋避雨。"

    BuSi "还在下雨吗？"


    PaBo "雨停了，太阳出来了。"

    BuSi "咱们还得晒晒。"

    scene dry:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    "于是，它们又再一次把自己吊在了绳子上。"

    "阳光灿烂，晒得浑身暖融融的。"
    
    scene rain: 
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    "转眼间又下起了雨。"

    PaBo "下雨了，咱们又会淋湿的，快下去！"


    scene avdrain: 
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with dissolve

    "说着，它们又下来避雨了。"

    "不一会儿，太阳又出来了，它们又吊在绳子上晒太阳。"

    "不久，又下雨了，它们又跑进小屋避雨。"

    "天黑了，它们浑身的毛终于干了。"

    jump ending

label ending:
    play music "暖かな時間 - 松本文紀.mp3"

    scene sleep: 
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade

    BuSi "全干了！"

    PaBo "应该像人一样把洗干的东西放进篮子里。"

    "于是它们爬进篮子里。"

    "它们太乏了，不一会儿就睡着了，一觉睡到第二天早上才醒。"

    scene black
    with dissolve
    "{b}看起来不坏的坏结局{/b}."

    jump info

label badEnding:
    # 猫生气地把狗扔出了木屋
    scene bde:
        zoom 1.25
        xalign 0.5
        yalign 0.5
    with dissolve

    "布斯非常生气，把帕波扔出了门外！"

    scene black
    with dissolve

    "{b}坏结局{/b}."

    jump info

label info:
    play music "When I See The Sparkle Of Your Tears - 松本文紀.mp3"
    with fade

    "我当然知道这个游戏很不完美。"

    "不管是剧情还是场景角色，都并非原创。"

    "其中，故事来自于《伊索寓言》的《小猫布斯和小狗帕波的故事》，美中不足的是，它是个寓言；场景均使用豆包AI生成，你可以看到一些图片是真的一言难尽。"

    "音乐嘛，来自https://music.163.com/album?id=96848090&uct2=U2FsdGVkX1+E2w2VDiZ8lVVkYDFRALS10QmJ0Krj18s="

    "所有素材均无版权，此作品为闲暇打法时间的练手作品，仅供学习交流之用，禁止商用！"

    "PFOLG「名为作者之人」" "感谢您的游玩！"

    return

