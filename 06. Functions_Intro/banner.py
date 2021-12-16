def banner_text(text=" ", screen_width=80) -> None:
	"""
	Print a string centered, with ** either side.
	:param text: The string to print.
	An asterisk (*) will result in a row of asterisks.
	:param screen_width: The overall width to print within
	(including the 4 spaces for the ** either side.
	:raises ValueError: if the supplied string is too large.
	"""
	if len(text) > screen_width - 4:
		raise ValueError('String {0} is larger than specified width {1}'
						 .format(text, screen_width))

	if text == '*':
		print('*' * screen_width)
	else:
		centered_text = text.center(screen_width - 4)
		output_string = '**{0}**'.format(centered_text)
		print(output_string)


banner_text("*", 60)
banner_text()
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of life...", 66)
banner_text()
banner_text("*", 60)

# NOTES
# ValueError is an exception
# TODO check python documentation for other exceptions
# https://docs.python.org/3/tutorial/errors.html
# NOTES default value of parameters are defined without space "screen_width=80" or "text=' '"
