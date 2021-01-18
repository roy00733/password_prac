# 密碼重試程式
# passwod = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果輸入正確,就印出"登入成功!"
# 如果不正確,就印出"密碼錯誤! 還有___次機會"
# 如果輸錯3次 就印出"你已經沒機會了! 即將封鎖帳號"

password = 'a123456'
i = 3
while i > 0:
	psw = input('請輸入密碼: ')
	if psw == password:
		print('登入成功!')
		break
	else:
		i = i - 1
		print('密碼錯誤!')
		if i > 0:
			print('你還有', i,'次機會')
		else:
			print('你已經沒機會了! 即將封鎖帳號!')
