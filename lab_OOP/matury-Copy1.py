
import pandas as pd


def compared(dictionary: dict, keyword: str):
    for k, v in dictionary.items():
        if k.startswith(keyword):
            print(f"{k} : {v}")

def results(dict1:dict,dict2:dict):
    new_dict = {}
    one_dict = {}
    for (k1, v1), (k2, v2) in zip(dict1.items(), dict2.items()):
        new_dict[k1[:4]] = k1[4:] + str(v1)
        one_dict[k2[:4]] = k2[4:] + str(v2)
    for (kk, vv), (kk1, vv1) in zip(new_dict.items(), one_dict.items()):
        print(f"{kk} : {vv}")


df = pd.read_excel("ujass.xlsx")

X = df.to_numpy()

rows_list = []
values = []

for row in X:
    rows = ([row[3], row[2], row[4]])
    rows = (' '.join(str(row) for row in rows))
    rows_list.append(rows)
    value = row[5]
    values.append(value)

dictionary_2025 = dict(zip(rows_list, values))

df = pd.read_excel("edited.xlsx")
#df = pd.read_excel("ed_27.xlsx")
data_dict = df.to_numpy()
mapper_data = {}
index_1 = []
index_2 = []
index_3 = []
index_4 = []
for el in data_dict:
    mapper_data[el[1], el[2], el[3]] = el[4]
    index_1.append(el[1])
    index_2.append(el[2])
    index_3.append(el[3])
    index_4.append(el[4])

df_1 = pd.read_excel("ball.xlsx")
data_dict_1 = df_1.to_numpy()
mapper_data_2 = {}
element_1 = []
info_list = []
element_4 = []
mapper_data_dict_1 = {}

for y in data_dict_1:
    mapper_data_2[y[0], y[1], y[3]] = y[4:]
    element_1.append(y[1])
    info_list.append(y[2])
    element_4.append(y[4])

string_w = dict(zip(index_2, index_4))
stright_y = dict(zip(element_1, element_4))

A = sorted(string_w.items(), key=lambda x: x[0])
B = sorted(stright_y.items(), key=lambda x: x[0])

concatenated_mapper = {}
for y in data_dict:
    concatenated_mapper[str(y[2]) + " " + y[1] + " " + y[3]] = y[4]

concatenated_mapper_2 = {}
for z in data_dict_1:
    concatenated_mapper_2[str(z[1]) + " " + z[0] + " " + z[2]] = z[4]


while True:
    try:
        convertor = {6: 50, 5: 39, 4: 26, 3: 15, 2: 0}

        print("Въведи оценките от дипломата!")

        math = int(input("Математика :"))
        bel = int(input("БЕЛ :"))
        phz = int(input("Физика :"))
        ic = int(input("История :"))
        kt = int(input("Ком. моделиране и ИТ :"))
        fl = int(input("Чужд език :"))
        music = int(input("Музика :"))
        ii = int(input("Изобразително искуство :"))
        bio = int(input("Биология :"))
        geo = int(input("География :"))
        fv = int(input("Физическо възпитание :"))
        chem = int(input("Химия :"))
        tp = int(input("Технологии и предприемчество :"))

        if (
            math in convertor.keys()
            and bel in convertor.keys()
            and phz in convertor.keys()
            and ic in convertor.keys()
            and kt in convertor.keys()
            and fl in convertor.keys()
            and bio in convertor.keys()
            and geo in convertor.keys()
            and fv in convertor.keys()
            and chem in convertor.keys()
            and tp in convertor.keys()
        ):
            math_points = convertor[math]
            bel_points = convertor[bel]
            phz_points = convertor[phz]
            ic_points = convertor[ic]
            kt_points = convertor[kt]
            fl_points = convertor[fl]
            music_points = convertor[music]
            bio_points = convertor[bio]
            geo_points = convertor[geo]
            fv_points = convertor[fv]
            chem_points = convertor[chem]
            tp_points = convertor[tp]
            ii_points = convertor[ii]

            break

    except (KeyError, ValueError):
        print("Въведи цяло число от 2 до 6!")

while True:
    try:
        print()

        special_exams = False

        math_exam = float(input("Въведи оценка от НВО - Математика:  "))
        bel_exam = float(input("Въвди оценка от НВО - БЕЛ:  "))
        specials_array = {
            "music_exam": 1.0,
            "ii_exam": 1.0,
            "fv_exam": 1.0,
            "bio_exam": 1.0,
            "chem_exam": 1.0,
            "phz_exam": 1.0,
            "geo_exam": 1.0,
        }
        print(
            "Ако кандидатствате за профилирана гимназия с доп. НВО изберте '1' ако не '0"
        )

        additional = int(input("Въведи:  "))

        if additional == 1:
            special_exams = True
            while True:
                try:
                    specials_array = {
                        "music_exam": 1.0,
                        "ii_exam": 1.0,
                        "fv_exam": 1.0,
                        "bio_exam": 1.0,
                        "chem_exam": 1.0,
                        "phz_exam": 1.0,
                        "geo_exam": 1.0,
                    }
                    flag = False
                    for _ in range(int(input("Въведи брой на доп. НВО:   "))):
                        nvo_1 = input(
                            "Въведи music_exam, ii_exam, fv_exam, bio_exam, chem_exam, phz_exam:"
                        )
                        special_nvo = float(input("Въведи оценка от НВО (0 - 100):   "))
                        if nvo_1 in specials_array.keys() and special_nvo <= 100:
                            specials_array[nvo_1] = special_nvo
                            flag = True
                    if flag:
                        break
                except (KeyError, ValueError, IndexError):
                    print("Въведете валидни данни")

        if 0 < math_exam <= 100 and 0 < bel_exam <= 100:
            break

    except (
        IndexError,
        ValueError,
    ):
        print("Въведи влидни данни - от 0 до 100")

print(math_exam)
print(bel_exam)

if special_exams:
    for key, value in specials_array.items():
        if value > 0:
            print(f"{key}: {value}")

mapper_convertor = {
    "(3 * БЕЛ + 1 * МАТ) + (1 * ФВС + 1 * ЧЕз)": 3 * bel_exam
    + math_exam
    + fv_points
    + fl_points,
    "(1 * БЕЛ + 1 * МАТ + 2 * ИИ) + (1 * ИИ + 1 * КМИТ)": bel_exam
    + math_exam
    + 2 * specials_array["ii_exam"]
    + ii_points
    + kt_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * ИЦ + 1 * ГИ)": 2 * bel_exam
    + 2 * math_exam
    + bel_points
    + geo_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЕЛ + 1 * ГИ)": 2 * bel_exam
    + 2 * math_exam
    + bel_points
    + geo_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ГИ + 1 * КМИТ)": 2 * bel_exam
    + 2 * math_exam
    + geo_points
    + kt_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЗО + 1 * ХООС)": 3 * bel_exam
    + math_exam
    + bio_points
    + chem_points,
    "(1 * БЕЛ + 3 * МАТ) + (1 * БЕЛ + 1 * М)": 3 * math_exam
    + bel_exam
    + bel_points
    + math_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * КМИТ + 1 * ЧЕз)": 3 * bel_exam
    + math_exam
    + kt_points
    + fl_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * ИЦ + 1 * Муз.)": 3 * bel_exam
    + math_exam
    + ic_points
    + music_points,
    "(1 * БЕЛ + 1 * МАТ + 2 * МУЗ) + (1 * БЕЛ + 1 * Муз.)": bel_exam
    + math_exam
    + 2 * specials_array["music_exam"]
    + bel_points
    + music_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ГИ + 1 * БЗО)": 2 * bel_exam
    + 2 * math_exam
    + geo_points
    + bio_points,
    "(1 * БЕЛ + 2 * МАТ + 1 * НПМГ, Ф) + (1 * М + 1 * ФА) или (1 * БЕЛ + 2 * МАТ + 1 * ФИЗ, ОК) + (1 * М + 1 * ФА)": bel_exam
    + 2 * math_exam
    + specials_array["phz_exam"]
    + math_points
    + phz_points,
    "(1 * БЕЛ + 3 * МАТ) + (1 * БЗО + 1 * ХООС)": bel_exam
    + 3 * math_exam
    + bio_points
    + chem_points,
    "(1 * БЕЛ + 1 * МАТ + 2 * БИО, ОК) + (1 * БЗО + 1 * ХООС) или (1 * БЕЛ + 1 * МАТ + 2 * НПМГ, Б) + (1 * БЗО + 1 * ХООС)": bel_exam
    + math_exam
    + 2 * specials_array["bio_exam"]
    + bio_points
    + chem_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЕЛ + 1 * КМИТ)": 2 * bel_exam
    + 2 * math_exam
    + bel_points
    + kt_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * ИЦ + 1 * КМИТ)": 3 * bel_exam
    + math_exam
    + ic_points
    + kt_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * ГИ + 1 * ТП)": 3 * bel_exam
    + math_exam
    + geo_points
    + tp_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * ИИ + 1 * КМИТ)": 3 * bel_exam
    + math_exam
    + bio_points
    + chem_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * ИЦ + 1 * ЧЕз)": 3 * bel_exam
    + math_exam
    + ic_points
    + fl_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * ГИ + 1 * ЧЕз)": 3 * bel_exam
    + math_exam
    + geo_points
    + fl_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЕЛ + 1 * М)": 3 * bel_exam
    + math_exam
    + bel_points
    + math_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ИИ + 1 * ТП)": 2 * bel_exam
    + 2 * math_exam
    + ii_points
    + tp_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЗО + 1 * ЧЕз)": 3 * bel_exam
    + math_exam
    + bio_points
    + fl_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ИЦ + 1 * ГИ)": 2 * bel_exam
    + 2 * math_exam
    + ic_points
    + geo_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЕЛ + 1 * КМИТ)": 3 * bel_exam
    + math_exam
    + bel_points
    + kt_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * ГИ + 1 * КМИТ)": 3 * bel_exam
    + math_exam
    + geo_points
    + kt_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЕЛ + 1 * БЗО)": 2 * bel_exam
    + 2 * math_exam
    + bel_points
    + bio_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ГИ + 1 * ЧЕз)": 2 * bel_exam
    + 2 * math_exam
    + geo_points
    + fl_points,
    "(1 * БЕЛ + 2 * МАТ + 1 * ХИМ, ОК) + (1 * БЗО + 1 * ХООС) или (1 * БЕЛ + 2 * МАТ + 1 * НПМГ, Х) + (1 * БЗО + 1 * ХООС)": bel_exam
    + 2 * math_exam
    + specials_array["chem_exam"]
    + bio_points
    + chem_points,
    "(1 * БЕЛ + 3 * МАТ) + (1 * БЕЛ + 1 * ГИ)": bel_exam
    + 2 * math_exam
    + bel_points
    + geo_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * М + 1 * ГИ)": 2 * bel_exam
    + 2 * math_exam
    + math_points
    + geo_points,
    "(1 * БЕЛ + 1 * МАТ + 2 * СПО) + (1 * БЗО + 1 * ЧЕз)": bel_exam
    + math_exam
    + 2 * specials_array["fv_exam"]
    + bio_points
    + fl_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ИИ + 1 * КМИТ)": 2 * bel_exam
    + 2 * math_exam
    + ii_points
    + kt_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЗО + 1 * ХООС)": 2 * bel_exam
    + 2 * math_exam
    + bio_points
    + chem_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЕЛ + 1 * ЧЕз)": 2 * bel_exam
    + 2 * math_exam
    + bio_points
    + chem_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЕЛ + 1 * БЗО)": 3 * bel_exam
    + math_exam
    + bel_points
    + bio_points,
    "(1 * БЕЛ + 1 * МАТ + 2 * СПО) + (1 * БЗО + 1 * ФВС)": bel_exam
    + math_exam
    + 2 * specials_array["fv_exam"]
    + bio_points
    + fv_points,
    "(1 * БЕЛ + 1 * МАТ + 2 * ИИ) + (1 * БЕЛ + 1 * ИИ)": bel_exam
    + math_exam
    + 2 * specials_array["ii_exam"]
    + bel_points
    + ii_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ГИ + 1 * ТП)": 2 * bel_exam
    + 2 * math_exam
    + geo_points
    + tp_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЕЛ + 1 * ИЦ)": 3 * bel_exam
    + math_exam
    + bel_points
    + ic_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ФА + 1 * БЗО)": 2 * bel_exam
    + 2 * math_exam
    + phz_points
    + bio_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЗО + 1 * ЧЕз)": 2 * bel_exam
    + 2 * math_exam
    + bio_points
    + fl_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЕЛ + 1 * ИИ)": 2 * bel_exam
    + 2 * math_exam
    + bel_points
    + ii_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЕЛ + 1 * ИИ)": 3 * bel_exam
    + math_exam
    + bel_points
    + ii_points,
    "(1 * БЕЛ + 1 * МАТ + 2 * ИИ) + (1 * ИИ + 1 * ЧЕз)": bel_exam
    + math_exam
    + 2 * specials_array["ii_exam"]
    + ii_points
    + fl_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЕЛ + 1 * ГИ)": 3 * bel_exam
    + math_exam
    + bel_points
    + geo_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * М + 1 * КМИТ)": 2 * bel_exam
    + 2 * math_exam
    + math_points
    + kt_points,
    "(1 * БЕЛ + 3 * МАТ) + (1 * М + 1 * ФА)": bel_exam
    + 3 * math_exam
    + math_points
    + phz_points,
    "(1 * БЕЛ + 3 * МАТ) + (1 * БЗО + 1 * ИИ)": bel_exam
    + 3 * math_exam
    + bio_points
    + ii_points,
    "(1 * БЕЛ + 3 * МАТ) + (1 * ФА + 1 * ИИ)": bel_exam
    + 3 * math_exam
    + phz_points
    + ii_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * КМИТ + 1 * ЧЕз)": 2 * bel_exam
    + 2 * math_exam
    + kt_points
    + fl_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЕЛ + 1 * ФВС)": 3 * bel_exam
    + math_exam
    + bel_points
    + fv_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЕЛ + 1 * ИЦ)": 2 * bel_exam
    + 2 * math_exam
    + bel_points
    + ic_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * КМИТ + 1 * ТП)": 2 * bel_exam
    + 2 * math_exam
    + kt_points
    + tp_points,
    "(1 * БЕЛ + 3 * МАТ) + (1 * М + 1 * КМИТ)": bel_exam
    + 3 * math_exam
    + math_points
    + kt_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * М + 1 * ФА)": 2 * bel_exam
    + 2 * math_exam
    + math_points
    + phz_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЗО + 1 * ИИ)": 3 * bel_exam
    + math_exam
    + bio_points
    + ii_points,
    "(1 * БЕЛ + 1 * МАТ + 1 * НПМГ, Х + 1 * НПМГ, Б) + (1 * БЗО + 1 * ХООС)": bel_exam
    + math_exam
    + specials_array["chem_exam"]
    + specials_array["bio_exam"]
    + bio_points
    + chem_points,
    "(3 * БЕЛ + 1 * МАТ) + (1 * БЕЛ + 1 * ЧЕз)": 3 * bel_exam
    + 1 * math_exam
    + math_points
    + fl_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * М + 1 * ЧЕз)": 2 * bel_exam
    + 2 * math_exam
    + bio_points
    + math_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * БЕЛ + 1 * М)": 2 * bel_exam
    + 2 * math_exam
    + bel_points
    + math_points,
    "(1 * БЕЛ + 2 * МАТ + 1 * ГЕО, ОК) + (1 * М + 1 * ГИ) или (1 * БЕЛ + 2 * МАТ + 1 * НПМГ, Г) + (1 * М + 1 * ГИ)": bel_exam
    + 2 * math_exam
    + specials_array["geo_exam"]
    + math_points
    + geo_points,
    "(2 * БЕЛ + 2 * МАТ) + (1 * ФА + 1 * КМИТ)": 2 * bel_exam
    + 2 * math_exam
    + phz_points
    + kt_points,
    "(1 * БЕЛ + 1 * МАТ + 2 * МиФВС) + (1 * БЕЛ + 1 * Муз.)": bel_exam
    + math_exam
    + 2 * specials_array["fv_exam"]
    + bel_points
    + music_points,
}
print()
print(
    "Списък с постигнатият бал, на база оценките"
    "\n"
    "от дипломата и резултата от НВО, в зависимост"
    "\n"
    "от всички възможни комбинации за балообразуване."
    "\n"
    "Данните са сортирани по низхдящ ред (Наи-висок -> Наи-нисък)"
)
print()
for result in sorted(mapper_convertor.items(), key=lambda kvp: round(-kvp[1], 2)):
    print(f"{result[0]:<90} : {result[1]:>5.2f}")
print()
print(
    f"Резултати от минималните балове за класиране по училища:"
    "\n"
    "за предходна година."
)
print()
las_score = []
for k, v in dictionary_2025.items():
    las_score.append(v)
    print(f"{k:<110} : {v:>7.2f}")
print()
print()
final_mapper = {}
for key, value in concatenated_mapper_2.items():
    if value in mapper_convertor.keys():
        value = mapper_convertor[value]
        final_mapper[key] = value

print()
print(f"Сортирани резултати от най-високият по училища.")
print()
for element in sorted(final_mapper.items(), key=lambda kvp: -kvp[1]):
    print(f"{element[0]:<110}:{element[1]:>7.2f}")
print()
print()
print(
    "Въвеждане на код за сравнвние на постигнатия бал на учника"
    "\n"
    "с минималнит бал за прием от предходната година. Изберете кода"
    "\n"
    "пред името на училището от списъка по-горе."
)
print()
while True:
    print()
    code = input(
        "Вевдете, код на училището, толкова пъти,"
        "\n"
        "за колкото рзултата искате да направите проврката."
        "\n"
        "За да прекратите въвеждането въведете END.- Въведи код!: "
    )
    if code == "END":
        break
    print()
    print("Вашият резултат:")
    compared(final_mapper, code)
    print()
    print("Минимален бал от предходха година:")
    compared(dictionary_2025, code)
    print()

print()
print()
print("Сравнение на бала с този от предходния период по училища.")
print()
print()
print("Код---------------------------------------------Училише---------------------------------------Бал минала година/Постигнат Бал")
print("-----------------------------------------------------------------------------------------------------------------------------")
key2_list = []
value2_list = []
value1_list = []
for (key_1, value_1), (key_2, value_2) in zip(
    final_mapper.items(), dictionary_2025.items()
):
    if value_1 >= value_2:

        key2_list.append(key_2)
        value2_list.append(value_2)
        value1_list.append(value_1)
        #print(f"{key_2:<100} : [{value_2:>5.2f} : {value_1:>5.2f}]")
print()
print()

results(final_mapper, dictionary_2025)








