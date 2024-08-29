def send_email(message, recipient = "gafur-5@mail.ru", sender = "university.help@gmail.com"):
    # for recipient
    l_r = len(recipient)
    n_r = recipient[-1: l_r-5:-1]
    dmn1 = n_r[::-1]
    m_r = recipient[-1: l_r-4:-1]
    dmn2 = m_r[::-1]

    l_s = len(sender)
    n_s = sender[-1: l_s - 5:-1]
    dmn3 = n_s[::-1]
    m_s = sender[-1: l_s - 4:-1]
    dmn4 = m_s[::-1]

    if (recipient.find('@') > 0 and sender.find('@') > 0) and ((dmn2 == '.ru' or dmn1 == '.com' or dmn1 == '.net') and (dmn4 == '.ru' or dmn3 == '.com' or dmn3 == '.net')):
        if sender == "university.help@gmail.com":
            print('Письмо успешно отправлено с адреса {} на адрес {}'.format(sender, recipient))
        elif sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        else:
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {} на адрес {}.'.format(sender, recipient))
    else:
        print('Невозможно отправить письмо с адреса {} на адрес {}'.format(sender, recipient))


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')