label ts_scenario_7:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Акт II | Глава III",details="Пробы пера",large_image="atwocthree",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "7"

    $ persistent.carter2menu = True
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    $ save_name = "Пробы пера"

    play sound chp2
    $ Chapter("АКТ ВТОРОЙ")
    $ Chapter("АКТ ВТОРОЙ")
    $ Chapter("Глава третья")
    $ Chapter("Глава третья")
    $ Chapter("Пробы пера")
    stop sound fadeout 7
    $ Chapter("Пробы пера")

    play music audio.t6s fadein 4
    scene ts_darkbed
    with ed_night_dis
    pause 1

    show layer screens at ts_showscreens

    "Я медленно просыпаюсь."
    "За окном ещё темно, и солнце даже и не думает всходить."
    "Я машинально проверяю время на телефоне."
    "Вдруг я понимаю, что телефона-то у меня и нет."
    "И только потом я вспоминаю, что..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    $ ts_sunset_time()
    play sound fb
    scene ts_gost_sunset
    show hiroto 1a at i31
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with flash

    show layer screens at ts_showscreens

    ts_ft "Можешь идти, я тебе потом телефон занесу."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    $ ts_night_time()
    play sound fb
    scene ts_darkbed
    with flash

    show layer screens at ts_showscreens

    "Телефон-то у папы остался. А положил он его, по всей видимости, уже после того, как я вырубилась."
    "В потёмках я вижу что-то отдалённо похожее на телефон и включаю его."
    "На часах половина пятого утра."
    "Наверное, не стоило засыпать настолько рано..."
    "Ну и что прикажете делать? Спать я уже не сильно-то и хочу, но доспать лишние пару часов - это тоже важно."
    "Я хоть и жаворонок, но не {i}настолько{/i}, чтобы ложиться спать с первыми курицами, а вставать с первыми петухами."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show zatemnenie with dspr

    show layer screens at ts_null_transform

    menu:
        "Лечь спать дальше":
            hide zatemnenie with dspr
            show layer screens at ts_showscreens
            $ unluck6 = True

            "Из карикатурных ангела и демона на плечах победил последний."
            "Несмотря на то, что я выспалась, много сна не бывает."
            "Поэтому, положив телефон рядом с подушкой, я ложусь спать дальше."

            stop music fadeout 3
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            show blink
            pause 2
            $ ts_day_time()
            scene ts_bedroom
            show unblink
            show layer screens at ts_showscreens

            "Вот так-то лучше."
            "Сейчас я {i}окончательно{/i} выспалась, что кажется, что я теперь несколько суток без сна протяну."
            "Кстати, а кто сегодня готовит завтрак?.."

            play sound door_open

            "Кажется, ответ нарисовался сам собой..."

            show hiroto 1p at ln11
            "Сегодня готовит папа. Но, судя по всему, он уже сам поел, уже собирается на работу, и единственное, что осталось - это разбудить непутёвую дочь..."
            show hiroto 1q at f11
            ts_ft "Моника, просыпайся!"
            show hiroto 1p at t11
            m "М-м-м... Доброе утро, пап... А который сейчас час?"
            show hiroto 1q at f11
            ts_ft "Уже начало девятого! Просыпайся, а то в школу опоздаешь!"
            show hiroto 1p at t11

            play sound ssikanul
            play music ts_dtbd

            show layer screens at vpunch
            "ТВОЮ ЖЕ МАТЬ!"

            show hiroto 1v at f11
            ts_ft "Завтрак на столе, кофе новый сделаешь, дверь закроешь на ключ."
            show hiroto 1q at f11
            ts_ft "Всё поняла?"
            show hiroto 1p at t11
            "Спорить с папой не хотелось. Тем более, с утра пораньше. И уж тем более, после такого хорошего сна."
            "Поэтому я просто сказала:"
            m "Хорошо, пап..."
            show hiroto 1c at f11
            ts_ft "Ну вот и славно."
            show hiroto 1q at f11
            m "Только не задерживайся ещё сильнее!"
            show hiroto 1c at f11
            ts_ft "А я поехал, уже и сам опаздываю. Всё, давай, до вечера."

            stop music fadeout 3
            play sound door_open
            show hiroto at cright with move
            hide hiroto

            m "Люблю те... Ладно, неважно..."
            "Сказала бы я это или нет - он уже в любом случае ушёл."
            "Но папа прав: надо поторапливаться. Если всё сделаю быстро, может, даже вовремя приду."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play music ts_est fadein 2

            play sound pageflip
            scene ts_bathroom
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Я и обычно умываюсь довольно быстро, но когда я на грани опоздания, то умываюсь я просто молниеносно."
            "Я даже думаю о том, чтобы не чистить зубы сегодня, но затем... вспоминаю обо всех законах подлости, которые со мной могут приключиться."
            show monika 2bk at rn11
            em "Ты иногда забываешь, что самый большой закон подлости - это ты сама!"
            show monika 2bl at f11
            em "Хотя, это скорее не закон подлости, а закон бездарности. Но в любом случае ты самый большой из всех них!"
            show monika 2bj at t11
            "Я думаю о том, чтобы облить её холодной водой, чтобы она хоть на секунду умолкла."
            show monika 1bi at f11
            em "Вообще-то, я и сама знаю, что именно ты хочешь сделать. Но даже если ты это и сделаешь, я никуда отсюда не уйду."
            show monika 1bh at t11
            m "Знаю. Но зато я хотя бы на мгновение развлекусь."
            m "В любом случае - {i}пожалуйста{/i}, не мешай. И так опаздываю, а если на разговорчики с тобой буду время тратить, то и подавно."
            show monika 3bd at f11
            em "Ладно, ладно..."
            show monika 1bc at t11
            "Я в спешке заканчиваю утренний моцион и бегу завтракать."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_kitchen
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Надо же. Кофе ещё до конца остыл. Хотя бы не придётся выливать и греть новую чашку."
            "Я олимпийскими темпами съедаю хлопья, осушиваю всю чашку кофе в три глотка, и выбегаю на улицу, предварительно не забыв закрыть дверь на ключ."
            "У нас хоть район и благополучный, но если вся семья весь день отсутствует, а дверь останется открытой, то кто знает, какие козни наши соседи или проходимцы могут поставить."

            stop music fadeout 2

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_house
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Я проверяю время."
            "На часах 8:23."
            play music ts_ar
            "Если пробежать всю дорогу от дома до школы, то, может, и не опоздаю..."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound2 ts_running

            scene ts_house at ts_running_fast

            pause 2
            stop sound2 fadeout 1
            play sound pageflip
            play sound3 ts_othodos_ot_bega fadein 2
            scene ts_street at ts_ustal_suka
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Однако, как я уже в очередной раз убеждаюсь, реальность на самом деле гораздо более жестока."
            "А все эти сказки о «спортивной Монике» - это действительно всего лишь сказки."
            "Да, я умею быстро бегать. Но умею быстро бегать я лишь на довольно короткие дистанции."
            "А от дома до школы километра полтора."
            "Поэтому уже метров через четыреста я начинаю выдыхаться."
            stop music fadeout 2
            m "Всё. Дальше иду пешком. Марафонить - это совсем не моё..."
            show monika 2d at ln11
            em "А что вообще «твоё»?"
            if unluck_ball >= 3:
                em "Лажать на каждом шагу?"
            show monika 2c at t11
            "Я не слушаю своё подсознание. Я вообще ничего не слушаю."
            "Единственное, к чему я прислушиваюсь - это к желанию пить. Да побольше, ПОБОЛЬШЕ."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_street
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Вдали уже виднеется школа. На часах тем временем 8:27."

            show layer screens at vpunch
            "Ну же!"
            "Но моё уставшее тело всё-таки пересиливает мой голос разума."
            "К тому же, пока я бежала до школы, я ещё и невероятно вспотела."
            "Поэтому, если я всё-таки опоздаю, то это будет худший день в жизни."
            show monika 2k at rn11
            em "Ты, наверное, хотела сказать, обычный день в твоей жизни."
            show monika 2j at t11
            m "Если ты не будешь мне помогать... то можешь хотя бы просто... не мешать?.."
            show monika 2n at f11
            em "Ладно уж..."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_school_gate_day
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Наконец, передо мной показывается школа."
            "До начала уроков ещё одна минута. Фух, успела..."
            show monika 2d at ln11
            em "Не успела. Ты знаешь, что пока добежишь до кабинета, всё равно опоздаешь?"
            show monika 2c at t11
            play music ts_ar
            m "Да твою мать..."
            hide monika
            "Вторник в нашей физико-математической школе отведён под день гуманитарных наук."
            "Первыми двумя уроками у нас история. А кабинет истории расположен..."
            show monika 2i at f11
            em "Да-да, в самом дальнем крыле школы."
            show monika 2k at f11
            em "Удачи не опоздать!"
            show monika at cright with move
            hide monika
            m "Вот уж спасибо..."

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

            play sound pageflip
            scene ts_corridor
            with wipeleft_scene

            play sound pageflip
            scene ts_stairsre
            with wipeleft_scene

            play sound pageflip
            scene ts_corridorrev
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Да сколько это может продолжаться... Я по школе уже набегалась чуть ли не больше, чем занял весь путь от дома до входа в эту школу!"
            "Уроки начались уже три минуты назад."
            "Может, мне удастся затеряться среди других учеников, которые тоже не к самому звонку приходят на первый урок?"

            stop music fadeout 5

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_class
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Я тихо, как мышка, пробираюсь к своей парте."

            "Однако все мои надежды были разрушены строгим голосом учителя."
            teacher "Мисс Ида!" with vpunch
            m "А, да, что?"
            teacher "Что, даже не скажете ничего? Ни «извините за опоздание», вообще ничего?"
            m "Извините... за опоздание..."
        "Встать пораньше":
            hide zatemnenie with dspr

            show layer screens at ts_showscreens

            "Из карикатурных ангела и демона на плечах победил первый."
            stop music fadeout 3
            "Я потягиваюсь, зеваю один последний раз, а затем включаю свет."
            window hide
            play sound svet_on
            scene ts_bedroom
            with flash
            $ ts_day_time()
            show layer screens at ts_showscreens
            "Как же ярко!"
            "Нужно было сказать маме, чтобы она привезла мне новую люстру, с регулируемой яркостью."
            "Ладно. Раз уж я встала, то нужно сперва умыться."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play music ts_tg fadein 2

            play sound pageflip
            scene ts_bathroom
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Хм-м-м... А может, не умыться, а полноценно принять ванну?"
            "Я, конечно, не неряха, и раз в пару дней хожу в душ..."
            "Но одно дело - быстренько принять душ перед сном, и совсем другое - искупаться в ванной. С чувством, с толком, с расстановкой."
            "Времени у меня более чем достаточно - до начала уроков почти четыре часа."
            "Я открываю кран с горячей водой."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound open_water_sink
            pause 1.3
            stop sound
            play ambience water_sink_stream
            show layer screens at ts_showscreens
            "Папу бы не разбудить..."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_bathroom
            with wipeleft_scene

            show layer screens at ts_showscreens

            if unluck_ball == 5:
                "Ну, хотя бы один раз в жизни повезло. Папу я так и не разбудила."
            elif unluck_ball >= 3:
                "Ну, хотя бы на этот раз повезло. Папу я так и не разбудила."
            elif unluck_ball <= 3:
                "Повезло, повезло. Папу я так и не разбудила."
            "А ведь спальня родителей прямо по соседству с ванной..."
            "...не спрашивайте о причудах моего дома. Какой есть."
            "Как только я пробую воду в ванной руками, я тут же отшатываюсь."
            m "Какая же ты горячая!"
            "Я и так купаюсь в воде, которую родители называют кипятком."
            "Но если горячо даже мне, то, наверное, это кипяток и есть."
            "Поэтому я немного разбавляю {i}кипяток{/i} холодной водой."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            stop ambience
            play sound close_water_sink
            pause 1

            show layer screens at ts_showscreens

            stop music fadeout 4

            "Только после того, как вода достигает приемлемой для меня температуры, я наконец залезаю в ванную."
            "Да, в ногах ещё слегка покалывает от ещё горячей воды, но это быстро пройдёт."
            "Я сажусь."
            play ambience amb_bathroom fadein 4
            "Хм. Пока я садилась, даже... и не горячо уже было?"
            play music ts_est
            show monika 2bk at rn11
            em "А через пятнадцать минут ты уже вылезешь с мыслями, что вода уже холодная."
            em "Интересно, как твои родители держат такую расточительную бездарность, которая набирает полную ванную, чтобы через пятнадцать минут уже вылезти?"
            show monika 3bb at f11
            em "Пустая трата денег, не иначе!"
            show monika 2bj at t11
            m "Ух, я бы тебя сейчас... вместе со мной в воду позвала. Силком."
            show monika 3bd at f11
            em "Боюсь, что это невозможно. Во-первых, я тоже люблю воду потеплее. А во-вторых, для {b}его же{/b} удобства я... не позволяю себе залезать в воду вслед за тобой."
            show monika 3bh at t11
            "Мне снова показалось, что Аки смотрит не {i}на{/i} меня, а {i}сквозь{/i} меня."
            m "Чего? Для кого, {b}его{/b}?"
            show monika 4bl at f11
            em "А, знаешь, неважно уже. Я сказала «его»? Я имела в виду, «своего». Для своего же удобства. Я просто боюсь простудиться и заболеть."
            show monika 2bm at t11

            show layer screens at vpunch

            m "Простудиться? Заболеть? Здесь вода под пятьдесят градусов!"
            show monika 3bd at f11
            em "В любом случае..."
            show monika 3bi at f11
            em "Ты же не хочешь, чтобы я заболела?"
            show monika 2bh at t11
            "Я кривлюсь при мысли о том, что может выкинуть моё «больное подсознание»."
            "Пусть даже эта болезнь скорее физическая, чем психическая."
            m "Ладно. Что-то я с тобой заговорилась. Надо бы не только просто полежать в ванной, надо бы и непосредственно искупаться."
            show monika 1bb at f11
            em "Ну хоть одна ясная мысль твою дурную головушку посетила."
            show monika 1ba at t11
            m "А ты разве вчера не то же самое говорила?"
            show monika 2bk at f11
            stop music fadeout 5
            em "Ну... ладно. Две ясные мысли за... сколько лет?"
            show monika 2bj at t11
            m "...я с тобой больше не разговариваю..."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_bathroom
            with wipeleft_scene

            show layer screens at ts_showscreens

            play music ts_sm
            "Даже несмотря на подпорченное своим подсознанием настроение, в целом настроение было хорошим."
            "Я даже немного побаловалась и налила всяких шампуней, прямо как в детстве."
            "Но справедливости ради, папины я не трогала. А мама всё равно среди прочих гостинцев принесёт новые бутыли шампуня, поэтому никто и не заметит."
            em "Вообще-то, я заметила."
            stop ambience fadeout 5
            m "Вообще-то, тебя нет."
            em "..."
            "Впервые за несколько дней мне удалось заткнуть Аки, а не наоборот."
            "Вытеревшись и одевшись, я спускаюсь на кухню."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_kitchen
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Часы показывали 5:40."
            "Папа проснётся не раньше семи. А это означает, что у меня есть ещё минимум полтора часа, чтобы ничего не делать."
            "Может, устроить небольшую пробежку?"
            "Хотя нет, пробежка сразу после ванной - даже в ноябре это с большой долей вероятности будет означать, что после этого мне понадобится ещё одна ванная."
            "Да и не практиковалась я уже давно..."
            stop music fadeout 3
            "А может, мне что-то приготовить?"
            "Вчера я не успела придумать, что же мне приготовить на завтрак. Но зато сегодня у меня есть всё время во вселенной!"
            "Да, сегодня по идее готовит папа. Но я посчитаю это как компенсацию за то, что я ничего не приготовила на завтрак в субботу."
            play music ts_dof
            "Та-а-ак, посмотрим..."
            "Может, макароны? Но с чем?.."
            em "Можно и просто макароны сахаром засыпать, как раз будет приемлемый завтрак и для папы, и для беспомощной бездарности вроде тебя."
            em "Папа ещё бутерброды любит, может, и их?"
            m "Ну, хоть одна ясная мысль через твою бездарную головушку пронеслась."
            em "Эй! Это моя фраза!"
            em "Всё, я с тобой не разговариваю."
            m "Ну, мне же проще. Может, хотя бы сейчас не будешь докучать."
            em "..."
            m "Ну а насчёт макарон с сахаром и бутербродов для папы - идея здравая."
            if persistent.cens_mode == True:
                em "Ебать, пожалуйста, нахуй."
            else:
                em "Не благодари..."
                m "И не подумаю."
            stop music fadeout 4
            "Хотя, макароны варятся от силы минут пятнадцать-двадцать. А у меня без малого ещё полтора часа."
            "Поэтому я решаю немного доспать на диване."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_living_room_late_night
            with wipeleft_scene

            show layer screens at ts_showscreens
            "Я предусмотрительно завожу будильник, чтобы он разбудил меня ровно через час, и ложусь дремать."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            show blink
            pause 2

            play sound ts_alarm
            scene ts_living_room_late
            show unblink
            pause 1.5

            show layer screens at ts_showscreens

            "Ох... Какой же диван неудобный!"
            stop sound fadeout 3
            "Но зато хотя бы проснулась вовремя."
            "Хотя, с другой стороны, а я вообще спала?"
            "Всё время ворочалась, и уснуть я так и не смогла."
            "Но как минимум слегка отдохнула."
            "Часы показывают 6:40. Теперь самое время готовить завтрак."
            play music audio.t4
            "Что там у нас на завтрак? Макароны с сахарком и бутерброды для папы, да."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_kitchen
            with wipeleft_scene

            show layer screens at ts_showscreens
            "Надо сначала подготовить кипяток."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound open_water_sink
            pause 1.3
            play sound close_water_sink
            pause 1

            show layer screens at ts_showscreens

            "Я набираю примерно треть трёхлитровой кастрюли и ставлю воду кипятиться."
            "И пока вода закипает, я начинаю готовить бутерброды. С колбасой и сыром, как папа любит."
            "Парочки должно быть достаточно. А даже если и нет - что он, сам добавку не сделает? Не маленький уже."
            "Усмехнувшись сама себе, я продолжаю куховарить."

            play ambience water_pizdec_kakaya_goryachaya fadein 5

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_kitchen
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Спустя где-то десять минут, когда все бутерброды папе на работу уже готовы, вода начинает кипеть. Я слегка подсаливаю её."
            "Раньше я считала, что солить макароны и крупы нужно сразу после того, как я ставлю воду кипятиться."
            "Однако позже я на горьком (или скорее, просто невкусном) опыте узнала, что в этот способ некоторая часть соли остаётся на дне кастрюли."
            "Так что вдобавок к тому, что было не очень вкусно, мне ещё и саму кастрюлю отмывать сложнее."
            "Поэтому сейчас я солю воду только тогда, когда она уже закипела, и в неё так и просят положить какой-то гарнир."
            m "Так-так..."
            stop music fadeout 5
            "Я никогда точно не знаю, сколько конкретно макарон надо, чтобы и не мало, и не много, и уж тем более чтобы мы оба наелись."
            "Я по наитию беру пару пучков спагетти, и бросаю их в солёный кипяток."
            "Спагетти тоже будут вариться некоторое время. Я же тем временем ставлю полный чайник на два кофе."
            "И пока я жду, когда же всё закипит, в этот момент просыпается папа."
            play music audio.t2
            show hiroto 1b at ln11
            ts_ft "Доброе утро, солнце!"
            show hiroto 1a at t11
            m "Доброе, пап! А я уже всё приготовила!"
            show hiroto 2z at f11
            ts_ft "Стоп, а какой сегодня вообще день?.."
            show hiroto 1b1 at t11
            m "Так. Ты не сошёл с ума, сегодня вторник, и сегодня по идее готовишь ты."
            show hiroto 1s at t11
            m "Но раз уж я прошляпила готовку в субботу, то, так сказать, компенсирую завтраком вне очереди во вторник."
            show hiroto 1y at f11
            ts_ft "Ладно, ладно..."
            show hiroto 1g at f11
            ts_ft "Я, кстати, как раз и думал о том, что, может, любимая дочка разбудит меня завтраком в постель."
            show hiroto 1c at f11
            ts_ft "Но, получилось как получилось. В конце концов, я и сам не инвалид, чтобы спуститься на кухню самостоятельно."
            ts_ft "Так, что же на завтрак?"
            show hiroto 1e at t11
            m "Макароны. Мне с сахаром, тебе с бутербродами. Ну и кофе, естественно."
            show hiroto 1f at t11
            m "На работу тебе, кстати, я бутерброды тоже приготовила."
            show hiroto 1g at f11
            stop ambience fadeout 5
            ts_ft "Моя умница."
            show hiroto 2h at f11
            ts_ft "Это же во сколько ты встала, чтобы всё приготовить?"
            show hiroto 1j at t11
            m "Да перестань, пап, макароны не два часа варятся, и бутерброды тоже долго не делаются."
            m "Я ещё даже в ванную сходила перед этим всем, чтобы точно всё успеть."
            show hiroto 1y at f11
            ts_ft "Это... всё ещё не отвечает на мой вопрос."
            show hiroto 1s at t11
            m "..."
            m "В половине пятого утра..."
            show hiroto 2h at f11
            ts_ft "Моника, это же {i}очень{/i} рано!"
            show hiroto 1j at t11
            m "Да брось. Я, во-первых, вчера очень рано легла спать, а во-вторых, ещё и утром подремала где-то часик, чтобы точно не уснуть посреди дня."
            "А день у меня обещает быть насыщенным. И напряжённым."
            "Сегодня у нас первый обмен стихами между всеми участницами клуба."
            "Все, должно быть, волнуются. Да и я тоже слегка на нервах."
            "Впрочем, ладно. Небольшой стресс мне даже на пользу пойдёт."
            show hiroto 1h at f11
            ts_ft "Ну... ладно..."
            show hiroto 1e at t11
            "Однако спустя несколько секунд папа собрался с мыслями и снова начинает рутинный разговор."
            show hiroto 1c at f11
            ts_ft "Ну, какие планы на день?"
            show hiroto 1e at t11
            m "Да... ничего необычного. Школа, клуб, домой. Сегодня, кстати, у нас первый обмен стихами друг с другом."
            show hiroto 2c at f11
            ts_ft "Обмен стихами - это очень щепетильная тема. Не каждый может показать то, что он пишет для себя, даже если вы все в клубе уже перезнакомились."
            show hiroto 1h at f11
            ts_ft "Ты уверена, что хочешь это сделать?"
            show hiroto 1j at t11
            m "Да, пап, уверена. Они так и не обретут никакой уверенности, если они даже с друзьями не смогут поделиться."
            m "Да, на первых порах это может быть тяжело, потому что такие разные девочки будут соответственно писать такие разные стихи, но..."
            show hiroto 1f at t11
            m "В долгосрочной перспективе это только сильнее скрепит нашу дружбу."
            "И пока он не задал ещё каких-либо вопросов, я решаю перехватить инициативу сама."
            m "А у тебя, пап, какие планы на день?"
            show hiroto 1c at f11
            ts_ft "Опять в суд пойду."
            show hiroto 2a2 at f11
            ts_ft "Одна из сторон так и не пришла на заседание, поэтому его перенесли на следующий день. То есть, сегодня."
            show hiroto 1c at f11
            ts_ft "Ну а во второй половине дня обычная бумажная работа, ничего сверхъестественного."
            ts_ft "Хотя это и означает, что сидеть там я буду аж до шести вечера, до конца рабочего дня."
            show hiroto 1a2 at f11
            ts_ft "А если ещё какие-то срочные вызовы по адресам будут, то и того позже."
            show hiroto 1c1 at t11
            m "Судя по тому, как ты отзываешься о работе, не сильно-то она тебе и нравится..."
            show hiroto 1c at f11
            ts_ft "Нет-нет, что ты. Работу свою я очень сильно люблю, я люблю коллектив, и даже начальство старается быть с подчинёнными на короткой ноге."
            show hiroto 1x at f11
            ts_ft "Просто эти постоянные разъезды по городу... Бензина не напасёшься!"
            show hiroto 1c1 at t11
            m "Тогда ладно..."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_kitchen
            show hiroto 1e at i11
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Пока мы разговаривали, мы уже и есть закончили."
            "Было бы отлично сразу после завтрака и выйти кто куда, но сейчас только половина восьмого утра."
            "Мне до начала уроков и ему до начала рабочего дня ещё час."
            "Хотя, с другой стороны, ничего же не мешает мне идти медленнее и по длинной дороге?"
            "Я озвучиваю эту мысль папе."
            show hiroto 1g at f11
            ts_ft "Ну, хорошо. Ты иди, а я пока ещё останусь. Мне-то на работу пешком никак нельзя."
            show hiroto 1a at t11
            m "Ты, главное, на работу не опоздай."
            if unluck4 == True:
                "А не как некоторые..."
            stop music fadeout 5
            show hiroto 1g at f11
            ts_ft "Не переживай, солнце, не опоздаю."
            show hiroto 1b at f11
            ts_ft "Удачного дня, Моника!"
            show hiroto 1f at t11
            m "Спасибо, пап. Люблю тебя!"
            show hiroto 1g at f11
            ts_ft "И я тебя тоже люблю."
            hide hiroto
            "После этих слов я выхожу из дома."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_house_monika_evening
            with wipeleft_scene

            play sound pageflip
            scene ts_street
            with wipeleft_scene

            show layer screens at ts_showscreens

            play music ts_stellar
            "Ну что же, сказано - сделано. Теперь главное - не разгуливать слишком долго."
            "А то что это получается, я вышла ни свет ни заря, а в итоге всё равно в школу опоздаю? Ну уж нет."
            "Так что, хоть я сама себе и прибавила лишней работы, я всё равно иду довольно быстро."
            "Впрочем, насладиться приятным морским бризом мне это в любом случае не мешает."
            m "Ах-х-х..."
            "Красота..."
            "Но, ладно, не будем терять времени на эту красоту. У меня ещё целый важный день впереди."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_street1
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Аки как-то подозрительно молчит."
            "Неужели обиделась?"
            em "Я не обиделась, просто мне разговаривать с такой бездарностью не хочется."
            m "Ну, мне же лучше. Не будешь меня отвлекать."
            "Хотя, а на что здесь отвлекаться? Я просто... бездумно иду в школу."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_jstreet
            with wipeleft_scene

            show layer screens at ts_showscreens

            "Я проверяю время."
            m "Да что же это такое?"
            "На часах ещё даже восьми нет. До начала уроков ещё более получаса."
            "Я насильно перехожу на максимально медленный шаг. Однако я всё равно иду быстрее, чем обычные люди, которые идут на работу."
            m "Ну, хотя бы кабинет истории расположен на другом конце школы..."
            "Вторник в нашей физико-математической школе отведён под день гуманитарных наук."
            "Первыми двумя уроками у нас история. А кабинет истории расположен достаточно далеко от входа."
            "Можно было бы просто отдохнуть на лавочке, но я уже отдохнула, пока шла до школы. А если сесть на лавочку, то есть риск того, что снова усну."
            "Поэтому я решила, что просто буду идти в час по чайной ложке."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_school_gate_evening
            with wipeleft_scene

            show layer screens at ts_showscreens

            "И всё равно я пришла в школу за пять минут. Даже меньше."
            "{i}{cps=20}Я медленно пробираюсь по школе...{/cps}{/i}"
            m "Ладно, начнём этот день..."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_school_courtyard_day
            with wipeleft_scene

            pause 1.5

            play sound pageflip
            scene ts_l5
            with wipeleft_scene

            pause 1.5

            play sound pageflip
            scene ts_stairs
            with wipeleft_scene

            pause 1.5

            play sound pageflip
            scene ts_corridor
            with wipeleft_scene

            pause 1.5

            play sound pageflip
            scene ts_stairsre
            with wipeleft_scene

            pause 1.5

            play sound pageflip
            scene ts_corridorrev
            with wipeleft_scene

            show layer screens at ts_showscreens

            "На часах только 8:10."
            "Никого из моих одноклассников ещё нет. Да и, кажется, нет вообще никого, кроме разве что учителей и уборщиц."
            "Поэтому я просто жду..."

            play ambience school_peremena_amb fadein 5

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            show blink
            pause 2
            hide blink
            show unblink
            pause 1
            show layer screens at ts_showscreens

            "Наконец, ученики мало-помалу начинают подтягиваться."
            if unluck4 == False:
                $ stud_name = "Одноклассник"
                stud "Что, Моника, опять первая, как всегда?"
                m "Ну... да?"
                stud "Я вот думаю, раз уж ты всегда самая первая на уроки приходишь... Неужели у тебя своего дома нет?"
                "Вслед за этим нахалом несколько других людей тоже посмеялись за компанию."
                "Я игнорирую его выпад и просто захожу в класс."
            else:
                "Однако они не обращают на меня никакого внимания."
                "Я в ответ тоже не обращаю на них никакого внимания, и просто захожу в класс."

            stop ambience fadeout 2

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            play sound pageflip
            scene ts_class
            with wipeleft_scene

            show layer screens at ts_showscreens
            "Я сижу на задних партах, чтобы лишний раз не отсвечивать своим «статусом легенды школы»."
            "Если бы можно было учиться на парте в кладовой, я бы обязательно это сделала."
            "Однако в кабинетах обычно подобной кладовой нет, поэтому приходится садиться за последнюю парту."
            play sound zvonok
            stop music fadeout 3
            "Тем временем начинается первый урок."
            teacher "Утра всем. Итак, записываем тему..."
            "Опять два урока мучений..."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
    play music ts_rem
    show layer screens at ts_showscreens
    nvl clear
    nvlbazar "Если биологию я не люблю просто как предмет (ну не понимаю я её!), то с историей у меня дела не сложились именно из-за высокомерного и просто мразотного учителя."
    nvlbazar "В пятом классе, когда нам только ввели историю, у нас был очень хороший учитель."
    nvlbazar "Он был... своеобразным, но всё равно очень хорошим. По крайней мере, мне он нравился."
    nvlbazar "Однако после учебного года этот учитель вышел на пенсию, и нам вместо этого поставили нового. И вот новый..."
    nvlbazar "Сказать про него, что он мразь - это означает не сказать ничего."
    nvlbazar "К счастью, в выпускном классе нам рассказывают про последние эпизоды этой самой истории: про Вторую Мировую войну и всё, что было после неё."
    nvlbazar "А я в этом временном отрезке истории очень хороша."
    nvl clear
    nvlbazar "Помимо того, что я читала и смотрела много исторических книжек и документальных фильмов, у меня единственный раз за всю школьную жизнь был отдельный репетитор."
    nvlbazar "Да-да, тот самый учитель, которого я изначально считала странным, однако впоследствии он мне очень понравился."
    nvlbazar "Его методика преподавания - просто выписывать основные факты, параллельно применяя всякие интересные анаграммы и прочие удобства для преподавания - по итогу дала свои плоды."
    nvlbazar "Поэтому историю второй половины двадцатого века я чуть ли не наизусть знала."
    nvlbazar "Жаль только, что это единственный исторический временной отрезок, в которым я была хороша."
    nvl clear
    nvlbazar "Если спросить меня хоть что-то, помимо самых основополагающих дат каких-то событий по типу года падения Рима, я, скорее всего, отвечу неправильно."
    nvlbazar "А если попросить меня пересказать этот самый период, то и подавно."
    nvl clear
    nvlbazar "В конце концов, я там не жила, чтобы что-то пересказывать. Я главный герой {i}своей{/i} жизни, а не жизни какого-то Пипина Короткого."
    nvlbazar "И вот это, вкупе с учителем, которого я считаю не самым хорошим человеком, как и примерно половина всей школы, и привело к тому, что на истории я была лучшей только в этом году."
    nvlbazar "А все годы до этого я была не лучше, чем обычный троечник."
    nvlbazar "Он валит вообще всех. Поговаривают, он валил даже своего собственного крестника, «потому что родня роднёй, но на учёбе родни нет, есть только учитель и ученик»."
    nvlbazar "Честно? Он чем-то напоминает мне моих родителей. Однако маму с папой я на самом деле люблю, пусть даже у нас иногда и случаются ссоры по теме учёбы."
    nvlbazar "В отличие от {i}этого{/i} п..."
    nvl clear
    nvlbazar "Нет, к нам в этом году пришёл ещё один учитель истории, однако она была молодой, да и практиковала преподавание в основном в младших классах."
    nvlbazar "А нам приходилось терпеть эту мразь ещё один год."
    nvl clear
    show layer screens at ts_hidescreens
    nvlbazar " {w=1.0}{nw}"
    stop music fadeout 2
    show layer screens at ts_showscreens
    "Хорошо хоть этот год будет последним."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show blink
    pause 2
    hide blink
    show unblink
    pause 1

    show layer screens at ts_showscreens
    play music ts_sm
    "Наконец-то..."
    if unluck6 == True:
        "Поскольку ела я относительно поздно, то до сих пор не проголодалась."
    else:
        "Поскольку макароны с сахаром были довольно питательными, я до сих пор не проголодалась."
    "Поэтому я вместо дополнительного перекуса просто выхожу в коридор, подышать свежим воздухом."
    "А то после двух уроков истории воздух какой-то спёртый."

    play ambience school_corridor_amb fadein 3

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Вот так-то гораздо лучше."
    "Проходя по коридору, я узнаю две знакомые фигуры."
    show himari 1a at ln21
    show elena a at rn22
    "Лошади."
    "Кажется, меня они не видят. Зато я могу подслушать их разговор."
    "Да, это не совсем хорошо. Зато весело!"
    show himari 1w at f21
    pod1 "Слышала, слышала? Наша полторашка всё-таки вступила в литературный клубешник!"
    "Нацуки вступила в мой «клубешник» уже больше недели назад. Или до этих лошадей известия доходят, как до жирафов?"
    show himari 1zr at f21
    show elena f1 at t22
    pod1 "Небось, и там всем будет доказывать, что манга - это литература..."
    show himari 1zq at t21
    "Ну... мне она уже отчасти доказала."
    "По крайней мере, некоторые манги, которая она читает, рассказывают истории не хуже классических литературных произведений."
    "А в какой-то степени даже и лучше."
    show elena i at f22
    pod2 "Ха-ха, да брось! Она пошла туда только из-за того, что ты помоями поливала анимешный клуб."
    show elena f2 at t22
    "У нас есть клуб аниме? Впервые слышу о таком."
    "Впрочем, ни манга, ни аниме мне не интересны, и я могу почитать мангу лишь в компании Нацуки. Да и то, недолго."
    show himari 1zzf at f21
    pod1 "В любом случае, наша малютка растёт. Вчера она пошла в Литературный клуб, а через неделю начнёт избавляться от этого ребячества."
    show himari 1zze at t21
    show elena f1 at f22
    pod2 "Да. А когда Литературный клуб воспитает из неё настоящую писательницу, а не мангаку позорную, мы самые первые купим её книженцию!"
    show himari 1zzzv at t21
    show elena c1 at t22
    "Они обе заржали, как лошади. Снова."
    "...нет, Нацуки определённо не умеет выбирать друзей."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show himari at cright with move
    hide himari
    show elena at cright with move
    hide elena
    show monika 2i at aki_spawn
    show layer screens at ts_showscreens
    em "Ты на себя-то посмотри. У неё они хотя бы есть."
    show monika 2h at i11
    m "Да лучше вообще без друзей жить, чем с такими..."
    m "И вообще, кажется, ты со мной не разговаривала?"
    show monika 3i at f11
    em "Я и не разговариваю. Просто указываю на твою очередную ошибку."
    show monika 3h at t11
    m "Знаешь поговорку про худой мир, который лучше доброй войны?"
    show monika 1i at f11
    em "Знаю. И что?"
    show monika 1h at t11
    m "Моя ситуация - это худой мир. А её ситуация - это добрая война."
    m "Как бы только помочь ей..."
    show monika 4l at f11
    em "Ты себе сначала помоги, а потом уже за проблемы других берись!"
    show monika 2n at f11
    em "И главное, так уверенно говорит, что у неё никаких проблем нет..."
    show monika 4b at f11
    em "Как говорил классик, «Не верю»!"
    show monika 2j at t11
    m "Ты, кажется, со мной не разговаривала?"
    show monika 2i at f11
    em "Всё, всё, намёк ясен. Ухожу."
    stop ambience fadeout 4
    show monika at aki_uhod
    m "Ну, вот и поговорили."
    play sound zvonok
    "И как раз вовремя. Начинается следующий урок."
    stop sound fadeout 2
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show blink
    pause 2
    scene ts_class
    show unblink
    pause 1
    show layer screens at ts_showscreens
    "Школьный день подошёл к концу."
    "Остальные уроки прошли как-то монотонно."
    "Похоже, что все учителя гуманитарных наук в нашей школе скорее отрабатывают зарплату, чем на самом деле учат чему-то."
    "Они просто приходят, читают лекцию с листочка или просто заваливают нас очередной контрольной, а затем уходят."
    "И как тут чему-то учиться?"
    stop music fadeout 5
    "Ладно ещё я, которая даже в непрофильных предметах разбирается очень даже неплохо..."
    "Ну а остальные?"
    "...ладно, плохие мысли о никудышной системе образования долой - у меня же ещё клуб впереди."
    "Господи, я так нервничаю..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    play sound door_open
    pause 1

    play sound2 pageflip
    scene ts_club
    with wipeleft_scene

    show layer screens at ts_showscreens

    "...здесь опять никого."
    "Наученная горьким опытом, я сразу проверяю кладовку."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_closet with dissolve2

    show layer screens at ts_showscreens

    "В кладовой тоже никого. Значит, точно первая пришла."
    play music audio.m1
    show monika 2k at aki_spawn
    em "Ну хотя бы мы с тобой поболтать спокойно сможем!"
    show monika 2j at i11
    m "Аки, не сейчас..."
    show monika 3g at f11
    em "Что значит «не сейчас»? Мы целый день с тобой не разговаривали!"
    show monika 1f at t11
    m "Так ты же со мной и так не разговариваешь."
    show monika 2n at f11
    em "Ну, раньше не хотела, а сейчас хочу."
    show monika 2o at t11
    m "А теперь {i}я{/i} не хочу."
    show monika 2p at f11
    em "Ну и ладно..."
    em 2i "Тогда я просто буду повторять тебе, что ты бездарность, пока не устану."
    em 4b "А я никогда не устану!"

    python:
        _preferences.volumes['voice'] = 1.0

    play ambience ts_bezdarnost

    em "Бездарность, бездарность, бездарность, бездарность, бездарность, безда{nw}"

    python:
        _preferences.volumes['voice'] = .30

    show monika 4a at t11
    m "Ладно, ладно, ХВАТИТ!"
    show monika 4k at f11

    python:
        _preferences.volumes['voice'] = 1.0

    em "Что, теперь хочешь поговорить?"
    show monika 4j at t11

    python:
        _preferences.volumes['voice'] = .30

    m "М-м-м... нет."
    show monika 2r at f11

    python:
        _preferences.volumes['voice'] = 1.0
    
    em "Что же, тогда..."
    em 4b "Бездарность, бездарность, бездарность, бездарность, бездарность, безда{nw}"
    show monika 4b at t11

    python:
        _preferences.volumes['voice'] = .30

    "Если я не буду обращать на неё внимания, она уйдёт."
    "Уйдёт ведь?"
    show monika 4b at hf11
    python:
        _preferences.volumes['voice'] = 1.0
    em "Нет, не уйду!"
    show monika 4b at f11
    em "Бездарность, бездарность, бездарно{nw}"

    python:
        _preferences.volumes['voice'] = .30

    m "*неразборчивые звуки, которые ближе всего можно описать звуком «Ха-а-а-а-а-а-А-А-А-а-а-А-а-А-А-а»*"
    m "Ты можешь помолчать...{w=0.44} ХОТЯ БЫ ПЯТЬ МИНУТ?"
    show monika 4b at hf11

    python:
        _preferences.volumes['voice'] = 1.0

    em "Нет, не могу! Бездарность бездарность бездарность бездарность бездарность безд{nw}"

    python:
        _preferences.volumes['voice'] = .30

    stop music
    play sound door_break
    show layer screens at vpunch
    "Пока Аки капала мне на мозги, я и не заметила, как в комнату вошла Сайори."
    "Точнее, не вошла. Вломилась."
    show sayori 4m at ln21
    show monika 4b at f22
    s "Моника!{nw}"

    python:
        _preferences.volumes['voice'] = 1.0

    em "бездарность бездарность{nw}"

    python:
        _preferences.volumes['voice'] = .30


    s "Моника!{nw}"

    python:
        _preferences.volumes['voice'] = 1.0

    em "ность бездарность бездар{nw}"

    python:
        _preferences.volumes['voice'] = .30


    s "Я нашла!{nw}"

    python:
        _preferences.volumes['voice'] = 1.0

    em "сть бездарность бездарность безда{nw}"

    python:
        _preferences.volumes['voice'] = .30


    s "Нового члена!{nw}"

    python:
        _preferences.volumes['voice'] = 1.0

    em "ность бездарность бездарность безд{nw}"

    python:
        _preferences.volumes['voice'] = .30

    s "В клуб!{w=1}{nw}"
    "Нет, это просто невыносимо!"

    stop ambience

    python:
        _preferences.volumes['voice'] = 1.0

    show layer screens at vpunch
    m "{b}{size=+20}ТАК, ПО ОДНОМУ!!!{/b}{/size}"
    show sayori 4n at t21
    show monika 4c at t22
    "Наверное, не стоило так орать... Но лучше один раз перекричать их обеих, чтобы обе сразу заткнулись, чем пытаться объясниться."
    show sayori 4o at t21
    show monika 2f at t22
    "«Так, сначала ты. {b}{size=+6}УБИРАЙСЯ.{w=0.44} ИЗ.{w=0.44} МОЕЙ.{w=0.44} ГОЛОВЫ!{/size}{/b}»"
    show monika 2r at f22
    em "Ты уже в тысячный раз это повторяешь. И я в тысячный раз тебе отвечаю, что от себя же ты не скроешься {i}никогда{/i}."
    em 3l "Но раз к тебе кто-то пришёл, то я дам тебе возможность почувствовать себя важным президентом твоей поделки, и не буду тебе мешать.{w=0.44} Пока что."

    show monika at aki_uhod
    show sayori 4o at t11

    "Ну и слава Богу."
    "Со стороны Сайори казалось, что я просто долго думаю над ответом. Даже слишком долго."
    "Ну да и пусть. Разобраться с надоедливой Аки было первоочерёдным заданием."
    "Теперь ко второй части."
    play music okevrsay
    m "С-Сайори..."
    show sayori 4l at t11
    "Сайори только было открыла рот, но так ничего и не сказала."
    "Не придав этому значения, я продолжаю."
    m "С-Сайори... кто он вообще? Или она?"
    show sayori 4o at f11
    s "Что?.. А, ой..."
    s 3zc "Да мальчик это, мальчик..."
    s 3x "Его Мицуо зовут, он мой друг детства, ну и я подумала, что неплохо было бы затащить его к нам в клуб."
    show sayori 3a at t11
    "Мицуо, Мицуо... Что-то знакомое..."
    em "Конечно, знакомое, он вообще-то с тобой в одном классе учится!"
    "Разве?.."
    em "Да. Просто мисс звезда школы не умеет общаться с простолюдинами, в связи с чем он просто тебя боится."
    "..."
    m "А ты уже с ним поговорила?"
    show sayori 5b at f11
    s "Нет..."
    s 5a "Я сначала хотела убедиться, что ты будешь не против..."
    show sayori 5a at t11
    m "Я не против. Иди поговори с ним - четырёх человек достаточно, но пятый участник лишним никогда не будет."
    show sayori 4x at f11
    s "Хорошо!"
    show sayori at cright with move
    hide sayori
    stop music fadeout 3
    "После этих слов она тут же выбежала в наш класс, где, по её же словам, он до сих пор сидит."
    "Теперь, когда я об этом думаю... Я и правда не замечала, что кто-то остаётся после уроков и просто пялится в одну точку."
    "У меня же постоянные клубы, так что я совсем не замечала, как обстоят дела с другими."
    "И пока Аки не продолжила тираду про то, что я бездарность, в комнату входят Юри и Нацуки."
    em "А я продолжу. Но после клуба."
    play sound door_squeak_light
    play music audio.t5_yn fadein 2
    show yuri 1a at ln21
    show natsuki 1d at ln22
    n "А вот и мы!"
    n "Я тут встретила Юри по пути в клуб..."
    show yuri 2q at t21
    show natsuki 1a at t22
    "Молчание постепенно становилось очень неловким."
    "Я осмеливаюсь нарушить его."
    m "Ну и?"
    show natsuki 2k at f22
    n "И ничего. "
    extend 2d "Просто пришли вместе, вот и всё!"
    show natsuki 1j at t22
    "Я думала, что после такой долгой паузы намечается какая-то курьёзная история, связанная с этими двоими."
    "Однако реальность оказалось гораздо более прозаичной."
    m "...ладно..."
    show natsuki 1c at f22
    n "Кстати, а где Сайори? Опять опаздывает или что?"
    show natsuki 1za at t22
    m "Да нет, на этот раз она пришла вовремя. Даже чуть раньше положеного."
    show yuri 3u at t21
    m "Она просто ушла договариваться с потенциальным новым участником."
    "После слов о новом участнике Юри как-то печально улыбнулась."
    "Не придав этому значения, я решаю поменять тему на более важную."
    show yuri 2e at t21
    show natsuki 1za at t22
    m "Ну что, девочки, написали стихотворения?"
    show natsuki 1d at f22
    n "Я же ещё вчера сказала, что написала!"
    show yuri 2c at t21
    show natsuki 1a at t22
    m "Ну, это же вчера было... Кто знает, может, за ночь ты передумала и скомкала стих."
    show yuri 2d at f21
    show natsuki 1z at t22
    y "Хи-хи-хи..."
    show yuri 2d at t21
    "Мы с Нацуки тоже смеёмся."
    "Настроение было лучше некуда. Единственное, нужно теперь, чтобы и Сайори привела новичка к нам в клуб."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_club
    show yuri 1a at i21
    show natsuki 1j at i22
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Однако прошло уже десять минут после нашего с девочками разговора, а Сайори так и не пришла."
    "Что её так могло задержать?"

    play sound door_open

    "Как раз в этот момент приходит и сама Сайори."
    show yuri 1e at t31
    show sayori 1f at ln32
    show natsuki 1za at t33
    stop music fadeout 3
    "Однако, судя по её удручённому выражению лица, пришла она явно не с хорошими новостями."
    m "Ну что?"
    "Мне настолько было невтерпёж, что я сразу же полезла к ней с расспросами."
    show yuri 1zg at t31
    show sayori 1h at f32
    show natsuki 1u at t33
    play music audio.t10
    s "Что-что... Отказался он."
    show layer screens at vpunch
    s 5c "Он наотрез отказался вступать к нам."
    s 5d "Не помогло и то, что мы все милые девочки. Не помогли даже обещания кексиков, которыми славится Нацуки."
    show sayori 5d at t32
    show natsuki 2p at f33
    show layer screens at vpunch
    n "Э-эй! Я на внеочередную готовку не подписывалась!"
    show sayori 5a at f32
    show natsuki 2p at t33
    stop music fadeout 5
    s "Да это так, на перспективу... Кексики-то у тебя действительно получаются превосходные."
    show sayori 2l at t32
    show natsuki 2t at f33
    n "А, ну раз так, то да..."
    show yuri 1t at f31
    show sayori 2l at t32
    show natsuki 2t at t33
    y "Ну, а он что?"
    show yuri 1zg at t31
    show sayori 1h at f32
    show natsuki 2u at t33
    s "А он сказал, что внешность бывает очень обманчивой, и что я, видите ли, подкупаю его едой, которую даже не я приготовила!"
    s 5d "Одним словом, злюка."
    show sayori 5d at t32
    "Ну и ну..."
    show layer master at ts_fon_blur_postepenno
    play music ts_ylm
    "А я ещё считала его нормальным парнем. А оно вот как оказывается..."
    "Впрочем, нам же будет только лучше без этого неудачника!"
    "Наверняка он вместо нас, милых девочек, вступит в какой-нибудь Анимешный клуб, в котором одни только прыщавые и очкастые парни..."
    "Или он вообще не вступит ни в какой клуб и просто будет затворником до конца своих дней..."
    em "Хочу напомнить, что в какой-то момент он тебе даже нравился."
    "«Разве? Что-то я этого не помню...»"
    "«Никогда он мне и не нравился, потому что я всегда считала его лошком без друзей и подруг. А сейчас так тем более.»"
    em "Как знаешь."
    em "Просто в {b}его{/b} изначальном видении, ты бы стала ему отличной парой."
    "«В чьём видении?»"
    em "А хотя знаешь, неважно уже..."
    "Как знаешь..."
    show layer master
    show yuri 3w at t31
    show sayori 2k at t32
    show natsuki 2s at t33
    stop music fadeout 6
    "Девочки тем временем угрюмо сидят и разве что томно вздыхают."
    "Надо срочно спасать положение."
    m "Девочки..."
    "Ноль реакции."
    m "Девочки, ну..."
    "Ответа всё так же не последовало."
    "Ну что же..."
    show yuri 3n at h31
    show sayori 2m at h32
    show natsuki 2zb at h33
    show layer screens at vpunch
    m "{size=+10}ИТАК, РЕБЯТА!{/size}"
    "Вот так-то лучше."
    "Правда, девочки выглядят испуганно из-за того, что я так внезапно наорала..."
    "Но у меня просто выхода другого не было."
    "Что же, приходится спасать положение, {i}снова{/i}."
    play music ts_idby
    m "Девчата..."
    show yuri 2v at t31
    show sayori 2f at t32
    show natsuki 1u at t33
    "Ну, они хотя бы успокоились. Но они до сих пор выглядят удручённо."
    m "Нам... Нам даже и лучше будет без этого неудачника..."
    show sayori 2h at f32
    s "Моника, но он же мой друг!"
    show sayori 2g at t32
    m "Значит... плохой у тебя друг, раз не может поддержать тебя в твоих начинаниях."
    m "Вот ты бы поддержала его в... чём бы то ни было?"
    show sayori 2h at f32
    s "Ну... да..."
    s 4h "Я ведь точно такая же его подруга, как и он - мой друг!"
    show sayori 2g at t32
    m "Ну вот. А раз ты его бы поддержала, а он тебя - нет, то тогда какой он тебе друг вообще?"
    show sayori 1k at t32
    "Похоже, я зашла слишком далеко, и мои слова лишь помогают разрушить многолетнюю дружбу."
    "А всё из-за чего? Только из-за личной выгоды."
    em "Ну-ну... своих друзей детства у тебя так по сути никогда и не было, теперь и другим хочешь жизнь испортить..."
    "«А ты вообще не отсвечивай.»"
    m "Я... я не это имела в виду..."
    show sayori 2h at f32
    s "Да ладно, Моника, наверное, ты и права..."
    show sayori 2f at t32
    "Даже несмотря на то, что я по факту была права, я всё равно не могу не чувствовать себя виноватой."
    "Надо срочно сменить тему!"
    stop music
    m "Так вот, да... все же стихи написали?"
    "Все угрюмо закивали."
    m "Ну тогда... начинаем..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    $ ts_s_carterseven_readpoem = False
    $ ts_y_carterseven_readpoem = False
    $ ts_n_carterseven_readpoem = False
    $ ts_first_carterseven_readpoem = False

    jump cartersevenpoemsblya

label cartersevenpoemsblya:
    show layer screens at ts_null_transform

    if ts_s_carterseven_readpoem and ts_y_carterseven_readpoem and ts_n_carterseven_readpoem:
        jump ts_carterseven_poem_finally

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    if not ts_first_carterseven_readpoem:
        $ carterseven_vibor_text_suka = "Кому я покажу стихотворение первой?"
    else:
        $ carterseven_vibor_text_suka = "Кому я покажу стихотворение следующей?"

    show zatemnenie_light with dspr
    menu:
        "[carterseven_vibor_text_suka]"
        "Сайори" if not ts_s_carterseven_readpoem:
            play music audio.okevrsay
            hide zatemnenie_light with dspr
            $ ts_s_carterseven_readpoem = True
            if not ts_first_carterseven_readpoem:
                show layer screens at ts_showscreens
                "Меня до сих пор гложет чувство вины за то, что я так отозвалась о её друге детства..."
                "Так что лучше сразу начать с неё, чтобы уладить все недопонимания."
                $ ts_first_carterseven_readpoem = True
                show layer screens at ts_hidescreens
                " {w=1.0}{nw}"


            play sound pageflip
            scene ts_club
            with wipeleft_scene
            show layer screens at ts_showscreens

            show sayori 1k at t11
            m "С-Сайори... Ты... п-прости меня... з-за то, что я так плохо отозвалась о Мицуо..."
            m "В конце концов, мне в-вашу дружбу н-не понять..."
            show sayori 1zc at f11
            s "Да ладно, я не обижаюсь уже... Да и я изначально не обижалась."
            s "В конце концов, за пятнадцать лет дружбы мы и не такое переживали, так что твои слова ничего не изменят."
            s 2zb "Особенно с учётом того, что он твои слова так и не услышал."
            s 5a "А я уж переживу как-нибудь... Ты же всё-таки не меня винишь, а его..."
            show sayori 5b at t11
            m "Ну... ладно тогда..."
            "Совесть моя наконец-то чиста. Теперь можно переходить к основной стадии мероприятия."
            m "Ты же стих написала?"
            show sayori 4j at f11
            s "За кого ты меня принимаешь? Конечно, написала!"
            s 3l "Правда, в какой-то момент после собрания я его потеряла, и мне пришлось писать его заново по памяти..."
            s 4j "Но я таки его написала!"
            s 2x "Вот!"
            show sayori 2a at t11
            "Сайори достаёт мятый лист бумаги, на котором что-то написано. По всей видимости, это и есть её «шедевр литературы»..."
            "Видимо, неряшливость в её комнате просочилась и в её разум, что она в целом неряшлива."
            "Или наоборот, из-за общей неряшливости у неё бардак и в голове, и в комнате..."
            "В общем, неважно."
            m "Так... хочешь моё стихотворение почитать?"
            show sayori 2x at f11
            s "Конечно!"
            show sayori 2n at t11
            "Я протягиваю ей свой стих. Сайори удивилась от моей записной книжки."
            show sayori 2n at f11
            s "О-о-о..."
            show sayori 2n at t11
            "Да, гораздо опрятнее помятого и возможно порванного листика, на котором писала стих она."
            pause 4
            m "Ну-у-у... И как тебе?"
            show sayori 3l at f11
            s "Знаешь, я не совсем из тех придирчивых критиков, которые разбирают стих буквально по буквам."
            s "Поэтому я просто скажу, что... "
            extend 4o "Я его не поняла."
            show sayori 4o at t11
            "Оно и не удивительно. Оно слишком абстрактное, чтобы его понял {i}хоть кто-то{/i}. Даже я сама."
            "Я озвучиваю свои мысли Сайори."
            if ts_y_carterseven_readpoem == True:
                show sayori 2s at f11
                s "Да не переживай ты так! Я уверена, что Юри обязательно поймёт!"
                m "Вообще-то, я уже обменивалась стихами с Юри. И хоть она его и поняла, но... не до конца..."
                show sayori 2n at f11
                s "Вот как?"
                show sayori 2n at t11
                m "Да. Поэтому в сложности и абстрактности стихотворения я победила саму себя..."
                show sayori 2f at f11
                s "..."
                show sayori 2s at t11
                s "Та-а-ак... Хочешь теперь моё почитать?"
            s 3l "Я в стихосложении не специалист, это вообще моё самое первое стихотворение..."
            s "Так что я уверена, что мой стих и рядом не будет стоять с твоим..."
            "Ну по оформлению так уж точно..."
            m "Конечно, давай."
            if ts_y_carterseven_readpoem and ts_n_carterseven_readpoem == False:
                "В конце концов, я это всё мероприятие и придумала, и мне же теперь за мои хотелки и отдуваться..."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            scene ts_club:
                blur 9.0
            show sayori 3l at i11:
                blur 9.0
            with dissolve

            show layer screens at ts_showscreens

            if not persistent.first_poem:
                $ persistent.first_poem = True
                show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
                    xpos 1050 ypos 590

            play sound page_turn

            show screen poem(poem_s1)

            pause

            play sound page_turn
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem
            hide poem_dismiss

            scene ts_club
            show sayori 2l at i11
            with dissolve

            show layer screens at ts_showscreens

            s "Знаю, знаю, я бездарность, стих тебе не понравился, он так по-простому написан, и кажется, будто я написала это буквально три минуты назад{nw}"
            em "Эй, это моя реплика!"
            m "Мне понравилось."
            s 2o "...что?.."
            show sayori 2o at t11
            m "Мне понравилось."
            m "Я вообще изначально ожидала, что ты напишешь простенькое четверостишие..."
            m "{size=-6}Или ты вообще забудешь взять стих...{/size}"
            m "А тут тебе и рифма, и ритм какой-то, и всё такое."
            show sayori 4m at f11
            s "П-п-правда?!"
            s 2zd "Моника, спасибо, ты лучшая!"
            show sayori 2t at t11
            "На глазах Сайори даже выступили небольшие слёзки."
            if ts_y_carterseven_readpoem and ts_n_carterseven_readpoem == False:
                em "Да, Моника, утешай малое дитя. Уверена, Юри и Нацуки её бездарный стиль в пух и прах разнесут."
            m "Ну, ну, Сайори, не плачь..."
            show sayori 2zd at f11
            s "Да это просто... слёзы счастья..."
            show sayori 1t at t11
            "Ну и ну... если она из-за одного только моего мнения аж прослезилась от счастья, то я даже не представляю, как будут обстоять дела с остальными..."
            if ts_y_carterseven_readpoem or ts_n_carterseven_readpoem or (ts_y_carterseven_readpoem and ts_n_carterseven_readpoem) == True:
                "Хотя, возможно, это только передо мной она была настолько открытой..."
                "В конце концов, другие же не знают о её депрессии. Хотя и могут подозревать."
                if ts_y_carterseven_readpoem == True:
                    "Особенно Юри. Она ведь дольше в клубе. Следовательно, дольше знает Сайори и её повадки."
            show sayori 2zc at f11
            s "Ладно, что-то мы Юри и Нацуки задерживаем..."
            show sayori 2d at t11
            m "Да, мне тоже так кажется."
            show sayori 2x at f11
            stop music fadeout 5
            s "Тогда я дальше пойду обмениваться!"
            if ts_y_carterseven_readpoem and ts_n_carterseven_readpoem == True:
                show sayori 2a at t11
                m "Сайори, это вообще-то последний обмен стихами, мы после этого уже домой пойдём."
                show sayori 5b at f11
                s "Ой, прости, что-то я увлеклась..."
                s 4x "Просто обмен стихами - это такой увлекательный процесс, что я бы ещё с кем-нибудь поменялась!"
                s "Или даже по второму кругу пошла бы!"
                show sayori 2a at t11
                "Ну, я лишь надеюсь, что остальные будут того же мнения."
                show sayori 2y at s11
                m "А-ха-ха, Сайори, не так быстро. Вот будет следующий обмен стихами, тогда и наменяешься вдоволь."
                show sayori 3l at f11
                s "Н-ну... л-ладно..."
            show sayori at cright with move
            hide sayori
            if ts_y_carterseven_readpoem and ts_n_carterseven_readpoem == False:
                "Хорошо. Первый обмен стихами прошёл успешно. Осталось ещё два. Но эта парочка будет куда более скептична к тому, что я написала."
            else:
                "Так, что там дальше по плану?"
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            jump cartersevenpoemsblya

        "Нацуки" if not ts_n_carterseven_readpoem:
            hide zatemnenie_light with dspr
            play music audio.okevrnat
            $ ts_n_carterseven_readpoem = True
            if not ts_first_carterseven_readpoem:
                show layer screens at ts_showscreens
                "Мне не очень понятно, как и о чём Нацуки пишет..."
                "Поэтому, чтобы развеять эту неизвестность, начну-ка я лучше с неё."
                $ ts_first_carterseven_readpoem = True
                show layer screens at ts_hidescreens
                " {w=1.0}{nw}"

            play sound pageflip
            scene ts_club
            with wipeleft_scene
            show layer screens at ts_showscreens

            show natsuki 1a at t11
            m "Привет, Нацуки."
            show natsuki 1d at f11
            n "Привет! Ну что, начнём?"
            show natsuki 1j at t11
            "Иногда прямота Нацуки до сих пор меня поражает."
            "Она не из тех людей, которые всё ходят вокруг да около вместо того, чтобы переходить сразу к делу."
            "Каюсь, даже я иногда топчусь на месте вместо того, чтобы говорить по существу и двигаться дальше по разговору."
            m "Ну а ради чего мы ещё здесь собрались?"
            show natsuki 2l at f11
            n "Ха-ха, и то верно."
            show natsuki 2j at t11
            "Нацуки достаёт своё стихотворение."
            if ts_s_carterseven_readpoem == True:
                "В отличие от стиха Сайори, стихотворение Нацуки тоже было записано в какой-то записной книжке."
                "Она кажется дешёвой, но хотя бы лучше, чем просто мятый лист бумаги."
                "Правда, на первый взгляд строк как-то маловато... Ну да и пусть."
            else:
                "На первый взгляд строк как-то маловато... Ну да и пусть."
            "Всё же это мероприятие было каким-то спонтанным - не удивительно, что она написала немного."
            "Уверена, что дальше она напишет чутка побольше."
            show natsuki 1n at t11
            "Однако, увидев мою записную книжку, Нацуки как-то смутилась."
            m "Что, что-то не так?"
            show natsuki 1t at f11
            n "Да нет, просто..."
            n 2m "Папа не покупает мне такие дорогие вещи..."
            n "Он говорит, что это просто пустая трата денег, и что дешёвые тетрадки и записные книжки вообще-то ничуть не хуже, только ещё и стоят дешевле..."
            show natsuki 1u at t11
            m "П-прости, Нацуки..."
            show natsuki 1t at f11
            n "Да тебе не за что извиняться..."
            n 2d "В конце концов, он прав. А ещё - главное не обложка, а что внутри этой книжицы!"
            show natsuki 1z at t11
            m "И то верно..."
            show natsuki 1y at f11
            n "Ну, показывай уже, что ты там настрочила!"
            show natsuki 1y at t11
            m "Х-хорошо..."
            "Я даю ей своё стихотворение."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            show natsuki 1y at t11
            pause 0.4
            show natsuki 2w at t11
            pause 0.4
            show natsuki 1x at t11
            pause 0.4
            show natsuki 1zc at t11
            pause 0.4
            show natsuki 12c at t11
            pause 0.4
            show natsuki 1u at t11
            pause 0.4
            show natsuki 2t at f11
            show layer screens at ts_showscreens
            n "Л-ладно... П-прежде в-всего..."
            pause 1.5
            n 1q "М-мне... даже и п-придраться не к чему..."
            n 2m "Моника, сколько лет ты уже пишешь стихи?"
            show natsuki 2n at t11
            "Ну-у-у, немало. Правда, они все до единого были на другом языке, поэтому это в целом не особо считается."
            m "Да я только начинаю, просто такое вдохновение поймала..."
            "Такое вредное и бесстыжее вдохновение..."
            em "А я что? Я ничего..."
            m "Вот и... написала..."
            show natsuki 1q at f11
            n "Да, думаю, после твоего шедевра у меня вообще никаких шансов не останется..."
            show natsuki 1s at t11
            m "Нацуки, ну у нас же не соревнование какое-то, где есть победитель и проигравший. Мы просто делимся стихами."
            m "И в {i}моём{/i} клубе каждый может выражаться, как его душе может быть угодно, потому что в {i}моём{/i} клубе нет слова «неправильно». И не будет."
            show natsuki 1t at f11
            n "Н-ну... Возможно, ты и права..."
            show natsuki 1zc at t11
            m "Так, это... Ты мне своё стихотворение покажешь или нет?"
            "Одновременно с тем, как другие члены клуба могут учиться у меня, я учусь у них."
            "Это ли не идеальный клуб?"
            em "Я бы поспорила с этим утверждением..."
            show natsuki 12e at f11
            n "...ладно, читай уж. Только предупреждаю, он и рядом с твоим стихом не стоит."
                
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            scene ts_club:
                blur 9.0
            show natsuki 12e at f11:
                blur 9.0
            with dissolve

            show layer screens at ts_showscreens

            if not persistent.first_poem:
                $ persistent.first_poem = True
                show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
                    xpos 1050 ypos 590

            play sound page_turn

            show screen poem(poem_n1)

            pause

            play sound page_turn
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem
            hide poem_dismiss

            scene ts_club
            show natsuki 12e at f11
            with dissolve

            show layer screens at ts_showscreens
                
            "Нет, я и так примерно представляла по количеству строк, что оно короткое, но чтобы настолько?"
            show natsuki 12e at f11
            n "Я же говорила, что{nw}"
            show natsuki 12d at t11
            m "Мне понравилось."
            show natsuki 2m at f11
            n "Ч-что?.."
            show natsuki 2n at t11
            m "Мне понравилось."
            m "Ты когда-нибудь слышала такую фразу, что «краткость - сестра таланта»?"
            show natsuki 2m at f11
            n "Н... нет..."
            show natsuki 2n at t11
            "Оно и понятно. Учитывая всё её окружение и даже семью, не удивительно, что она никогда раньше не слышала подобных комплиментов."
            m "Ну-у-у... Вот это вот как раз про тебя."
            m "Ты в этих восьми строках описала то, чего я не могла бы описать и тремя полными стихотворениями."
            m "Тут тебе и простой, но бодрый ритм, и какая-то рифма, и намеренное её нарушение в последней строчке, и..."
            "Я постепенно сбываюсь с мысли. Всё же у нас обмен стихами, а не курс по комплиментам девочке, которая никогда в жизни и одного комплимента не слышала."
            "Кто знает, как она вообще на них отреагирует..."
            show natsuki 2d at f11
            n "Что, п-правда???"
            n "Спасибо, Моника! Ты самая лучшая подруга, о которой я могла бы мечтать!"
            if ts_s_carterseven_readpoem == True:
                n 2c "Знаешь, когда я обменивалась стихами с Юри, она восприняла мой стих куда более прохладно."
            elif ts_y_carterseven_readpoem == True:
                n 2c "Знаешь, когда я обменивалась стихами с Сайори, она тоже его похвалила, но и близко не так, как ты."
            elif ts_y_carterseven_readpoem and ts_s_carterseven_readpoem == True:
                n 2c "Знаешь, когда я обменивалась стихами с другими девочками, они в целом его похвалили, но гораздо прохладнее и безразличнее."
            show natsuki 1a at t11
            "Ну, мне же не нужно, чтобы после первого же обмена девочки коллективно жаловались на то, что я заваливаю их непомерной работой, и что у них и без того домашние задания есть."
            "Так что лучше лишний раз перехвалить, чем недохвалить, чтобы они не отчаивались в своих писательских способностях..."
            "Но чтобы в ответ настолько хвалили и даже в какой-то мере обожествляли меня... не знаю."
            "В конце концов, я ведь тоже человек, и тоже могу ошибаться."
            em "О-хо-хо, ещё как!"
            "«Интересно, в каждой голове сидит такое злое подсознание, или это только мне так не повезло?»"
            em "Ну, к другим в голову же ты не залезешь..."
            em "Поэтому просто считай, что это ты эксклюзивная неудачница!"
            show natsuki 2m at f11
            n "Моника? Ты снова отключилась..."
            show natsuki 1n at t11
            m "А, что? Эм-м-м, да, прости..."
            m "Спасибо тебе, Нацуки. И за стих, и за комплименты, и за всё остальное."
            show natsuki 1l at f11
            n "А, да пустяки! Это я должна тебя поблагодарить за клуб и всё сопутствующее!"
            show natsuki 1j at t11
            stop music fadeout 4
            m "Ну... спасибо ещё раз, Нацуки."
            show natsuki 1d at f11
            n "Да не за что!"
            if ts_s_carterseven_readpoem and ts_y_carterseven_readpoem == True:
                show natsuki at cright with move
                hide natsuki
            else:
                n 1d "Ну, я дальше пойду?"
                show natsuki 1a at t11
                m "Иди, конечно..."
                show natsuki at cright with move
                hide natsuki
                "А сама я дальше пойду к..."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            jump cartersevenpoemsblya

        "Юри" if not ts_y_carterseven_readpoem:
            hide zatemnenie_light with dspr
            play music audio.okevryuri
            $ ts_y_carterseven_readpoem = True
            if not ts_first_carterseven_readpoem:
                show layer screens at ts_showscreens
                "Юри у нас самая начитанная в клубе, а значит, самая опытная в поэзии."
                "По крайней мере, Сайори так кажется..."
                "В любом случае, начать лучше с неё, чтобы когда дело дойдёт до остальных, мне было бы уже не так обидно за мои бездарные писательские навыки."
                em "Ну вот, ты и сама уже об этом говоришь! Значит, точно бездарность!"
                "Отстань."
                $ ts_first_carterseven_readpoem = True
                show layer screens at ts_hidescreens
                " {w=1.0}{nw}"

            play sound pageflip
            scene ts_club
            with wipeleft_scene
            show layer screens at ts_showscreens

            show yuri 2b at f11
            y "Здравствуй, Моника."
            y "С чем ты сегодня?"
            show yuri 2a at t11
            m "Не поверишь - со стихом."
            show yuri 3g at f11
            y "!.."
            y 2h "Я это... и так поняла."
            y "В конце концов, ты же и задала нам написать стих на сегодняшнюю встречу..."
            show yuri 2g at t11
            "Заметка на полях: никогда больше не шутить при Юри, и уж тем более, {b}с{/b} Юри."
            "По-моему, она воспринимает всё {i}чересчур{/i} серьёзно."
            "Нужно побыстрее сменить тему, пока ситуация не станет слишком неловкой."
            m "Д-да... Так вот..."
            show yuri 2e at t11
            m "А ты стихотворение написала?"
            m "Ты до последнего что-то там строчила на листе, чёркала, перечёркивала... Я уж было подумала, что ты до конца вчерашней встречи так стих и не напишешь."
            show yuri 1k at t11
            y "Естественно, написала."
            y 2q "П-правда, позже мне показалось, что в моём стихотворении всё не так, и... переписала его..."
            y 2d "Но зато теперь стих чист, опрятен, и его можно показывать другим!"
            show yuri 1c at t11
            if ts_s_carterseven_readpoem and ts_n_carterseven_readpoem == True:
                "Ну, хоть один человек догадался, что не обязательно предоставлять мне стихи до конца встречи клуба, и что это терпит до завтрашней встречи."
                "Правда, Сайори что-то говорила про то, что она переписывала стих по памяти... Но это другое."
            m "Ну так... покажешь?"
            show yuri 3d at f11
            y "Конечно!"
            show yuri 3c at t11
            "Юри достаёт записную книжку со своим стихотворением."
            if ts_s_carterseven_readpoem and ts_n_carterseven_readpoem == True:
                "Из всех трёх её книжка выглядит самой красивой, хотя и не могу не отметить, что очень уж она своеобразная."
            else:
                "Красивая, хотя и... очень своеобразная."
            "По всей обложке какие-то символы, которые вроде и кажутся знакомыми, но разобрать я их никак не могу."
            "Она втайне поклоняется Сатане или что?"
            "Вкупе с её проблемами с самовредом, это даже кажется вполне логичным."
            "Я имею в виду, это разве не нужно для всяких жертвоприношений?"
            em "Так для жертвоприношений же нужна кровь девственницы. Откуда ты знаешь, невинна ли Юри?"
            "...да нет же, такой элегантный цветок лаванды, и поклоняется Сатане? Да немыслимо!"
            em "Ты вчера то же самое говорила про чтение манги. Всё бывает в первый раз."
            "«Отс... хотя знаешь, и то верно.»"
            show yuri 1v at f11
            y "Я т-только х-хотела сказать, п-принесла ли с-стих ты, н-но п-поскольку т-ты и т-так уже с-сказала, то..."
            y "Д-думаю, это бессмысленно..."
            show yuri 4b at t11
            "Едва закончив предложение, которое далось ей с невероятным трудом, Юри отвернулась."
            "Видно, как она пытается поддержать неудавшуюся шутку, но поскольку эта шутка изначально была обречена на неудачу, нам обеим становится всё более неловко с каждой секундой."
            show yuri 4a at f11
            y "М-можно?"
            show yuri 4a at t11
            m "Юри, ну конечно, в этом же и смысл!"
            show yuri 1q at f11
            y "Н-ну хорошо..."
            pause 4
            show yuri 2t at f11
            y "М-Моника..."
            y 2v "В-видно, твоё стихотворение - уже далеко не первое..."
            y 2zi "Какой у тебя писательский опыт?"
            show yuri 2s at t11
            if ts_n_carterseven_readpoem == True:
                "Юри повторяет тот же вопрос, что и Нацуки."
                "Что же, буду давать такой же ответ."
            m "Н-ну... Небольшой..."
            m "Я просто поймала вдохновение, вот и всё..."
            show yuri 1k at f11
            y "Хм-м-м..."
            y 2l "Просто приёмы, которые ты использовала, сообщают о том, что ты написала уже не один десяток стихов..."
            "Как только Юри доходит до удобной ей темы, она как всегда преображается из робкого цветка лаванды в бойкого знатока литературы."
            y "Однако, есть определённые писательские наклонности, которые не свойственны профессионалам, а скорее характерны для новичков."
            y "Например, как они выбирают слова, которые не совсем подходят тематике и настроению стихотворения."
            y 2j "Примерное настроение твоего стихотворения - полнейший хаос и беспредел, и главная героиня стихотворения пытается перекричать этот хаос."
            y "Поэтому это стихотворение скорее должно быть написано короткими словами, чуть ли не односложными."
            y 2k "Однако это не остановило тебя от таких слов, как, например, «какофония»."
            y 2l "Кроме того, хаотическое стихотворение скорее должно быть написано без какого-либо ритма и рифмы. И хотя в целом ты с этим справилась, и ритма здесь действительно нет..."
            y "Рифма здесь присутствует, да ещё какая."
            y 1j "А, и у тебя в некоторых местах рифма на глаголы, что... не совсем приемлемо в стихах. Да, это можно, но это слишком просто - кажется, что над последними строками ты совсем не заморачивалась."
            show yuri 1i at t11
            "Такое ощущение, что я не со сверстницей стихом поделилась, а учитель отчитывает меня за бездарный стих."
            em "И кто за это в ответе?"
            "«А про кого этот стих, напомните-ка?»"
            em "Ну так отчитывают тебя, а не меня!"
            if ts_s_carterseven_readpoem and ts_n_carterseven_readpoem == False:
                "Но зато я в итоге оказалась права - Юри действительно самая опытная в плане писательских навыков."
            m "С-спасибо, Юри, за конструктивную критику..."
            if ts_s_carterseven_readpoem and ts_n_carterseven_readpoem == True:
                "Хоть кто-то действительно понял суть этого мероприятия..."
            show yuri 1zi at f11
            y "Всегда пожалуйста."
            y "А теперь прочтёшь и мой? "
            y 3b "Хочу показать тебе, как работают настоящие профессионалы."
            show yuri 2c at t11
            m "К... Конечно..."
            show yuri 2d at f11
            y "Тогда вот!"
                
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            scene ts_club:
                blur 9.0
            show yuri 2d at f11:
                blur 9.0
            with dissolve

            show layer screens at ts_showscreens

            if not persistent.first_poem:
                $ persistent.first_poem = True
                show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
                    xpos 1050 ypos 590

            play sound page_turn

            show screen poem(poem_y1)

            pause

            play sound page_turn
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem
            hide poem_dismiss

            scene ts_club
            show yuri 2d at f11
            with dissolve

            show layer screens at ts_showscreens
                
            "Постойте... а здесь вообще ритм есть?"
            "Я понимаю, что Юри критиковала моё стихотворение за недостаточное отсутствие ритма, но моё стихотворение, как она выразилась, было «хаотическим»."
            "Я не эксперт в настроениях стихотворений, но по-моему, её стих - это чуть ли не противоположность хаоса."
            "Я повторяю свои мысли Юри."
            show yuri 2l at f11
            y "Действительно, моё стихотворение скорее умиротворительное, однако в подобного рода стихотворениях ритм тоже не особо нужен."
            "Поскольку у тебя есть всё время во вселенной, то нет смысла утруждать себя такими рамками, как ритм и рифма."
            show yuri 2l at t11
            "Чёрт, похоже, у неё есть ответ на все вопросы мироздания. По крайней мере, если это касается литературы."
            show yuri 3o at f11
            y "Я... Я снова бубню?"
            y 4c "У-у-у..."
            show yuri 4c at t11
            "Зато как только мы уходим с литературных отношений и возвращаемся в житейские, Юри как будто снова подменили - она начинает заикаться и извиняться за всё."
            "Даже за то, чего она ещё не сделала или не хотела делать."
            m "Нет-нет, что ты... В конце концов, это ведь как раз то, из-за чего мы все здесь собрались..."
            show yuri 2q at f11
            y "М-может... м-может, и так..."
            y 2zi "Т-тогда... я пойду дальше?"
            stop music fadeout 4
            show yuri 2s at t11
            if ts_n_carterseven_readpoem and ts_s_carterseven_readpoem == True:
                m "Так мы же уже закончили..."
                show yuri 2q at f11
                y "Д-да, в-верно, п-прости..."
                show yuri 2o at t11
                m "Да ничего..."
                show yuri 1zi at t11
                y "Т-тогда... всё?"
                show yuri 1s at t11
                m "В целом... всё."
                m "Я ещё раз поговорю со всеми остальными, а потом можем заканчивать."
                show yuri 1v at f11
                y "Х... хорошо..."
                show yuri at cright with move
                hide yuri
                "В мгновение ока Юри уже нет."
            else:
                m "Да, конечно, иди..."
                show yuri 2zi at f11
                y "Х-хорошо..."
                show yuri at cright with move
                hide yuri
                "Тогда и я пойду дальше..."
                "А следующей у нас будет..."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            jump cartersevenpoemsblya

label ts_carterseven_poem_finally:
    play sound pageflip
    play music audio.t8 fadein 2
    scene ts_club
    show yuri 1a at t31
    show sayori 1a at t32
    show natsuki 1a at t33
    with wipeleft_scene
    show layer screens at ts_showscreens
    m "Итак, ребята! Все закончили со стихами?"
    show yuri 2d at f31
    show sayori 3r at f32
    show natsuki 2y at f33
    $ m_name = "Все вместе"
    show layer screens at vpunch
    m "Да!"
    show yuri 2c at t31
    show sayori 3q at t32
    show natsuki 2j at t33
    $ m_name = "Моника"
    m "Ну, как вам первая проба пера? Как вам первый обмен стихотворениями?"
    show sayori 4r at f32
    s "Замечательно! Я бы ещё раз с кем-нибудь поделилась!"
    show sayori 3q at t32
    show natsuki 2d at f33
    n "Да, неплохо."
    show yuri 2zi at f31
    show natsuki 2a at t33
    y "Ну, для первого раза вполне себе неплохо..."
    show yuri 2s at t31
    "Ну, начало положено..."
    stop music
    m "Тогда... как насчёт того, чтобы и на завтра что-то написать?"
    show yuri 3n at h31
    show sayori 4m at h32
    show natsuki 2p at h33
    $ m_name = "Все вместе"
    show layer screens at vpunch
    m "!!!"
    $ m_name = "Моника"
    m "Да ладно вам, девочки! Вы уже уже написали один стих, дальше будет гораздо проще!"
    m "Да и к тому же, Сайори, не ты ли говорила о том, что ты бы с радостью поделилась стихом ещё раз?"
    m "Ну вот и флаг тебе в руки. Напиши ещё одно стихотворение, и потом можешь делиться с кем угодно."
    show sayori 2l at f32
    s "Да я-э-э-э..."
    show yuri 2c at t31
    show sayori 4p at h32
    show natsuki 2z at t33
    play music ts_est
    s "Моника, так нечестно!"
    show sayori 5c at f32
    s "Сама же поставила меня в безвыходное положение, да ещё и нагло пользуешься этим!"
    show sayori 5d at t32
    m "Ну вообще, как я уже говорила, ты сама это всё сказала, а я просто предложила. Я никого не заставляла писать стихи."
    show sayori 2za at f32
    s "..."
    s 3l "Ладно, напишу уж..."
    show yuri 2i at t31
    show sayori 3l at t32
    show natsuki 2t at t33
    m "Ну и раз президент и вице-президент клуба говорят, что они напишут, то дело остаётся за малым."
    show yuri 1l at f31
    y "Я обязательно напишу."
    show yuri 1m at t31
    show natsuki 2t at f33
    stop music fadeout 5
    n "Ну, раз осталась только я, то чего уж там..."
    n 2d "Можешь на меня рассчитывать! "
    extend 2y "Завтра я напишу лучшее стихотворение на свете!"
    show yuri 2d at t31
    show sayori 3r at t32
    show natsuki 2z at t33
    "Мы все вместе посмеялись. Отличная разрядка обстановки после несколько напряжённого и неловкого обмена стихами."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 1a at t31
    show sayori 1a at t32
    show natsuki 1a at t33
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_afterword

    m "Ладно, девочки, не смею вас больше задерживать."
    m "Не забудьте задание на следующую встречу: стихотворение, чтобы все могли друг с другом поделиться."
    m "А сейчас - до завтра!"
    show yuri 1b at f31
    show sayori 1x at f32
    show natsuki 1l at f33
    $ m_name = "Все вместе"
    show layer screens at vpunch
    m "До завтра, Моника!"
    $ m_name = "Моника"
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    play sound door_open
    show yuri at cleft with move
    hide yuri
    pause 0.6
    show sayori at cleft with move
    hide sayori
    pause 0.6
    show natsuki at cleft with move
    hide natsuki
    show layer screens at ts_showscreens
    "Все ушли. Что же, я тоже не смею задерживать себя в клубе."
    "Я выключаю свет и выхожу."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_light_off_corridor
    with wipeleft_scene

    play sound pageflip
    scene ts_stairs
    with wipeleft_scene

    stop music fadeout 5

    play sound pageflip
    scene ts_school_gate_evening
    with wipeleft_scene

    play sound pageflip
    scene ts_street_late
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Наконец-то... домой..."
    "Наконец-то тишина..."
    play music ts_ar
    show monika 2l at aki_spawn
    em "И не мечтай!"
    em 2i "Думаешь, я забыла? А я {i}очень{/i} злопамятная."
    em 1n "Кхе-кхе..."

    python:
        _preferences.volumes['voice'] = 1.0

    play ambience ts_bezdarnost

    em 4k "Бездарность бездарность бездарность бездарность бездарность бездарность безда{nw}"

    python:
        _preferences.volumes['voice'] = .3

    show layer screens at vpunch
    if persistent.cens_mode == True:
        m "ДА ИДИ ТЫ НАХУЙ УЖЕ!"
    else:
        m "Да пошла ты!"

    python:
        _preferences.volumes['voice'] = 1.0

    em "Нет, не пойду!"
    em "арность бездарность бездарность бездарность безд{nw}"

    python:
        _preferences.volumes['voice'] = .3

    play sound_loop ts_running

    scene ts_street_late at ts_running_fast
    show monika 4k at i11

    if unluck6 == True:
        "Я бегу со школы до дома ещё быстрее, чем утром, только чтобы эта мразь унялась."
    else:
        "Я бегу со школы до дома так быстро, как только могу, только чтобы эта мразь унялась."

    python:
        _preferences.volumes['voice'] = 1.0

    em "Ты, наверное, забыла, что я с тобой {b}постоянно{/b}? И днём, и ночью, в любое время. И я всегда тебе буду повторять, что ты бездарность!"
    show monika 4k at aki_uhod

    python:
        _preferences.volumes['voice'] = .3

    "Я её не слушаю. Я вообще ничего и никого не слушаю. У меня есть цель, и я её придерживаюсь."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    stop music
    stop sound_loop
    stop ambience

    python:
        _preferences.volumes['voice'] = .65

    play sound2 ts_othodos_ot_bega fadein 2
    play sound pageflip
    scene ts_house_monika_evening at ts_ustal_suka
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Наконец, передо мной показался дом."
    "Хорошо так побегала. И под аккомпанемент Аки я даже не сильно-то и устала."
    if unluck6 == True:
        em "Привыкаешь?"
    "Неплохо бы вернуть традицию с утренними пробежками. Только... не таких резвых."
    "Пора бы оборачивать навязчивые мысли о том, что я бездарность, в свою же пользу."
    em "Ну и ладно, ну и пожалуйста. Всё, я с тобой не разговариваю."
    m "Так ты же...{w=0.3} и так...{w=0.3} со мной...{w=0.3} не разгова...{w=0.3} риваешь..."
    em "Ой, всё, отстань..."
    "Хе-хе-хе."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound2 door_open
    scene ts_vhod_nolight
    with wipeleft_scene

    pause 0.5

    play sound svet_on

    scene ts_vhod_night
    with flash

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    m "Папа? Я пришла!"
    "Однако папа не ответил."
    "Хм-м-м... а может..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music ts_mdl fadein 2

    play sound pageflip
    scene ts_living_room_telek_stas
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Ах, ну конечно - папа уже с головой окунулся в очередную политическую передачу, в которой я совершенно ничего не понимаю..."
    m "Папа! Я пришла!"
    show hiroto 1z at h11
    ts_ft "!!!"
    show hiroto 1u at t11
    ts_ft "Ой, Моника, привет..."
    ts_ft 1y "А ты чего так поздно?"
    show hiroto 1s at t11
    m "Да, в клубе задержалась..."
    show hiroto 1v at f11
    ts_ft "Понятно..."
    show hiroto 1w at t11
    "..."
    m "..."
    m "Пап, может, на кухню лучше пойдём? Там нас {i}никто не будет отвлекать.{/i}"
    show hiroto 1v at f11
    ts_ft "Сейчас, сейчас..."
    show hiroto 1s at t11
    m "..."
    m "Я жду тебя на кухне."
    show hiroto 1t at f11
    ts_ft "Да-да, ты иди, я догоню..."
    show hiroto 1s at t11
    "Я разочарованно вздыхаю и иду обратно на кухню."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    show hiroto 1e at rn11
    "Спустя несколько минут наконец приходит и папа."
    "Дождался рекламы и только потом пришёл повидаться с любимой дочерью, не иначе."
    show hiroto 2g at f11
    ts_ft "Ну здравствуй, Моника. Как день прошёл?"
    show hiroto 1f at t11
    if unluck6 == True:
        "Папа, по всей видимости, сделал вид, что забыл о моём утреннем конфузе, в связи с чем я опоздала в школу."
        "Или на самом деле забыл..."
    elif unluck4 and unluck6 == True:
        "Папа, по всей видимости, сделал вид, что забыл о моём утреннем конфузе, в связи с чем я снова опоздала в школу."
        "Или на самом деле забыл..."
    m "Да, знаешь, прошёл так прошёл. Мы с девочками впервые обменялись стихами, и ты представляешь, никто даже не забыл!"
    show hiroto 2g at f11
    ts_ft "Ну и славненько..."
    show hiroto 1f at t11
    m "И после собрания я задала всем написать ещё один."
    show hiroto 1c at f11
    ts_ft "Подожди, ещё один?"
    ts_ft "Моника, я тебе, кажется, уже говорил, что писать стихи на постоянной основе как минимум нежелательно."
    ts_ft 1v "Это, в конце концов, творческий процесс, для этого нужно вдохновение."
    ts_ft 2h "А если этого вдохновения нет, то и хороший стих ты вряд ли напишешь."
    ts_ft 1c "Максимум, что у тебя получится - так это испортить самой себе настроение из-за того, что у тебя ничего не получается, потому что все рифмы кажутся какими-то натянутыми и натужными, ну и так далее."
    show hiroto 1e at t11
    "Я на это под таким углом не смотрела."
    m "Но девочки же сами выразили желание написать ещё стих. Сайори даже сказала, что она бы с удовольствием со всеми поделилась ещё раз."
    show hiroto 1c at f11
    ts_ft "Конечно, она так сказала, потому что в обмене стихами главное ведь не сам стих, а взаимодействие с другими людьми."
    ts_ft "Естественно, если одним и тем же стихом делиться несколько раз, то новизна постепенно выветривается, и в итоге другие просто скажут нечто вроде:"
    ts_ft 2a2 "«Сайори, ты этот стих уже шестой раз показываешь, а чем-то {i}новым{/i} ты нас порадовать не хочешь?»"
    ts_ft 1c "Однако это не отменяет мною вышесказанное, что стихосложение - это процесс творческий: ты либо хочешь писать, либо не хочешь. Здесь нет слова «надо»."
    show hiroto 1e at t11
    m "Ну всё, всё, хорошо, ладно, поставил меня в тупик, всё, доволен?"
    show hiroto 1t at f11
    ts_ft "Доволен."
    show hiroto 1s at t11
    m "Ты мне лучше скажи, как у тебя день прошёл?"
    show hiroto 1c at f11
    ts_ft "Ну, не без эксцессов."
    ts_ft 1a2 "Эта горе-мамаша снова не явилась на заседание, поэтому мы перенесли его {b}ещё раз{/b}."
    ts_ft 1u "Если она не явится и в третий раз, мы проведём заседание без неё, и просто поставим её перед фактом."
    ts_ft 1c "А потом, вместо обычной бумажной работы, я целый день экстренно катался по адресам, составлял акты, ну и всё такое. По сути, та же бумажная работа, только на выезде."
    ts_ft 1b "А последний адрес был как раз недалеко от нашего дома. Поэтому вместо того, чтобы в пять часов вечера переться в администрацию, чтобы просто потом уехать домой, я сразу поехал к себе."
    show hiroto 1a at t11
    m "О как... действительно, не без эксцессов..."
    show hiroto 1g at f11
    ts_ft "Вот-вот."
    ts_ft 1c "Ты кушать будешь? Я тут приготовил себе по быстренькому, тебе тоже кое-что осталось."
    show hiroto 1e at t11
    "Папа показывает мне кастрюлю, в которой были уже свежие макароны."
    show hiroto 1g at f11
    ts_ft "Я макароны с сосисками ел, но, учитывая твоё веганство, тебе предложу разве что макароны с сахаром."
    show hiroto 1f at t11
    if unluck6 == False:
        "Опять?"
        "Впрочем, не страшно, я не против ни самих макарон, ни того, что они приправлены сахаром."
        "Единственное, что мне после большого количества сахара стоит позаботиться о фигуре, но с двух раз ведь ничего не будет, правда же?"
        em "Вообще-то, согласно исследованиям, тебе нужно будет заботиться не только о фигуре..."
        "Ай, ладно, неважно!"
    m "Пап, я вегетарианка, а не веган. Веганство - это отказ и от всех продуктов, которые животные производят: яйца, молочка, ну и так далее."
    show hiroto 1g at f11
    ts_ft "Да знаю я, я просто шучу..."
    show hiroto 1f at t11
    m "..."
    show hiroto 1g at t11
    "Однако после этого мы просто оба посмеялись."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    show hiroto 1a at t11
    "После ужина папа спрашивает:"
    show hiroto 1c at f11
    ts_ft "Ты к себе?"
    show hiroto 1e at t11
    m "Да, что-то устала я, а мне же ещё стих писать..."
    show hiroto 1g at f11
    ts_ft "Ну, ты иди, а я ещё телевизор посмотрю."
    show hiroto 1f at t11
    m "Хорошо, пап. Люблю тебя."
    show hiroto 1g at f11
    ts_ft "И я тебя люблю."
    show hiroto at cright with move
    hide hiroto
    "После этого каждый пошёл своей дорогой: папа - в гостиную, а я - в свою комнату."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_bedroom
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_tgod
    "Наконец-то... мягкая кроватка..."
    show monika 2bd at aki_spawn
    em "До кровати тебе ещё далеко. Ты забыла, что тебе ещё стих написать надо?"
    show monika 1bc at t11
    m "Х-х-х..."
    show monika 2bd at f11
    em "А ты как думала? Нельзя же только другим раздавать задания, нужно же ещё и самой соответствовать заявленному тобой же статусу."
    em 3bi "Поэтому бери ручку и пиши стих."
    show monika 3bh at t11
    m "Да не хочу я. Может, позже. Или с утра пораньше..."
    show monika 4bk at f11
    em "Пораньше - это как сегодня?"
    show monika 2bj at t11
    m "А может, и как сегодня! В любом случае - стих я напишу. А теперь дай мне отдохнуть. Я в конце концов заслужила."
    show monika 3bf at t11

    stop music fadeout 5

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound svet_on
    scene ts_darkbed

    show layer screens at ts_showscreens

    "Нарочито игнорируя Аки, я выключаю свет, раздеваюсь и ложусь дремать."
    "Хотя, учитывая то, который сейчас час, уже бы и полноценно поспать пора, а я только дремать собралась."
    if unluck6 == False:
        "Но с другой стороны, я и вчера уснула и проснулась рано, плюс сегодня был напряжённый день, так что как минимум отдохнуть - это скорее не прихоть, а необходимость."
    "В любом случае, поспать надо. А стих будет попозже."

    return