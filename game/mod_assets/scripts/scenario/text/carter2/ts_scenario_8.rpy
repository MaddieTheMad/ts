label ts_scenario_8:

    $ renpy.block_rollback()

    python: # ОБНОВЛЯЕМ RPC
        ts_rpc_carter8()

    $ persistent.rpclabel = "8"
    $ persistent.uncolorize = "none"
    $ persistent.sprite_time = "day"
    $ persistent.carter2menu = True
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    if _preferences.language == "english":
        $ save_name = "Calm before the storm"
    else:
        $ save_name = "Затишье перед бурей"

    play sound chp2
    if _preferences.language == "english":
        $ Chapter("ACT TWO")
        $ Chapter("ACT TWO")
        $ Chapter("chapter four")
        $ Chapter("chapter four")
        $ Chapter("Calm before the storm")
        stop sound fadeout 7
        $ Chapter("Calm before the storm")
    else:
        $ Chapter("АКТ ВТОРОЙ")
        $ Chapter("АКТ ВТОРОЙ")
        $ Chapter("Глава четвёртая")
        $ Chapter("Глава четвёртая")
        $ Chapter("Затишье перед бурей")
        stop sound fadeout 7
        $ Chapter("Затишье перед бурей")


    play sound ts_alarm fadein 2

    pause 2

    scene ts_bedroom
    show unblink
    show layer master at ts_vstavai_shashlik
    pause 3
    play sound svet_on
    pause 1.5

    show layer screens at ts_showscreens

    "О-о-ох..."
    "Пятница..."
    "На часах, как обычно, семь утра. Но мне {b}та-а-ак{/b} не хочется вставать..."
    show monika 1pd at ln11
    em "Хочешь-не хочешь, а вставать всё равно придётся. Тебе напомнить, какой сегодня день?"
    show monika 1pc at t11
    m "Да без тебя знаю... сегодня завтрак готовлю я."
    m "Но можно же полежать в кровати ещё... пять... минуточек?.."
    if unluck6:
        show monika 3pi at f11
        em "Ты уже один раз полежала ещё пять минуточек. Рассказать тебе, чем это всё закончилось, или ты «и без меня знаешь»?"
        show monika 1ph at t11
        m "Гх-х-х... Ладно, встаю я, встаю!"
        show monika 3pk at f11
        em "Вот так-то гораздо лучше!"
    else:
        show monika 3pl at f11
        show layer screens at vpunch
        em "Нет, нельзя! Вставай давай!"
        show monika 1pj at t11
        m "Да встаю я уже, встаю..."
        show monika 3pk at f11
        em "Вот это другое дело."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music okevrmon fadein 2

    play sound pageflip
    scene ts_bathroom
    with wipeleft_scene


    show layer master at ts_clean_eblet
    pause 2
    play sound open_water_sink
    pause 0.5
    stop sound
    play sound_loop water_sink_stream
    pause 1
    play sound water_splash
    pause 1.6
    stop sound_loop
    play sound close_water_sink
    pause 0.5

    show layer screens at ts_showscreens

    "Холодная вода, как и всегда, одинаково бодрящая и противная."
    m "Бр-р-р..."
    "И как только люди в прошлом умывались только холодной водой? Это же невообразимо!"
    "А я хоть и говорю, что привыкла, на самом деле до сих пор до конца привыкнуть не могу."
    "Умывшись и почистив зубы, я спускаюсь вниз на кухню."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    "За всё это время я так и не придумала, что же приготовить нам с папой на завтрак."
    "Кажется, папа вчера покупал десяток яиц?"
    "Значит, решение пришло само собой."
    "Яичница с беконом для папы, а для меня..."
    "Да я, наверное, и хлопьями перебьюсь. В конце концов, в столовой всегда можно перекусить."
    show monika 3bi at aki_spawn
    em "Ты всегда говоришь, что можно и в столовой перекусить, но так никогда там и не перекусываешь."
    show monika 2bh at t11
    m "А тебе-то вообще какое дело? Ты же даже не ешь. И вообще тебя нет."
    if unluck_ball >= 4:
        show monika 2bh at aki_uhod
        stop music
        python:
            _preferences.volumes['sfx'] = 1.0
        play sound lite_scrimak
        show hiroto 1h at ln11
        show layer screens at vpunch
        ts_ft "Кого нет, Моника?"
        show hiroto 1j at t11
        "Упс..."
        play music ts_mdl fadein 2
        m "А... да никого... Кстати, доброе утро, пап!"
        show hiroto 1g at f11
        ts_ft "Да, доброе..."
        ts_ft 2h "Моника, что-то ты зачастила разговаривать сама с собой. У тебя всё хорошо?"
        show hiroto 1j at t11
        m "А... да, пап, всё хорошо, просто замечательно! Просто... много всего на уме, фестиваль скоро, вот и волнуюсь, даже, вот, сама с собой начинаю разговаривать..."
        "Надеюсь, для папы это прозвучало достаточно убедительно..."
        "Хотя, с другой стороны, это и не сильно далеко от правды..."
        show hiroto 1h at f11
        ts_ft "Ну, как скажешь..."
        ts_ft 1u "Ну да ладно, не об этом..."
    else:
        stop music fadeout 3
        show monika 1bi at f11
        em "Это ещё кого здесь нет..."
        show monika 1bi at aki_uhod
        m "Что?"
        "Однако Аки испарилась так же быстро, как и появилась. В том числе и потому, что на кухню вошёл папа."
        play music ts_mdl fadein 2
        show hiroto 1b at ln11
        ts_ft "Доброе утро, солнце!"
        show hiroto 1a at t11
        m "Доброе, пап."
    show hiroto 1b at f11
    ts_ft "Что на завтрак?"
    show hiroto 1a at t11
    m "На завтрак у тебя яичница с беконом, а у меня... Да, наверное, опять хлопья с молоком и кофе..."
    show hiroto 1h at f11
    ts_ft "Ну нет, так дело не пойдёт, завтракать всё-таки нужно, давай я тебе хоть макароны разогр{nw}"
    show hiroto 1j at t11
    m "Нет. Сегодня завтрак готовлю я, поэтому если я говорю, что мне и одних хлопьев будет достаточно, то так оно и будет."
    show hiroto 1f at t11
    m "В крайнем случае, в столовой поем."
    show hiroto 1g at f11
    ts_ft "Моника, ты уже не первый раз говоришь, что если ты за завтраком не наешься, то в столовой поешь, только вот я сомневаюсь, что ты в столовую вообще ходишь..."
    show hiroto 1j at t11
    em "Вот и я о том же!"
    m "Ну, если ты чего-то не видел, то это не значит, что этого нет в принципе."
    m "Я ем в школе."
    "Иногда..."
    show hiroto 1z at f11
    ts_ft "Ну-у-у... ладно..."
    show hiroto 1b1 at t11
    m "Вот и хорошо. А теперь, попрошу посторониться, а то мы на лишние разговорчики и так достаточно времени потеряли."
    show hiroto 1y at f11
    ts_ft "Ладно, ладно, прошу к плите."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    show hiroto 1a at i11
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Спустя некоторое время завтрак уже был готов и разложен по двум тарелкам."
    "Некоторое время мы просто молча едим, как вдруг папа внезапно произносит:"
    show hiroto 1c at f11
    ts_ft "Кстати, Моника..."
    show hiroto 1e at t11
    m "М-м?.."
    "Мои родители, конечно, очень хорошие и замечательные..."
    "Но я просто ненавижу, как они спрашивают меня о чём-то, пока я сижу с полным ртом."
    "К счастью, папа не задал вопрос, а просто рассуждает."
    show hiroto 1c at f11
    ts_ft "По прогнозу погоды где-то с полудня начинает сереть, а к вечеру обещают сильный дождь."
    ts_ft 2h "Ты уверена, что не хочешь одеться потеплее?"
    show hiroto 1j at t11
    "Дожевав и проглотив хлопья, я ему отвечаю."
    m "Нет, пап, не хочу. От школы до дома всё равно не очень далеко, да и мелкий дождик я люблю."
    show hiroto 1q at f11
    ts_ft "Так обещают не маленький дождик, а целый ливень! И пик как раз приходится на примерно то время, в которое ты из своего клуба возвращаешься!"
    show hiroto 1p at t11
    m "Папа-а-а..."
    m "До школы меньше двух километров, да и хожу я быстро."
    show hiroto 1j at t11
    m "Но раз уж ты так хочешь обо мне позаботиться, то, так уж и быть, возьму зонтик."
    show hiroto 1f at t11
    m "Правда, утром, когда ещё нет ни намёка на тучки, я буду выглядеть с ним, как дура, но... надеюсь, тебе так будет лучше."
    show hiroto 1g at f11
    ts_ft "Да, солнце, мне так будет лучше."
    show hiroto 1g at t11
    "Он грустно усмехается. Чтобы поддержать беседу, я тоже натягиваю улыбку. Однако былой радости в наших лицах уже не осталось."
    show hiroto 1y at t11
    "Впрочем, как нам обоим показалось, беседа уже закончена. Мы молча заканчиваем есть и убираем тарелки в посудомойку."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    show hiroto 1j at i11
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Я проверяю время. Уже 7:55."
    "Чёрт. Уже пора бы и в школу потихоньку собираться."
    "Я озвучиваю эту мысль папе."
    show hiroto 1c at f11
    ts_ft "Ты иди, а я тарелки ещё помою, и тоже выйду. Я на машине, доеду относительно быстро."
    show hiroto 1e at t11
    m "Хорошо. Люблю тебя, пап."
    show hiroto 1g at t11
    ts_ft "Я тоже тебя люблю."
    show hiroto 1g at cright with move
    hide hiroto
    stop music fadeout 3
    "Распрощавшись, я отправилась в школу, а папа отправился домывать тарелки."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Я оглядываюсь в небо. Действительно, на нём нет не то, что {i}ни единого{/i} облачка, даже намёка на эти облачка нет."
    "И чего только папа всё утро говорил о том, что к вечеру пойдёт сильный дождь?"
    "Может, синоптики просто ошиблись? Они же, в конце концов, тоже люди, им тоже свойственно ошибаться."
    "Пожав плечами, я с улыбкой пошла... А, нет, никуда я не пошла – я же зонтик забыла!"
    "Я позорно возвращаюсь в дом, чтобы взять этот проклятый зонтик."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_entrance_day
    with wipeleft_scene

    show layer screens at ts_showscreens
    m "{size=+3}Папа! А ты мой зонт не видел?{/size}"
    ts_ft "{size=+3}Так он на вешалке, рядом с остальными зонтиками.{/size}" #офскрин батя
    m "{size=+3}Спасибо.{/size}"
    "Взяв свой, я уже окончательно выхожу из дома."
    stop music fadeout 4
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene

    play sound pageflip
    scene ts_street
    show ts_green_part
    with wipeleft_scene

    show layer screens at ts_showscreens
    play music ts_tg fadein 3
    "Пока суть да дело, уже и несколько минут прошло."
    "Я ещё раз проверяю время. Уже ровно восемь."
    if unluck6:
        show monika 2d at aki_spawn
        em "Что-то ты рановато на этот раз."
        if unluck4:
            em 3k "Устала опаздывать?"
            show monika 3j at t11
            m "Гр-р-р... Отстань, а?"
            show monika 3k at f11
            em "Всё, всё, ухожу. Просто захотелось пошутить над вечно опаздывающей бездарностью!"
        else:
            show monika 2c at t11
            m "Ну... Да? И что в этом такого?"
            show monika 3d at f11
            em "Да ничего. "
            extend 3k "Просто захотелось подшутить над опоздуньей!"
        show monika 3j at t11
        "Совсем от неё покоя нет..."
        show monika 4b at f11
    em "Не переживай, скоро это всё закончится!"
    show monika 4a at t11
    m "О чём ты вообще говоришь?!"
    show monika 2n at f11
    em "А... Да ни о чём... Просто мысли вслух..."
    show monika 2m at t11
    m "Так ты же, по сути, и есть мои мысли!"
    show monika 2i at f11
    em "Если я сказала, что это не твоего ума дело, значит, это не твоего ума дело."
    show monika 2h at t11
    m "Но ты же и есть мой ум!"
    show monika 1r at f11
    em "Просто... отстань..."
    show monika 1r at aki_uhod
    m "Эй, ты куда? Я с тобой ещё не закончила!"
    stop music fadeout 3
    "Однако Аки не отвечала. Кажется, она со мной уже закончила..."
    if unluck_ball <= 4:
        "К счастью, в это время суток этот район города ещё пустует, поэтому никто и не заметил «странную девочку, разговаривающую сама с собой»."
        "А даже если бы кто-то и заметил, то я всегда могу сослаться на то, что я просто по телефону разговариваю."
        "Пусть этот разговор и был... не из самых нормальных."
    "А тем временем уже виднеется и сама школа."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_street at ts_bg_into
    show ts_green_part
    pause 0.5
    scene ts_school_gate_day at ts_bg_exodus
    pause 0.5

    show layer screens at ts_showscreens

    play music ts_mdl fadein 3
    "Я в очередной раз смотрю на часы."
    "«Моника, зачем ты постоянно смотришь на часы, если время особо и не изменилось?» – спросите вы. А я вам отвечу: просто привычка."
    "Нет, конечно, можно ответить что-то модное, что-то вроде «я всегда стараюсь идти нога в ногу со временем», но это же просто... нелогично."
    "Поэтому для простоты я просто говорю, что это привычка. Да и это как-то логичнее, чем заковыристое и абстрактное «иду нога в ногу со временем»."
    "А часы тем временем показывают уже 8:20."
    "Разговор с Аки занял чуть больше времени, чем мне казалось."
    "Ну что же, сегодня все уроки исключительно физико-математические, поэтому все кабинеты расположены в ближнем крыле школы."
    if unluck4 and unluck6:
        em "Ура, хоть раз не опоздаешь."
        "«А когда я вообще в школу опаздывала, не считая этих двух раз?»"
        em "...неважно..."
        "Не обращая внимания на Аки, я неторопливо добираюсь до кабинета."
    elif unluck4:
        em "Ну хотя бы в эту пятницу ты не опоздаешь."
        "«А когда я вообще опаздывала, не считая прошлой пятницы?»"
        em "...неважно..."
        "Не обращая внимания на Аки, я неторопливо добираюсь до кабинета."
    else:
        "Я неторопливо добираюсь до кабинета."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_school_courtyard_day
    with wipeleft_scene

    play sound pageflip
    scene ts_l5
    with wipeleft_scene

    play sound pageflip
    scene ts_stairs
    with wipeleft_scene

    play ambience school_peremena_amb fadein 2

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    show layer screens at ts_showscreens

    "До уроков ещё пара минут. Одноклассники, как и большую часть времени, либо меня боятся, либо с презрением смотрят на меня, либо смотрят куда угодно, но не на меня."
    "Не то чтобы мне было не всё равно – я уже привыкла к своего рода нелюдимости..."
    "Мы всем классом плавно переходим в кабинет."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    stop ambience fadeout 3
    play sound door_open
    scene ts_corridor:
        align (0.5, 0.5) zoom 1
        ease 1.2 align (0.3, 0.4) zoom 1.5
    pause 1.2
    scene ts_class at ts_bg_exodus
    pause 0.5
    show layer screens at ts_showscreens

    "Впереди ещё целых два урока алгебры..."
    "Сегодня на уроке у нас новая тема: комбинаторика."
    "И вот из всей школьной программы лишь комбинаторику я понимаю не очень хорошо."
    "Впрочем, это же новая тема, мы все в равных условиях..."

    $ persistent.uncolorize = "none"
    "Что же, начнём этот день!"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show blink
    pause 2

    $ persistent.uncolorize = "lite"
    hide blink
    show unblink
    pause 1
    show layer screens at ts_showscreens

    "После алгебры понемногу начинают сгущаться тучи."
    "Да, пока они ещё небольшие, однако, по всей видимости, на этот раз синоптики не ошиблись, и сегодня дождь ещё как намечается."
    "Хорошо хоть я зонтик взяла. Даже не могу себе представить, какой же дурой я бы была, если бы всё-таки не решилась его взять."

    play sound stomach_growl

    "О, кстати. Надо бы поесть. А то что это я, сама же сказала папе, что поем сегодня в столовой, а на самом деле есть не буду? Как-то это... неправильно."
    em "Значит, ты всё-таки признаёшь, что я в итоге была права?"
    "Да и это не то чтобы мне самой это было нужно – поесть мне всё-таки необходимо, потому что сегодня хлопьями я совершенно не наелась."
    "Решено: я иду в столовую.{w=1} А ты затыкаешься."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_cafeteria
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Как же давно я не была в столовой... Это вообще та же столовая, или я в какой-то другой школе?"
    "Все эти разноцветные вывески, куча маленьких столиков, да и вообще всё как-то слишком ярко и красочно..."
    "Конечно, в пасмурную погоду всё это выглядит слегка блекло, но всё равно достаточно ярко, чтобы я на пару секунд даже потерялась в пространстве."
    "Не зря же говорят, что «всё лучшее – детям», вот хотя бы один раз администрация школы постаралась на славу, чтобы хотя бы есть было приятнее."
    "Самое главное, чтобы сама еда была настолько же вкусной, как и интерьер столовой – красивым."
    "Собравшись с силами, я встаю в очередь."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    pause 2

    show layer screens at ts_showscreens
    "Закупив всё, что мне было нужно, я подхожу к одному из свободных столиков. Наконец-то можно спокойно поесть..."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    pause 1.5

    show layer screens at ts_showscreens
    "М-м-м..."
    "Кажется, на качестве самой еды такие перестановки также отразились. Я такого вкусного тортика не ела никогда в жизни, даже на свой собственный день рождения."
    if not unluck6:
        em "Я тебе уже говорила, что ещё несколько приёмов пищи сладкого, и твоя толстая задница больше в дверной проём вмещаться не будет?"
        show layer screens at vpunch
        "«Отстань уже, а?»"
        "«Тортик-то небольшой. Я же не весь торт за один заход съем, а только маленький кусочек. Это ничего не изменит.»"
        em "Ну-ну... Только потом не жалуйся мне, что твои жировые складки будут больше, чем весят некоторые первоклашки."
        "Я просто продолжаю есть, не обращая внимания на её укоры."
    "Просто прелестно... И почему только на столовой всё должно было заканчиваться?"
    "Следующим этапом обязательно должен стать разгон всех этих бездарных учителей гуманитарных наук, а на их место должны прийти действительно хорошие."
    show monika 2d at aki_spawn
    em "Это тоже будет. Просто ты этого уже не увидишь."
    show monika 2c at t11
    "А, да, действительно, я же в этой школе последний год нахожусь."
    show monika 1n at f11
    em "Ну-у-у, да, и это тоже..."
    show monika 1m at t11
    "Я не обращаю внимания на Аки и её таинственные послания и просто продолжаю есть."
    stop music fadeout 4
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    pause 3

    show layer screens at ts_showscreens
    ts_unk "Привет, я подсяду?"
    m "Вообще-то, я не разреша... А, ой..."
    show monika 1m at aki_uhod
    show sayori 1a at rn11
    play music okevrsay fadein 3
    m "П-привет, Сайори. Я т-тебя не узнала..."
    m "Садись, конечно!"
    show sayori 3s at f11
    s "Отлично!"
    show sayori 3q at t11
    "В следующую же секунду Сайори плюхается на стол с несколькими блюдами на подносе."
    "Я уже говорила, что её не кормят дома? Ну я на всякий случай повторю."
    show sayori 2c at f11
    s "Я тут хотела поговорить с тобой кое о чём."
    show sayori 2b at t11
    m "И-и-и... о чём же именно ты хотела со мной поговорить?"
    show sayori 2c at f11
    s "Ну-у-у, насчёт фестиваля, конечно же."
    s 2h "До фестиваля осталось три дня, а мы к нему вообще не готовы!"
    s "А я в конце концов вице-президент нашего клуба, я слегка волнуюсь!"
    show sayori 2f at t11
    "Надо же... В такие моменты она кажется даже куда более ответственней меня."
    em "Любой человек будет куда более ответственней тебя, потому что ты бездарность и лентяйка, которая за полтора месяца даже не удосужилась ничего показать, что же в вашем клубе такого интересного."
    em "Вы только и делаете, что обсуждаете книжки, что скучно, и только недавно начали стишками обмениваться."
    "«Ну, мы же пишем стихи каждый день, и с каждым днём этот процесс становится всё лучше и лучше...»"
    em "Это совершенно ничего не меняет. Твой карманный клуб просто опозорится на фестивале, а после этого твоя поделка будет просто закрыта."
    "Как бы мне ни хотелось спорить с Аки, я всё же понимаю, что она права."
    show sayori 3h at f11
    s "Моника? Ты снова отключилась..."
    show sayori 2f at t11
    m "А, что? Д-да..."
    show sayori 3e at f11
    s "С тобой в последнее время такое часто случается... У тебя всё хорошо?"
    show sayori 2f at t11
    m "Д... да... я просто тоже волнуюсь насчёт фестиваля, и собираюсь сделать так, чтобы всё прошло идеально."
    m "А для этого обо многом нужно подумать."
    show sayori 2l at f11
    s "Н-ну хорошо..."
    show sayori 2y at t11
    "Некоторое время мы просто едим молча. Но потом я внезапно заговариваю."
    m "Слушай, Сайори..."
    show sayori 1b at f11
    s "М-м-м?"
    show sayori 1b at t11
    m "Ну, мы же пишем стихи уже несколько дней подряд, и причём довольно успешно, все счастливы и довольны..."
    "Хотя, касательно того, что счастливы и довольны {i}все{/i}, я, наверное, слегка преувеличиваю..."
    "...потому что Юри и Нацуки... скажем так, недолюбливают стили друг друга."
    "Конечно, до ссор и уж тем более драк дело пока не дошло, но каждый день я вижу, как Юри говорит, что Нацуки пишет стихи, которые мог бы написать любой первоклашка."
    "А её почерк выглядит так, как будто тот же первоклашка только неделю назад узнал, как вообще писать, поэтому и выводит такие каракули."
    "Нацуки же в свою очередь говорит, что Юри как будто словарь проглотила, и теперь каждое её ик{b}а{/b}ние образует случайное слово, которое вообще не к месту."
    "А что она говорит по поводу почерка Юри... Один из самых безобидных её упрёков заключается в том, что Юри будет поступать в медицинский университет, а потому заранее готовится к этому."
    "Я точную цитату не помню, но почерк у неё действительно... не из самых читабельных."
    "Впрочем, неважно. Главное, что нам всем обмен стихами нравится, а то, что кто-то упрекает за спиной кого-то другого – это уже дело десятое."
    em "Такими темпами твой клубешник развалится ещё до самого фестиваля..."
    show sayori 2c at f11
    s "Ну, и что с того?"
    show sayori 2b at t11
    m "А что, если..."
    show sayori 4m at h11
    m "Что, если нашим выступлением на фестивале как раз и будет чтение стихов на публику?"
    show sayori 4m at hf11
    s "М-Моника! Но это же так неожиданно и внезапно!"
    show sayori 4n at t11
    m "Сайори, ты уже как минимум в третий раз за неделю это говоришь, но при этом всё равно обмениваешься стихами день за днём."
    m "Какая вообще разница, три человека это будут или пара десятков человек?"
    show sayori 3j at f11
    s "Большая разница, Моника!"
    s "Вы же мои друзья, и я к вам уже привыкла!"
    s 2h "А какой смысл позориться на публику перед людьми, которые скорее всего придут к нам в первый и последний раз?"
    show sayori 2f at t11
    m "Ну так... в этом же и смысл."
    m "Если они придут к нам в первый и в последний раз, то ты больше их никогда и не увидишь."
    m "А если кто-то после фестиваля и захочет присоединиться к нам, то ты и к этим новым людям быстро привыкнешь."
    show sayori 2y at t11
    m "Сайори, ты же очень открытый человек, ты Юри с Нацуки уже считаешь своими друзьями..."
    "В отличие от меня же..."
    m "Я тебя уверяю, не пройдёт и недели, как ты уже будешь считать и этих новых людей своими новыми друзьями, с которыми уже не так страшно будет делиться..."
    show sayori 3l at f11
    s "Н-ну ладно, убедила..."
    show sayori 3y at t11
    m "Теперь самое главное: убедить и Юри с Нацуки, чтобы мы все были заодно..."
    show sayori 2x at f11
    s "О, за это не переживай, я с ними ещё поговорю."
    s 3r "У нас будет самое лучшее представление клуба во всей школе!"
    show sayori 3q at t11
    "Мне бы твоей уверенности, Сайори..."
    m "Э-э-э... да, именно!"
    "Пока разговаривали, мы уже давно доели и просто говорили о клубе."
    "Поэтому, закончив разговор, мы с Сайори расстаёмся."
    show sayori 2x at f11
    s "Ладно, я пошла. До скорого, Моника!"
    show sayori 2a at t11
    m "Да, до скорого..."
    show sayori at cright with move
    hide sayori
    "Сайори ушла. Да и мне надо поторапливаться, до звонка меньше минуты."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_class
    with wipeleft_scene

    show layer screens at ts_showscreens
    "Фух, успела... Теперь начинаются уже не такие приятные предметы..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show blink
    pause 2
    play ambience rain_int fadein 2
    play music ts_raindrops fadein 2
    pause 1
    if renpy.android:
        scene ts_class_rain_vedro
        show ts_rain
    else:
        scene ts_class_rain_shader
    show ts_class_rain_ovr
    show unblink
    pause 1
    show layer screens at ts_showscreens

    "Школьный день постепенно подходит к своему логическому завершению."
    "Тем временем на улице уже слышны первые перестуки дождя."
    "Кап-кап-кап, кап-кап-кап... Я очень люблю дождь. Причём я одновременно люблю как просто наблюдать за ним за окном, так и гулять под самим дождём."
    "Ну, только если он не очень сильный, конечно, а то так и простудиться недалеко..."
    if not unluck6:
        em "А следовательно, простужусь и я. А ты знаешь, на что готово твоё «больное подсознание»."
        "«Вообще-то, не знаю – я поэтому потом и передумала и любезно отказалась, хотя изначально приглашала тебя к себе в воду.»"
        em "Ой, ну и пожалуйста..."
    "Бр-р-р..."
    "Ладно, дождь дождём, но у меня же ещё и клуб впереди..."
    $ persistent.sprite_time = "day"
    "Осталось только надеяться, что Сайори уговорила Юри и Нацуки..."

    stop music fadeout 3

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show blink
    pause 1.5

    if renpy.android:
        scene ts_corridor_rain_vedro
        show ts_rain
    else:
        scene ts_corridor_rain_shader
    show ts_corridor_rain_ovr
    show unblink

    pause 2

    show blink
    pause 1.5

    if renpy.android:
        scene ts_club_rain_vedro
        show ts_rain
    else:
        scene ts_club_rain_shader
    show ts_club_rain_ovr
    show unblink

    show layer screens at ts_showscreens

    $ persistent.sprite_time = "cloudly"

    "Я снова пришла в клуб первой."

    play sound stuk1

    "Впрочем, буквально через секунду после того, как я об этом подумала, в клуб входят и все остальные девочки."
    play sound door_open
    play music t5_all fadein 2
    show yuri 1g at ln31
    show sayori 3r at ln32
    show natsuki 1t at ln33
    s "Привет, Моника! Я их всё-таки уговорила на выступление!"
    show yuri 1q at f31
    show sayori 3q at t32
    y "П-пусть и н-не без труда..."
    show yuri 1q at t31
    show natsuki 1t at f33
    n "Да, Юри прям конкретно поломалась перед тем, как Сайори её наконец уговорила!"
    show yuri 3v at f31
    show sayori 2e at t32
    show natsuki 1z at t33
    y "А я-то ч-что? М-мне просто... н-неловко б-будет..."
    show yuri 3w at t31
    "Юри от волнения даже закрыла глаза и тяжело задышала."
    m "Юри, да не тушуйся ты так, нам всем будет немного неловко перед выступлением!"
    show yuri 3n at hf31
    show layer screens at vpunch
    y "!!!"
    show yuri 3n at t31
    m "Я и-имела в виду, что мы все будем в примерно равных условиях."
    m "Ведь никому же из нас не доводилось публично выступать ранее?"
    show yuri 2o at t31
    show sayori 2k at t32
    show natsuki 1u at t33
    "Все замотали головой."
    m "Ну вот."
    stop music fadeout 3
    m "Я, если честно, тоже никогда публично не выступала."
    show natsuki 2h at f33
    n "Моника, ты же раньше в Дискуссионном клубе была..."
    n 2e "Никогда не поверю, что президент Дискуссионного клуба никогда не выступал публично!"
    show natsuki 2g at t33
    "Чёрт, она так-то права..."
    "Но у меня был заготовлен ответ на этот вопрос."
    play music audio.t9 fadein 2
    m "Н-Нацуки, Дискуссионный клуб – это место для оттачивания навыков ораторского искусства, и в особенности для тех, кто этим раньше никогда не занимался."
    m "Да и дискутируем мы в основном между самими членами клуба. А это же не сильно отличается от обмена стихами в Литературном?"
    "Нацуки отрицательно мотает головой."
    m "Вот именно. На момент предыдущего фестиваля я ещё даже президентом не была, и вместо этого просто сослалась на то, что у меня... живот разболелся, и я ушла домой."
    m "Нет, я никого не подводила, я изначально была как бы заменой для девочки из основного состава, и ответственности я не боюсь..."
    em "Это кто там говорит?"
    m "{size=+6}Поэтому-то я и создала новый клуб с нуля, потому что я не боюсь ответственности, а наоборот, иду навстречу к ней.{/size}"
    "Последнее предложение я сказала с небольшим нажимом, чтобы даже Аки услышала."
    em "Во-первых, я и так всегда с тобой, так что кричать было не обязательно. А во-вторых, ну ладно, в этот раз убедила."
    m "Что вообще сложного в том, чтобы постоять две минуты и зачитать небольшой стишок?"
    show yuri 2q at f31
    y "Н-ну, м-много сложного..."
    show yuri 2o at t31
    m "Юри, я тебе ещё раз говорю, не переживай ты так."
    m "А ещё я повторяю, что все мы в равных условиях, нет кого-то лучше или хуже. Все мы равны."
    m "Вы же уже привыкли к тому, чтобы обмениваться стихами друг с другом?"
    show yuri 2zg at t31
    show sayori 2f at t32
    show natsuki 1s at t33
    "Все закивали."
    m "Ну вот и здорово."
    "И пока Нацуки или ещё кто-то снова не предъявил мне что-то, я сама решаю взять инициативу."
    m "Кстати, об обмене стихами – все ведь написали стихи?"
    show yuri 1i at t31
    show sayori 2d at t32
    show natsuki 1j at t33
    "Все ещё раз закивали, однако здесь в них уже чувствовалась какая-то уверенность."
    m "Тогда начинаем. У нас ещё после обмена стихами важный разговор есть."
    "Все девочки достают свои стихи. Я тем временем перечитываю свой."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show layer master at ts_blur_ahuenno
    with dissolve

    show layer screens at ts_showscreens

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_m3_eng)
    else:
        show screen poem(poem_m3)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem
    hide poem_dismiss

    show layer master
    with dissolve

    show layer screens at ts_showscreens

    stop music fadeout 5

    "Ну что же, неплохо."
    em "Ну надо же, ты снова написала стих обо мне?"
    "«Нет, обо мне.»"
    em "Так ты же ни черта не знаешь, потому что ты бездарность!"
    "«И как, простите, одно соотносится с другим?»"
    em "Угх... обменивайся уже стихами давай, девочки одну только тебя ждут..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show blink
    pause 1.5

    if renpy.android:
        scene ts_club_rain_vedro
        show ts_rain
    else:
        scene ts_club_rain_shader
    show ts_club_rain_ovr
    show unblink

    show layer screens at ts_showscreens

    $ ts_carter8_poem_firstread = False
    $ ts_carter8_poem_sayori = False
    $ ts_carter8_poem_natsuki = False
    $ ts_carter8_poem_yuri = False
    $ ts_carter8_poem_yuri_first = False
    $ ts_carter8_poem_natsuki_first = False
    $ ts_carter8_poem_sayori_first = False
    jump poemresponses2suka

label poemresponses2suka:

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show layer screens at ts_null_transform

    if ts_carter8_poem_sayori and ts_carter8_poem_natsuki and ts_carter8_poem_yuri:
        jump ts_carter8_posle_poems_suka

    if not ts_carter8_poem_firstread:
        if _preferences.language == "english":
            $ menutext = "Who should I show my poem to first?"
        else:
            $ menutext = "Кому я покажу стихотворение первой?"
    else:
        if _preferences.language == "english":
            $ menutext = "Who should I show my poem to next?"
        else:
            $ menutext = "Кому я покажу стихотворение следующей?"

    play music audio.t5 fadein 2

    menu:
        "[menutext]"
        
        "Сайори" if not ts_carter8_poem_sayori:
            if not ts_carter8_poem_yuri_first or ts_carter8_poem_natsuki_first:
                $ ts_carter8_poem_sayori_first = True

            $ ts_carter8_poem_sayori = True
            if not ts_carter8_poem_firstread:
                show layer screens at ts_showscreens
                "Начну-ка я сначала с Сайори."
                $ ts_carter8_poem_firstread = True
                show layer screens at ts_hidescreens
                " {w=1.0}{nw}"

            stop music fadeout 2

            show blink
            pause 1.5

            if renpy.android:
                scene ts_club_rain_vedro
                show ts_rain
            else:
                scene ts_club_rain_shader
            show ts_club_rain_ovr
            show sayori 1a at i11
            show unblink

            show layer screens at ts_showscreens

            play music audio.okevrsay fadein 2

            m "Ну, привет ещё раз, Сайори."
            show sayori 2x at f11
            s "Привет, Моника!"
            show sayori 1a at t11
            m "Ты стих написала?"
            show sayori 4j at f11
            s "Моника, я тебе уже тысячу раз ответила: да, написала!"
            show sayori 4i at t11
            m "Ну прости, Сайори. Я просто слегка волнуюсь, это же последний обмен стихами перед фестивалем, вот и всё."
            "И кстати, это недалеко от правды: когда я переживаю или волнуюсь, перед тем, как что-то сказать или сделать, я тысячу раз подумаю, ничего ли я не забыла и всё ли у меня есть."
            show sayori 3l at f11
            s "Ну, я, вообще-то, тоже волнуюсь, я же в конце концов твой вице-президент всё-таки..."
            show sayori 2y at t11
            "Я подумываю о том, чтобы сказать ей, что она уже тысячу раз сказала, что она вице-президент, и что если она скажет это в тысячу первый раз, ничего от этого не изменится."
            "Однако в последний момент отказываюсь."
            "Всё-таки она очень польщена тем, что я назначила вице-президентом именно её, и очень гордится этим званием."
            "Чем бы дитя ни тешилось... Впрочем, мы же с ней одногодки, поэтому это кто ещё тут заслуживает называться дитём."
            "А, кстати, об этом..."
            show sayori 2b at t11
            m "С-Сайори... у меня тут к тебе один вопросик небольшой..."
            m "А к-когда у тебя... д-день рождения? А то я тут подумала как-то... И не знаю, когда у моего {i}вице-президента{/i} день рождения."
            "Я делаю акцент на слове «вице-президент», чтобы поддержать этот статус."
            "Иначе в чём его смысл, если кроме себя самого, тебя никто так не называет?"
            show sayori 2c at f11
            s "А ты что, забыла уже? Я же говорила тебе..."
            show sayori 2b at t11
            m "Разве? Что-то я запамятовала..."
            show sayori 2zc at f11
            s "Да ладно, все ошибаются, и никто не может помнить вообще всего..."
            s 3zb "А день рождения у меня, кстати, восьмого апреля!"
            s 2x "И раз уж ты сама спросила..."
            s 5a "А у тебя день рождения когда?.."
            show sayori 5a at t11
            "А вот это уже потяжелее..."
            "Свой день рождения я знаю (в конце концов, это же {b}мой{/b} день рождения), но показывать такую личную информацию мне просто... не совсем свойственно."
            "Впрочем, это же моя подруга Сайори – она хоть человек и открытый, но за то время, что я её знаю, она не из таких, кто будет трепаться языком по поводу и без."
            "Что вообще плохого может случиться?"
            m "Э-э-э... двадцать девятого мая..."
            show sayori 5b at f11
            s "Да-а-а, далеко ещё тебе до дня рождения..."
            show sayori 5b at t11
            "Да как будто тебе сильно раньше..."
            m "Далековато, да..."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            pause 2
            show sayori 4n at t11
            pause 0.5
            show sayori 3o at t11
            pause 0.5
            show sayori 4n at f11
            show layer screens at ts_showscreens
            s "Ой, я же тебе стих не показала!"
            s 3x "Вот он!"
            show sayori 3a at t11
            "Ну, уже лучше, уже хотя бы не на мятом листочке, а в каком-то подобии записной книжки. Похвально."
            show sayori 2y at t11
            "Сайори, кажется, тоже уловила мою мысль и продолжает."
            show sayori 2zc at f11
            s "Я очень серьёзно отношусь к написанию стихов, и с каждым разом пишу стихи всё сложнее и длиннее."
            show sayori 2d at t11
            "...или нет, не совсем уловила. Но посыл всё равно ясен – более качественные стихи примерно и означает более качественное оформление этого самого стихотворения."
            m "Ну давай посмотрим, что ты там написала..."
        
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            show layer master at ts_blur_ahuenno
            with dissolve

            show layer screens at ts_showscreens

            if not persistent.first_poem:
                $ persistent.first_poem = True
                show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
                    xpos 1050 ypos 590

            play sound pageflip

            if _preferences.language == "english":
                show screen poem(poem_s2_eng)
            else:
                show screen poem(poem_s2)

            pause

            play sound pageflip
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem
            hide poem_dismiss

            show layer master
            with dissolve

            show layer screens at ts_showscreens
    
            show sayori 3i at t11
            "Я буквально поражена."
            "За эти четыре дня Сайори очень сильно продвинулась в стихосложении."
            "От парочки четверостиший на вырванном листе бумаги до настоящей поэмы, с разным количеством строк в строфах, перекрученными, но в то же время простыми рифмами, и довольно сложным, но бодрым ритмом."
            m "С-Сайори, я поражена... Ты очень, {i}очень{/i} быстро учишься."
            show sayori 2zc at f11
            s "Ч-что, п-правда?"
            show sayori 2d at t11
            m "Я это совершенно серьёзно."
            m "Ты очень продвинулась за этот короткий срок."
            m "За три дня пройти путь от пары четверостиший без особой рифмы до самой настоящей поэмы..."
            m "Похоже, что не зря я в тот день назначила вице-президентом именно тебя."
            show sayori 2t at t11
            "Не сдержав эмоций, Сайори снова начинает плакать."
            show sayori 2zd at f11
            s "П-прости, Моника... Я просто не сдержалась."
            s "Н-но это очень многое для меня значит..."
            s "Обещаю, что я тебя не подведу на фестивале..."
            show sayori 2t at t11
            show blink
            m "Всё хорошо, Сайори..."
            "Я обнимаю её."
            "Видимо, она в этом плане такая же, как и Нацуки: она тоже не умеет принимать комплименты."
            "Ну, по крайней мере, она хотя бы их лучше воспринимает."
            hide blink
            show unblink
            show sayori 3l at f11
            s "Ладно, эм-м-м..."
            s "Можно и я теперь твой стих почитаю?"
            show sayori 3y at t11
            m "Ну что за вопросы, конечно, можно."
            show sayori 2x at f11
            s "Хорошо!"
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            pause 3
            show layer screens at ts_showscreens
            "Это занимает некоторое время."
            show sayori 2a at t11
            m "С-Сайори...{nw}"
            s 2j "Тихо ты, я ещё не дочитала!"
            show sayori 2i at t11
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            pause 4
            show layer screens at ts_showscreens
            show sayori 3l at f11
            s "Да, не ожидала я от тебя такого, Моника..."
            show sayori 3y at t11
            m "А это всё в хорошем смысле или в плохом?.."
            show sayori 2zc at f11
            s "Ну что ты вопросы задаёшь дурацкие, естественно, в хорошем смысле."
            s 2x "Оно тоже в какой-то мере абстрактное, и в целом очень хорошее, просто... "
            extend 5a "Очень длинное..."
            if ts_carter8_poem_yuri:
                show sayori 5b at f11
                s "Очень похоже на то, как пишет Юри."
            show sayori 5b at t11
            m "А-ха-ха, ну..."
            m "Я просто поймала вдохновение и писала... а потом ещё писала... и ещё... а потом оказалось, что я целую поэму настрочила, а не обычный стишок."
            show sayori 2l at f11
            s "Ну, с твоей-то поэмой мой стих и рядом не стоит..."
            show sayori 2k at t11
            m "Так, Сайори, ну-ка... {w=0.44}это... {w=0.44}прекращай принижать себя и все свои творения."
            show sayori 2f at t11
            m "То, что я написала стих больше, вовсе не означает, что сам стих лучше."
            m "Вот хотя бы возьми Юри и Нацуки для сравнения."
            m "У одной получаются довольно длинные стишки со сложными словами, а у другой стихи получаются коротенькими и с простенькими словами."
            m "Но это не значит, что кто-то пишет лучше, а кто-то – хуже. Они обе пишут одинаково хорошо."
            m "Вот как и мы с тобой. Ты до этой недели вообще ни одного стиха не написала, а уже стоишь на одном уровне со мной, которая написала кучу стихов."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            show sayori 3d at t11
            pause 0.88
            show sayori 3t at t11
            pause 0.88
            show sayori 3zd at f11
            show layer screens at ts_showscreens
            s "С-спасибо, Моника."
            s "Да... "
            extend 4j "Мы обязательно проявим себя на фестивале с самой лучшей стороны!"
            s 4j "И не только я, и не только ты."
            s "Это всего клуба касается."
            show sayori 2i at t11
            m "Обязательно, Сайори... Обязательно проявим себя..."
            show sayori 5a at f11
            s "Ну, я тогда дальше пойду?"
            show sayori 5a at t11
            stop music fadeout 5
            if ts_carter8_poem_yuri and ts_carter8_poem_natsuki:
                m "Подожди, я ещё объявлю, кто что делает для подготовки к фестивалю, а потом можешь со спокойной душой идти."
                show sayori 5b at f11
                s "О, ладно тогда..."
                show sayori at cright with move
                hide sayori
                "После этих слов Сайори как будто и след простыл."
                "Что же, ладно, всё равно мы после этого снова все вместе соберёмся."
            else:
                m "Да, конечно, иди."
                show sayori 3r at f11
                s "Здорово!"
                show sayori at cright with move
                hide sayori
                if ts_carter8_poem_yuri_first:
                    "После этих слов она быстро пошла обмениваться стихами с Юри."
                elif ts_carter8_poem_natsuki_first:
                    "После этих слов она быстро пошла обмениваться стихами с Нацуки."
                elif not ts_carter8_poem_yuri_first and ts_carter8_poem_natsuki_first:
                    "После этих слов она быстро пошла обмениваться стихами с другой участницей."
                "Да и мне тоже не стоит терять времени."

            jump poemresponses2suka
    
        "Нацуки" if not ts_carter8_poem_natsuki:
            if not ts_carter8_poem_yuri_first or ts_carter8_poem_sayori_first:
                $ ts_carter8_poem_natsuki_first = True

            $ ts_carter8_poem_natsuki = True
            if not ts_carter8_poem_firstread:
                show layer screens at ts_showscreens
                "Пожалуй, начну с Нацуки."
                $ ts_carter8_poem_firstread = True
                show layer screens at ts_hidescreens
                " {w=1.0}{nw}"

            stop music fadeout 2

            show blink
            pause 1.5

            if renpy.android:
                scene ts_club_rain_vedro
                show ts_rain
            else:
                scene ts_club_rain_shader
            show ts_club_rain_ovr
            show natsuki 1a at i11
            show unblink

            show layer screens at ts_showscreens

            play music audio.okevrnat fadein 2

            m "Привет, Нацуки."
            show natsuki 1d at f11
            n "Ну привет."
            n 2k "Ты стих написала?"
            show natsuki 1j at t11
            m "Ну конечно."
            m "Хотела спросить, а написала ли стих ты, но, думаю, это бессмысленно."
            show natsuki 2l at f11
            n "Естественно!"
            show natsuki 1j at t11
            m "Тогда без лишних слов, начинаем."
            "Мы обе достаём свои стихотворения."
            "Стихотворение Нацуки во всё той же мятой дешёвой тетрадке."
            "Ставлю на то, что эту же тетрадь она использует ещё по как минимум трём предметам."
            "Или у неё вообще одна тетрадь для всего: и для учёбы, и для себя."
            "Я даже и сама не заметила, как вскинула одну бровь в недоумении."
            show natsuki 1n at t11
            "Видя моё недоумение, Нацуки спрашивает."
            show natsuki 1m at f11
            n "Что, что-то не так? У меня на лице что-то?"
            show natsuki 1n at t11
            m "Да нет, у тебя нет ничего на лице..."
            m "Просто я тут подумала, что, э-э-э..."
            show natsuki 1m at f11
            n "Моника, заканчивай уже мысль быстрее."
            if not ts_carter8_poem_sayori or ts_carter8_poem_yuri or not (ts_carter8_poem_sayori and ts_carter8_poem_yuri):
                show natsuki 1t at f11
                n "Ты ведь не последняя на очереди, мне ещё с другими девочками меняться..."
            show natsuki 1n at t11
            m "Да-да, уже заканчиваю."
            show natsuki 1i at t11
            m "Нацуки, у тебя что, одна тетрадка на все предметы?"
            show natsuki 1s at t11
            "Теперь уже мешкается Нацуки."
            show natsuki 1t at f11
            n "Ну-у-у, не одна, но..."
            n 12c "У меня всех тетрадей по пальцам одной руки пересчитать."
            show natsuki 12b at t11
            "Нацуки даже отвернулась. Наверняка по сравнению с остальными она чувствует себя бедняком, и ей в какой-то мере стыдно это признавать."
            "Да, во вторник она сама говорила мне, что книгу по обложке не судят, и главное – не обложка книги, а что внутри этой самой книги, но..."
            "Подростковый период – это, по сути, то время, в котором очень хочется похвастаться всем, чем только можно."
            "Кто-то умнее других, кто-то красивее других, кто-то может забросить мяч дальше или выше, у кого-то просто родители богаче других..."
            show natsuki 12g at t11
            "Однако Нацуки хвастаться было просто нечем. По крайней мере, на первый взгляд."
            "А потому неудивительно, что когда она достаёт свои дешёвые тетрадки, её одноклассники с тетрадями покрасивее просто стыдят её."
            "Хотя внутри этой тетради точно такие же записи, как и у других её одноклассников. А ещё она в них стихотворения пишет."
            "Довольно красивые на первый взгляд. Но на второй взгляд – это подростковое трактование многих экзистенциальных проблем."
            "Иными словами, за красивой обложкой стихов Нацуки скрываются темы, которые посильнее многих стихов Сайори и Юри будут."
            m "Н-Нацуки..."
            show natsuki 12c at f11
            n "Что ещё?"
            show natsuki 12b at t11
            m "А давай... Давай я тебе тетрадки куплю..."
            show natsuki 2n at h11
            "После этих слов Нацуки заметно занервничала."
            show natsuki 1m at f11
            n "Моника, спасибо тебе, конечно, но... я, пожалуй, откажусь."
            n 1t "Во-первых, папа не поймёт, откуда у меня взялись новые навороченные тетрадки..."
            n 1q "А во-вторых, одноклассники засмеют меня ещё больше, если увидят новые тетради. А если они узнают, откуда именно взялись эти тетради, то я и тебе репутацию подпорчу."
            n "Правда, спасибо, но... не надо. Я лучше сама как-нибудь."
            n 2t "Тут всего полтора года до выпускного осталось, а время на самом деле быстро летит. Оглянуться не успеешь, а ты уже взрослая и самостоятельная."
            show natsuki 1zc at t11
            "Надо же..."
            "Оказывается, что мы с Нацуки ещё ближе, чем могло показаться..."
            "Да, пусть у нас очень разная внешность, однако говорим мы очень похожими словами."
            m "Д-да, и-именно..."
            show natsuki 2d at f11
            n "Ну ладно, не будем о плохом!"
            show natsuki 2a at t11
            "Я дёрнулась."
            "Внезапно Нацуки весело заговорила. Даже как-то... неестественно весело..."
            show natsuki 2d at f11
            n "Стих-то покажи!"
            show natsuki 1a at t11
            m "Ах... Д-да, к-конечно."
            "Я протягиваю Нацуки стихотворение."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            pause 3

            show natsuki 1za at t11

            pause 3

            show layer screens at ts_showscreens

            "Нацуки как-то слишком долго читает мою стену текста."
            "Хотя, это не удивительно."
            if ts_carter8_poem_sayori_first:
                "Сайори тоже его долго читала."
                "Даже слишком долго..."
            elif ts_carter8_poem_yuri_first:
                "Юри тоже его долго читала."
            elif ts_carter8_poem_sayori and ts_carter8_poem_yuri:
                "Остальные девочки тоже его долго читали."
                "Особенно Сайори."
            show natsuki 1k at f11
            n "Моника..."
            n "Ты стих написала или целую поэму?"
            show natsuki 1za at t11
            "Бинго."
            if ts_carter8_poem_sayori or ts_carter8_poem_yuri or (ts_carter8_poem_sayori and ts_carter8_poem_yuri):
                m "Ну, ты уже не первая, кто так о моей {i}поэме{/i} отзывается..."
            show natsuki 1k at f11
            n "Нет, нет, это очень хорошее стихотворение, но просто..."
            n 1m "Тебе не кажется, что оно {i}слишком{/i} длинное?"
            show natsuki 1n at t11
            m "Знаешь, кажется. Однако у меня уже есть что-то вроде привычки, что пока вдохновение не закончится, я буду писать и писать."
            em "Вот как сейчас..."
            m "И по итогу получилось больше, чем даже я ожидала."
            m "В любом случае, не переживай, это стихотворение я на фестиваль не возьму. Возьму стишок покороче и повыразительнее."
            show natsuki 1k at f11
            n "Хорошо..."
            show natsuki 1za at t11
            m "Кстати..."
            "Я хотела сказать «насчёт покороче», но не думаю, что Нацуки правильно меня поймёт."
            m "Насчёт повыразительнее..."
            m "Дай-ка я теперь и твой стих прочитаю."
            show natsuki 1l at t11
            n "Да без вопросов!"
            n 1y "Покажу тебе, как писать стихи кратко и чтобы сразу к делу!"
    
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            show layer master at ts_blur_ahuenno
            with dissolve

            show layer screens at ts_showscreens

            if not persistent.first_poem:
                $ persistent.first_poem = True
                show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
                    xpos 1050 ypos 590

            play sound pageflip

            if _preferences.language == "english":
                show screen poem(poem_n2_eng)
            else:
                show screen poem(poem_n2)

            pause

            play sound pageflip
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem
            hide poem_dismiss

            show layer master
            with dissolve

            show layer screens at ts_showscreens
    
            show natsuki 1y at f11
            n "Ну как тебе?"
            show natsuki 1za at t11
            m "Ну-у-у... как обычно?"
            show natsuki 1j at t11
            m "Это твоя очередная аллегория на проблемы в мире или что?"
            show natsuki 1l at f11
            n "Ну, что-то вроде того."
            show natsuki 2y at f11
            n "А ещё, прошу заметить, прошу подметить, стих получился не таким громоздким, как у тебя!"
            n "С первой же строки – и сразу к делу!"
            show natsuki 2z at t11
            "Ладно, сама виновата, меня за язык никто не тянул."
            "Впрочем, этот стих Нацуки мне тоже понравился: строфы стали чуть посложнее, с разным количеством строк в каждой, но ему присущи и какая-то рифма, и ритм."
            if ts_carter8_poem_sayori or ts_carter8_poem_yuri or (ts_carter8_poem_sayori and ts_carter8_poem_yuri):
                "Она тоже очень сильно продвинулась в стихосложении за эти несколько дней."
            else:
                "Она очень сильно продвинулась в стихосложении за эти несколько дней."
            m "Ладно, ладно, убедила..."
            show natsuki 1l at f11
            n "Ну вот и поговорили тогда."
            show natsuki 1j at t11
            show layer screens at vpunch
            em "Эй, это моя реплика!\n\n{b}Аки:{/b} Эй, это моя реплика!{fast}"
            "«А ты не забыла, что ты – это часть меня, поэтому любая твоя реплика становится моей?»"
            em "..."
            m "Л-ладно..."
            show natsuki 1k at f11
            n "Ну, я пойду тогда?"
            stop music fadeout 5
            if ts_carter8_poem_sayori and ts_carter8_poem_yuri:
                show natsuki 1za at t11
                m "Подожди, я ещё одно небольшое объявление хочу сделать, и тогда уже все вместе пойдём."
                show natsuki 1k at f11
                n "Хорошо тогда."
                show natsuki at cright with move 
                hide natsuki
            else:
                show natsuki 1j at t11
                m "Не буду тебя больше задерживать, иди тогда."
                show natsuki 2l at f11
                n "Хорошо!"
                show natsuki at cright with move 
                hide natsuki
                "И раз уж такое дело, то тогда и я задерживаться не буду."

            jump poemresponses2suka
    
        "Юри" if not ts_carter8_poem_yuri:
            if not ts_carter8_poem_natsuki_first or ts_carter8_poem_sayori_first:
                $ ts_carter8_poem_yuri_first = True

            $ ts_carter8_poem_yuri = True
            if not ts_carter8_poem_firstread:
                show layer screens at ts_showscreens
                "Наверное, мне лучше стоит начать с Юри."
                $ ts_carter8_poem_firstread = True
                show layer screens at ts_hidescreens
                " {w=1.0}{nw}"
            stop music fadeout 2

            show blink
            pause 1.5

            if renpy.android:
                scene ts_club_rain_vedro
                show ts_rain
            else:
                scene ts_club_rain_shader
            show ts_club_rain_ovr
            show yuri 1c at i11
            show unblink

            show layer screens at ts_showscreens

            play music audio.okevryuri fadein 2

            m "Здравствуй, Юри."
            show yuri 2b at f11
            y "Привет, Моника."
            show yuri 2a at t11
            m "Смотрю, у тебя настроение какое-то приподнятое."
            show yuri 2d at f11
            y "Ну а чего же мне грустить? Мы обмениваемся стихами, узнаём друг друга куда лучше."
            y 2b "Да и другие девочки, которые до этого ни одного стихотворения не написали, за эту неделю продвинулись в стихосложении."
            show yuri 2c at t11
            if ts_carter8_poem_sayori or ts_carter8_poem_natsuki:
                "Значит, не одна я это заметила."
                "Впрочем, это и не удивительно. Юри из нас четырёх самая опытная."
            m "Понятно..."
            "Видимо, в плане поддержания светской беседы мы с Юри похожи: мы абсолютно одинаково совершенно не умеем поддерживать её."
            "Тот эмоциональный всплеск, который был у нас пару недель назад, был скорее исключением, подтверждающим правило."
            "Ладно, ближе к делу."
            show yuri 1e at t11
            m "Юри, ты стих написала?"
            show yuri 1f at f11
            y "Естественно, написала."
            y 2l "Сегодня я решила написать что-то вроде продолжения стиха, который я писала к собранию клуба ещё во вторник."
            y 2j "Вчера вечером мне показалось, что я не написала в стихе всё, о чём я думаю, поэтому я решила продолжить, или скорее, расширить эту тему."
            y 1f "Но не об этом... А ты стих написала?"
            show yuri 1e at t11
            m "За кого ты меня принимаешь? Конечно, написала!"
            "Я вспомнила слова Нацуки, которые она неоднократно говорила мне по поводу того, написала ли я стих, поэтому я подумала, что уместно будет слегка подшутить и поднять настроение нам обеим."
            show yuri 1g at t11
            "Однако я совершенно забыла о том, что Юри не из тех, кто понимает импровизацию."
            em "А я же говорила, что у тебя память, как у золотой рыбки!"
            em "Как ты вообще лица родителей запомнить умудрилась?"
            "«Да отстань ты уже...»"
            show yuri 1h at f11
            y "П-понятно..."
            y 1j "Н-ну, раз мы обе написали стихи, может, тогда ими поделимся?"
            show yuri 1i at t11
            m "И то верно."
            "Я первой протягиваю Юри стихотворение."
            show yuri 1e at t11

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            pause 3

            show yuri 1f at f11

            pause 3

            show layer screens at ts_showscreens


            y "Моника, это стихотворение гораздо лучше всех предыдущих."
            y 2j "Вижу, ты всё-таки прислушалась к моим советам..."
            show yuri 2i at t11
            "Я боюсь признаваться ей, что ни к чьим советам я не прислушивалась, и просто дальше писала по наитию и как вдохновение придёт."
            "Однако я всё равно приятно удивлена, что даже Юри меня хвалит."
            show yuri 1q at f11
            y "Мне даже и придраться особо не к чему."
            y 2q "Кроме разве что одного места, когда ты ни с того ни с сего очень своеобразно выделила слово «перо»."
            show yuri 1s at t11
            m "Ну-у-у..."
            m "Мне нравится играть с местом на бумаге, и если лист большой и мне хватает места, то вместо банального выделения жирным шрифтом или подчёркиванием, я выделяю слова вот так."
            m "Я же и до этого писала стихи подобным образом, когда я очень сильно отделяла строфы, чтобы они казались выразительнее, ты разве не помнишь?"
            show yuri 1zi at f11
            y "Да, что-то такое припоминаю..."
            y 2b "Ладно, хочешь теперь почитать моё стихотворение?"
            show yuri 2a at t11
            m "Конечно, давай."
    
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            show layer master at ts_blur_ahuenno
            with dissolve

            show layer screens at ts_showscreens

            if not persistent.first_poem:
                $ persistent.first_poem = True
                show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
                    xpos 1050 ypos 590

            play sound pageflip

            if _preferences.language == "english":
                show screen poem(poem_y3b_eng)
            else:
                show screen poem(poem_y3b)

            pause

            play sound pageflip
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem
            hide poem_dismiss

            show layer master
            with dissolve

            show layer screens at ts_showscreens
    
            show yuri 2c at t11
            "Судя по всему, она и в расширенном стихотворении не написала обо всём, что думает."
            "Кто знает, может, после фестиваля она и третью часть этого стихотворения напишет?"
            em "Да, кстати, об этом..."
            "«А ты вообще рот закрой и не открывай, пока не спросят.»"
            em "..."
            "Обиделась. Ну что же, мне же проще."
            m "Юри...{w=0.44} кажется мне, ты и со второго раза не написала обо всём, о чём думаешь."
            show yuri 2k at f11
            y "Возможно..."
            y 3d "В любом случае, на данный момент мне в этом стихе нравится всё."
            y 2b "Может, позже, когда я стану ещё более опытной, я вернусь к этому стиху, ужаснусь, и перестану писать про призрака в тусклом свете вообще, но сейчас мне всё нравится."
            show yuri 2a at t11
            m "П-понятно..."
            m "Мне этот стих тоже понравился. Ты удачно продолжила этот стих. Или расширила его..."
            m "Называй это как хочешь, но в общем, мне понравилось."
            em "Ну ты же снова нагло врёшь."
            "«{b}ЧТО Я ГОВОРИЛА О ТОМ, ЧТОБЫ ОТКРЫВАТЬ РОТ ТОЛЬКО В ТОМ СЛУЧАЕ, КОГДА ТЕБЯ СПРОСЯТ?»{/b}"
            "Помните, как я говорила, что мы с Аки стали ладить лучше?"
            "Так вот, это оказалось наглой ложью. За эту неделю она меня невероятно выбесила. А впереди ещё весь вечер, выходные и фестиваль..."
            em "Это ты ещё следующую неделю со мной не жила..."
            "«...»"
            show yuri 2b at f11
            y "Спасибо, Моника."
            y 1f "Ну, я пойду?"
            show yuri 1e at t11
            stop music fadeout 5
            if ts_carter8_poem_sayori and ts_carter8_poem_natsuki:
                m "Постой, мне ещё всем вам надо сказать кое-какую важную информацию, а потом пойдём все вместе."
                show yuri 2f at f11
                y "О, хорошо тогда."
                y "Тогда я к остальным пойду."
                show yuri at cright with move
                hide yuri
                "После этих слов Юри отправилась к Сайори и Нацуки, которые уже давно обменялись стихами, и просто ждут, когда же закончим мы."
                "Ладно, Моника, это будет несложно..."
                em "Опять наглая ложь."
                m "Х-х-х..."
            else:
                m "Да, конечно, иди."
                show yuri 2q at f11
                y "Т-тогда до с-свидания..."
                show yuri at cright with move
                hide yuri
                m "П-подожди!.."
                "Однако Юри уже ушла. А я ведь всего-то хотела ей сказать, что после обмена стихами у меня будет ещё одно объявление касательно фестиваля..."
                "Впрочем, и мне нечего прохлаждаться, надо и мне идти."
                "Кто там у нас дальше?.."

            jump poemresponses2suka

label ts_carter8_posle_poems_suka:
    show blink
    pause 1.5
    if renpy.android:
        scene ts_club_rain1_vedro
        show ts_rain
    else:
        scene ts_club_rain_shader1
    show ts_club_rain_ovr1
    show yuri 1e at i31
    show sayori 1b at i32
    show natsuki 1za at i33
    show unblink

    show layer screens at ts_showscreens

    play music audio.t8 fadein 2

    "Все девочки выжидающе смотрят на меня."
    "Давай, Моника, ты сможешь. В конце концов, это твой же клуб."
    m "И-и-и... итак, ребята!"
    m "Обмен стихами, как я погляжу, прошёл... успешно."
    m "Теперь самое время... заняться подготовкой к фестивалю..."
    "Вот, начало положено. Теперь главное не сбиться с мысли."
    m "Да, нас всего четверо, и на фестивале наш клуб будет выглядеть скромно, но..."
    m "Каждая из нас выложится на максимум, чтобы..."
    show natsuki 1l at f33
    n "Да ладно, Моника, не нервничай ты так!"
    n 2d "Уж кто-кто, а я-то точно выложусь на максимум и напеку самые лучшие кексы, которые эти бездари могут себе только вообразить!"
    show natsuki 1a at t33
    "Ну хоть один человек правильно продолжил мысль за меня."
    em "Это потому что ты сама ни одной мысли больше, чем в пару предложений, составить не можешь."
    m "Верно. Нацуки будет печь кексы, теперь к остальным..."
    show yuri 4c at t31
    show sayori 2k at t32
    "Я смотрю на Юри, но она как будто избегает моего взгляда."
    "Да что же это такое?! Я ведь сюда не ругать её пришла, а просто обсудить, кто что будет готовить для фестиваля."
    "Что же, ладно... Придётся надавить самой. И только пусть попробует возразить, что эта работа ей не подходит!"
    m "Так... сначала ты, Юри..."
    show yuri 3n at h31
    "Услышав своё имя, Юри слегка дёрнулась."
    show yuri 2o at t31
    m "Да, так вот..."
    m "Юри, у тебя же очень красивый почерк."
    show natsuki 1t at f33
    n "{size=-8}Я бы с этим поспорила...{/size}"
    show natsuki 1zb at h33
    m "Что-что?"
    "Нацуки надеялась, что я этого едкого комментария не услышу. Однако у меня слух развит хорошо, как музыкальный, так и обычный."
    "Всё-таки занятия на пианино даром не прошли."
    show natsuki 1q at f33
    n "А... Да нет, ничего..."
    show natsuki 1s at t33
    "..."
    m "Да, так вот..."
    show yuri 4b at t31
    m "Юри, у тебя же очень красивый и уникальный почерк..."
    m "Ты могла бы красиво написать всякие красивые слова, это же {i}литературное{/i} мероприятие, в конце-то концов. А литература без слов – это как, я не знаю, музыка без нот."
    m "Плюс ко всему, ты могла бы задать этому {i}литературному{/i} мероприятию соответствующее настроение, подобрав нужную атмосферу."
    m "Поэтому я бы очень хотела, чтобы всем этим занялась именно ты."
    m "Да и к тому же, подобрать соответствующую атмосферу – это дело очень скрупулёзное."
    "Последнее предложение я произнесла с некоторым нажимом, намекая Юри, что до фестиваля ей резаться не стоит."
    "Резаться в принципе не стоит, но начинать-то тоже откуда-то нужно."
    "Надеюсь лишь, что Юри этот намёк поняла."
    show yuri 4a at f31
    y "Атмосферу, говоришь?.."
    y "Вообще..."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show yuri 1l at f51
    show sayori 2o at t32
    show natsuki 1za at t33
    pause 0.25
    show yuri 1l at f43
    pause 0.25
    show yuri 1l at f21
    pause 0.25
    show yuri 3r at f31
    show layer screens at ts_showscreens
    y "Я {b}обожаю{/b} атмосферные мероприятия!"
    show yuri 2l at t31
    show sayori 2m at f32
    s "Надо же, теперь и Юри загорелась!"
    show sayori 2n at t32
    "Я вообще забыла, что она всё это время была с нами. С того момента, как мы закончили обмен стихами, она не произнесла ни слова."
    "Ну, раз так, то..."
    show sayori 2o at t32
    m "Теперь ты, Сайори. Ты у нас будешь... э-э-э..."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = 0.0
    play sound ts_flashback
    show layer master at ts_blur_ahuenno1
    with dissolve2
    show layer screens at ts_showscreens
    "«Аки, можно мне немного помощи?»"
    em "Всё-таки признаёшь, что сама ты ничего придумать не можешь, и наконец обращаешься за помощью ко мне, к своему {i}больному подсознанию?{/i}"
    "«Да, признаю, признаю, а теперь не могла бы ты помочь, а то девочки начинают думать, что я слишком долго думаю над ответом?»"
    em "Ты не только бездарность в моих глазах, но ещё и тугодум в глазах остальных..."
    em "Эх-х-х, ладно, помогу уж."
    em "Ни одно мероприятие от мала до велика не обходится без какой-либо рекламы."
    em "Иначе какой смысл в том, чтобы делать мероприятие, если о нём всё равно никто не узнает?"
    em "Поэтому дай Сайорьке задание сделать листовки и буклетики, да поярче, покрасочнее, как раз под настроение и атмосферу Юри."
    "«А что, это хорошая идея...»"
    em "Конечно, это хорошая идея. Любая идея будет лучше твоей, мисс «девочки, я слишком бестолочь, чтобы сделать что-то стоящее, поэтому придумайте задание вместо меня»."
    "«Х-х-х...»"
    python:
        _preferences.volumes['music'] = .45
    play sound fb
    show yuri 1e at i31
    show sayori 2o at i32
    show natsuki 1a at i33
    show layer master
    with flash
    show layer screens at ts_showscreens

    m "Сайори, ты же у нас человек самый открытый из всех нас, так ведь?"
    show sayori 2y at t32
    "Сайори смущённо кивает головой, явно польщённая моим комментарием."
    m "А никакое мероприятие не обходится без какой-то рекламы. Неважно, литературное оно или нет."
    m "Можешь нарисовать листовки и буклетики? Только чтобы они поярче были, покрасочнее."
    show sayori 2x at f32
    s "А, да без вопросов!"
    s 3c "Только мне нужно сначала узнать, какие именно стихи мы вообще читать будем."
    s "Нарисовать-то я их нарисую, но если мы все разойдёмся по домам, и соберёмся вместе не раньше понедельника, то у нас банально не хватит времени на то, чтобы качественно всё подготовить."
    s 3h "Иначе какой тогда во всех этих приготовлениях смысл, если самое главное – мы сами – не готово от слова совсем?"
    show sayori 3g at t32
    "Твою же мать, я совершенно об этом не подумала."
    m "Э-э-э, ладно, тогда, что же, ну..."
    m "Девочки, выберите по одному стихотворению, которое у вас получилось лучше всего. То стихотворение каждая из вас и будет читать на фестивале."
    show yuri 1g at t31
    show sayori 2b at t32
    show natsuki 1za at t33
    m "Я начну. Я выбираю стихотворение, которое я написала на собрание в среду."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show layer master at ts_blur_ahuenno
    with dissolve

    show layer screens at ts_showscreens

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_m2_eng)
    else:
        show screen poem(poem_m2)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem
    hide poem_dismiss

    show layer master
    with dissolve

    show layer screens at ts_showscreens
    
    "Я решила продолжать тему первого стихотворения, правда, на два дня раньше, чем до этого додумалась Юри."
    em "Эй-эй, ты же сама во вторник говорила, что у вас просто обмен стихами, а не соревнование какое-то."
    em "Или... ты что, лицемерка?"
    "Я не обращаю на Аки внимания и продолжаю."
    em "Нет-нет-нет, никуда ты не продолжаешь, пока я не получу свои ответы!"
    show sayori 2x at f32
    s "Я следующая! Я возьму, э-э-э..."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    pause 2
    show layer screens at ts_showscreens
    s 3p "Блин! Всего четыре стихотворения, а уже так сложно выбрать!"
    show sayori 3p at t32
    m "Ну-у-у, выбери тот, который больше всего по душе."
    show sayori 3p at f32
    s "Так они все одинаково мне по душе!"
    s 2ze "..."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    pause 1.5
    show layer screens at ts_showscreens
    show sayori 3j at f32
    s "Ладно! Тоже возьму стихотворение, которое я написала на собрание в среду."
    show sayori 3i at t32

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show layer master at ts_blur_ahuenno
    with dissolve

    show layer screens at ts_showscreens

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_su_eng)
    else:
        show screen poem(poem_su)


    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem
    hide poem_dismiss

    show layer master
    with dissolve

    show layer screens at ts_showscreens

    show sayori 3x at f32
    s "Он не слишком длинный, не слишком короткий, и в нём присутствует какая-то двойственность настроений. В общем, всё как я люблю!"
    show sayori 2a at t32
    m "Замечательно. Теперь ты, Юри."
    show yuri 2o at f31
    y "М-мне действительно стоит это делать?.."
    show yuri 2o at t31
    show sayori 3j at f32
    s "А ты сама-то как думаешь? Естественно, стоит. Мы можем наделать сколько угодно декораций, напечь миллион кексов, но если мы сами не будем читать стихи, то всё пойдёт коту под хвост!"
    show yuri 2o at f31
    show sayori 3i at t32
    y "Н-ну... Х-хорошо..."
    show yuri 2l at t31
    "Юри переводит дыхание несколько раз, и только затем говорит."
    show yuri 2q at f31
    y "Х-хорошо, тогда я... в-возьму с-стихотворение... которое я н-написала н-на в-вчерашнюю встречу..."
    
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show layer master at ts_blur_ahuenno
    with dissolve

    show layer screens at ts_showscreens

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_y2_eng)
    else:
        show screen poem(poem_y2)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem
    hide poem_dismiss

    show layer master
    with dissolve

    show layer screens at ts_showscreens

    show yuri 2o at f31
    show sayori 2b at t32
    show natsuki 1za at t33
    y "Н-надеюсь, это м-можно?"
    show yuri 2o at t31
    m "Юри, о чём ты говоришь? Конечно, это можно! В моём клубе можно всё!"
    show yuri 2t at f31
    y "Н-ну, просто он о..."
    y 2zi "Впрочем, л-ладно, неважно уже..."
    show yuri 2s at t31
    "Я не обратила внимания на ремарку Юри, хотя и поняла намёк: ножи, резать, соблазн, возбуждение – намёк прямее некуда."
    "Впрочем, Сайори и Нацуки не знают того, что знаю я. Ну да ладно, это для их же блага."
    m "Так, и осталась только..."
    show natsuki 2t at f33
    n "Да, да, осталась только я."
    n 2d "Что же, не буду заморачиваться и зачту стих, который я написала на сегодня."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show layer master at ts_blur_ahuenno
    with dissolve

    show layer screens at ts_showscreens

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_n2_eng)
    else:
        show screen poem(poem_n2)
        
    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem
    hide poem_dismiss

    show layer master
    with dissolve

    show layer screens at ts_showscreens
    
    stop music fadeout 5

    show natsuki 2y at f33
    show layer screens at vpunch
    n "Легко и просто!"
    show yuri 2c at t31
    show sayori 3r at t32
    show natsuki 2z at t33
    "Мы все засмеялись."
    "Как же мне всё-таки повезло, что я нашла этих троих..."
    "Если бы не их проблемы, у нас бы был лучший клуб на свете."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show blink
    pause 1.5

    if renpy.android:
        scene ts_club_rain1_vedro
        show ts_rain
    else:
        scene ts_club_rain_shader1
    show ts_club_rain_ovr1
    show yuri 1a at i31
    show sayori 1a at i32
    show natsuki 1a at i33

    show unblink

    show layer screens at ts_showscreens

    play music ts_afterword fadein 2

    m "Итак, ребята!"
    m "Поскольку времени на то, чтобы потренироваться зачитывать стихи у нас уже не осталось, потренируемся уже в понедельник непосредственно перед фестивалем."
    m "Всем задание ясно?"
    show natsuki 1g at t33
    "Юри и Сайори согласно кивнули. Нацуки же озлобилась."
    play music ts_tom
    show natsuki 1e at f33
    show layer screens at vpunch
    n "Минуточку! Подожди-ка подожди, Моника. То есть, ты всем задания раздала, а сама будешь прохлаждаться все выходные или что?"
    show natsuki 1g at t33
    "Э-э-э..."
    show sayori 3m at f32
    s "Постойте, а ведь и правда!"
    s 2j "Моника, так нечестно! Сама навалила работы на нас всех, а ты будешь отдыхать!"
    show yuri 1h at f31
    show sayori 2i at t32
    y "Моника, это же просто некрасиво по отношению к нам..."
    show yuri 1g at t31
    stop music
    play sound ssikanul
    m "{size=+10}{b}ДА ПОГОДИТЕ ВЫ ВСЕ!{/b}{/size}" with vpunch

    show yuri 3n at h31
    show sayori 3m at h32
    show natsuki 2zb at h33
    "Все как один резко подскочили."
    show yuri 2o at t31
    show sayori 2g at t32
    show natsuki 1n at t33
    m "Я не говорила, что вы будете делать за меня всю работу, пока я буду отдыхать!"
    "Хотя, честно говоря, я об этом думала..."
    m "Я помогу каждой из вас по мере своих возможностей."
    em "А возможностей у тебя не то чтобы и сильно много..."
    m "Поэтому в субботу я сначала пойду к Сайори, а затем к Юри, а в воскресенье буду помогать Нацуки, чтобы кексы к этому моменту не превратились в сухари."
    em "То есть, поможешь только Сайорьке, а у Юри и тем более Нацуки ты будешь разве что под ногами мешаться. Поняла."
    show yuri 2zi at f31
    show sayori 2g at t32
    show natsuki 1n at t33
    y "В-вот это уже б-более справедливо..."
    show yuri 2s at t31
    show sayori 2l at f32
    s "Да, вот так-то лучше..."
    show sayori 2y at t32
    show natsuki 1t at f33
    n "А я всё думала, что ты оставишь всё как есть..."
    n 2z "Ну, вот так и поступают настоящие друзья!"
    show yuri 2c at t31
    show sayori 3r at t32
    show natsuki 2z at t33
    "Все снова засмеялись."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show blink
    pause 1.5
    if renpy.android:
        scene ts_club_rain1_vedro
        show ts_rain
    else:
        scene ts_club_rain_shader1
    show ts_club_rain_ovr1
    show yuri 1a at i31
    show sayori 1a at i32
    show natsuki 1a at i33
    show unblink

    show layer screens at ts_showscreens

    play music ts_afterword fadein 2
    m "Давайте-ка все обменяемся контактами, чтобы я знала, когда и куда конкретно мне подходить."
    "Мы все обменялись контактами."
    m "Тогда... на такой положительной ноте я официально объявляю последнее собрание клуба перед фестивалем оконченным!"
    if _preferences.language == "english":
        $ m_name = "Everyone"
    else:
        $ m_name = "Все вместе"
    show yuri 2d at h31
    show sayori 3s at h32
    show natsuki 2z at h33
    show layer screens at vpunch
    m "Ура!"
    show yuri 2c at t31
    show sayori 3s at t32
    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"
    m "У нас впереди ещё очень важные выходные, и за эти выходные мы должны показать, что у нас клуб, достойный того, чтобы в него вступить."
    m "Так, с Юри и Сайори я увижусь ещё завтра, а с Нацуки я увижусь в воскресенье."
    m "Но на сегодня я больше вас не задерживаю."
    if _preferences.language == "english":
        $ m_name = "Everyone"
    else:
        $ m_name = "Все вместе"
    show yuri 2d at h31
    show sayori 3s at h32
    show natsuki 2z at h33
    show layer screens at vpunch
    m "До скорого, Моника!"
    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"
    stop music fadeout 3
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    play sound door_open
    show yuri at cleft with move
    hide yuri
    pause 0.5
    show natsuki at cright with move
    hide natsuki
    pause 0.5
    show sayori at cleft with move
    hide sayori
    show layer screens at ts_showscreens
    "После этих слов девочки расходятся. Да и мне смысла задерживаться больше нет. В конце концов, уже поздно, даже несмотря на то, что сегодня мы начали пораньше."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    if renpy.android:
        scene ts_corridor_rain1_vedro
        show ts_rain
    else:
        scene ts_corridor_rain_shader1
    show ts_corridor_rain_ovr1
    with wipeleft_scene

    stop ambience fadeout 2

    pause 1

    play sound pageflip
    scene ts_l5
    with wipeleft_scene

    play ambience rain_out fadein 2
    play sound pageflip
    scene ts_nebo_fon_bgshka_suka
    show ts_shkola_rain_ovr
    show ts_rain
    with wipeleft_scene

    pause 2

    play sound pageflip
    scene ts_nebo_fon_bgshka_suka
    show ts_street_rain_ovr
    show ts_rain
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_raindrops fadein 2
    "Твою же мать!"
    "Я, конечно, понимала, что за окном ливень бушует всё сильнее и сильнее, но я всё равно не ожидала, что ливень будет настолько сильным!"
    "Да, я помню, как рассказывала о том, что люблю погулять в дождь, но не в настолько сильный ливень. Здесь вообще ни одной души, кроме девочек из Литературного клуба. Да и то, не всех."
    "Нацуки и Юри в надежде на то, что дождь рано или поздно закончится, просто остались сидеть у входа."
    "Что касается Сайори, то, как я знаю, её дом находится недалеко от школы, поэтому она всё-таки решила испытать удачу и пошла навстречу ливню даже без зонтика."
    "Кстати, о нём – зонтик тут тоже не особый помощник, поскольку, помимо сильного дождя, сегодня ещё и сильный ветер, и капли всё равно будут падать на меня."
    "Поэтому я, по сути, просто зря его взяла."
    "Так что единственным решением будет просто пробежать рысью от школы до дома."
    if unluck6:
        "Тем более, что я в этом деле уже оскомину набила, сейчас мне будет легче."
    else:
        "Всего-то полтора километра. Не умру же я, пока буду бежать!"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound2 ts_woda_beg

    show layer master at ts_running_fast

    pause 4
    stop sound2 fadeout 1
    play sound pageflip
    play sound3 ts_othodos_ot_bega fadein 2
    scene ts_nebo_fon_bgshka_suka
    show ts_house_rain_ovr
    show ts_rain
    show layer master at ts_ustal_suka
    with wipeleft_scene

    show layer screens at ts_showscreens
    "Фух."
    if unluck6:
        "Понемногу я уже начинаю привыкать к забегам на средние дистанции, и пока я бежала до дома, не сильно и устала."
        $ persistent.sprite_time = "cloudly"
        "Правда, как только я подхожу к дому и вхожу в него, то буквально вваливаюсь из последних сил."
    else:
        "Видимо, желание не намокнуть было сильнее усталости, поэтому пока я бежала до дома, не сильно и устала."
        $ persistent.sprite_time = "cloudly"
        "Правда, к моменту, когда до дома оставалось вот буквально пара шагов, адреналин кончился, и я буквально вваливаюсь из последних сил."

    stop ambience fadeout 1
    stop music fadeout 4

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play ambience rain_int fadein 2
    play sound pageflip
    scene ts_vhod_nolight
    with wipeleft_scene

    pause 1

    play sound svet_on
    scene ts_vhod_night
    with flash

    pause 1

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    $ persistent.sprite_time = "day"

    m "Папа!.. Я пришла..."
    "Поскольку у папы ненормированный рабочий день, но нормированная 40-часовая рабочая неделя, в пятницу папа уходит с работы пораньше где-то на полтора часа."
    "Но даже если бы это была не пятница, а любой другой рабочий день, я знаю, что пришла слишком поздно, чтобы прийти домой первой."
    play music ts_row fadein 2
    show hiroto 2g at rn11
    ts_ft "Ну здравствуй, Моника."
    ts_ft 2h "Что-то ты сегодня слишком поздно домой пришла."
    ts_ft "Ты хоть не промокла?"
    show hiroto 1j at t11
    m "Что? А, да нет, я просто очень быстро бежала, я промокнуть просто не успела бы."
    show hiroto 2h at f11
    ts_ft "Точно не промокла? Может, лучше горячий душ примешь? А не то простудишься..."
    show hiroto 2j at t11
    m "Пап, да говорю же тебе, я и не замёрзла, и не промокла особо. Тут от школы до дома десять минут пешком, а если бежать всю дорогу, то и не больше пяти."
    show hiroto 1z at t11
    ts_ft "Ну, за пять минут непрерывного бега многое может произойти..."
    ts_ft 1h "Кстати, почему так поздно?"
    show hiroto 1j at t11
    m "Да опять в клубе задержалась..."
    show hiroto 1z at f11
    ts_ft "Понятно... Как в клубе дела?"
    show hiroto 1b1 at t11
    m "Да как обычно, мы поделились стихами, а потом... ну, это же последний учебный день перед фестивалем, поэтому я всем дала задание сделать кое-что, в чём каждая из них хороша."
    show hiroto 1c at f11
    ts_ft "Так, подожди, а ты что будешь делать?"
    show hiroto 1e at t11
    "Значит, не одна Нацуки такая вредина, а это просто вполне логичный вопрос."
    m "А я просто буду помогать каждой из них."
    "Что, кстати, вполне логичный ответ, потому что я хороша во всём понемногу."
    "Ну, кроме готовки, разумеется. Не знаю, почему Нацуки согласилась на это, но я буду что-то вроде помощницы повара из разряда «подай-принеси», пока сама она будет непосредственно готовить."
    m "Сначала помогу Сайори с листовками, потом помогу Юри с украшениями, а в воскресенье помогу Нацуки с выпечкой кексов."
    show hiroto 2b at f11
    ts_ft "У-у-у, да у вас очень качественное мероприятие будет, с учётом того, что вас всего четверо."
    ts_ft "Вот что: я в понедельник как-то отпрошусь, если не на целый день, то хотя бы на пару часов, чтобы посмотреть на ваш клуб."
    show hiroto 2a at t11
    m "Пап, впереди два выходных дня, а фестиваль уже в понедельник – отгул тебе никто не подпишет."
    show hiroto 1v at f11
    stop music fadeout 4
    ts_ft "И то верно."
    ts_ft 2b "Но я же всегда могу отпроситься на пару часов, чтобы посмотреть на любимую дочурку и её поделку, которую она смастерила с нуля."
    ts_ft 1z1 "А если я не смогу отпроситься легально, я просто скажу, что мне нужно будет в несколько судов сразу, а сам просто в школу пойду."
    show hiroto 2b at t11
    "После этого папа рассмеялся. Да и я тоже начинаю смеяться."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    show hiroto 1c at f11
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_mdl fadein 2

    ts_ft "Ладно, шутки шутками, но есть тоже нужно."
    ts_ft "Я сегодня пораньше с работы ушёл, так что успел полноценный ужин приготовить."
    show hiroto 1a at t11
    m "Так а что же на ужин?"
    show hiroto 2b at f11
    ts_ft "На ужин у нас рис с овощным салатом."
    stop music fadeout 4
    ts_ft 1c "Правда, я уже поел, поэтому рис с овощным салатом будет только у тебя."
    show hiroto 1a at t11
    m "Отлично."
    "Я подхожу к кастрюле и накладываю себе столько риса, сколько я могу себе позволить."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show layer master at ts_blur_ahuenno1
    with dissolve2
    show layer screens at ts_showscreens_nvl
    play music ts_rem fadein 2
    nvl clear
    nvlbazar "{font=[prologue_font]}У нас вообще семья довольно... взрослая и понимающая. Нет такого, чтобы родители готовили то, что я совсем есть не буду, да и накладываем мы каждый себе сам, ровно столько, сколько мы можем съесть."
    nvlbazar "{font=[prologue_font]}Нет такого, чтобы папа наложил мне больше положенного, а я как маленькая девочка дулась, наотрез отказываясь от того, что мне было насыпано."
    nvlbazar "{font=[prologue_font]}...ладно, каюсь, в детстве было несколько раз, и иногда до сих пор происходит, если это опять какая-то рисовая каша. Но поскольку мы все втроём уже взрослые, то таких казусов обычно не происходит."
    nvl clear
    nvlbazar "{font=[prologue_font]}Да, кстати, как вы уже могли догадаться, никаких других сестёр и братьев у меня тоже никогда не было. Всю жизнь были лишь мама, папа да я."
    nvlbazar "{font=[prologue_font]}Бабушек и дедушек, естественно, я в учёт не беру."
    nvl clear
    nvlbazar "{font=[prologue_font]}Хотя, если бы и брала, родители и мамы, и папы живут очень далеко от нас, да и приезжают они к нам довольно редко, поэтому можно сказать, что воспитали меня лишь мама с папой."
    nvlbazar "{font=[prologue_font]}Но даже несмотря на то, что они редко к нам приезжают, в детстве я очень часто каталась к ним на лето, а иногда и на зимние каникулы."
    nvlbazar "{font=[prologue_font]}Хорошее время было, беззаботное. До всех этих клубов, стресса и всего сопутствующего."
    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    show layer master
    with dissolve2
    stop music fadeout 2
    show layer screens at ts_showscreens
    "Но что-то я отвлеклась."
    play music ts_mdl fadein 2
    "Я накладываю рис в тарелку, а также досыпаю немного овощного салата."
    show hiroto 1c at f11
    ts_ft "Так, в общем, ты кушай, пей чаёк, а я пока телевизор пойду посмотрю."
    show hiroto 1e at t11
    m "Хорошо, пап."
    show hiroto 2b at f11
    ts_ft "Ну вот и славненько."
    ts_ft "Всё, приятного тебе аппетита."
    show hiroto 2a at t11
    m "Спасибо, пап. Люблю тебя."
    show hiroto 2g at f11
    ts_ft "И я тебя люблю, солнышко."
    show hiroto at cright with move
    hide hiroto
    stop music fadeout 4
    "С этими словами папа отправлися обратно в гостиную, досматривать очередную политическую передачу, в которой я ничего не смыслю."
    "А я приступаю к тому, чего я ждала со второй перемены: кушать."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens
    play music audio.t8 fadein 3
    "Ужин получился просто замечательным."
    "Теперь надо бы как-то и сказать «пока» по-хорошему, чтобы папа не подумал, что я от него просто убегаю."
    "Я кое-как доковыливаю до гостиной."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show blink
    pause 1.5

    if renpy.android:
        scene ts_living_room_rain_vedro
        show ts_rain
    else:
        scene ts_living_room_rain_shader
    show ts_living_room_rain_ovr
    show unblink

    show layer screens at ts_showscreens
    "Папа, как всегда, даже не обращает на меня внимания, пока по телевизору идёт какая-то политическая передача."
    m "Пап, спасибо за ужин, было очень вкусно."
    ts_ft "Не за что, дорогая."
    "Я пытаюсь придумать ещё хоть что-то для поддержания беседы."
    m "Ты же не забыл, что завтрак на следующий день готовишь ты?"
    ts_ft "Не забыл, конечно."
    "Разговор очевидно не клеился, но к счастью, папа спасает меня."
    ts_ft "Ты к себе пойдёшь или как?"
    m "Да, что-то устала я... Пойду отдыхать."
    ts_ft "Хорошо тогда. Я ещё телевизор посмотрю немного, и тоже уже спать лягу."
    m "Тогда, спокойной ночи?"
    ts_ft "Спокойной ночи, солнце. Люблю тебя."
    "Жаль только, что сегодня к вечеру солнце полностью исчезло."
    em "И не говори..."
    m "И я тебя люблю, пап."
    "С этими словами папа продолжил смотреть телевизор, а я отправилась к себе."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show blink
    pause 1.5

    scene ts_bedroom
    show unblink

    show layer screens at ts_showscreens

    "Наконец-то... Родная спальня..."
    play music ts_dtn fadein 2
    show monika 2bi at aki_spawn
    em "Что же, что же..."
    em "Пришла пора поговорить с тобой начистоту."
    show monika 2bh at t11
    m "Что ты вообще имеешь в виду?"
    show monika 4bd at f11
    em "Я имею в виду всю эту неделю."
    em 3bi "Я надеюсь, что даже такая бездарность, как ты, за неделю успела понять, что разговор со своим «подсознанием» – это..."
    em 2bn "Ну, не совсем правильно."
    show monika 2bm at t11
    m "Я повторяю свой вопрос: что ты вообще имеешь в виду?"
    if not renpy.android:
        show layer master at Static(0.1)
        show layer screens at Static(0.1)
    show monika 2bi at f11
    em "Я, видимо, переоценила твои умственные способности."
    em 4bi "Ты спишь. Всё происходящее за эту неделю – это всё не было реальностью. Это было лишь твоё воображение."
    em "Всё, включая похмелье и утро у Сайори."
    if act2_chess:
        em "Включая партию в шахматы с папой."
    if not renpy.android:
        show layer master at Static(0.3)
        show layer screens at Static(0.3)
    em "Написание своего первого стиха спустя несколько лет застоя, чтение манги с Нацуки, обмен стихами, подготовка к фестивалю..."
    em "Всё происходящее за эту неделю с того момента, как ты проснулась в субботу с дикого похмелья, и вплоть до того, как ты уснёшь сегодня..."
    if not renpy.android:
        show layer master at Static(0.5)
        show layer screens at Static(0.5)
    em "Было просто сном. Больной фантазией одной девочки, которой захотелось друзей и уважения."
    em 3bd "Поэтому-то ты разговариваешь с моей {i}телесной формой{/i} только эту неделю. Потому что всё остальное время ты просто отмахивалась от меня, как от назойливых мух."
    if not renpy.android:
        show layer master at Static(0.7)
        show layer screens at Static(0.7)
    em 4bi "Потому что я ненастоящая. Просто плод твоего воображения."
    hide monika
    show layer master
    show layer screens
    play music ts_roae fadein 2
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show blink
    pause 1.5

    if renpy.android:
        scene ts_residential_rain_vedro
        show ts_rain
    else:
        scene ts_residential_rain_shader
    show unblink

    show layer screens at ts_showscreens
    "Я подхожу к окну и задумываюсь."
    "Что, если всё, что происходило в эту неделю, на самом деле было просто сном?"
    "Да ну нет же, я же точно помню, как мне и самой снились сны..."
    "А сон во сне, внутри сна... Ну это же немыслимо!"
    "Как я каждое утро прощалась с папой..."
    if unluck6:
        "Ну, или почти каждое..."
    "А потом каждый вечер мы снова здоровались..."
    "Мы же обнимались при этом! И объятия при этом были очень даже реальными!"
    "Я кушала каждый день, пила кофе, умывалась ледяной водой, чистила зубы..."
    "...ну нет же, я в это просто не верю!"
    "Всё происходящее было слишком реальным, чтобы обозвать это «просто сном»!"
    "А Аки просто как обычно врёт... Ха-ха-ха, хе-хе-хе... Да, врёт..."
    "Да точно говорю, врёт и не краснеет!"
    "На этой ноте самовнушения я нервно хихикаю, выключаю свет, раздеваюсь и готовлюсь ко сну."
    em "Спокойной ночи, {i}Моника{/i}."
    em "Впереди у тебя будет {b}очень{/b} тяжёлая неделя."
    m "Ну, мы за выходные подготовимся к фестивалю, в понедельник будет сам фестиваль... Но потом-то что?"
    em "Увидишь сама. Завтра же."
    em "Посмотрим, как у тебя медленно будет течь крыша."
    em "Ты же помнишь, как я в субботу что-то говорила про циклы?"
    m "Помню, ясно и отчётливо. Так что ты всё-таки под этим имела в виду?"
    em "Ну, в общем... ты и сама завтра увидишь."
    show layer screens at vpunch
    m "ЧТО Я ДОЛЖНА УВИДЕТЬ?"
    em "Всё."
    em "А сейчас – спокойной ночи, правда."
    stop music fadeout 5
    em "Это будет последняя твоя спокойная ночь..."
    em "Затишье уже закончилось. С завтрашнего дня начинается настоящая буря..."
    "Я не обращаю внимания на угрозы Аки и просто ложусь спать."
    "Завтра будет большой день."
    em "О-хо-хо, ещё какой!"
    m "Ну вот завтра и посмотрим..."
    stop ambience fadeout 3
    show blink
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    scene black with ed_night_dis
    show layer screens at ts_null_transform
    pause 2
    jump ts_scenario_9