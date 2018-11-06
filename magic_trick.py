import sys
import argparse

magic_number={
    "ZIP":b'\x50\x4B',
    "ELF":b'\x7F\x45\x4C\x46',
    "JPEG":b'\xFF\xD8\xFF\xE0',
    "RAR1.5":b'\x52\x61\x72\x21\x1A\x07\x00',
    "RAR5.0":b'\x52\x61\x72\x21\x1A\x07\x01\x00',
    "PNG":b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',
    "JAVACLASS":b'\xCA\xFE\xBA\xBE',
    "UTF-8":b'\xEF\xBB\xBF',
    "PDF":b'\x25\x50\x44\x46\x2d\x0a',
    "ASF":b'\x30\x26\xB2\x75\x8E\x66\xCF\x11\xA6\xD9\x00\xAA\x00\x62\xCE\x6C', #advanced system format
    "WMA":b'\x30\x26\xB2\x75\x8E\x66\xCF\x11\xA6\xD9\x00\xAA\x00\x62\xCE\x6C',
    "WMV":b'\x30\x26\xB2\x75\x8E\x66\xCF\x11\xA6\xD9\x00\xAA\x00\x62\xCE\x6C',
    "MP3":b'\xFF\xFB',
    "ISO":b'\x43\x44\x30\x30\x31'
}

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument("file",
                        type=str,
                        help="Specify input file")
    
    parser.add_argument("type",
                        type=str,
                        help="Specify the type of magic number", choices=magic_number.keys())
    
    parser.add_argument("-o",
                        "--output",
                        help="Specify the name of output file")
    
    return parser.parse_args()

def main (argv):
    print("\n\n##############\t\tWELCOME TO MAGIC_TRICK.PY\t\t##############\n")

    fh = open('avadakedavra.txt', 'r')
    print(fh.read()+"\n\n\n")
    fh.close()
    args = parse()
    output_file = "output"
    if args.output != None:
        output_file = args.output
   
    # Open file that contains the script
    fr = open(args.file,'rb')
    fw = open(output_file, 'wb')
    
    # Change file signature
    fw.write(magic_number[args.type])
    
    # Write input file content
    fw.write(fr.read())

    # Close the files
    fw.close()
    fr.close()
    print("Done")

if __name__ == '__main__':
    main(sys.argv)