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
    m = r"[ABCU]"
    let = r"[A-Z]\-[A-Z]"
    code = r"\d{9}"
    num = r"\d{2}"
    local_name = r"(?:\w| )+?"
    street = r"(?:\w| |\d)+?"
    postal_code = r"\d{5}"
    town = r"(?:\w| )+?"
    province = r"(?:\w| )+?"
    
    # (\d{2})\s+(\d{3})\s+([ABCU])\s+([A-Z]\-[A-Z])\s+(\d{9})\s+(\d{2})\s+((?:\w| )+?)\s{2,}((?:\w| |\d)+?)\s{2,}(\d{5})\s((?:\w| )+?)\s{2,}((?:\w| )+?)\s{2,}
    regex = (
        rf"({di})",
        AT_LEAST_ONE_SPACE,
        rf"({sec})",
        AT_LEAST_ONE_SPACE,
        rf"({m})",
        AT_LEAST_ONE_SPACE,
        rf"({let})",
        AT_LEAST_ONE_SPACE,
        rf"({code})",
        AT_LEAST_ONE_SPACE,
        rf"({num})",
        AT_LEAST_ONE_SPACE,
        rf"({local_name})",
        AT_LEAST_TWO_SPACES,
        rf"({street})",
        AT_LEAST_TWO_SPACES,
        rf"({postal_code})",
        AT_LEAST_ONE_SPACE,
        rf"({town})",
        AT_LEAST_TWO_SPACES,
        rf"({province})",
        AT_LEAST_TWO_SPACES,
    )
    return "".join(regex)
    


if __name__ == "__main__":
    text = get_text_from_pdf("boletin.pdf")
    regex = get_regex()
    print(re.findall(regex, text)[:3])