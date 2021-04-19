import cipher


def test_cipher():
    assert cipher.ciphes('Hello world!') == 'Svool dliow!'
    assert cipher.ciphes('Christmas is the 25th of December') == 'Xsirhgnzh rh gsv 25gs lu Wvxvnyvi'
    assert cipher.ciphes('My name is xyz') == 'Nb mznv rh cba'
    assert cipher.ciphes('This is something') == 'Gsrh rh hlnvgsrmt'
