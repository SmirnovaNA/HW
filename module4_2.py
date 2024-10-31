def test_funstion():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_funstion()
inner_function()
