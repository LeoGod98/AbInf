#!/usr/bin/bash

read -p "Nome file:" nome
wget -O "$nome" "https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat"
echo "$nome" | python3 godeas.py 
