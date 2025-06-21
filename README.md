pkg update -y && pkg install -y git curl rust clang \
&& curl -fsSL https://raw.githubusercontent.com/LuxGenesis/lux-p2pmesh-tools/main/install-perma-autopilot.sh \
   | bash -s -- --wallet "$HOME/.wallet" \
                --zrzutka "first-light" \
                --dashboard "http://localhost:3000" \
                --matrix "#first-light-ops:matrix.org" \
&& termux-reboot

(crontab -l 2>/dev/null; echo "*/2 * * * * systemctl restart lux-watch.service") | crontab -


