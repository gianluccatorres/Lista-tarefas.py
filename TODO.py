link = input('Digite seu texto aqui')  # ex: https://x.com/i/status/2040156457094566163
# encontra onde está 'x.com' na URL
pos = link.find('x.com')
# nova URL: f + x + twitter + com/...
novo_link = link[:pos] + 'fxtwitter' + link[pos+1:]  # pos+1 para manter o 'com' intacto

print(novo_link)