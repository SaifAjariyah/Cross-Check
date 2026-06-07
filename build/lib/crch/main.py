# src/crch/main.py
import sys

def process_stream(stream1, stream2, p1, p2):
        for nu, (line1, line2) in enumerate(zip(stream1, stream2)):
            if (line1 == line2):
                print('\033[32m<%s:%s> line %d is equal...\033[0m' % (p1, p2, nu))
            else:
                print('\033[31m<%s:%s> line %d does not match!\033[0m' % (p1, p2, nu))

def main():
    print("Cross Check tool running")
    if len(sys.argv) == 3:
        with open(sys.argv[1], 'r') as f1:
            with open(sys.argv[2], 'r') as f2:
                process_stream(f1, f2, sys.argv[1], sys.argv[2])
            
    else:
        print("<usage>: crch file1 file2")

if __name__ == "__main__":
    main()
