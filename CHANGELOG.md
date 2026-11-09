# Changelog

All notable changes to the Cognitive Bias Encyclopedia are documented here. Format: [Keep a Changelog](https://keepachangelog.com/). Versions follow [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Added

- **Идентификаторы у всех источников**: в 69 записях каталога каждый буллет секции «Источники» теперь содержит DOI, ISBN или устойчивую ссылку — 283 буллета, из них 207 идентификатора не имели. Формат: `[DOI](https://doi.org/…)` для статей, `ISBN 978…` для книг, `[URL]`/`[PDF]`/`[скан]`/`[оглавление]`/`[выпуск]`/`[журнал]` — для источников без DOI. В `.github/scripts/validate.py` добавлена проверка: булет без `https?://` и без `ISBN` — ошибка
- **Автоматическая пересборка сайта**: workflow `notify-site.yml` отправляет `repository_dispatch` типа `content-update` в `cognitive-bias-site` при каждом пуше в `main`. Требуется секрет `SITE_DISPATCH_TOKEN` (fine-grained PAT с правом Contents: Read and write на репозиторий сайта); без него пересборка пропускается с warning, CI не падает
- **Восемь новых записей** из тира 🟡 среднего приоритета (покрытие 34% → 38%):
  - `Peak-End Rule` — оценка опыта по пику и концу, а не по длительности
  - `Mere Exposure Effect` — симпатия к тому, что мы видим часто
  - `Conjunction Fallacy` — «A и B» кажется вероятнее, чем A
  - `Serial Position Effect` — преемственность и свежесть в запоминании последовательностей
  - `Actor-Observer Bias` — свои действия объясняем ситуацией, чужие — чертами
  - `Rosy Retrospection` — прошлое вспоминается лучше, чем было
  - `Looking-Glass Self` — образ себя через взгляд других (Кули)
  - `Conservatism` — недостаточное пересматривание убеждений
- **Новая запись `Belief Bias`** — предвзятость по убеждению: состоятельность аргумента оценивается по правдоподобию вывода, а не по посылкам. Источники: Evans, Barston & Pollard 1983, Newstead et al. 1992, Evans & Curtis-Holmes 2005, Evans, Handley & Bacon 2009 (покрытие 38% → 39%, 69 → 70 записей)
- **Новая запись `Outcome Bias`** — качество решения оценивается по исходу, а не по тому, каким оно было в момент выбора: одна и та же лотерея после выигрыша кажется хорошим решением, после проигрыша — плохим (Baron & Hershey 1988). Родственные формы: ошибка пропуска (Ritov & Baron 1995; Asch et al. 1994) и вознаграждение удачи в спорте (Gauriot & Page 2019)
- **Новая запись `Contrast Effect`** — оценка объекта определяется тем, с чем его сравнивают: при ожидании сходства сдвиг к сравниваемому (ассимиляция), при ожидании различия — от него (контраст). Механизм якоря объясняется сравнением, а не числовым усреднением (Mussweiler & Strack 1999; Mussweiler 2001, 2003)
- **Новая запись `IKEA Effect`** — самосборка повышает оценку предмета, но только при успешном завершении работы: если собрать и разобрать или не справиться, эффект исчезает (Norton, Mochon & Ariely 2012). Механизм — психологическое владение (Sarstedt et al. 2017) и воспринимаемая компетентность (Mochon et al. 2012); мета-анализ 55 работ (N = 5 454) даёт d = 0,57 (Pelled et al. 2025)
- **Новая запись `Focusing Effect`** — вклад одного фактора в общий результат переоценивается: удовлетворённость жизнью в Калифорнии и в Среднем Западе одинакова, но калифорнийцев ждут более довольными (Schkade & Kahneman 1998); вклад дохода в счастье переоценивается тем же способом (Kahneman et al. 2006). Строку 🟢 «Focusing Illusion» переведена в ⚪: она описывает то же явление, отдельная запись была бы дублем
- **Новая запись `Placebo Effect`** — изменение физического состояния в ожидании лечения: замещающие средства работают через эндогенную опиоидную систему (Benedetti 1997), а Kaptchuk (2002) описывает действующий механизм как «ответ на смысл» — ритуал, отношения и смысл процедуры, а не инертное вещество. Файл записи попал в предыдущий коммит (`447873f`) — здесь закрыта её часть в таксономии, README и CHANGELOG
- **Новая запись `Spacing Effect`** — разнесённые повторения дают лучшее долговременное удержание, чем повторения подряд; величина выигрыша растёт с длиной срока хранения, при долгих сроках выигрывают расширяющиеся интервалы (Cepeda et al. 2006), и эффект работает не только на запоминание, но и на приобретение знания (Cepeda et al. 2008). Техники распределённой практики и тестирования отнесены к высокополезным (Dunlosky et al. 2013)
- **Новая запись `Reminiscence Bump`** — автобиографическая память непропорционально богата событиями 15–25 лет (Rubin, Rahhal & Poon 1998); объяснение — плотность событийной сети (Jansari & Parkin 1996) и связь с идентичностью. Бугор подвижен: второй похожий период жизни способен его оттеснить (Conway & Haque 1999)
- **Новая запись `Mood-Congruent Memory`** — материал, совпадающий с состоянием в момент запоминания, вспоминается лучше; при явно осознанном состоянии эффект ослабевает, при неявном (аффективный фокус) — сохраняется (Rothkopf & Blaney 1991). Эмоциональное возбуждение сужает набор используемых признаков (Easterbrook 1959); вклад миндалины в консолидацию эмоционального материала зависит от состояния (Hamann 2001)
- **Новая запись `Zeigarnik Effect`** — незавершённое удерживается в памяти лучше завершённого: начатая задача оставляет «открытое поле» и специфическое напряжение по полевой теории Левина (Zeigarnik 1927). Эффект работает прежде всего для сожаления о бездействии (Savitsky et al. 1997); незакрытые задачи ухудшают сон через руминацию (Syrek et al. 2017); близость к концу задачи повышает мотивацию вернуться к ней — «эффект Хемингуэя» (Oyama et al. 2018)
- **Новая запись `Bias Blind Spot`** — искажения узнают в чужих решениях, но не в своих: свыше 85 % респондентов считали себя менее предвзятыми, чем «средний американец», и лишь один признал обратное (Pronin, Lin & Ross 2002). Эффект — устойчивая индивидуальная разница, не связанная с качеством решений (Scopelliti et al. 2015); в трёх пре-регистрируемых репликах (N = 969) воспроизведён с эффектом d = −1,00, а вера в свободную волю его усиливает (Chandrashekar et al. 2021)
- **Новая запись `Projection Bias`** — приписывание другим своих качеств, знаний и состояний: телефонный эксперимент показал, что участники считали своё волнение практически нечитаемым, тогда как наблюдатели определяли его заметно точнее (Gilovich, Savitsky & Medvec 1998). Принятие чужой позиции описывается как эгоцентрический якорь со слабой коррекцией (Epley et al. 2004); базовая асимметрия «внутреннее/внешнее» разобрана у Pronin (2008)
- **Новая запись `Impact Bias`** — переоценка силы и длительности будущих эмоциональных реакций: в жилищной лотерее предсказанные различия в счастье через год фактически не проявились (Gilbert et al. 1998). Источники переоценки — фокализм (Wilson et al. 2000), иммунное неведение (Gilbert et al. 1998) и неожиданная скорость осмысления события (Wilson & Gilbert 2005). Разбор мета-анализа Levine et al. (2012) показал, что после исправления ошибок отбора и кодирования эффект сохраняется (Wilson & Gilbert 2013)
- **Новая запись `Egocentric Bias`** — сквозная настройка социального познания: события, доступные из собственного опыта, оцениваются как более частые (Ross & Sicoly 1979); принятие чужой позиции устроено как эгоцентрический якорь со слабой коррекцией (Epley et al. 2004). Возрастная динамика эмоциональной эгоцентричности U-образна и связана с правой надкраевой извилиной (Riva et al. 2016, N = 114); смещение ослабевает, когда задача дана как работа по правилу, а не как «представь, как видит другой» (Samuel et al. 2020)
- **Новая запись `Egocentric Empathy Gap`** — переоценка сходства между своей психологической ситуацией и ситуацией другого: в сделках продавец добавляет к цене эффект владения, а покупатель не может оценить эту добавку, не будучи владельцем (Dunning, Van Boven & Loewenstein 2004). Зеркальная половина — эмпатическая невнимательность: мы недооцениваем, насколько наблюдатели смягчат выводы, если смогут принять нашу перспективу (Epley, Savitsky & Gilovich 2002). Основа механизма — недоступность причин собственных суждений (Nisbett & Wilson 1977) и «висцеральные» факторы (Loewenstein 1996)
- **Новая запись `Cultural Bias`** — суждение чужих практик по нормам своей культуры: между популяциями различия существенны, а WEIRD-образцы оказались выбросами, причём уже у детей (Henrich, Heine & Norenzayan 2010). Эмоции распознаются во всех культурах лучше случайного уровня, но точнее внутри своей группы, и преимущество убывает с ростом контакта между группами (Elfenbein & Ambady 2002, мета-анализ). Отдельная работа посвящена устойчивой предвзятости выборки в детской психологии (Nielsen et al. 2017)
- **Новая запись `Cross-Race Effect`** — чужие лица кодируются грубее и хуже узнаются: мета-анализ 39 работ, 91 выборки и почти 5 000 участников даёт «эффект зеркала» — больше верных узнаваний и меньше ложных для лиц своей расы (Meissner & Brigham 2001). У 129 участников собственный перекос в основном сводился к смещению ответа «я это видел» на чужих лицах, а самоотчёт о недавнем межрасовом опыте коррелировал с общей точностью (Slone, Brigham & Meissner 2000). Объяснение через перцептивное обучение и многомерное «пространство лиц» — у Valentine, Chiroro & Dixon (2017)
- **Новая запись `Deindividuation`** — потеря индивидуальности и личной ответственности в группе: в опыте с конфетами на Хэллоуин больше одной конфеты взяли 60 % анонимных детей группами и лишь 10 % опознаваемых поодиночке. Johnson и Downing (1979) показали, что действует не анонимность, а контекстные сигналы: в облачениях Ку-клукс-клана били сильнее, в форме медсестёр — слабее. Мета-анализ 60 работ не подтвердил ни существование «деиндивидуализированного состояния», ни рост антинормативного поведения: деиндивидуализированные группы сильнее подчиняются ситуативным нормам (Postmes & Spears 1998), что согласуется с моделью социальной идентичности (Reicher, Spears & Postmes 1995)
- **Новая запись `Cheerleader Effect`** — человек в группе воспринимается как привлекательнее, чем поодиночке; эффект впервые описан Walker и Vul (2014, онлайн 2013) и устойчив к времени просмотра, размеру группы и качеству изображения. Механизм: ансамблевое кодирование + привлекательность средних лиц + иерархия зрительной рабочей памяти. GA-эффект группы — d = 0,60 по 33 сравнениям, с лучшим объяснением через избирательное внимание к самым привлекательным (van Osch et al. 2015); на непривлекательных группах эффект **разворачивается** (van Osch & Sleegers 2021). Смещение оказалось **ошибкой памяти, а не восприятия** (Hsieh et al. 2020) и воспроизвелось на 1005 китайских участниках (Peng et al. 2020)
- **Новая запись `Mob Mentality`** — поведение толпы как коллективного субъекта: в опыте Аша (1951) наивные участники отвечали верно 68 % раз и соглашались с неверным ответом 32 % раз, тогда как в контрольной группе верные ответы составили более 99 %. Мета-анализ 133 работ из 17 стран показал снижение конформности в американских выборках с 1950-х годов и более высокий её уровень в коллективистских странах (Bond & Smith 1996). В онлайн-эксперименте на 100 000+ публикаций ложный первый плюс завышал последующие рейтинги: первый прочитавший комментарий с вероятностью 32 % поставил бы плюс, если бы он уже стоял (Muchnik, Aral & Taylor 2013). Достаточно 5 % «уверенно выглядящих» инструктированных людей, чтобы направить 95 % толпы из 200 добровольцев (Dyer et al. 2009). Современный подход социальной идентичности описывает толпу как сдвиг идентичности, а не утрату «я» (Drury & Reicher 2020)
- **Новая запись `Change Blindness`** — незамеченные изменения в зрительной сцене: словесная подсказка о месте изменения резко ускоряет обнаружение, что доказывает необходимость внимания (Rensink, O'Regan & Clark 1997); не меняющийся элемент среди мерцающих обнаруживается надёжно (Theeuwes 2004). Маскирующие вставки работают как скачки глаза (O'Regan, Rensink & Clark 1999), а в задаче выбора лица несовпадение между выбором и показанным заметили лишь 26 % (Johansson et al. 2005). Слепота к изменениям способна приводить к ошибочному опознанию свидетеля (Nelson et al. 2011). Главный механизм по Simons & Levin (1997) — ложная уверенность в полноте восприятия
- **Проверка длины секций** в `.github/scripts/validate.py`: подсчёт слов по восьми контентным секциям и сравнение с минимумом из `ru/CONTRIBUTING.md` §3.4. Обычный запуск даёт предупреждения, `--strict` превращает их в ошибку
- **Перекрёстные ссылки** из восьми существующих записей на новые — по правилу антиизоляции (CONTRIBUTING §6.3)

### Changed

- **Контракт объёма секций** в `ru/CONTRIBUTING.md` §3.4 переписан: вместо недостижимых 100–200 / 200–400 слов — фактические границы p10–p90 по текущим 69 записям. Старый контракт не выполнялся ни одной записью ни в одной из восьми секций

### Fixed

- **20 атрибуций в 17 записях** исправлены по зарегистрированным метаданным DOI (журнал, том, выпуск, страницы, название): `Backfire Effect` (Nyhan & Reifler → *Political Behavior* 32(2)), `Better-Than-Average Effect` и `Overconfidence Effect` (Moore → *OBHDP* 102(1)), `Cognitive Dissonance` (Aronson 1969 → AESP v2, pp. 1-34), `Effort Justification` (Aronson & Mills → *JASPP* 59(2)), `Endowment Effect` и `Status Quo Bias` (Kahneman et al. 1991 → «Anomalies: …»), `Hot-Cold Empathy Gap` (Van Boven → *OBHDP* 96(2)), `Illusion of Control` (Thompson 1999 → *CDPS* 8(6)), `Mere Exposure Effect` (Bornstein → *Psychological Bulletin* 106(2)), `Naive Cynicism` (Kruger & Gilovich → *JPSP* 76(5)), `Normalcy Bias` (Omer & Alon → *American Journal of Community Psychology* 22(2), «disaster and trauma»), `Overconfidence Effect` (Lichtenstein → глава в *Judgment under Uncertainty*, pp. 306-334), `Planning Fallacy` (Kahneman & Tversky → там же, pp. 414-421; Buechel → *Psychological Science* 29(11)), `Pygmalion Effect` и `Self-Fulfilling Prophecy` (Rosenthal & Jacobson → *The Urban Review* 3(1); Rosenthal 1994 → *CDPS* 3(6); McNatt → *Journal of Applied Psychology* 85(2)), `Reactance` (Miller et al. → *Human Communication Research* 33(2)), `Conjunction Fallacy` (Tversky & Kahneman 1983 → «Extensional versus intuitive reasoning: The conjunction fallacy»)
- **6 несуществующих веб-источников заменены** на существующие: `Barnum-Forer Effect` (Sullivan 2013 → French et al. 1991, PDF в *Skeptical Inquirer*), `Frequency Illusion` (Mowatt → Bellows, Damn Interesting; Zwicker → Zwicky, Language Log через archive.org), `Mandela Effect` (Broome → Broome 2010 на MandelaEffect.com; French 2019 → Polidoro 2022; Lanman 2020 → West 2024). Все новые ссылки проверены — HTTP 200 с содержимым
- **2 ссылки указывали на несуществующие публикации**: `Conjunction Fallacy` — «Human inference» в *American Psychologist* 35(7), 711-721 (июль 1980 — это стр. 603-683 по ключу пагинации тома; работа вышла монографией Prentice-Hall, ISBN 9780134451305); `Source Confusion` — Mather et al. (2000) → реальная работа 1997 года, *Memory & Cognition* 25(6), 826-837
- **Mealy & Tenove (2020)**: атрибуция не подтверждается — в *CJPS* 53(4) страницы 821-838 заняты другой статьёй, а в Crossref нет ни одной записи Mealy/Tenove за 2020 год. Ссылка ведёт на оглавление выпуска; источник требует подтверждения или замены (см. ISSUE-24 в трекере сайта)
- **Факт-чекинг восьми новых записей** по первоисточникам (сканы `Thinking, Fast and Slow` Ch. 5 и Ch. 15, Ch. 35; статьи на Wikipedia). Исправлены выдуманные примеры и неверные числа:
  - `Peak-End Rule` — эксперимент с холодным прессором был описан наоборот: у Канамана 80% испытуемых выбрали повторить **длинный** эпизод (60 с ледяной воды + 30 с постепенного облегчения), потому что для помнящего он лучше закончился. Убран выдуманный пример со стоматологом
  - `Mere Exposure Effect` — вместо выдуманного опыта с иероглифами реальный эксперимент Зайонца с «турецкими» словами в газетах Мичигана; убрано неверное утверждение, что неприятие от частого контакта сглаживается (для изначально неприятных объектов знакомство усиливает неприятие)
  - `Conjunction Fallacy` — вместо выдуманных чисел («85% против 60%», «0,6 × 0,25 = 0,15») фактические данные из Ch. 15: 85–90% студентов и 85% выпускников бизнес-школы ошибались, правильно ответили 64% аспирантов Стэнфорда и Беркли. «Грегори Стивенс» заменён на Стивена Джея Гулда с реальной цитатой
  - `Conservatism` — несуществующий «эксперимент с форелью» заменён на эксперимент Эдвардса (1968) с пакетами фишек; убрана неверная ссылка на Kahneman Ch. 19/21; в параллелях Канта вместо отсылки к Sonderbund и цитаты на китайском языке — *sapere aude*
  - `Actor-Observer Bias` — исправлено то, что показывает мета-анализ Малле (2006): асимметрия в предсказанном виде не подтверждается. Авторство гипотезы: Джонс и Нisbett (1971), а не Джонс и Харрис (1967)
  - `Rosy Retrospection` — добавлены измеримые результаты (двухчасовые оценки состояния за две недели; оценка отпуска до, во время и после поездки); *anamnesis* приписан Платону, а не Аристотелю
  - `Looking-Glass Self` — убрано английское слово «faces» из прозы, исправлен заголовок «Отставка во взгляде»
- **Атрибуции глав** в 22 записях сверены с первоисточниками (PDF-сканы `Thinking, Fast and Slow` и `The Art of Thinking Clearly`, оглавления извлечены `pdftotext`):
  - Kahneman: `Anchoring` (Ch. 2, 11 → Ch. 11), `Availability Heuristic` (→ Ch. 12, 13), `Base Rate Fallacy` (Ch. 14 без названия → с названием), `Dunning-Kruger` (Ch. 24 → Ch. 19, 20, 21), `Overconfidence Effect` (→ Ch. 19, 20, 21, 23), `Planning Fallacy`, `Optimism Bias`, `Illusion of Control`, `Hindsight Bias`, `Halo Effect` (несуществующее «Ch. 14 (Daniel Kahneman's Bio)» → Ch. 7), `Survivorship Bias` (несуществующее «Ch. 8 (Little Strokes of Fortune)» → Ch. 7), `Self-serving Bias` (→ Ch. 35), `Confirmation Bias` (→ Ch. 7, 23), `Framing Effect` (Ch. 25 → Ch. 34, 26), `Loss Aversion`, `Sunk Cost Fallacy` (Ch. 30 → Ch. 23, 32)
  - Dobelli: номера глав исправлены на английское издание 2013 года (99 глав) во всех 12 затронутых записях — в каталоге стояли номера из немецкого издания (52 главы) или выдуманные
  - Haidt: `Motivated Reasoning` (Ch. 7 → Ch. 2 «The Intuitive Dog and Its Rational Tail»)
- **29 секций в 21 записи** дописаны до минимума контракта: механизмы, философские параллели, диалектические зеркала, примеры и приёмы смягчения
- **validate.py**: `AGENTS = RU_DIR / "AGENTS.md"` указывал на несуществующий файл (переименован в `CONTRIBUTING.md`); в `EXTERNAL_LINKS` `"AGENTS"` заменено на `"CONTRIBUTING"`, чтобы устаревшая ссылка ловилась валидатором. Добавлена проверка существования `CONTRIBUTING.md` и `4. Таксономия.md` — переименование этих файлов теперь ломает CI, а не проходит молча
- **Битые ссылки после переименования AGENTS.md → CONTRIBUTING.md**: `[[AGENTS]]` в `ru/4. Таксономия.md` → `[[CONTRIBUTING]]`; в схемах структуры (`README.md`, `ru/CONTRIBUTING.md`) исправлено имя файла; markdown-ссылки `[AGENTS.md](../../AGENTS.md)` в `ru/CONTRIBUTING.md` вели на несуществующий путь — заменены на wiki-ссылку `[[AGENTS]]` (корневой AGENTS.md лежит в Obsidian-хранилище, вне репозитория)
- **Форматирование**: убран trailing whitespace в CHANGELOG, восстановлен горизонтальный разделитель `---` в записи [0.3] (слипся с текстом пункта), в `ru/0`…`ru/3` возвращена пустая строка после `---` — как в остальных файлах

- **OG image generation**: refactored from Astro integration hook (which failed with "Vite module runner has been closed") to standalone Node script. Generates 62 PNGs (61 entries + default) using `@fontsource/inter` instead of a broken bundled WOFF
- **Repository structure**: removed `scripts/symlink-content.sh` (machine-specific, replaced by `CONTENT_PATH` env var)
- **Dependencies**: removed unused `@astrojs/rss` and `flowbite` packages; added `@fontsource/inter` for OG generation
- **Documentation**: created `en/` skeleton (AGENTS.md + CONTRIBUTING.md) for the planned English translation
- **Documentation**: renamed `ru/AGENTS.md` → `ru/CONTRIBUTING.md` to disambiguate from the root `AGENTS.md` (the encyclopedia-specific file describes how to contribute, the root describes vault-wide agent rules)
- **Documentation**: updated site README with current architecture (post-OG-fixes)

### Migration planned (not done in this release)

- `loadAllBiases()` → Astro Content Collections. Plan documented in `docs/MIGRATION_TO_CONTENT_COLLECTIONS.md`. Current implementation is functional but uses direct file reads instead of Astro's built-in collection API. Target: ~4-6 hours of focused work.

---

## [0.4] — 2026-07-29

### Fixed

- **Search bug**: search input button was hidden below 1024px breakpoint — mobile users had no access to search. Now icon is always visible; "Поиск..." label appears from 640px+
- **Search magnifier icon**: Pagefind renders the magnifier via `.pagefind-ui__form::before` with `mask-image` (not `background-image`). My earlier `background-image: none` fix didn't work. Replaced with `display: none !important` on the `::before` pseudo-element
- **Search results highlighting**: added yellow `<mark>` styling (yellow-200 / yellow-600 in dark mode) for matched terms in result titles and excerpts
- **Pagination**: added pagination to `/biases/` (pageSize 24) and category pages. URLs: `/biases/`, `/biases/page/2/`, `/categories/<name>/`, `/categories/<name>/page/2/`
- **Description rendering**: extended `renderMarkdown()` to accept `base` parameter; catalog wiki-links now produce kebab-case URLs (`availability-heuristic`) with the correct base prefix; non-catalog wiki-links (e.g. `[[Диалектическое мышление]]`) render as plain italic text instead of broken 404 links
- **OG description**: was leaking raw markdown (`**bold**`) and was truncated mid-word. Now uses `stripMarkdown()` + `truncateDescription()` (cuts at sentence boundary within 155 chars)
- **Footer links**: `CONTRIBUTING.md` and `LICENSE` now point to GitHub repo (they don't exist on the deployed site)
- **Internal links**: fixed `404` issues on category links by adding missing `/categories/` index page

### Changed

- **Navbar logo**: changed from "Cognitive Bias Encyclopedia" / "CBE" to "Энциклопедия" (with full name in `sr-only` span for screen readers)
- **Home page H1**: changed from "Cognitive Bias Encyclopedia" to "Энциклопедия когнитивных искажений"
- **Header consistency**: fixed `Dunning-Kruger.md` H1 from "Dunning-Kruger Effect" to "Dunning-Kruger" (matches the filename and the 11 inbound `[[Dunning-Kruger]]` wiki-links)
- **Definition lengths**: expanded 5 shortest definitions (Optimism Bias, Loss Aversion, Backfire Effect, In-group Bias, Anchoring) from <30 words to 40-80 words. Compressed 4 longest definitions (Motivated Reasoning, Barnum-Forer, Mandela, Hawthorne) by moving historical context into "Пример" section

### Added

- `src/components/Pagination.astro` — reusable pagination component
- `src/components/Search.astro` — fullscreen modal overlay for Pagefind search (replaces inline `<div>` that was invisible)
- `scripts/generate-og.ts` — standalone OG image generator (run via `npm run og` after `astro build`)

### Content quality

- Fixed 5 quote attribution errors:
  - `Reactance`: Сартр → Камю (`L'Homme révolté` is Camus, not Sartre)
  - `Cognitive Dissonance`: rephrased dubious Nietzsche quote as paraphrase
  - `Motivated Reasoning`: rephrased dubious Nietzsche quote as paraphrase
  - `Mandela Effect`: kept Nietzsche but marked as paraphrase (no verbatim quote)
  - `Frequency Illusion`: removed duplicated Nietzsche paraphrase
  - `In-group Bias`: cited Kant's categorical imperative properly (*Основы метафизики нравов*, 1785)
- Removed `[[Доказательство отсутствия Бога как создателя]]` (article doesn't exist) from 9 entries (FAE + 8 others)
- Added back-links to 18 orphaned entries (now 0 orphans in the catalog graph)
- Renamed `## Дialectical mirror` → `## Диалектическое зеркало` across all 61 entries (typo fix)
- Translated English fragment-indicators (e.g. "Diversify your sources", "Reading across the aisle") to Russian; kept academic psychology terms (e.g. "Cognitive dissonance reduction", "Diffusion of responsibility") as-is

---

## [0.3] — 2026-07-05

### Added

- Initial multilingual structure with `ru/` and planned `en/`
- 10-section template documented in `ru/AGENTS.md`
- Inline metadata convention (`**Status:**`, `**Date:**`, `**Tags:**`) instead of YAML frontmatter

---

## [0.2] — 2026-07-05

### Added

- 29th entry (Authority Bias) — first entry to follow the formalized AGENTS.md template
- Strict template rules: 10 sections in fixed order, H1 format `# English (Русский)`, category taxonomy (6 canonical categories)

---

## [0.1] — Initial

### Added

- 34 cognitive biases in Russian (initial commit)
- Obsidian-vault structure with inline metadata
- CC BY-SA 4.0 license