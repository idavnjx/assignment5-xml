import sys

def filter_xml (infile, outfile):
    import re
    out_string = ''
    replacement = '<.*?>'
    with open(infile) as instream:
        instring = instream.read()
        xml_pattern = re.compile('(?s)<style>.*?</style>')
        alt_pattern = re.compile('<[^>]*>')
        final_pattern = re.compile('&nbsp;')
        out_string = xml_pattern.sub('',instring)
        alt_out_string = alt_pattern.sub('', out_string)
        final_out_string = final_pattern.sub(' ', alt_out_string)
    with open(outfile,'w') as outstream:
        outstream.write(final_out_string)

def main(args):
    infile = args[1]
    split_point = infile.rindex('.')
    outfile = infile[:split_point]+'.txt'
    filter_xml(infile,outfile)

sys.exit(main(sys.argv))
