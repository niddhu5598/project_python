msg = 'brandon sanderson is an American author of epic fantacy and science function'

author_idx = msg.find('author')
print('author word start at',author_idx)

and_idx = msg.find('and')
print('and occurs at index',and_idx)

and_idx = msg.find('and',10)
print('and occurs at index',and_idx)

and_idx = msg.rfind('and')
print('and occurs at index',and_idx)

and_idx = msg.index('and',10)
print('and occurs at index',and_idx)

writer_idx = msg.find('writer')
print('writer occurs at index',write_idx)
