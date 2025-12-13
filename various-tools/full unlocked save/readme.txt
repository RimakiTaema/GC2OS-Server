This is a base64 string for the server to deliver the save data to the client.

It unlocks all the songs and difficulties. Avatars and items are not unlocked.

For 7002 and prior:

Paste the B64 string into `player.db`'s `user` table. 

Find the row of your user and paste the content into the `data` field. 

Save the database.


For 7003:

Open `player.db` and go to `accounts` table. Find the `id` of your account.

Create a `save` folder at the server root directory if it is not already there.

Create a new text file called `{YOUR_ACCOUNT_ID}.dat`, for example, `1.dat`.

Open that file and paste the B64 string in, and save.

