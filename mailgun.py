def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/mg.aktarzaman.com/messages",
		auth=("api", "ad4467d080e665eac956ce8719464be3-f696beb4-91d4c5d2"),
		data={"from": "Excited User <mailgun@mg.aktarzaman.com>",
			"to": ["auz.zamy@gmail.com", "YOU@mg.aktarzaman.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
