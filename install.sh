#!/bin/bash
cd
mkdir consegna_godeas
cd consegna_godeas
wget -O "godeas.py" "https://raw.githubusercontent.com/LeoGod98/AbInf/main/godeas.py"
wget -O "get_file.bash" "https://raw.githubusercontent.com/LeoGod98/AbInf/main/get_file.bash"
chmod a+rwx "get_file.bash"
chmod a+rwx "godeas.py"
./get_file.bash
