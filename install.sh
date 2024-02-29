#!/bin/bash
mkdir consegna_godeas
cp get_file.bash godeas.py consegna_godeas
chmod a+rwx "consegna_godeas/get_file.bash"
chmod a+rwx "consegna_godeas/godeas.py"
cd consegna_godeas
./get_file.bash
