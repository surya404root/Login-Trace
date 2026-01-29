#!/bin/bash
clear
RED="\033[1;31m";GREEN="\033[1;32m";CYAN="\033[1;36m";MAGENTA="\033[1;35m";RESET="\033[0m"
slow(){ for ((i=0;i<${#1};i++));do echo -ne "${1:$i:1}";sleep 0.02;done;echo;}
menu(){ echo -e "$GREEN [1] 🔍 Start Trace Scan";echo -e "$CYAN  [2] 📡 Loaded Modules";echo -e "$MAGENTA[3] 🧠 Framework Info";echo -e "$RED   [0] ❌ Exit";echo;read -p " Select ➜ " opt;}
modules(){ clear;echo -e "$CYAN Active Modules\n";ls core config;echo;read -p " Press Enter...";}
about(){ clear;echo " LOGIN TRACE OSINT FRAMEWORK";echo " Pure OSINT presence scanner";echo " No login | No password | No hacking";echo;read -p " Press Enter...";}
scan(){ clear;slow "Booting OSINT Engine...";sleep 1;slow "Loading modules...";sleep 1;echo;python main.py;read -p " Press Enter...";}
while true;do clear;python -c "from core.banner import show;show()";menu;case $opt in
1) scan;;2) modules;;3) about;;0) echo -e "$RED Shutting down...";sleep 1;exit;;*) echo "Invalid";sleep 1;;esac;done
