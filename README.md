- Uses Gmail API to obtain Emails received in the past week. 
- Takes message body data and sends it to HuggingFace API to obtain summarized message and rewards/incentives of joining the event, if any.

# Installation
1. Enable Gmail API from Google Cloud Console
2. Configure the OAuth consent screen
3. Authorize credentials for a desktop application
4. Download the OAuth 2.0 Client ID and save it as 'credentials.json' in the working directory
5. Upon running GetEmails.py for the first time, 'token.json' gets created


## Note:-
'simplegmail' directory contains code that performs the similar task
Here, our job becomes easier as all the procedural flow of 'GetEmail.py' is wrapped in the module Gmail of simplegmail
So, it is much more convenient to use simple gmail instead of above
<b>Important: Follow the same installation steps for this directory as given above, except, rename 'credentials.json' to 'client_secret.json'.
To run 'main.py', ensure that simplegmail is the parent directory of the current project </b>
