# ХУЕТА ДЛЯ ТЕСТОВ
label testing_label_blya:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state=glitchtext(12),details="Снова что-то мутит",large_image="logogovna",start=time.time())
        except AssertionError:
            pass

    scene black


    scene white
    $ persistent.sprite_time = "day"
    show sayori 4z at t41
    show yuri 4f at t42
    show monika 1f at t43
    show natsuki 1e at t44
    "day"

    show screen poem(poem_peacedets)
    pause
    show screen poem(poem_y2)
    pause
    show screen poem(poem_su)
    pause
    show screen poem(poem_n2)




    $ persistent.sprite_time = "cloudly"
    "cloudly"
    $ persistent.sprite_time = "sunset"
    "sunset"
    $ persistent.sprite_time = "night"
    "night"


    $ persistent.uncolorize = "none"

    #$ persistent.uncolorize = "lite"

    #$ persistent.uncolorize = "full"


    show screen dialog("truestory.exe\n\nВ файлах скрипта обнаружена критическая ошибка. Попробуйте ещё раз.", ok_action=Return())

    return