violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код

amount_songs = int(input('Сколько песен выбрать? '))
result = 0
for _ in range(amount_songs):
    song = input('Название первой песни: ')
    if song in violator_songs:
        result += violator_songs[song]
    else:
        print('К сожалению у нас нет такой композиции :(')

print('Общее время звучания песен:', round(result, 2))

# зачтено
