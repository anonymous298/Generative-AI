from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

hf_model = pipeline('text-generation', model='gpt2')

llm = HuggingFacePipeline(pipeline=hf_model)

prompt_template = PromptTemplate(
    input_variables=['topic'],
    template="Answer the following question: {topic}"
)

chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

response = chain.run('What is AI?')
print(response)
