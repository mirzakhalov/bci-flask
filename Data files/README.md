
## Before you start


Install the following requirements with `pip`:
    pip install -r requirements.txt

To run the files you will need to do a few things.

1. [Download and install](https://www.emotiv.com/developer/) the Cortex
   service.  Please note that currently, the Cortex service is only available
   for Windows and macOS.
2. Next, to get a client id and a client secret, you must connect to your
   Emotiv account on
   [emotiv.com](https://www.emotiv.com/my-account/cortex-apps/) and create a
   Cortex app. If you don't have a EmotivID, you can [register
   here](https://id.emotivcloud.com/eoidc/account/registration/).
3. Then, if you have not already, you will need to login with your Emotiv id in
   the EMOTIV App.
4. Finally, the first time you run these examples, you also need to authorize
   them in the EMOTIV App.


## Basics

With the prerequisites complete, you can 
update the credentials file with your client ID and secret, and then run the
test file

This will use your client_id and client_secret to connect to Cortex, and return data on Alpha, Beta, and Theta waves of each channel

## Details

After securing a proper connection, running ``testfile.py`` will output the data.
See [here](https://emotiv.github.io/cortex-docs/#pow-event) for data details.

## Debug Notes

Uncomment logger.debug instances in ``cortex.py`` in the lib file to help debug