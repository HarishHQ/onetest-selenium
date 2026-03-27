import ollama
from ollama import Client
from com.onetest.utils import XPathUtils

prefix_msg = """
Role: senior selenium test automation expert
Task: Generate xpath using page source and semantic context provided
Output: One working xpath generated using page source and semantic context provided
"""

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'})

def heal(broken_xpath:str, page_source:str, semantic_context:str) -> str:
    # response = client.chat(model='lfm2',messages=[
    #     {
    #         'role': 'user',
    #         'content': prompt +
    #             '' + 'Input:\nBroken XPath:\n'+broken_xpath+'\nHTML Page Source:\n'+page_source+
    #                 '\nSemantic Context:'+semantic_context,
    #     }
    # ])
    response = ollama.generate(model='lfm2:latest', prompt=prefix_msg + 'Input:\nBroken XPath:\n'+broken_xpath+'\nHTML Page Source:\n'+page_source+'\nSemantic Context:'+semantic_context)
    xpath = XPathUtils.sanitize_xpath(response['response'])
    print(f"Ollama healed XPath: {xpath}")
    return xpath