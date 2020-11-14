# simple-imap-lister
Just logins to an imap server, performs a LIST on the server, returns the 'folders' and quits.

Takes about ~0.2sec per login.

```
=======================================
Trying Mailbox:  xyz@bluewin.ch
=======================================
Connecting to imaps.bluewin.ch
Logging in as xyz@bluewin.ch
<imaplib.IMAP4_SSL instance at 0x10ccb3ea8>
RetValue: OK
Data: ['(\\HasNoChildren \\Drafts) "/" Drafts', '(\\NoInferiors) NIL INBOX', '(\\HasNoChildren) "/" nonspam', '(\\HasNoChildren \\Sent) "/" "Sent Items"', '(\\HasNoChildren \\Junk) "/" Spam', '(\\HasNoChildren \\Trash) "/" Trash']
=======================================
Trying Mailbox:  abc@bluewin.ch
=======================================
Connecting to imaps.bluewin.ch
Logging in as abc@bluewin.ch
<imaplib.IMAP4_SSL instance at 0x10ccadf38>
RetValue: OK
Data: ['(\\HasNoChildren \\Drafts) "/" Drafts', '(\\NoInferiors) NIL INBOX', '(\\HasNoChildren \\Sent) "/" "Sent Items"', '(\\HasNoChildren \\Junk) "/" Spam', '(\\HasNoChildren \\Trash) "/" Trash']
...
```

Just add the username and password with a space/tab separated in the config file. 
Yeah, I know - this is insecure - but it's just a proof of concept :)
