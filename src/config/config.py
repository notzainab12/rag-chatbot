"""Configuration module for Agentic RAG system"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class Config:
    """Configuration class for RAG system"""

    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 100

    DEFAULT_URLS = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
    ]

    @classmethod
    def get_llm(cls):
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )