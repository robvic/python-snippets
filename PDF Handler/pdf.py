from collections import Counter
import PyPDF2

class PDF():
    def __init__(self, filename) -> None:
        with open(filename, 'rb') as f:
            self.pdf = PyPDF2.PdfFileReader(f)
            self.num_pages = self.pdf.getNumPages()

    def read(self):
        for i in range(self.num_pages):
            self.text = self.pdf.getPage(i).extract_text()
        return self.text

    def write_summary(self):
        writer = PyPDF2.PdfFileWriter()
        reader = PyPDF2.PdfFileReader(open('output/output.pdf', 'rb'))
        page = reader.getPage(0)
        writer.addPage(page)
        writer.add

    def summarize(self):
        total_pages = self.num_pages
        num_words = len(self.text.split(sep=' '))
        starting_words = self.text.split(sep=' ')[0:10]
        most_used_words = Counter(self.text.split(sep=' ')).most_common(10)
        summary = f'''
        Total pages = {total_pages}
        Number of words = {num_words}
        Starting words = {starting_words}
        Most used words = {most_used_words}
        '''
        return summary
