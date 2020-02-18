# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

Doc_Control_Manager = 'joneil@busek.com'
Busek_API_Key = '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'

def fSendEmail(Email_List,message_content):

    # e_address is a list of email addresses (maybe just one)
    # doc_files is a dictionary of files that pertain to that email address

    message = Mail(
        from_email=Doc_Control_Manager,
        to_emails=Email_List,
        subject='Document Release Notification',
        html_content=message_content)
    try:
        sg = SendGridAPIClient(Busek_API_Key)
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e.message)


def fBuildEmailList(loc):

    with open(loc,'r') as e_file:
        e_list = e_file.readlines()

    Email_Dict = {}

    for line in e_list:
        processed_line = line.replace('\n','').replace(' ','').split('=')

        key = processed_line[0]
        value = processed_line[1].split(',')

        Email_Dict[key] = value

    return Email_Dict

def fRetrieveEmail(project,Email_Dict):

    try:
        emails = Email_Dict[project]
        return emails
    except:
        return ['']

ED = {'1295': ['mstrain@busek.com', 'michael.e.strain@gmail.com'],
 '1310': ['michael.e.strain@gmail.com'],
 '1354': ['mstrain@busek.com'],
 '1349': ['michael.e.strain@gmail.com', 'mstrain@busek.com']}

project = '1310'

print(fRetrieveEmail(project,ED))