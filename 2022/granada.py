import slate3k as slate
import re

def get_text_from_pdf(filename: str) -> str:
    with open(filename, "rb") as pdf_file:
        pages = slate.PDF(pdf_file)

    return "\n".join(pages)    


def get_regex():
    AT_LEAST_ONE_SPACE = r"\s+"
    AT_LEAST_TWO_SPACES = r"\s{2,}"
    
    di = r"\d{2}"
    sec = r"\d{3}"
    su = r"\d{2}|"
    m = r"[A-Z]"
    let = r"[A-Z]\-[A-Z]"
    code = r"\d{9}"
    num = r"\d{2}"
    local_name = r"(?:\S| )+?"
    street = r"(?:\S| |\d)+?"
    optional_place = r"(?:\S| )+?"
    ignore_pattern = r"(?:\*DISEMINADO\*| )"
    postal_code = r"\d{5}"
    town = r"(?:\S| )+?"
    province = r"(?:GRANADA| )"
    
    # (\d{2})\s+(\d{3})\s+(\d{2}|)\s+([A-Z])\s+([A-Z]\-[A-Z])\s+(\d{9})\s+(\d{2})\s+((?:\S| )+?)\s{2,}
    # ((?:\S| |\d)+?)\s{2,}(?:\*DISEMINADO\*| )\s{2,}((?:\S| )+?)\s{2,}(\d{5})\s+((?:\S| )+?)\s{2,}(?:GRANADA| )\s{2,}
    regex = (
        rf"({di})", AT_LEAST_ONE_SPACE,
        rf"({sec})", AT_LEAST_ONE_SPACE,
        rf"({su})", AT_LEAST_ONE_SPACE,
        rf"({m})", AT_LEAST_ONE_SPACE,
        rf"({let})", AT_LEAST_ONE_SPACE,
        rf"({code})", AT_LEAST_ONE_SPACE,
        rf"({num})", AT_LEAST_ONE_SPACE,
        rf"({local_name})", AT_LEAST_TWO_SPACES,
        rf"({street})", AT_LEAST_TWO_SPACES,
        rf"{ignore_pattern}", AT_LEAST_TWO_SPACES,
        rf"({optional_place})", AT_LEAST_TWO_SPACES,
        rf"({postal_code})", AT_LEAST_ONE_SPACE,
        rf"({town})", AT_LEAST_TWO_SPACES,
        rf"{province}", AT_LEAST_TWO_SPACES,
    )
    return "".join(regex)
    
def create_csv_from_list(data: list):
    output = "\n".join([";".join(row) for row in data])
    with open("data.csv", "w") as f:
        f.write(output)

if __name__ == "__main__":
    print("Getting text...")
    with open("data.txt", "r") as f:
        text = f.read()

    print("Executing regex...")
    regex = get_regex()
    data = re.findall(regex, text)

    print(f"Extracted {len(data)} rows")
    print(f"Creating CSV...")
    create_csv_from_list(data)
