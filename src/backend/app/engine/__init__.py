import os
from llama_index.core.settings import Settings
from llama_index.core.agent import AgentRunner
from llama_index.core.tools.query_engine import QueryEngineTool
from app.engine.tools import ToolFactory
from app.engine.index import get_index
from llama_index.core.postprocessor.types import BaseNodePostprocessor
from llama_index.postprocessor.cohere_rerank import CohereRerank

def get_chat_engine(filters=None, params=None):
    system_prompt = os.getenv("SYSTEM_PROMPT")
    top_k = os.getenv("TOP_K", "3")
    tools = []
    # Add query tool if index exists
    index = get_index()
    if index is not None:
        query_engine = index.as_query_engine(
            similarity_top_k=int(top_k),
            filters=filters,
            node_postprocessors= [get_reranker()] if os.getenv("COHERE_API_KEY") != "" else None,
        )
        query_engine_tool = QueryEngineTool.from_defaults(query_engine=query_engine)
        tools.append(query_engine_tool)

    # Add additional tools
    tools += ToolFactory.from_env()

    return AgentRunner.from_llm(
        llm=Settings.llm,
        tools=tools,
        system_prompt=system_prompt,
        verbose=True,
    )

def get_reranker() -> BaseNodePostprocessor:
    api_key = os.getenv("COHERE_API_KEY")
    top_k = int(os.getenv("TOP_K", "3"))
    if api_key is None:
        raise ValueError(
            "Please set your COHERE_API_KEY. Get it from https://dashboard.cohere.com/api-keys"
        )

    return CohereRerank(
        api_key=api_key,
        top_n=top_k,
    )
