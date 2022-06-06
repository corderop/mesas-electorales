import slate3k as slate

regex = r"(\d{2})\s+(\d{3})\s+([ABCU])\s+([A-Z]\-[A-Z])\s+(\d{9})\s+(\d{2})\s+((?:[A-Z]| )+?)\s{2,}"

with open("boletin.pdf", "rb") as pdf_file:
    pages = slate.PDF(pdf_file)
    with open("data.txt", "a") as write_file:
        for page in pages:
            string = page
            string += "\n"
            write_file.write(string)
    