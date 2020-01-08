from urls_utils import gen_from_urls

urls = ('http://mail.ru', 'http://yandex.com', 'http://python.org')

for resp_len, status, url, in gen_from_urls(urls):
	print(resp_len, '->', status, '->', url)