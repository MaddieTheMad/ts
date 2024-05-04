label ts_scenario_1:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Акт I | Глава I",details="Поиски. Сайори",large_image="aonecone",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "1"

    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False


    $ save_name = "Поиски. Сайори"

    scene black
    pause 2
    play sound chp1
    $ Chapter("АКТ ПЕРВЫЙ")
    $ Chapter("АКТ ПЕРВЫЙ")
    $ Chapter("глава первая")
    $ Chapter("глава первая")
    $ Chapter("Поиски. Сайори")
    stop sound fadeout 7
    $ Chapter("Поиски. Сайори")
    play music ts_rem
    scene ts_club
    with ed_night_dis

    $ TS.Screens(ts_showscreens)

    "Сказать гораздо проще, чем сделать."
    "Я же хотела создать Литературный клуб. Я и создала. Но, как оказалось, одного только моего желания ой как недостаточно."
    "К счастью, я, поучаствовав во многих других клубах и позанимав там высокие должности, и так уже примерно знаю, что именно мне нужно для открытия нового клуба."
    "И прежде всего, мне нужны новые люди... Хотя бы ещё три человека."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Отец, узнав, что я ушла из Дискуссионного клуба, очень на меня разозлился."
    "Он сказал, что это очень важно для поступления в университет, и что моё легкомыслие меня до добра не доведёт."
    "Ну, хотя бы из дома не выгнал. Уже достижение."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Я уже довольно долгое время одна-единственная в клубе."
    "Администратор клубов, конечно, пошёл мне навстречу и дал мне время хотя бы до фестиваля, который предстоит ещё нескоро, но..."
    "Время на самом деле идёт гораздо быстрее, чем кажется."
    "Кажется, как будто я только позавчера перешла в новую школу. Вчера познакомилась с Каори..."
    "А сегодня я уже в выпускном классе, тщетно пытаюсь найти хоть кого-то в качестве члена Литературного клуба."
    "А завтра – уже пресловутый фестиваль."
    "А реальность на самом деле довольно жестока."
    "Я расклеивала листовки по всей школе, обращалась ко всем и каждому с просьбой хотя бы заглянуть в мой клуб…"
    "Но всё без толку."
    "В лучшем случае они обещают, что придут, но на самом деле никто так и не приходит."
    "В худшем же – они просто максимально игнорируют меня, как будто я для них пустое место. Как будто и нет никакой Моники."
    "«С должным старанием всё должно получиться»?"
    "Но у меня не получается!"

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Время идёт."
    "До этого злополучного фестиваля осталось чуть больше месяца."
    "А время неумолимо идёт, и повернуть его вспять не получится ну никак, даже при всём желании."
    "Я уже постепенно схожу с ума."
    "Я всё чаще замечаю, что общаюсь с несуществующими членами клуба."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show yuri 1 at ln31:
        alpha 0.5
    show sayori 1 at ln32:
        alpha 0.5
    show natsuki 1 at ln33:
        alpha 0.5

    $ TS.Screens(ts_showscreens)

    "Я общаюсь с ними, делюсь с ними сокровенным, задаю домашние задания на следующие встречи клуба…"
    "Да у меня же шизофрения, самая что ни на есть настоящая."
    "Если кто-то со стороны посмотрит, то мне быстро выпишут направление в жёлтый дом, накормят вкусными таблеточками и уложат спать."
    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)
    "Так продолжалось день за днём."
    "Каждую новую неделю администратор клубов приходит в клуб, видит, что так никто и не появился, даже несмотря на всю мою рекламу, разочарованно вздыхает и жестом показывает на часы."
    if persistent.cens_mode == True:
        "Я и так, блять, знаю, что время идёт, не надо мне лишний раз об этом напоминать."
    else:
        "Я и так знаю, что время идёт, не надо мне лишний раз об этом напоминать."
    "Но очень немногие жаждут вкладывать силы и старания в создание чего-то нового."
    "Особенно если это что-то не привлекает сразу твоего внимания. Как, например, Литературный клуб..."
    if persistent.cens_mode == True:
        "Неужели нет ни единой живой души во всей этой блядской школе, которой бы была интересна литература?"
    else:
        "Неужели нет ни единой живой души во всей этой грёбаной школе, которой бы была интересна литература?"
    "«Литература – это же так весело и интересно! Можно вместе читать книги, можно писать стихи, можно...»"

    stop music fadeout 5

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"
    pause 1
    $ TS.Screens(ts_showscreens)

    "Хотя, а что «можно»? Я же даже не знаю, какие активности можно предложить новым членам клуба!"
    "Наверное, зря я ушла из Дискуссионного клуба..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Настал очередной день моей шизофрении, которую я называю Литературным клубом."
    "Я опять одна-одинокая."
    "Не то, чтобы мне это было совсем непривычно, но после шума и гомона Дискуссионного клуба Литературный клуб кажется каким-то особенно тихим."
    "Я снова раздаю задания несуществующим людям, мы вместе с несуществующими людьми их обсуждаем, несуществующие люди читают несуществующие книги…"
    "Как вдруг..."

    play music okevrsay fadein 3

    window hide
    play sound stuk
    with vpunch
    pause 1.5
    play sound door_open

    show sayori 3b zorder 2 at ln11

    $ TS.Screens(ts_showscreens)

    s "Извините, а это Литературный клуб?"

    "Это хоть и не было резко, но я всё равно дёрнулась. В общий шум моего голоса и тишины врезался ещё один голос."

    m "А!.. Э-э-э... Да..."

    show sayori 2s at h11

    $ TS.Screens(vpunch)

    s "О, отлично! Я как раз по адресу!"

    show sayori 2x at h11

    s "Я тут увидела листовку с приглашением всех желающих в Литературный клуб."
    
    show sayori 2 at s11

    "Где тебя только черти носили все эти недели? Я уж было подумала, что зря я вообще затеяла всю эту идею с Литературным клубом…"

    m "А-ха-ха... Ну, добро пожаловать, э-э-э..."

    show sayori 2x at f11

    s "Меня зовут Сайори, а тебя как?"
    
    show sayori 2 at t11
    
    m "А я Моника. Приятно познакомиться."
    
    show sayori 2x at h11

    $ TS.Screens(vpunch)

    s "Взаимно!"

    show sayori 1o at s11

    s "Э-э-э… А где остальные?"
    m "А остальных… пока ещё нет. Ты вообще первая, кто пришла. Я даже подумала, что зря я это всё затеяла..."

    show sayori 2h at d11

    $ TS.Screens(vpunch)

    s "Почему это зря?"
    
    show sayori 2f at s11
    
    m "Ну, потому что... Далеко не все хотят вкладывать своё время и желание в создание чего-то нового."
    m "Особенно если это новое ещё и очень непопулярное."
    m "Повторюсь, ты первый человек за месяц с лишним, который хотя бы соизволил заглянуть в эту дверь."

    "Учитывая мой статус, мне выделили целую комнату, поэтому я теперь в одном ряду с такими мастодонтами клубов, как Дискуссионный, Шахматный и Музыкальный клубы."
    "Жаль только, что мне до любого из них в плане статуса как до Луны пешком..."

    show sayori 4h at h11

    $ TS.Screens(vpunch)

    s "Но это же глупо! Не поверю, что в этой школе нет ни одного человека, которого бы не интересовала литература!"

    show sayori 3g at s11

    m "Вот и я до недавнего времени была того же мнения. Но раз уж ты пришла, то всё-таки есть надежда."

    show sayori 2y at f11

    m "Где один человек, там и два. А где два, там и три. А где три, там и десять."
    m "И поскольку ты всё-таки пришла, то, садись, что ли."

    show sayori 4x at h11

    $ TS.Screens(vpunch)

    s "Спасибо!"

    show sayori 3n at d11

    s "И-и-и... что мы будем делать?"

    show sayori 3f at s11

    m "Пока будем думать, как бы нам набрать ещё участников."
    m "По правилам, в клубе должно быть не менее четырёх членов."
    m "Я, конечно, уже довольно многое пробовала, но всё без толку."
    
    show sayori 3h at f11
    s "А что именно ты пробовала?"
    
    show sayori 3f at t11
    m "Ну-у-у... Листовки расклеивала... просила лично присоединиться к клубу... всё такое..."
    
    show sayori 3h at f11
    s "Мда-а-а... Негусто..."
    
    show sayori 3f at t11
    m "Ну, в этом-то и суть нашего собрания - придумать и другие способы привлечения новых участников!"

    show sayori 3k at s11

    s "..."
    m "..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show sayori 1 at t11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Остальная часть собрания клуба прошла гораздо быстрее."
    "Мы с Сайори придумывали идеи, как бы нам набрать участников, чтобы добрать до минимально разрешённого состава клуба."
    "Однако из стоящих идей нам обеим приглянулась разве что одна:"
    "Нарисовать плакат с зазыванием присоединиться к клубу."
    "Хотя, скажу честно - я не знаю, как это отличается от тех же листовок."
    "Если это вообще отличается..."
    "Ну да и пусть - эту идею всё равно предложила Сайори. Аргументировала она это тем, что большой плакат будет всё-таки красочнее, чем какие-то, маленькие бездушные и бесцветные листовки."
    "В любом случае, по итогам встречи мы не добились ничего, кроме того, что у нас обеих вскипел мозг от такого мозгового штурма."

    show sayori 1p at s11

    s "Фу-у-ух."
    s "Как же я устала!"

    show sayori 1r at f11

    $ TS.Screens(vpunch)

    s "Но всё равно мы здорово поработали!"

    show sayori 1q at s11

    m "Да, недурно."

    show sayori 1x at d11

    s "Ну что, тогда до завтра?"

    "Завтра?.."
    "Хотя что я несу? Завтра же тоже будет встреча клуба. И послезавтра тоже. И каждый день после этого."

    m "Да... До завтра..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    stop music fadeout 6

    "После того, как Сайори ушла, я осталась в клубе."
    "Кто вообще эта девочка? Почему она выглядит настолько счастливой?"
    "Даже... неестественно счастливой..."
    "Впрочем, я подумаю об этом завтра..."
    "Сегодня я так устала..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show sayori 1 at t11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    play music ts_mdl

    "На следующий день мы с Сайори продолжили мозговать по поводу привлечения новых участников."

    show sayori 3l at f11

    s "Слушай, а может, нам что-то приготовить для потенциальных участников?"

    show sayori 3y at s11

    "Как бы мне ни хотелось это признавать, готовка всегда была моим слабым местом."
    "Это возвращаясь к тому, что я умею всё бесполезное, но не умею ничего полезного."
    "Так что этот вопрос застал меня врасплох."

    show sayori 1g at h11

    m "С-Сайори... Я... не очень хорошо умею готовить. Готовка никогда не была моим коньком."
    m "Нет, если, конечно, ты приготовишь, то без проблем, но по секрету тебе скажу, что готовлю я не очень."

    show sayori 3l at s11

    s "Чёрт, я надеялась, что за готовку будешь отвечать как раз ты."

    $ TS.Screens(vpunch)

    "Её что, не кормят?"

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show zatemnenie with dspr

    $ TS.Screens(ts_showscreens)

    show screen chp_text_20
    pause
    $ TS.Screens(ts_hidescreens)
    show screen chp_text_20
    pause 1
    hide screen chp_text_20

    hide zatemnenie with dspr

    show sayori 1u at f11

    $ TS.Screens(ts_showscreens)

    show sayori 3b at d11

    s "Потому что я готовлю даже хуже тебя, вне зависимости от того, насколько плохо готовишь ты."

    show sayori 1d at s11

    m "Как скажешь..."

    show sayori 1zc at d11

    s "В общем, идею с готовкой чего-то съестного вычёркиваем, да?"
    
    show sayori 1d at s11
    
    m "Да..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show sayori 1k at t11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Следующие несколько дней прошли в таком же ритме."
    "Мы с Сайори безуспешно пытались найти новых участников, а новые участники что-то не спешили подходить к нам."
    "Подавленной стала выглядеть как я, так и Сайори."
    "Но если я уже почти всю жизнь так живу, и научилась справляться, то насчёт Сайори я не знаю."
    "Первые несколько дней она была неестественно счастливой и активной, но сегодня..."
    "Сегодня она выглядит так, как будто ей сказали, что она завтра умрёт, и ничего с этим поделать нельзя."
    "Я не большой знаток психических заболеваний, но, судя по всему, у неё маниакально-депрессивное расстройство."
    m "Сайори?.."
    "Ответа нет."
    "..."
    "...Нет, в этой атмосфере работать просто невыносимо!"

    stop music fadeout 5

    $ TS.Screens(vpunch)

    m "Сайори!"
    s "Да?"
    m "Что-то не так? Только не ври мне, что всё нормально, потому что я же явно вижу, что что-то не так!"

    show sayori 1zd at s11

    s "Нет... Просто... Всё это сложно... Да ещё и серые тучки..."
    show sayori 1t at d11
    m "Серые тучки?"

    show sayori 1v at s11

    s "Да."
    
    show sayori 1k at t11

    "Не удовлетворившись такой расплывчатой формулировкой, я решила повторить вопрос, но настойчивее."

    $ TS.Screens(vpunch)

    m "Сайори. Посмотри на меня."

    show sayori 1f at s11

    "Сайори повинуется."

    m "Что-то не так?"

    "Я чеканю каждое слово, произнося их как будто отдельно."
    
    show sayori 1v at t11
    
    "Вместо ответа Сайори снова начинает слезиться."

    show sayori 1w at h11

    play music ts_mk fadein 3

    show sayori 1w at fleft with move
    hide sayori

    "А затем просто уходит из класса, всё ещё оставляя меня без ответа."

    "Я тем временем остаюсь думать."
    "Может, зря я на неё накричала?"
    "При депрессивных расстройствах люди обычно срываются даже по каким-то мелочам..."
    "Впрочем, я же к ней в голову не залезу."
    play sound pageflip
    scene ts_club
    with wipeleft_scene
    "Прошло примерно пятнадцать минут."
    "Сайори так и не появилась. Я уже начинаю переживать."
    "Что, если она уже..."
    m "ГОСПОДИ, САЙОРИ!"
    "Я выбегаю вслед за ней."

    $ TS.Screens(vpunch)

    m "Сайори!"

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    m "Сайори!"

    "Всё это время она с пустым и безразличным выражением лица стоит в дальнем конце коридора, недалеко от туалетов."
    "Что же, уже радует."
    "Я перехожу на гораздо более тихий голос, чтобы не спугнуть ни учителей, ни учеников, ни саму Сайори."

    m "{size=-6}Сайори, я же отчётливо вижу, что что-то не так! Что вообще случилось?{/size}"
    m "{size=-6}Ты же раньше была таким счастливым лучиком солнца!{/size}"
    m "{size=-6}Тогда почему сегодня всё иначе?{/size}"

    show sayori 2v at t11 with easeinright

    "Сайори наконец оборачивается в мою сторону. Её глаза блестят от плача."

    s "…"
    "Я понимаю, что она вся на нервах, и в любой момент сорвётся, но сейчас она ещё говорит тише обычного."
    
    show sayori 4w at hf11
    
    s "{size=-6}Что тебе непонятно в словосочетании «серые тучки»?{/size}"
    
    show sayori 3u at t11

    "Я не ожидала такого вопроса."
    "Сайори понимающе продолжает."

    show sayori 1v at s11

    s "Видишь ли... То, какой ты видишь меня сегодня... На самом деле, я такой была всегда."

    show sayori 1v at d11
    
    s "Каждое утро я просыпалась с мыслью: а зачем мне ходить в школу?"
    s "Зачем мне учиться? Зачем мне есть? Зачем мне вообще вставать с кровати?"
    s "Зачем мне вообще жить?"

    show ts_corridor at ts_fon_blur_postepenno
    show sayori 1w at s11

    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    s "Если можно просто умереть."
    s "Раз уж я такая бесполезная."

    show sayori 1zd at t11
    
    s "А затем я подумала, что раз уж я такая бесполезная, и если мне в любом случае будет плохо, то нужно, чтобы хотя бы другим было хорошо."
    
    show sayori 1v at f11
    
    s "Обычно я притворялась счастливой в кругу новых знакомых, чтобы они подумали, что я всегда такая, и что обидеть меня невозможно."

    show sayori 1t at t11
    
    s "Так было и с тобой. С тобой я тоже изначально притворялась счастливой, чтобы тебе было лучше, чтобы в свою очередь было лучше и мне."

    show sayori 1v at s11

    s "Но затем, когда я увидела, насколько ты была разочарована по поводу того, что у твоего клуба ничего не получается, я и сама сбросила маску."

    show sayori 2v at t11

    s "Теперь ты меня, скорее всего, выгонишь из клуба..."

    play sound fb
    scene ts_corridor
    show sayori 3p at h11
    with flash

    $ TS.Screens(vpunch)

    m "Ну уж нет!"

    "Выпалила я, не подумав."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show zatemnenie with dspr

    $ TS.Screens(ts_showscreens)

    show screen chp_text_21
    pause
    $ TS.Screens(ts_hidescreens)
    show screen chp_text_21
    pause 1
    hide screen chp_text_21

    hide zatemnenie with dspr

    show sayori 1u at f11

    $ TS.Screens(ts_showscreens)

    m "Я изначально хотела, чтобы Литературный клуб был местом, где не будет слова неправильно."
    m "И это касается не только всяких книжек и прочего... Но и людей тоже."
    m "Я не выгоняю людей только потому, что они какие-то дефектные."
    m "И это одновременно справедливо как для физических увечий... Так и для психических."
    m "И неважно, будь то нежелание жить, или если тебя бьют родители – в Литературном клубе рады всем."

    show sayori 1t at t11

    m "И раз уж ты рассказала мне большой секрет, то будет справедливо, если и я расскажу."
    
    show sayori 1k at s11

    m "У меня тоже с самого детства были навязчивые мысли. Только немного другие."
    m "Мне всегда казалось, что если у меня что-то не получается с первого раза, то внутренний голос как бы твердил мне, что оно и в принципе не получится."
    m "Я хоть и умею многое, но я всё умею плохо."
    m "Как я говорила себе, я мастерица на все руки... да вот только руки у меня из неправильного места растут."
    m "Мне всё быстро надоедает, мне очень быстро становится скучно. Меня саму это вымораживает, но сделать с этим я уже ничего не могу."
    "Любой психиатр, посмотрев на меня, сказал бы, что у меня налицо все симптомы синдрома дефицита внимания."
    "И хотя в целом я с этим согласна, но приписывать себе лишние психические заболевания, которых может и не быть - это как минимум некрасиво."
    "У меня просто навязчивые мысли. На этом можно и остановиться."
    m "Удивительно, что я так долго в Литературном клубе. Я бы уже вообще давно забросила эту затею и вернулась в любой другой клуб..."
    
    show sayori 3y at t11
    
    m "Но я чувствую, что литература – это моё призвание. А если ты зашла в эту дверь и до сих пор от меня не сбежала – то это и твоё призвание тоже."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene black
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Я обнимаю Сайори."

    m "И не нужно расстраиваться из-за того, что что-то не получается."
    m "Если что-то не получается, нужно просто лучше стараться."
    m "И если нас в клубе до сих пор двое, то это лишь значит, что мы просто недостаточно делаем для его развития."
    s "Но мы же... {nw}"
    m "И так делаем всё возможное? Это то, что сказал бы слабак. Но я же не слабак. И ты не слабак. И ты, и я очень сильные духом люди."
    m "А сильные духом люди не сдаются на полпути. Мы разовьём этот клуб."
    m "Обязательно."

    "Сюрреалистичная сцена – вот вроде две относительно взрослые девушки, а плачем обе как маленькие девочки."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    $ TS.Screens(ts_showscreens)

    show screen chp_text_22
    pause
    $ TS.Screens(ts_hidescreens)
    show screen chp_text_22
    pause 1
    hide screen chp_text_22

    #$ TS.Screens(ts_null_transform)

    play sound pageflip
    scene ts_corridor
    show sayori 1zc at t11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Наконец, Сайори отпускает меня из объятий и вытирает слёзы."

    show sayori 1j at h11

    $ TS.Screens(vpunch)

    s "Да! Мы обязательно разовьём этот клуб и покажем всему миру, чего мы стоим!"

    show sayori 1i at f11

    m "Обязательно, Сайори..."

    show sayori 1d at t11

    "Сайори впервые за сегодняшнюю встречу искренне улыбается мне."
    "Хотя, после сегодняшнего, я уже не знаю, насколько эта улыбка, да и сама она в целом, искренняя..."
    
    show sayori 2zc at f11

    s "Тогда, до завтра?"
    
    show sayori 2d at t11
    
    m "Но завтра же суббота..."

    show sayori 5b at s11

    s "Ой, точно, я как-то и забыла…"

    show sayori 1x at t11

    s "Тогда, до понедельника?"
    
    show sayori 1 at h11
    
    m "До понедельника."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Сайори вприпрыжку идёт по коридору по направлению к выходу."
    "А я остаюсь думать, кто же на самом деле Сайори?"

    stop music fadeout 5

    "Ласковый лучик солнца, который делает день всех остальных лучше?"
    "Или же девочка с «серыми тучками»?"
    "Что же, надеюсь, что эти «серые тучки» наконец рассеются, и наконец принесут нам обеим радугу..."

    play music ts_rem

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    scene ts_club
    with poplil_pacan

    $ TS.Screens(ts_showscreens)

    "С момента нашего «разговора по душам» с Сайори прошла неделя."
    "За это время мы особенно сдружились."
    "Нет, мы не стали такими уж закадычными друзьями, как мы были с Мирой или с Каори..."
    "Но это всё равно можно назвать довольно крепкой дружбой."
    "Да, за всё это время в клуб к нам так никто и не пришёл, но..."
    "Честно говоря, это и не было нужно."
    "Нам и с Сайори было хорошо вместе."
    "Мы обсуждали книги, просто разговаривали часами напролёт, как самые настоящие подружки..."
    "А расходились мы с ней лишь из-за времени..."
    "Чтобы на следующий день после школы снова собраться вместе и пообсуждать с ней что-то."
    "И только я начала замечать, что, может, и не нужен мне этот Литературный клуб вовсе, как вдруг однажды..."

    play sound door_break
    stop music fadeout 4
    show sayori 2m zorder 2 at t11

    s "Моника!" with vpunch
    extend " Моника!" with vpunch
    extend " Я нашла!" with vpunch
    extend " Нашла!.." with vpunch

    "Запыханная Сайори тяжело и прерывисто дышит."

    show sayori 2n at s11
    play music t6

    m "Ну, во-первых, здравствуй, Сайори..."

    show sayori 3x at t11

    s "Да, привет..."

    show sayori 1b at h11

    m "А во-вторых... Кого именно ты нашла?"
    
    show sayori 1o at s11
    
    s "Что?.."

    show sayori 3m at t11

    s "Ах да! Я нашла девочку в столовой!"
    m "Ну-у-у... и что?"

    show sayori 3x at f11

    s "Как что? Пока все обедали, она просто взяла чай и начала читать книжку!"
    
    show sayori 3 at t11

    "Это совершенно меняет дело."

    show sayori 2d at s11

    m "Так, давай-ка по порядку."
    m "Как её зовут вообще?"

    show sayori 5b at t11

    s "А я-э-э-э..."

    show sayori 5 at s11

    $ TS.Screens(vpunch)

    extend " Не знаю..."

    "Типичная Сайори..."

    show sayori 1h at t11

    s "Я увидела её в столовой, она читала какую-то книжку, я тут же убежала, и целый день с нетерпением ждала возможности рассказать всё тебе."

    show sayori 1f at s11

    m "Ладно, ладно, всё хорошо, Сайори, не переживай."
    m "Может, она ходит в Книжный клуб, и мы просто не знаем об этом."
    m "Или у неё вообще нет клуба, и она уже ушла домой."

    show sayori 1g at t11

    m "Но в любом случае, сегодня мы её уже не застанем."
    m "А с учётом того, что сегодня пятница, то увидим мы её и вовсе не раньше понедельника."
    
    show sayori 1i at f11

    "Сайори хмуро смотрит на меня."

    $ TS.Screens(vpunch)

    "Да она сама виновата!"
    "Хотя, если так подумать, то она делает для клуба хотя бы что-то, а не просто сидит на пятой точке ровно, как я."
    
    show sayori 2h at t11

    s "Ла-а-а-адно..."

    "Но уже спустя мгновение хмурое выражение её лица меняется на такое же неестественно весёлое, которое я и видела, когда только познакомилась с ней."

    show sayori 1x at f11

    s "Тогда до понедельника!"
    
    show sayori 1d at t11
    
    m "Да, до понедельника..."

    stop music fadeout 5

    play sound door_open
    show sayori 1 at cleft with move
    hide sayori

    "Сайори уходит. Я же остаюсь ещё ненадолго, чтобы подумать о произошедшем."
    "Впрочем, думаю я недолго, потому что уже начинает темнеть."
    "Ладно. По дороге домой что-нибудь решу."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play music ts_dreams

    play sound pageflip
    scene ts_street_late
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Ненавижу ходить в школу в октябре. А ноябрь-декабрь - это и вовсе пиши пропало."
    "Утром идёшь в школу по темноте, после уроков в четыре часа вечера идёшь домой по темноте..."
    "Холод, слякоть, всё такое мерзкое... Бе-е-е..."
    "Вот гораздо лучше ходить в школу весной, особенно где-то в апреле-мае."
    "Вот это совсем другой разговор."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house_monika_evening
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Пока я думала о том, как же плохо ходить в школу зимой, и как же хорошо ходить в школу весной, я сама не заметила, как уже дошла до дома."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    m "Мам, пап, я пришла!"

    show hiroto 1b zorder 2 at ln11

    ts_ft "Добрый уже вечер, Моника. Как дела в школе?"
    
    show hiroto 1a zorder 2 at f11
    
    m "Как обычно, хорошо."
    
    show hiroto 1b zorder 2 at t11
    
    ts_ft "Как дела в {i}клубе{/i}?"

    show hiroto 1a1 at s11

    m "Как обычно... плохо..."

    show hiroto 1a2 at t11

    ts_ft "Что, так до сих пор никто и не пришёл?"
    
    show hiroto 1b1 at f11
    
    m "Да..."

    "Отец до сих пор не простил меня за то, что я всё же ушла из Дискуссионного клуба, создав свой."
    "По всей видимости, он с каждым днём всё больше убеждается в том, что лучше бы я осталась в Дискуссионном."
    "Но он хотя бы с этим смирился... Уже хорошо."

    show hiroto 1c at t11

    ts_ft "Кушать будешь?"
    
    show hiroto 1d at s11
    
    m "Да, я просто умираю с голоду."

    show hiroto 2b at t11

    ts_ft "Ну хорошо. На ужин у нас отбивные, если что!"
    
    show hiroto 2e at f11

    $ TS.Screens(vpunch)

    m "Папа!.."
    m "Ты же знаешь..."
    ts_ft "..."
    m "..."

    show hiroto 2g at t11

    ts_ft "Да шучу я!"
    ts_ft "У нас на ужин рис с мясом и овощами."
    
    show hiroto 2f at f11
    
    m "Вот так-то гораздо лучше."

    "Пройдя основную стадию юношеского максимализма, которая у меня была ещё пару лет назад, житейские отношения у нас в семье стали гораздо веселее."
    "Мы постоянно подшучиваем друг над другом."
    "Например, на прошлое первое апреля я сказала папе, что с треском провалила какое-то соревнование по настольному теннису."
    "Папа изначально очень расстроился, но затем он вспомнил, какой сегодня день, и в итоге мы оба просто над этим посмеялись."
    "Нет, выиграть его я тоже не выиграла, но всё было гораздо лучше, чем то, как я изначально «жалобно» рассказывала папе."
    "В отместку на это на первое апреля этого года мои родители сообщили мне, что в семье ожидается пополнение."
    "Я уже ждала, как где-то в декабре-январе мне придётся ухаживать за младшим братиком или сестричкой, пока родители будут в очередной командировке..."
    "Но в итоге мы тоже все просто с этого посмеялись."
    "Потому что это просто немыслимо, что с такой разницей в возрасте мне придётся ухаживать ещё за кем-то."
    "Ну то есть, я буду уже достаточно взрослой, чтобы стать ему или ей скорее тёткой, чем старшей сестрой..."
    "Но недостаточно взрослой, чтобы быть ему или ей второй мамой, пока первая в очередной заграничной командировке."
    "Кстати, о птичках..."

    show hiroto 2d at t11

    m "Кстати, а где мама?"
    
    show hiroto 1c at t11
    
    ts_ft "Мама сегодня снова уехала в командировку, вернётся не раньше твоего фестиваля."
    
    show hiroto at cright with move
    hide hiroto

    "Дальнейший ужин происходит в тишине."
    "Как вдруг папа говорит."

    show hiroto 2t at ln11

    ts_ft "Моника, солнце моё, а ты не будешь против, если я немного порасспрашиваю о тебе?"
    m "Ну-у-у... не буду?"

    show hiroto 2b at f11

    ts_ft "Отлично."

    "Казалось, что он весь вечер ждал этого ответа."

    ts_ft "Как дела, как жизнь вообще?"
    
    show hiroto 1a at t11
    
    m "Да в целом, нормально. Жизнь как жизнь. Вот, недавно нашла себе новую подругу."
    
    show hiroto 2b at f11
    
    ts_ft "Ну, вот и замечательно. А то я уж думал, что ты вообще без друзей останешься."
    show hiroto at cright with move
    hide hiroto
    "Не знаю, шутил он или нет, но в сердце всё равно кольнуло."
    show kaori 21a at ts_showscreens:
        xpos 150 alpha 0.5
    "Каори уже давно была в прошлом, но воспоминания о ней жалят до сих пор."
    show kaori at ts_hidescreens:
        xpos 150 alpha 0.5
    "Да, пусть и меньше, но жалят всё равно."
    hide kaori

    show hiroto 2b at ln11
    ts_ft "А расскажи-ка о ней. Сатори, кажется?"
    show hiroto 2a at f11
    m "Сайори."
    show hiroto 2b at t11
    ts_ft "Да, извини."
    show hiroto 2a at s11
    m "Ну-у-у... Она... хорошенькая. Причём очень хорошенькая. Она как лучик солнца."
    show hiroto 2c at t11
    ts_ft "Это хорошо..."
    show hiroto 2e at f11
    "Я сознательно не рассказываю о проблмах Сайори."
    "Должно быть, это и есть депрессия?.."
    "В любом случае, это секрет, который я не собираюсь рассказывать {b}никому{/b}, и этот секрет я унесу с собой в могилу."
    "Пусть лучше папа думает, что с ней всё хорошо. Это для его же блага."
    "Тем более, что я не особо-то и вру, мы с Сайори действительно в последнее время очень сдружились."
    "Тем временем, папа и не намеревается заканчивать разговор."
    
    show hiroto 1c at t11

    ts_ft "Ладно, Моника, подруги - это всё, конечно, здорово, но друзьями могут быть и не только девочки..."
    ts_ft "Я как бы ни на что не намекаю, но...{nw}"
    
    show hiroto 2j at h11

    $ TS.Screens(vpunch)

    m "Папа!.."

    "Резким, но весёлым тоном, чтобы он не обиделся на меня, отвечаю я, не давая ему договорить."
    "Впрочем, что-то мне подсказывает, что он уже договорил."

    m "Ты же знаешь, что с моей занятостью мне... не совсем до мальчиков..."
    
    show hiroto 2g at f11
    
    ts_ft "Конечно, знаю. Но иногда влюблённость - это такая нелогичная зараза, что она не поддаётся никакому здравому объяснению."
    
    show hiroto 2f at t11

    "Это уже далеко не первый раз, когда папа заговаривает со мной о потенциальных парнях."
    "Он вообще даёт мне очень много дельных советов по тому или иному вопросу."
    "Когда мне было лет двенадцать, и у меня пошли первые месячные, папа проводил для меня импровизированные уроки полового воспитания."
    "Папа - это, конечно, не мама, но мамы очень часто нет дома, поэтому бремя трудности подростковой жизни было возложено на папу."
    "И он даже хорошо старался."
    "Как для мужчины, который попросту не до конца знает обо {b}всех{/b} тонкостях, он был довольно хорош."
    "Хотя и было для него это всё, по сути, в новинку."
    "Нет, он, конечно, и без того знал это всё в общих чертах..."
    "Но одно дело - просто знать в общих чертах, и совсем другое - подробно рассказывать своей дочери о том, что же делать, когда, условно, в тебя влюбился мальчик."
    "Или как справляться с очередными месячными."
    "Или что делать, если они так и не начинаются..."
    
    show hiroto 2f at f11
    
    "А иногда он даже специально старается быть как можно ближе ко мне."
    show hiroto 2j at t11
    "Как-то раз, классе в девятом, я довольно сильно сломала ногу."
    "Было больно и мучительно."
    "Папа же, узнав об инциденте, так распереживался, что ударился затылком о неровный асфальт."
    show hiroto 2f at s11
    "И то ли это была случайность, то ли что-то ещё, но поселили его в ту же больницу, в то же отделение, в ту же палату, где лежала и я."
    "Так что всё это время он был со мной рядом."
    "Интересно, как он отреагирует, когда я скажу ему, что отчаливаю в университет."
    "Наверное, с инфарктом сляжет, не иначе."

    stop music fadeout 5

    m "Я поняла, пап."
    
    show hiroto 2b at t11
    
    ts_ft "Ну, вот и славненько."

    "Выглядело это скорее как допрос бедной Моники, чем «обычный разговор в пятницу вечером»."

    ts_ft "Хочешь, в шахматы сыграем?"
    
    show hiroto 1j at s11
    
    m "Я что-то не хочу, пап, спасибо."
    
    show hiroto 1h at t11
    
    ts_ft "Ну, как знаешь."

    show hiroto at cright with move
    hide hiroto

    "После этих слов каждый отправился к себе: папа - в гостиную, я же отправилась наверх к себе."

    play music ts_mk

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_bedroom
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "У меня есть несколько вопросов касательно сегодняшних событий."
    "Но прежде всего - кто же эта таинственная девушка?"
    "Ведь мы же даже имени её не знаем!"
    "Не говоря уже о том, в каком она классе учится и в каком клубе состоит. Если вообще состоит..."
    "Ну, мы знаем хотя бы об общей внешности..."
    "Но учитывая то, что нашла её именно Сайори, я не удивлюсь, если к моменту, когда она начала рассказывать это мне, она о внешности уже напрочь всё забыла."
    "Хорошо хоть не забыла рассказать об этом мне..."
    "Проще иголку в стоге сена найти, чем отыскать её."
    "Сайори сказала, что она читала книгу за обедом."
    "Может, нам удастся переманить её на свою сторону и стать частью Литературного клуба..."
    "А может, она вообще без клуба, а мы как раз с таким предложением."
    "Да от такого предложения просто невозможно отказаться!"
    "..."
    "Как же я устала за сегодняшний день..."
    "Может, мне что-нибудь почитать?"
    "Я уже давно не брала никакую книжку в руки, но раз я президент {i}Литературного{/i} клуба, то совершенно логично, что я буду читать {i}литературу{/i}."
    "Хоть какую-то."
    "Но все книги кажутся такими толстыми и скучными... В каждой книге не менее пятисот страниц текста!"
    "Да и не {i}настолько{/i} у меня много книг..."
    "Нет, всё-таки я слишком устала, чтобы даже читать литературу, не говоря уже о том, чтобы самой написать что-то."
    "Вот будут выходные, будет новый день, будет новая пища, буду читать новые книжки."
    "Сейчас же, наверное, лучше стоит спуститься в гостиную и посмотреть телевизор вместе с папой."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    $ generate_random_number_tv() # ВЫЗОВ ФУНКЦИИ НА ПЕРЕЗАПИСЬ ПЕРЕМЕННОЙ

    play sound pageflip
    if random_tv_label == 2 or random_tv_label == 8:
        scene ts_living_room_late_telek_hors
    elif random_tv_label == 6 or random_tv_label == 7 or random_tv_label == 5 or random_tv_label == 1:
        scene ts_living_room_late_telek_bumer
    elif random_tv_label == 9:
        scene ts_living_room_late_telek_oxik
    elif random_tv_label == 3 or random_tv_label == 4 or random_tv_label == 10:
        scene ts_living_room_late_telek_sudba
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    ts_ft "Моника, это ты?"
    m "Ну а кто же ещё, пап?"
    m "В комнате нечего делать, а если и есть что-то, то это слишком сложно для моего уставшего мозга."
    m "Поэтому я лучше проведу вечер с тобой, бездумно пялясь в телевизор."
    ts_ft "Ну-у-у, хорошо, как скажешь..."
    m "Вот и здорово!"

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    $ generate_random_number_tv() # ВЫЗОВ ФУНКЦИИ НА ПЕРЕЗАПИСЬ ПЕРЕМЕННОЙ

    play sound pageflip
    if random_tv_label == 2 or random_tv_label == 8:
        scene ts_living_room_night_telek_hors
    elif random_tv_label == 6 or random_tv_label == 7 or random_tv_label == 5 or random_tv_label == 1:
        scene ts_living_room_night_telek_bumer
    elif random_tv_label == 9:
        scene ts_living_room_night_telek_oxik
    elif random_tv_label == 3 or random_tv_label == 4 or random_tv_label == 10:
        scene ts_living_room_night_telek_sudba
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    if random_tv_label == 2 or random_tv_label == 8:
        "За просмотром очередного видоса на вечер время пролетело гораздо быстрее, чем ожидалось."
    elif random_tv_label == 6 or random_tv_label == 7 or random_tv_label == 5 or random_tv_label == 1:
        "За просмотром легендарного криминального фильма на вечер время пролетело гораздо быстрее, чем ожидалось."
    elif random_tv_label == 9:
        "За просмотром легендарного батла на вечер время пролетело гораздо быстрее, чем ожидалось."
    elif random_tv_label == 3 or random_tv_label == 4 or random_tv_label == 10:
        "За просмотром ностальгического фильма на вечер время пролетело гораздо быстрее, чем ожидалось."

    "Настолько, что уже начало одиннадцатого, хотя начали мы смотреть телевизор вот буквально пять минут назад."
    
    show hiroto 2g at ln11

    ts_ft "Моника, что-то поздно уже, ты спать не думаешь?"
    show hiroto 2f at f11
    m "Я, кстати, тоже задаюсь этим вопросом, и этот же вопрос я хотела и тебе задать."
    show hiroto 2s at t11
    ts_ft "Хех."
    show hiroto 1c at s11
    ts_ft "Да, поздновато уже. Хоть завтра и выходной, но всё равно нужно ложиться пораньше, чтобы побольше сделать в завтрашнем дне."

    show hiroto 1f at t11

    "Каждый раз, когда мы заканчиваем вечер подобным образом, папа говорит одно и то же. Слово в слово."
    "Впрочем, я не раздражаюсь. Я и сама жаворонок."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_gost_night
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    show hiroto 1f at ln11

    "Мы оба расходимся по своим спальням."
    ts_ft 1g "Спокойной ночи, Моника."
    show hiroto 1f at f11
    ts_ft "Спокойной ночи, пап. Люблю тебя."
    ts_ft 1g "Я тоже тебя люблю."

    show hiroto at cright with move
    hide hiroto

    "Каждый ушёл в свою спальню."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_darkbed
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Как только я разделась и легла, я ещё немного думаю перед сном."
    "Завтра будет день, завтра будет пища."
    "А в понедельник мы обязательно спросим у этой девочки насчёт её желания присоединиться к Литературному клубу."
    "Как же её зовут?"
    "Вот же Сайори бал-{nw}" 

    window hide
    stop music
    play sound br_glitch
    show ts_bedroom as bg1 at br_glitches(_fps=160, glitch_strength=1)
    $ renpy.pause(0.4, hard=True)
    stop sound
    scene black

    jump ts_scenario_2