from pypdf import PdfMerger
import sys
inputArgs = sys.argv[1:]
def remove_duplicates(l):
    return list(set(l))
arguments=remove_duplicates(inputArgs)


inp = arguments[:-1]
out = arguments[-1]


merger = PdfMerger()

for pdf in inp:
    merger.append(pdf)

merger.write(out)
merger.close()
