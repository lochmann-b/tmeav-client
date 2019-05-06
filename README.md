A very simple GUI for our wonderful tmeav web service.

Start the client from a terminal window with:
python tmeav_client.py

The client will try to send the validation requests to http://localhost:5000/api/v1/isEmailAddressValid.
You can overwrite the default url by setting the environment variable TMEAV_URL