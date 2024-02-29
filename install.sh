#!/bin/bash
mkdir consegna_godeas
cd consegna_godeas
wget -O "godeas.py" "https://raw.githubusercontent.com/LeoGod98/AbInf/main/godeas.py"
wget -O "get_file.bash" "https://raw.githubusercontent.com/LeoGod98/AbInf/main/get_file.bash"
cp get_file.bash godeas.py consegna_godeas
chmod a+rwx "consegna_godeas/get_file.bash"
chmod a+rwx "consegna_godeas/godeas.py"
./get_file.bash
