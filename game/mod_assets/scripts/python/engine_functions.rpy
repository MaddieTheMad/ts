# TRUE STORY ENGINE FUNCTIONS
# by @b3rg3n
# Since 2024

init -1000 python:

    import os.path

    def get_image(file): # ФУНКЦИЯ ГОПА КАРТИНКИ
        return "mod_assets/source/images/%s" % file

    def get_font(file): # ФУНКЦИЯ ГОПА ШРИФТА
        return "mod_assets/source/fonts/%s" % file

    def get_videosos(file): # ФУНКЦИЯ ГОПА ВИДЕОСОСА
        return "mod_assets/source/videosos/%s" % file

init -1199 python:
    from os import path
    modID = 'mod_assets/source/audio/'

    for file in renpy.list_files(): # ФУНКЦИЯ ГОПА АУДИО БЕЗ ДЕФАЙНА
        if modID in file:
            file_name = path.splitext(path.basename(file))[0]
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file


init -1001 python:
# РЕГЕСТРИРУЕМ ДОП КАНАЛЫ
    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound_loop", "voice", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)
    renpy.music.register_channel("ambience2", "voice", False)
    renpy.music.register_channel("music2", "music", False)

    def volume(vol, chnl): # ФУНКЦИЯ РЕГУЛИРОВКИ ГРОМКОСТИ ОДНОЙ СТРОКОЙ КОДА
        renpy.music.set_volume(vol, channel=chnl)

    def stop_music(): # ДОБАВЛЯЕМ НОВЫЕ КАНАЛЫ В СТОП МУЗОН
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music", "music2"):
            renpy.music.stop(channel=chnl)

    def stop_sound(): # ДОБАВЛЯЕМ НОВЫЕ КАНАЛЫ В СТОП ЗВУКИ
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "ambience2"):
            renpy.sound.stop(channel=chnl)

    def reload_names(): # ПЕРЕЗАГРУЖАЕМ ИМЕНА ПРИ ПЕРЕВОДЕ
        global store
        for x in store.names_list:
            char_define(x)
