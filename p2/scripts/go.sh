gcc -Werror -Wall -Wpedantic -Wextra -Wvla -std=c99 -Wredundant-decls -Wsign-conversion -Wfloat-equal -Wconversion -Wvla main1.c -o app1.exe
gcc -Werror -Wall -Wpedantic -Wextra -Wvla -std=c99 -Wredundant-decls -Wsign-conversion -Wfloat-equal -Wconversion -Wvla main2.c -o app2.exe
gcc -Werror -Wall -Wpedantic -Wextra -Wvla -std=c99 -Wredundant-decls -Wsign-conversion -Wfloat-equal -Wconversion -Wvla main3.c -o app3.exe

touch gen_10.txt
touch gen_100.txt
touch gen_1000.txt
touch gen_10000.txt

python gen_10.py
python gen_100.py
python gen_1000.py
python gen_10000.py