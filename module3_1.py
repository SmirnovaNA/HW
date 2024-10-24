calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return (calls)
def string_info(string):
    count_calls()
    return (len(string), string.lower(), string.upper())
print(string_info('Smirnova'))
print(string_info('Ivanova'))
def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        return True
    else:
        return False
print(is_contains("Nata", ['Egor', 'Vera', 'Nata']))
print(is_contains('phenol', ['benzene','xylene','toluene']))
print(calls)