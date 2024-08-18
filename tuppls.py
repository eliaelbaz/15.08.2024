# a
tup_a = (99,);
print("Part a:", tup_a);

# b
tup_b = (77, 88, 99);
print("Part b:", tup_b);

# c
def tuple_length(t: tuple) -> int:
    return len(t);

print("Part c:", tuple_length(tup_b));

# d
def tuple_concat(t1: tuple, t2: tuple) -> tuple:
    return t1 + t2

t1 = (1, 2, 3);
t2 = (4, 5, 6);
print("Part d:", tuple_concat(t1, t2));

# e
def tuple_intersection(t1: tuple, t2: tuple) -> tuple:
    return tuple(set(t1) & set(t2));

t3 = (3, 4, 5);
print("Part e:", tuple_intersection(t1, t3));

# f
def tuple_difference(t1: tuple, t2: tuple) -> tuple:
    return tuple(set(t1) - set(t2));

print("Part f:", tuple_difference(t1, t3));

# g
def get_element_at_index(t: tuple, index: int):
    return t[index] if 0 <= index < len(t) else None;

print("Part g:", get_element_at_index(t1, 1));
print("Part g:", get_element_at_index(t1, 10));

# h
def reverse_tuple(t: tuple) -> tuple:
    return t[::-1];

print("Part h:", reverse_tuple(t1));

# i
def count_and_divisors(t: tuple, number: int) -> int:
    return sum(1 for item in t if item % number == 0);

t4 = (10, 20, 30, 40, 50);
print("Part i:", count_and_divisors(t4, 10));

# j
def multiply_tuple(t: tuple, multiplier: int) -> tuple:
    return t * multiplier

print("Part j:", multiply_tuple(t1, 2));

# k
def tuple_with_indices(t: tuple) -> tuple:
    return tuple(enumerate(t));

print("Part k:", tuple_with_indices(t1));

# l
def tuple_statistics(t: tuple) -> dict:
    return {
        'max': max(t),
        'min': min(t),
        'average': sum(t) / len(t),
        'count': len(t),
        'sorted_asc': tuple(sorted(t)),
        'sorted_desc': tuple(sorted(t, reverse=True)),
        'frequency': {x: t.count(x) for x in t}
    };

t5 = (10, 20, 10, 40);
print("Part l:", tuple_statistics(t5));

# m
def tuple_to_string(t: tuple) -> str:
    return ''.join(t);

t6 = ('H', 'e', 'l', 'l', 'o');
print("Part m:", tuple_to_string(t6));

# n
def string_to_tuple(s: str) -> tuple:
    return tuple(s);

s = "Hello";
print("Part n:", string_to_tuple(s));

# o
def remove_element(t: tuple, element: int) -> tuple:
    return tuple(x for x in t if x != element);

print("Part o:", remove_element(t4, 30));

# p
def remove_duplicates(t: tuple) -> tuple:
    seen = set();
    result = [];
    for item in t:
        if item not in seen:
            result.append(item);
            seen.add(item);
    return tuple(result);

t7 = (1, 2, 2, 3, 3, 3)
print("Part p:", remove_duplicates(t7));

# q
def find_indices_of_element(t: tuple, element: int) -> tuple:
    return tuple(i for i, x in enumerate(t) if x == element);

print("Part q:", find_indices_of_element(t4, 10));

# r
def create_name_score_tuple():
    names = [];
    while True:
        name = input("Enter a name (or 'done' to finish): ");
        if name == 'done':
            break
        names.append(name);

    scores = [];
    while True:
        score = input("Enter a score (or '-999' to finish): ");
        if score == '-999':
            break
        scores.append(int(score));

    return tuple(zip(names, scores));

# 2
# ההבדל בין tuple ו list הוא: ש tuple הוא מייצג סדרה של ערכים שלא נינתים לשינוי אף פעם list יכולים לשנות אותו כמה שרק רוצים
# אני ישתמש ב tuple במצב שאני לא ירצה שישנו אותו ולא יוסיפו לו דברים מלבד מה שאני הוספתי
# tuple עדיף לפעמים כי הוא תופס פחות זיכרון מרשימה
# list זה עשוי להשתנות לפי הצרכים לשנות ערכים או להסיר אותם
# מקווה שזה עונה על השאלה


# 3
data_tuple = (
    {"name": "Alice", "age": 30, "city": "New York"},
    1000,
    "secret-code"
)
data_tuple[0]["age"] = 31
data_tuple[0].clear()

#השגיאה מתרחשת משום ש-tuple הוא בלתי משתנה. אמנם ניתן לשנות את תוכן האובייקטים בתוך ה-tuple (כמו המילון במקרה הזה)
# , אך לא ניתן לשנות את ה-tuple עצמו.
#במקרה הזה, הקוד מנסה לשנות ערך בתוך מילון שנמצא בתוך ה-tuple.
# הפעולה data_tuple[0]["age"] = 31 תצליח, משום שהיא משנה את תוכן המילון ולא את ה-tuple עצמו.
#לעומת זאת, הפעולה data_tuple[0].clear() תגרום לשגיאה אם המילון היה מוגדר כמילון "מוגן" או בלתי ניתן לשינוי.
# אך במקרה הזה, הפעולה הזו דווקא תצליח משום שהיא פשוט מרוקנת את המילון. כך שהשגיאה המוזכרת לא נובעת מפעולה זו.
