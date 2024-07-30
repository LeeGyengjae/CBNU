from langchain_community.document_loaders import PyPDFLoader

pdf_filepath = '000660_SK_2023.pdf'
loader = PyPDFLoader(pdf_filepath)
pages = loader.load()

print(len(pages))
print(pages[10])