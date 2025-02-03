client<llm> GPT4o {
  provider openai
  options {
    model "gpt-4o"
    api_key env.OPENAI_API_KEY
  }
}

client<llm> Deepseek {
  provider ollama
  options {
    base_url "http://localhost:11434/v1"
    model "deepseek-r1"
  }
}

client<llm> Phi {
  provider ollama
  options {
    base_url "http://localhost:11434/v1"
    model "phi4"
  }
}

client<llm> Llama {
  provider ollama
  options {
    base_url "http://localhost:11434/v1"
    model "llama3.2"
  }
}

client<llm> ToolClient {
  provider ollama
  options {
    base_url "http://localhost:11434/v1"
    model "llama3-groq-tool-use"
  }
}

client<llm> Qwen {
  provider ollama
  options {
    base_url "http://localhost:11434/v1"
    model "qwen2.5-coder:14b"
  }
}
