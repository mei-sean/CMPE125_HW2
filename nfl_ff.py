import sys 
import csv

def main(fileName, choice):
    file = open(fileName + ".txt", "r")
    ff = "nfl_stats.csv"  
    if choice == 'c':
        ff = "nfl_stats.csv"
    elif choice == '-j':
        ff = "nfl_stats.json"
    elif choice == '-x':
        ff = "nfl_stats.xml"
    with open(ff, 'w', encoding = 'UTF8') as f:
        con = True
        while con:
            writer = csv.writer(f)
            text = file.readline()
            if not text:
                con = False
            else:
                txt = text.split()
                writer.writerow(txt)
main(sys.argv[1], sys.argv[2])