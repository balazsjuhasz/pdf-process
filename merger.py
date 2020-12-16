import PyPDF2

import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        print(f'Merging: {pdf}')
        merger.append(pdf)

    merger.write('superpdf.pdf')


if __name__ == "__main__":
    pdf_combiner(inputs)
