import PyPDF2

def extractsample() :
    pdfFileObj = open('textdata/sampleText1.pdf', 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # print(len(pdfReader.pages))

    pageObj = pdfReader.pages[0]

    text=pageObj.extract_text()

    # print(type(pageObj.extract_text().splitlines()))
    # sentences = pageObj.extract_text().splitlines()
    # print(pageObj.)
    # i = 0
    #
    # for sentence in sentences:
    #     i += 1
    #
    #     print(i, ' ' + sentence)

    pdfFileObj.close()
    return str(text)

