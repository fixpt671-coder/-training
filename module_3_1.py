def count_cals():
    global calls
    calls += 1

def string_info(string):
    count_cals()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_cals()
    return string.lower() in str(list_to_search).lower()

calls = 0
print(is_contains("a)", ["A)", "asd"]), string_info("a)"))
print(calls)
