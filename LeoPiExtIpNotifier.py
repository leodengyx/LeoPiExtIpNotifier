import argparse
import subprocess
import smtplib
from email.mime.text import MIMEText
import os.path

def get_ext_ip():
    ext_ip = subprocess.check_output(["lynx", "--dump", "http://ipecho.net/plain"])
    return ext_ip

def read_ext_ip_from_file():
    file_hdlr = open("external_ip.txt", "r")
    ext_ip = file_hdlr.read()
    file_hdlr.close()
    return ext_ip

def write_ext_ip_to_file(ext_ip):
    file_hdlr = open("external_ip.txt", "w")
    file_hdlr.truncate()
    file_hdlr.write(ext_ip)
    file_hdlr.close()

def send_notify_email(ext_ip, from_email, password, smtp_server, smtp_port, to_email, title):
    msg = MIMEText(ext_ip)
    msg["Subject"] = title
    msg["From"] = from_email
    msg["To"] = to_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    #server.ehlo()
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Leo Raspberry External IP Notifier CLI Parser")
    parser.add_argument("--from", "-f", action="store", dest="from_email",
                        help="Email address that sends the notification")
    parser.add_argument("--password", "-p", action="store", dest="password",
                        help="Password of the email")
    parser.add_argument("--smtp", "-s", action="store", dest="smtp_server",
                        help="SMTP server URL name of from email")
    parser.add_argument("--port", "-r", action="store", dest="smtp_port", type=int,
                        help="SMTP server port of from email")
    parser.add_argument("--to", "-o", action="store", dest="to_email",
                        help="Email address that receives the notification")
    parser.add_argument("--title", "-t", action="store", dest="title",
                        help="Title of notification email")

    result = parser.parse_args()
    from_email = result.from_email
    password = result.password
    smtp_server = result.smtp_server
    smtp_port = result.smtp_port
    to_email = result.to_email
    title = result.title

    ext_ip = get_ext_ip()
    if not os.path.isfile("./external_ip.txt"):
        write_ext_ip_to_file(ext_ip)
        send_notify_email(ext_ip, from_email, password, smtp_server, smtp_port, to_email, title)
    else:
        ext_ip = get_ext_ip()
        old_ext_ip = read_ext_ip_from_file()
        if ext_ip != old_ext_ip:
            write_ext_ip_to_file(ext_ip)
            send_notify_email(ext_ip, from_email, password, smtp_server, smtp_port, to_email, title)

