<div align="center">
<pre>
███╗   ███╗██╗███████╗███████╗██╗   ██╗ ██████╗ ██╗   ██╗
████╗ ████║██║██╔════╝██╔════╝╚██╗ ██╔╝██╔═══██╗██║   ██║
██╔████╔██║██║███████╗███████╗ ╚████╔╝ ██║   ██║██║   ██║
██║╚██╔╝██║██║╚════██║╚════██║  ╚██╔╝  ██║   ██║██║   ██║
██║ ╚═╝ ██║██║███████║███████║   ██║   ╚██████╔╝╚██████╔╝
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ 

</pre>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>

</div>
# Overview
## A tool to bruteforce API endpoints(Sends conquerent requests to speed up the attack)![](https://travis-ci.org/CodeBreaker444/miss-you.svg?branch=master)

## Requirements:
- Python3
- pycharm(Optional)

## Installation
``` pip3 install -r requirements.txt ```
## Packages Used
```
json
requests
threading

```
> `Check it in Action:` [Click Here](https://travis-ci.org/CodeBreaker444/miss-you)

## Usage
``` python3 cb_missyou.py ```
## Screenshots
<img src="/Screenshots/main.png" width="500"></img>

<img src="/Screenshots/missyou-codebreaker.gif" width="500"></img>

## Limitations
- Only 4 digit pin bruteforcing is supported because 6 digit pin has 1 million combinations which is not practical to bruteforce.
- Multi-threading is locked to 24 threads but you can manually change it in code (variable name: lock -13th line). Don't increase it too much because your system my halt or crash.
- No user choice for entering response code (no reasons) but you can change it in the code(it's needed most of the time, default: ['response']['success']). Pull requests will be open and you can change the code too, I will merge it once i have reviewed the changes (special thanks will be credited).
- Bruteforce does not work when IP-ratelimiting or reset otp counter is in place.
- Let me know if there are any left.

## Where to use it
> More than 70% websites are running without IP-ratelimiting, with 4 digit reset pin, without number of tries counter. So, these sites can be easily hacked with MissYOU.
## Personal INFO:
`Donations Help Me to Keep The Support and Development:` [Click Here](https://paypal.me/zer0error).

`FollowMe:` [Click Here](https://facebook.com/zer0error/).

`Google Play:` [Codebreaker](https://play.google.com/store/apps/dev?id=8331274631553271784&hl=en).

`Website:` [Personal](https://govardhanchitrada.me).

