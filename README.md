LeoPiExtIpNotifier
==================
This little project is to send notification email when Raspberry PI external IP address is changed.

Requirements
============
+ Install lynx on Raspberry PI:   
```
sudo apt-get install lynx
```

+ Setup port forwarding on Router for Raspberry PI

Usage
=====
    (LeoPiExtIpNotifierEnv) C:\Github\LeoPiExtIpNotifier>python LeoPiExtIpNotifier.py -h
    usage: LeoPiExtIpNotifier.py [-h] [--from FROM_EMAIL] [--password PASSWORD]    
                             [--smtp SMTP_SERVER] [--port SMTP_PORT]   
                             [--to TO_EMAIL] [--title TITLE]   
    Leo Raspberry External IP Notifier CLI Parser   
    optional arguments:   
      -h, --help            show this help message and exit
      --from FROM_EMAIL, -f FROM_EMAIL
                            Email address that sends the notification
      --password PASSWORD, -p PASSWORD
                            Password of the email
      --smtp SMTP_SERVER, -s SMTP_SERVER
                            SMTP server URL name of from email
      --port SMTP_PORT, -r SMTP_PORT
                            SMTP server port of from email
      --to TO_EMAIL, -o TO_EMAIL
                            Email address that receives the notification
      --title TITLE, -t TITLE
                            Title of notification email


Notes
=====
+ If you are using gmail as the FROM_EMAIL, please generate the APP Password on gmail account instead of using the login
 password of gmail account.


