from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
	print('Please choose your album (invalid choice exits):')
	for index, (title, artist, year, songs) in enumerate(albums):
		print('{}: {}.'
			  .format(index + 1, title))

	choice = int(input())
	if 1 <= choice <= len(albums):
		songs_list = albums[choice - 1][SONGS_LIST_INDEX]
	else:
		break

	print('Please choose your song: ')
	for index, (track_number, song) in enumerate(songs_list):
		print('{}: {}'.format(index +1, song))

	song_choice = int(input())
	if 1 <= song_choice <= len(songs_list):
		title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
	else:
		print('Please chose your album (invalid choice exits):')
		print()
		songs_list = albums[choice - 1][SONGS_LIST_INDEX]

	print('Playing {}'.format(title))
	print('=' * 50)

	# NOTES
	# constants in python are written in ALL_CAPS
	# from ..... import  --> imports the whole file, if theres multiple code in it, it will run it all
	# if you want to use just some small code from the imported file, keep the file clean and short