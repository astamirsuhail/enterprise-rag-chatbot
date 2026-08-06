from pathlib import Path


class DocumentManager:

    def __init__(self):

        self.documents_path = Path("data/input")


    def get_all_documents(self):

        pdf_files = list(self.documents_path.glob("*.pdf"))

        return sorted(pdf_files)


    def count_documents(self):

        return len(self.get_all_documents())