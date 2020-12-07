import imaplib
import email
import variables


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(variables.login, variables.password)

mail.list()
mail.select("Daily_Coding_Problem")
result, data = mail.search(None, "ALL")
ids = data[0]
id_list = ids.split()
for id in id_list:
    result, data = mail.fetch(id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    email_message = email.message_from_string(raw_email_string)

    file_name = email_message['Subject']

    i = 0
    if email_message.is_multipart():
        for payload in email_message.get_payload():
            if i == 0:
                body = payload.get_payload(decode=True).decode('utf-8')
                body = body[:body.index("Upgrade to premium")]
                # print(body)
            i += 1
    else:
        body = payload.get_payload(decode=True).decode('utf-8')
        body = body[:body.index("Upgrade to premium")]
        # print(body)
    body = body.split("\n")
    try:
        with open("./gmail/" + file_name + '.py', 'x') as file:
            for line in body:
                if len(line) > 1:
                    file.write("# " + line + '\n')
                else:
                    file.write("#" + line + '\n')
    except FileExistsError:
        pass
