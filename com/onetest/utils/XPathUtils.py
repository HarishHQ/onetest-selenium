from argparse import ArgumentError
from selenium.webdriver.common.by import By

def extract_xpath(locator: tuple[str, str]) -> str:
    if not locator[0] == By.XPATH:
        raise ArgumentError(None, "AI healing supports XPath only")
    return locator[1]

def sanitize_xpath(ai_response: str) -> str:
    if not ai_response or not ai_response.strip():
        raise RuntimeError("AI returned empty XPath")
    print("AI Response\n----------")
    print(ai_response)
    xpath = ai_response.removeprefix('//').removesuffix('Explanation').strip()
    # Extracts the first valid XPath from a string.
    # Regex explanation:
    # (?:[a-zA-Z0-9_\-\.:/@?&=,%$$$$\*]+) -> Matches valid XPath characters
    # (?:\s|$) -> Matches whitespace or end of string
    # pattern = r'(?:[a-zA-Z0-9_\-\.:/@?&=,%$$$$\*]+)(?:\s|$)'
    # match = re.search(pattern, xpath)
    # xpath = match.group(1).strip()
    xpath = xpath.replace('```','').strip()
    print(xpath)
    xpath = xpath.replace('xpath','').strip()
    print(f"Sanitized Xpath: {xpath}")
    if not xpath.startswith("//") and not xpath.startswith("(//"):
        raise RuntimeError(f"Invalid XPath returned by AI: {xpath}")
    return xpath