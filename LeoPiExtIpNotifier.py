import argparse
import subprocess
import smtplib
from email.mime.text import MIMEText
import os.path

def get_ext_ip():
    #ext_ip = subprocess.check_output(["lynx", "--dump", "http://ipecho.net/plain"])
    ext_ip = "192.168.1.1"
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

def send_notify_email(ext_ip, email, password, title):
    msg = MIMEText(ext_ip)
    msg["Subject"] = title
    msg["From"] = email
    msg["To"] = email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, msg.as_string())
    server.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Leo Raspberry External IP Notifier CLI Parser")
    parser.add_argument("--email", "-e", action="store", dest="email",
                        help="Email address that sends/receive the notification")
    parser.add_argument("--password", "-p", action="store", dest="password",
                        help="Password of the email")
    parser.add_argument("--title", "-t", action="store", dest="title",
                        help="Title of notification email")

    result = parser.parse_args()
    email = result.email
    password = result.password
    title = result.title

    ext_ip = get_ext_ip()
    if not os.path.isfile("./external_ip.txt"):
        write_ext_ip_to_file(ext_ip)
        send_notify_email(ext_ip, email, password, title)
    else:
        ext_ip = get_ext_ip()
        old_ext_ip = read_ext_ip_from_file()
        if ext_ip != old_ext_ip:
            write_ext_ip_to_file(ext_ip)
            send_notify_email(ext_ip, email, password, title)

