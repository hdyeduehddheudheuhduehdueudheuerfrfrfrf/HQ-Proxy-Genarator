def proxy_gen():
	main = input("""
	1. Http
	2. Https
	3. Socks4
	4. Socks5
	""")
	main2 = input("@D1MOD1877 -->  ")
	
	main2 = int(main2) + 0
	if int(main2) > 10000 or int(main2) < 50:
		print("@D1MOD1877 -->")
		input("")
		return
	if main == "1":
		r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={main2}&country=all")
	if main == "2":
		r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout={main2}&country=all")
	if main == "3":
		r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={main2}&country=all")
	if main == "4":
		r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout={main2}&country=all")
	file = open("proxies.txt", "wb")
	file.write(r.content)
	print("Done")
	print("@D1MOD1877 --> CLICK BKA BO DARCHWN")
	input("")
	return
