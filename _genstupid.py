
stupid_template = """
class {NAME}(Enum):
{DOCS}{BLAHBLAH}
"""
def pair(key, val):
    return "{} = {}".format(key,val)

def magic_text(text):
    return str(text).upper().replace("-", "_")

def gen_from_list(name, lst, docs = None):
    totalstring = []
    for i in lst:
        totalstring.append("    {} = \"{}\"".format(magic_text(i), i))
    doc_write=""
    if docs:
        doc_write = "    \"\"\"{}\"\"\"\n".format(docs)
    return stupid_template.format(NAME=name, DOCS=doc_write, BLAHBLAH="\n".join(totalstring))


def main():
    name = input("Please enter the name of what we are generating")
    while arg := input("Please enter a type") == "":   
        pass

if __name__ == "__main__":
    main()
