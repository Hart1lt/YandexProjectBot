import telebot
import sqlite3

rating = False
bot = telebot.TeleBot('5990898499:AAEgSn5SOXrGD7xvaTxIR_OidqB0so35jcc')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    photo = open('start.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption='Привет! Я чат-бот. Введите /info, чтобы узнать больше.')


@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Я могу помочь вам найти игры в различных жанрах."
                          "Введите /<Название игры>, чтобы узнать больше об этой игре или введите комнду /all_game,"
                          "чтобы увидеть все игры и команды к ним.")


@bot.message_handler(commands=['all_game'])
def allGame(message):
    bot.send_message(message.chat.id, 'На данный момент в этом боте присутствуют только игры из рейтинга с 2007'
                                      'по 2014.\n. В дальнейшем бот будет развиваться и будут добавленно'
                                      'больше данных о играх.')
    bot.send_message(message.chat.id, 'Все игры на данный момент:\n'
                                      'Dota 2 (/dota2)\n'
                                      'STALKER:Тень Чернобыля (/STALKER:Тень_Чернобыля)\n'
                                      'Call of Duty 4: Modern Warfare (/CallOfDuty4)\n'
                                      'Ведьмак (/TheWitcher)\n'
                                      'Assassin’s Creed II (/AssassinsCreedII)\n'
                                      'Call of Duty: Modern Warfare 2 (/CallOfDuty:MW2)\n'
                                      'S.T.A.L.K.E.R.: Зов Припяти (/STALKER:Зов_Припяти)\n'
                                      'Batman: Arkham Asylum (/Batman:ArkhamAsylum)\n'
                                      'Dragon Age: Origins (/DragonAge:Origins)\n'
                                      'Mafia II (/MafiaII)\n'
                                      'Метро 2033 (/Metro2033)\n'
                                      'Mass Effect 2 (/MassEffect2)\n'
                                      'Fallout: New Vegas (/Fallout:NewVegas)\n'
                                      'Red Dead Redemption (/RDR)\n'
                                      'The Elder Scrolls V: Skyrim (/TESV:SKYRIM)\n'
                                      'The Witcher 2: Assassins of Kings (/TheWitcher2)\n'
                                      'Deus Ex: Human Revolution (/DeusExHR)\n'
                                      'Portal 2 (/Portal2)\n'
                                      'Call of Duty: Modern Warfare 3 (/CallOfDuty:MW3)\n'
                                      'Far Cry 3 (/FarCry3)\n'
                                      'Dishonored (/Dishonored)\n'
                                      'The Walking Dead: The Game (/TheWalkingDead)\n'
                                      'Assassin’s Creed III (/AssassinsCreedIII)\n'
                                      'Borderlands 2 (/Borderlands2)\n'
                                      'Grand Theft Auto V (/GTAV)\n'
                                      'BioShock Infinite (/BioShockInfinite)\n'
                                      'Metro: Last Light (/Metro:LastLight)\n'
                                      'Assassin’s Creed IV: Black Flag (/AssassinsCreedIV)\n'
                                      'The Last of Us Part I (/TheLastOfUs)\n'
                                      'Far Cry 4 (/FarCry4)\n'
                                      'Wolfenstein: The New Order (/Wolfenstein:TheNewOrder)\n'
                                      'Assassin’s Creed Unity (/AssassinsCreedUnity)\n'
                                      'Dark Souls II (/DarkSoulsII)\n'
                                      'Alien: Isolation (/Alien:Isolation)\n'
                                      'League of Legends (/LOL)'
                                      'Counter-Strike: Global Offensive (/CSGO)'
                                      'Valorant (/Valorant)'
                                      'Overwatch 2 (/Overwatch2)'
                                      'Tom Clancy’s Rainbow Six Siege (/R6S)'
                                      'Metro Exodus (/MetroExodus)'
                                      'Cyberpunk 2077 (/Cyberpunk2077)'
                                      'Stray (/Stray)'
                                      'Red Dead Redemption 2 (/RDR2)'
                                      'MinecraftLegends (/Minecraft Legends)'
                                      'Genshin Impact (/GenshinImpact)'
                                      'А также одна тайная команда.')


@bot.message_handler(commands=['game_rating'])
def send_rating(message):
    global rating
    bot.reply_to(message, "Рейтинг какого года вы хотите увидить?(Введите только год)")
    rating = True


@bot.message_handler(commands=['dota2'])
def send_dota2_info(message):
    bot.reply_to(message, "Dota 2 - это многопользовательская онлайн-игра в жанре MOBA."
                          "В этой игре вам нужно сражаться в команде из пяти человек против другой команды,"
                          "захватывая территории и уничтожая врагов.")


@bot.message_handler(commands=['STALKER:Тень_Чернобыля'])
def send_stlaker2007_info(message):
    bot.reply_to(message, "«S.T.Á.L.K.E.R.: Тень Черно́быля», официально названная в СНГ как S.T.A.L.K.E.R, "
                          "— компьютерная игра в жанре шутера от первого лица с элементами RPG и survival horror, "
                          "разработанная и выпущенная украинской компанией GSC Game World для Microsoft Windows в "
                          "2007 году.")


@bot.message_handler(commands=['CallOfDuty4'])
def send_COD4_info(message):
    bot.reply_to(message, "Call of Duty 4: Modern Warfare — компьютерная игра в жанре шутера от первого лица, "
                          "разработанная американской компанией Infinity Ward и изданная Activision. Является "
                          "четвёртой в серии Call of Duty и первой в подсерии Modern Warfare; официально проект был "
                          "анонсирован 26 мая 2007 года.")


@bot.message_handler(commands=['TheWitcher'])
def send_TheWitcher_info(message):
    bot.reply_to(message, "«Ведьма́к» — компьютерная ролевая игра, разработанная польской компанией CD Projekt RED по "
                          "мотивам одноимённой серии романов польского писателя Анджея Сапковского. Релиз игры на "
                          "платформе Windows состоялся 24 октября 2007 года — в России, 26 октября — в Европе и 30 "
                          "октября 2007 года — в США")


@bot.message_handler(commands=['AssassinsCreed2'])
def send_ACII_info(message):
    bot.reply_to(message, "Assassin’s Creed II — компьютерная игра в жанре action-adventure,"
                          "продолжение игры Assassin’s Creed от компании Ubisoft. Официальный анонс"
                          "состоялся 16 апреля 2009 года в журнале Game Informer.")


@bot.message_handler(commands=['CallOfDuty:MW2'])
def send_CODMW2_info(message):
    bot.reply_to(message, "Call of Duty: Modern Warfare 2, также известная ранее как Modern Warfare 2 —"
                          "компьютерная игра, в жанре шутера от первого лица, разработанная американской"
                          "компанией Infinity Ward и изданная Activision. Игра является шестой в серии Call of Duty."
                          "Проект официально анонсирован 11 февраля 2009 года.")


@bot.message_handler(commands=['STALKER:Зов_Припяти'])
def send_stalker2010_info(message):
    bot.reply_to(message, "S.T.A.L.K.E.R.: Зов Припяти — компьютерная игра в жанре FPS с элементами ролевой"
                          "игры и survival horror от украинской компании GSC Game World, сиквел игры"
                          "«S.T.A.L.K.E.R.: Тень Чернобыля». Выход игры состоялся 2 октября 2009 года.")


@bot.message_handler(commands=['Batman:ArkhamAsylum'])
def send_BatmanAA_info(message):
    bot.reply_to(message, "Batman: Arkham Asylum — компьютерная игра в жанре action-adventure с элементами стелса,"
                          "разработанная британской студией Rocksteady Studios и изданная Eidos Interactive совместно"
                          "с Warner Bros. Interactive Entertainment.")


@bot.message_handler(commands=['DragonAge:Origins'])
def send_DragonAgeOrigins_info(message):
    bot.reply_to(message, "Dragon Age: Origins — компьютерная ролевая игра, разработанная канадской студией BioWare"
                          "и выпущенная компанией Electronic Arts для Windows, Playstation 3, Xbox 360 и macOS в"
                          "2009 году. Это первая игра в серии Dragon Age.")


@bot.message_handler(commands=['MafiaII'])
def send_MafiaII_info(message):
    bot.reply_to(message, "Mafia II — компьютерная игра в жанре приключенческого боевика с открытым миром,"
                          "сочетающего в себе автомобильный симулятор и шутер от третьего лица, разработанная"
                          "чешской компанией 2K Czech; вторая игра серии Mafia. Сюжет Mafia II практически не имеет"
                          "связи с первой частью, однако существует с ней в одной вселенной.")


@bot.message_handler(commands=['Metro2033'])
def send_Metro2033_info(message):
    bot.reply_to(message, "Metro 2033 — компьютерная игра в жанре постапокалиптического шутера от первого лица"
                          "с элементами survival horror и стелса, разработанная украинской студией 4A Games и"
                          "изданная американской компанией THQ в марте 2010 года. Игра является интерпретацией"
                          "одноимённого романа российского писателя Дмитрия Глуховского.")


@bot.message_handler(commands=['dotaTrue'])
def send_TrueAboutDota_info(message):
    bot.reply_to(message, 'Это не игра, это помойка, патч - помойка, баланс - помойка, разрабы - помойка,'
                          'тимейты - помойка, ты - помойка, все твоя семья оказывается тоже помойка,'
                          'которая живёт на помойке.(Это не всё)')


@bot.message_handler(commands=['MassEffect2'])
def send_MassEffect2_info(message):
    bot.reply_to(message, "Mass Effect 2 — компьютерная игра в жанре ролевого боевика, разработанная канадской"
                          "студией BioWare и выпущенная американской компанией Electronic Arts в январе 2010 года"
                          "на платформах Xbox 360 и Windows, а также на PlayStation 3 в январе 2011 года")


@bot.message_handler(commands=['Fallout:NewVegas'])
def send_FalloutNV_info(message):
    bot.reply_to(message, "Fallout: New Vegas — компьютерная ролевая игра с открытым миром, разработанная"
                          "американской компанией Obsidian Entertainment и выпущенная Bethesda Softworks в"
                          "2010 году для Microsoft Windows, PlayStation 3 и Xbox 360. В России игра была"
                          "выпущена компанией 1С. Игра входит в серию и является каноном вселенной Fallout.")


@bot.message_handler(commands=['RDR'])
def send_RDR_info(message):
    bot.reply_to(message, "Red Dead Redemption — компьютерная игра, шутер от третьего лица с открытым миром"
                          "и элементами RPG в жанре приключенческий боевик-вестерн. Разработана компанией"
                          "Rockstar San Diego при поддержке Rockstar North, Rockstar NYC, Rockstar Leeds,"
                          "Rockstar New England и Rockstar Lincoln.")


@bot.message_handler(commands=['Crysis'])
def send_Crysis_info(message):
    bot.reply_to(message, "Crysis — серия компьютерных игр, которые разработаны немецкой компанией"
                          "Crytek и изданы американским издателем Electronic Arts. Серия игр Crysis"
                          "является научно-фантастической трилогией в жанре шутера от первого лица."
                          "Первая игра серии, Crysis, была выпущена 13 ноября 2007 года.")


@bot.message_handler(commands=['MassEffect'])
def send_MassEffect_info(message):
    bot.reply_to(message, "Mass Effect — научно-фантастическая медиафраншиза, созданная Кейси Хадсоном, Дрю"
                          "Карпишином и Престоном Ватаманюком. Франшиза рассказывает о далёком будущем, в"
                          "котором люди и инопланетяне колонизировали Млечный Путь с помощью технологий"
                          "древних цивилизаций. ")


@bot.message_handler(commands=['GTA4'])
def send_GTA_info(message):
    bot.reply_to(message, "Grand Theft Auto IV — компьютерная игра в жанре action-adventure, девятая в серии Grand"
                          "Theft Auto, выпущена 29 апреля 2008 года для двух игровых приставок — PlayStation 3 и"
                          "Xbox 360, также полгода спустя игру портировали на ПК")


@bot.message_handler(commands=['STALKER:ЧистоеНебо'])
def send_stalker2008_info(message):
    bot.reply_to(message, "«S.T.A.L.K.E.R.: Чистое небо» — компьютерная игра в жанре шутера от первого лица с"
                          "элементами ролевой игры, разработанная украинской компанией GSC Game World и выпущенная"
                          "в России 22 августа 2008 года. Издателем в странах СНГ и Украине является GSC World"
                          "Publishing, в остальном мире игру издаёт компания Deep Silver.")


@bot.message_handler(commands=['dotaTrueTrue'])
def send_TrueTrueAboutDota_info(message):
    bot.reply_to(message, 'Х**ня полная, но все играют.')


@bot.message_handler(commands=['Fallout3'])
def send_Fallout3_info(message):
    bot.reply_to(message, "Fallout 3 — компьютерная игра в жанре Action/RPG с открытым миром, третья игра в"
                          "серии Fallout. Была разработана компанией Bethesda Game Studios и издана Bethesda"
                          "Softworks и ZeniMax Media.")


@bot.message_handler(commands=['CallOfDuty:WorldAtWar'])
def send_CODWAW_info(message):
    bot.reply_to(message, "Call of Duty: World at War — компьютерная игра в жанре шутера от первого лица,"
                          "разработанная американской компанией Treyarch и изданная Activision. Пятая игра"
                          "в серии Call of Duty.")


@bot.message_handler(commands=['DeadSpace'])
def send_DeadSpace_info(message):
    bot.reply_to(message, "Dead Space — научно-фантастическая компьютерная игра в жанрах survival horror и"
                          "шутера от третьего лица, разработанная студией EA Redwood Shores и выпущенная"
                          "Electronic Arts для PC под управлением ОС Windows, а также консолей PlayStation 3 и"
                          "Xbox 360 в 2008 году. Первая игра серии Dead Space.")


@bot.message_handler(commands=['TESV:SKYRIM'])
def send_TES5_info(message):
    bot.reply_to(message, "The Elder Scrolls V: Skyrim — компьютерная игра в жанре action/RPG с открытым миром,"
                          "разработанная студией Bethesda Game Studios и выпущенная компанией Bethesda Softworks."
                          "Это пятая часть в серии The Elder Scrolls. Игра была выпущена 11 ноября 2011 года для"
                          "Windows, PlayStation 3 и Xbox 360.")


@bot.message_handler(commands=['TheWitcher2'])
def send_TheWitcher2_info(message):
    bot.reply_to(message, "Ведьма́к 2: Убийцы королей — компьютерная ролевая игра, разработанная польской компанией"
                          "CD Projekt RED по мотивам серии романов «Ведьмак» известного польского писателя Анджея"
                          "Сапковского, продолжение компьютерной игры «Ведьмак» 2007 года выпуска.")


@bot.message_handler(commands=['DeusExHR'])
def send_DeusExHR_info(message):
    bot.reply_to(message, "Deus Ex: Human Revolution — компьютерная игра в жанрах стелс-экшен и Action/RPG,"
                          "выполненная в стилистике киберпанк, разработанная компанией Eidos Montreal и выпущенная"
                          "компанией Square Enix для платформ Windows, Xbox 360 и PlayStation 3 в 2011 году.")


@bot.message_handler(commands=['Portal2'])
def send_Portal2_info(message):
    bot.reply_to(message, "Portal 2 — компьютерная игра в жанре головоломки от первого лица, продолжение игры"
                          "Portal, разработанная компанией Valve Corporation. Игра была официально анонсирована"
                          "Valve 5 марта 2010 года.")


@bot.message_handler(commands=['CallOfDuty:MW3'])
def send_CODMW3_info(message):
    bot.reply_to(message, "Call of Duty: Modern Warfare 3 — мультиплатформенная компьютерная игра в жанре"
                          "шутер от первого лица, сиквел Call of Duty: Modern Warfare 2, восьмая игра в серии"
                          "Call of Duty. Разработана компанией Infinity Ward совместно со студиями Sledgehammer"
                          "Games и Raven Software, издателем игры выступила Activision.")


@bot.message_handler(commands=['FarCry3'])
def send_FarCry3_info(message):
    bot.reply_to(message, "Far Cry 3 — компьютерная игра в жанре шутера от первого лица с элементами RPG,"
                          "разработанная Ubisoft Montreal при участии Ubisoft Shanghai и Ubisoft Massive и"
                          "изданная Ubisoft. Является третьей игрой из одноимённой серии игр.")


@bot.message_handler(commands=['Dishonored'])
def send_Dishonored_info(message):
    bot.reply_to(message, "Dishonored — серия компьютерных игр в жанре action-adventure разработанных"
                          "Arkane Studios и изданных Bethesda Softworks. Франшиза была запущена в 2012"
                          "году с Dishonored. Продолжение, Dishonored 2, было выпущено в 2016 году. Отдельное"
                          "дополнение к Dishonored 2, Death of the Outsider, было выпущено в 2017 году.")


@bot.message_handler(commands=['TheWalkingDead'])
def send_TheWalkingDead_info(message):
    bot.reply_to(message, "The Walking Dead: The Game — эпизодическая графическая приключенческая игра по"
                          "мотивам комикса Роберта Киркмана «Ходячие мертвецы». Игра разработана и издана"
                          "студией Telltale Games. Изначально выход планировался на последние месяцы 2012 года."
                          "Позже релиз The Walking Dead: The Game перенесли на 24 апреля 2012 года.")


@bot.message_handler(commands=['AssassinsCreedIII'])
def send_AssassinsCreedIII_info(message):
    bot.reply_to(message, "Assassin’s Creed III — компьютерная игра из серии Assassin’s Creed в жанре"
                          "action-adventure, разработанная компанией Ubisoft Montreal для платформ PlayStation 3,"
                          "Xbox 360, Wii U, Windows. В игре представлены новый главный герой и новое место действия.")


@bot.message_handler(commands=['Borderlands2'])
def send_Borderlands2_info(message):
    bot.reply_to(message, "Borderlands 2 — компьютерная игра в жанре шутера от первого лица с элементами RPG,"
                          "продолжение компьютерной игры Borderlands. Отличается от своей предшественницы улучшенной"
                          "системой модинга оружия и более продуманным сюжетом.")


@bot.message_handler(commands=['GTAV'])
def send_GTAV_info(message):
    bot.reply_to(message, "Grand Theft Auto V — компьютерная игра в жанре action-adventure с открытым миром,"
                          "разработанная компанией Rockstar North и изданная компанией Rockstar Games.")


@bot.message_handler(commands=['BioShockInfinite'])
def send_BioShockInfinite_info(message):
    bot.reply_to(message, "BioShock Infinite — компьютерная игра в жанре шутера от первого лица с элементами RPG,"
                          "стимпанка и научной фантастики, разработанная студией Irrational Games под руководством"
                          "геймдизайнера Кена Левина.")


@bot.message_handler(commands=['Metro:LastLight'])
def send_MetroLastLight_info(message):
    bot.reply_to(message, "Metro: Last Light — компьютерная игра в жанре постапокалиптического шутера от первого"
                          "лица с элементами survival horror и стелса, разработанная украинской компанией 4A Games"
                          "и изданная британской компанией Deep Silver на Windows, PlayStation 3 и Xbox 360 в мае"
                          "2013 года.")


@bot.message_handler(commands=['AssassinsCreedIV'])
def send_AssassinsCreedIV_info(message):
    bot.reply_to(message, "Assassin’s Creed IV: Black Flag — компьютерная игра в жанре action-adventure,"
                          "разработанная компанией Ubisoft Montreal и изданная Ubisoft. Является шестой основной"
                          "игрой в серии Assassin’s Creed.")


@bot.message_handler(commands=['TheLastOfUs'])
def send_TheLastOfUs_info(message):
    bot.reply_to(message, "The Last of Us Part I — компьютерная игра в жанре action-adventure с элементами"
                          "survival horror и стелс-экшена, разработанная студией Naughty Dog и изданная Sony"
                          "Interactive Entertainment. Является ремейком игры The Last of Us.")


@bot.message_handler(commands=['FarCry4'])
def send_FarCry4_info(message):
    bot.reply_to(message, "Far Cry 4 — компьютерная игра в жанре шутера от первого лица, разработанная студией"
                          "Ubisoft Montreal, при участии Ubisoft Red Storm, Ubisoft Toronto, Ubisoft Shanghai,"
                          "Ubisoft Kyiv и изданная Ubisoft.")


@bot.message_handler(commands=['Wolfenstein:TheNewOrder'])
def send_WolfensteinTheNewOrder_info(message):
    bot.reply_to(message, "Wolfenstein: The New Order — компьютерная игра в жанре шутера от первого лица,"
                          "разработанная шведской компанией MachineGames и изданная Bethesda Softworks в 2014"
                          "году на платформах Windows, PlayStation 3, PlayStation 4, Xbox 360 и Xbox One. Часть"
                          "серии компьютерных игр Wolfenstein.")


@bot.message_handler(commands=['AssassinsCreedUnity'])
def send_AssassinsCreedUnity_info(message):
    bot.reply_to(message, "Assassin’s Creed Unity — компьютерная игра из серии Assassin’s Creed в жанре"
                          "action-adventure, которую разработала компания Ubisoft для платформ PC, PlayStation"
                          "4 и Xbox One. Действие игры разворачивается в Париже в XVIII веке.")


@bot.message_handler(commands=['DarkSoulsII'])
def send_DarkSoulsII_info(message):
    bot.reply_to(message, "Dark Souls II — компьютерная игра в жанре Action/RPG с открытым миром, разработанная"
                          "и выпущенная компанией From Software для Xbox 360, PlayStation 3 и Microsoft Windows в"
                          "2014 году. За пределами Японии изданием игры занималась Bandai Namco. Игра является"
                          "продолжением Dark Souls.")


@bot.message_handler(commands=['Alien:Isolation'])
def send_AlienIsolation_info(message):
    bot.reply_to(message, "Alien: Isolation — компьютерная игра в жанре survival horror c элементами стелса"
                          " разработанная компанией Creative Assembly и изданная компанией Sega. Дистрибьютором"
                          "в России выступила компания «СофтКлаб». Выход игры состоялся 7 октября 2014 года.")


@bot.message_handler(commands=['LOL'])
def send_LOL_info(message):
    bot.reply_to(message, "League of Legends, сокращённо LoL — многопользовательская компьютерная игра в жанре"
                          "MOBA, разработанная и выпущенная американской компанией Riot Games в 2009 году для"
                          "платформ Microsoft Windows и macOS. Игра была разработана по образу и подобию DotA —"
                          "пользовательской карты для Warcraft III.")


@bot.message_handler(commands=['CSGO'])
def send_CSGO_info(message):
    bot.reply_to(message, "Counter-Strike: Global Offensive — многопользовательская компьютерная игра,"
                          "разработанная компаниями Valve и Hidden Path Entertainment. Выпуск игры для"
                          "персональных компьютеров на операционных системах Windows и macOS, также игровых"
                          "приставках Xbox 360 и PlayStation 3 состоялся 21 августа 2012 года.")


@bot.message_handler(commands=['Valorant'])
def send_Valorant_info(message):
    bot.reply_to(message, "Valorant — многопользовательская компьютерная игра, разработанная и издаваемая компанией"
                          "Riot Games. Valorant является первой игрой Riot Games в жанре шутер от первого лица.")


@bot.message_handler(commands=['Overwatch2'])
def send_Overwatch2_info(message):
    bot.reply_to(message, "Overwatch 2 — многопользовательская бесплатная компьютерная игра в жанре геройского шутера"
                          "от первого лица, разрабатываемая и издаваемая компанией Blizzard Entertainment.")


@bot.message_handler(commands=['R6S'])
def send_R6S_info(message):
    bot.reply_to(message, "Tom Clancy’s Rainbow Six Siege — тактический шутер от первого лица, разработанный"
                          "Ubisoft для Windows, Xbox One и PlayStation 4. Игра была анонсирована Ubisoft 9 июня 2014"
                          "года на E3 и выпущена 1 декабря 2015 года, а ровно через пять лет, 1 декабря 2020 года,"
                          "игра вышла для PlayStation 5 и Xbox Series X/S.")


@bot.message_handler(commands=['MetroExodus'])
def send_MetroExodus_info(message):
    bot.reply_to(message, "Metro Exodus — компьютерная игра в жанре шутера от первого лица, разработанная украинской"
                          "компанией 4A Games и изданная Deep Silver. Выход игры состоялся 15 февраля 2019 года для"
                          "игровых платформ ПК, PlayStation 4 и Xbox One.")


@bot.message_handler(commands=['Cyberpunk2077'])
def send_Cyberpunk2077_info(message):
    bot.reply_to(message, "Cyberpunk 2077 — компьютерная игра в жанре action-adventure в открытом мире, разработанная"
                          "и изданная польской студией CD Projekt. Действие игры происходит в 2077 году в Найт-Сити,"
                          "вымышленном североамериканском городе из вселенной Cyberpunk.")


@bot.message_handler(commands=['Stray'])
def send_Stray_info(message):
    bot.reply_to(message, "Stray — приключенческая компьютерная игра, разработанная студией BlueTwelve Studio и"
                          "изданная компанией Annapurna Interactive. Игра вышла 19 июля 2022 года для Windows,"
                          "PlayStation 4 и PlayStation 5. Ранее игра была известна под названиями HK_Project и"
                          "HK-Devblog, которые происходят от давнего блога её разработчиков.")


@bot.message_handler(commands=['RDR2'])
def send_RDR2_info(message):
    bot.reply_to(message, "Red Dead Redemption 2 — компьютерная игра в жанрах action-adventure и шутера от"
                          "третьего лица с открытым миром, разработанная Rockstar Studios и выпущенная Rockstar"
                          "Games для консолей PlayStation 4 и Xbox One 26 октября 2018 года и для персональных"
                          "компьютеров под управлением Windows 5 ноября 2019 года.")


@bot.message_handler(commands=['MinecraftLegends'])
def send_MinecraftLegends_info(message):
    bot.reply_to(message, "Minecraft Legends — компьютерная стратегическая игра, разработанная Mojang Studios и"
                          "Blackbird Interactive и изданная Xbox Game Studios. Релиз игры состоялся 18 апреля 2023"
                          "года для Windows, PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S и Nintendo"
                          "Switch. Это спин-офф Minecraft.")


@bot.message_handler(commands=['GenshinImpact'])
def send_GenshinImpact_info(message):
    bot.reply_to(message, "Genshin Impact — компьютерная игра в жанре action-adventure с открытым миром и"
                          "элементами RPG, разработанная китайской компанией miHoYo Limited. Игра распространяется"
                          "посредством цифровой дистрибуции по модели free-to-play, но имеет внутриигровой магазин,"
                          "использующий реальную валюту.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global rating
    if rating:
        try:
            con = sqlite3.connect('game_rating.db', check_same_thread=False)
            cur = con.cursor()
            year = int(message.text)
            db = cur.execute(f"""SELECT * FROM rating WHERE year = {year}""").fetchall()
            if db:
                bot.send_message(message.chat.id, "Вот рейтинг игр по данным сайта cubiq.ru")
                for i in db:
                    bot.send_message(message.chat.id, f"""{i[0]}. {i[2]}""")
                    rating = False
        except ValueError:
            bot.send_message(message.chat.id, "Что-то не так. Попробуйте сново")
            rating = False
    else:
        bot.reply_to(message, "Извините, такой игры или команды пока что здесь нет."
                              "Введите /help, чтобы узнать доступные команды.")


bot.polling()
