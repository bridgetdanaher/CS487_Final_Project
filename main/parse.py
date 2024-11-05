import sys

def parse_code(src_file):
    content = list()
    try:
        with open(src_file, "r") as src_code:
            return src_code.read()
    except Exception as e:
        print(e)
        return None

#def parse_afl_buglog()
