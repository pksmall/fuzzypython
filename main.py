from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def toresult(arr):
  for i in arr:
    print(i)
    print("ratio", fuzz.ratio(str(orig).lower(), str(i).lower()))
    print("part", fuzz.partial_ratio(str(orig).lower(), str(i).lower()))
    print("tkn sort", fuzz.token_sort_ratio(str(orig).lower(), str(i).lower()))
    print("tkn set", fuzz.token_set_ratio(str(orig).lower(), str(i).lower()))
    print(process.extract(str(i).lower(), arr))


arr = [
"Kleenex Туалетная бумага Premium Comfort 4 шт.",
  "KLEENEX PREMIUM CARE ТУАЛЕТНАЯ БУМАГА ЧЕТЫРЕХСЛОЙНАЯ N4",
"Туалетная бумага Kleenex Премиум Комфорт 4 слоя, 4 рулона",
  "Туалетная бумага Premium Comfort 4-слойная, Kleenex, 4 рулона, Швейцария",
"Туалетная бумага Kleenex 4слоя 4рулона",
"Туалетная бумага Kleenex 4-х слойная Премиум Комофрт, 4 шт"
]

orig = "Туалетная бумага Kleenex PremiumCare 4-слойная 4 рулона Швейцария"

toresult(arr)

orig = "Ежедневные гигиенические прокладки Always Незаметная Защита Нормал 20 шт"
arr =["Прокладки Always ежедневные гигиенические Незаметная Защита Normal Duo 20 шт",
"PROCTER & GAMBLE SP. O.O. Прокладки ежедневные женские ALWAYS (Олвейс) Незаметная защита Normal Deo (Нормал део) ароматизированные 20 шт",
"Прокладки ежедневные Always Незаметная защита Normal Single ароматизированные 20шт",
"Ежедневные прокладки Always Normal Duo Незаметная Защита, 20 шт.",
"Ежедневные прокладки Always Незаметная Защита Нормал 20 шт",
"Прокладки ежедневные Always Незаметная Защита Нормал 20 шт.",
"Прокладки ежедневные Always Незаметная защита Normal Single ароматизированные 20шт Германия"
]


toresult(arr)