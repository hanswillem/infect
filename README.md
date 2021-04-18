# Infect!
**Python script that replaces bytes in one file with bytes in another file.**

### REPLACE RANDOM CHUNCKS OF BYTES

`python infect.py kick.wav epilepticfit.csv -m 1 -c 45 -i 10 -f 5  `

-m = mode 1  
-n = maximum lenght of the chunk of bytes (the actual chunk will be random each itteration)  
-i = amount of itterations  
-f = amount of files that will be exported  

### REPLACE RANDOM BYTES  

`python infect.py kick.wav epilepticfit.csv -m 2 -r 1000 -f 5  `

-m = mode 2  
-n = amount of random bytes to replace  
-f = amount of files that will be exported  

### REPLACE EVERY N BYTES (works good for PNG's and MP4)  

`python infect.py kick.wav epilepticfit.csv -m 3 -n 512 -f 5  `

-m = mode 3  
-n = replace every n bytes  
-f = amount of files that will be exported
