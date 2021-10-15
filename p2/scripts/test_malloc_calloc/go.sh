gcc -Werror -Wall -Wpedantic -Wextra -Wvla -std=c99 -Wredundant-decls -Wsign-conversion -Wfloat-equal -Wconversion -Wvla main_1.c -o app1.exe
gcc -Werror -Wall -Wpedantic -Wextra -Wvla -std=c99 -Wredundant-decls -Wsign-conversion -Wfloat-equal -Wconversion -Wvla main_2.c -o app2.exe

for n in 10 50 100 500 1000 5000 10000 50000
do
	./app1.exe < gen_${n}.txt > time_${n}_1.txt
	./app2.exe < gen_${n}.txt > time_${n}_2.txt
done

python avg.py
python data.py

rm time*.txt
