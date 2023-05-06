import PyPDF2

Book=PyPDF2.PdfReader(r'D:\pythonpro\TheNarrator\raw_data\testPDF2.1.pdf')
# print(Book.metadata)
NumPages = len(Book.pages)
# print(NumPages)
def extractSample() :
  str=""
  for i in range (2, 5):
    Page=Book.pages[i]
    Text = Page.extract_text()
    # print("Page Number", i)
    # print(Text)
    str = str + Text
  return str;
# with open ("text.txt", "w", encoding='utf-8') as text:
#   text.write(str)