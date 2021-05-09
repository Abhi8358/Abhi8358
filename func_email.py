import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email import encoders

def send(file_name):
    from_add = "abhishekpatidar7446@gmail.com"
    to_add="abhishekpatidar8358@gmail.com"

    subject ="Recommended stoks"

    msg= MIMEMultipart()

    msg["From"] =from_add
    msg["To"] =to_add
    msg['Subject']=subject

    body = "Stocks analysis"

    msg.attach(MIMEText(body,"plain"))
    message = msg.as_string()

    my_file=open(file_name,"rb")  # rb is for binary
    part = MIMEBase("application","octet-stream")

    part.set_payload((my_file).read())
    encoders.encode_base64(part)  #for encoding the binary file

    part.add_header("Content-Disposition","attachment ; filename =" +file_name)
    msg.attach(part)
    message=msg.as_string()

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(from_add,"eerldlkwixapdxqo")

    server.sendmail(from_add,to_add,message)

    server.quit()
