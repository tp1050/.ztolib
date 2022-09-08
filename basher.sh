
if not ss -nlt|grep 9050
sudo echo SocksPort 0.0.0.0:9050>> /etc/tor/torrc
sudo systemctl restart tor
if not nmap 127.0.0.1 -p 9050|grep open
ufw enable 9050/tcp

# check see if tor is working
torbala="curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/api/ip"
# everything okay
sudo systemctl restart tor

python readyness

apt-get install python3-pip

python -m ensurepip --upgrade
