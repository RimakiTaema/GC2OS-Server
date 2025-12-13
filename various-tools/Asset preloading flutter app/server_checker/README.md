# server_checker

This is a flutter app for batch downloading GC2OS server assets (music and charts) to the user's device (their application folder).

Note: For 7003, the code has changed. Go to `lib` folder and replace `main.dart` with `main-7003.dart`.

To use it, you need to

1) Compile the project to .apk or .ipa. learn how to [here](https://docs.flutter.dev/deployment). A pre-compiled apk is provided, it has the same name and signature as the 4max version apk.

2) Sign the package to match the game client exactly (so you can install/sideload them and have them share the resource folders), this is general android/ios knowledge, use apktool + common certificate or a common ipa signing service.

3) Install the game. Then, install the package on the device,

4) Generate a `batch_token` in the database through some means (database edit, discord bot, etc.). The schema of the table is as follows: 

- `id`: auto generated primary key, simply ignore

- `batch_token`: The key string itself. Required field, String value

- `expire_at`: Datetime string of when the token expires. Required field, String value (e.g. 2026-11-27 06:37:48.170791)

- `uses_left`: Amount of uses the token can accrude before it stops working. Each time it queries the `/batch` api, this count will decrease by 1. Required field, Integer value.

- `auth_id`, `created_at`, `updated_at`: Simply left blank for local uses.

5) Open the app and enter the server base URL and token, click download and wait!

6) Once done, install the game pack.

This is a beta solution. Please report issues and errors.

Discord bot will not be open-sourced at the time being due to security concerns.
