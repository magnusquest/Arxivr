// Learn more about clients at https://docs.boundaryml.com/docs/snippets/clients/overview

client<llm> GPT4oMini {
  provider openai
  options {
    model "gpt-4o-mini"
    api_key env.OPENAI_API_KEY
  }
}

client<llm> DeepseekClient {
  provider ollama
  options {
    base_url "http://localhost:11434/v1"
    model "deepseek-r1"
  }
}

client<llm> PhiClient {
  provider ollama
  options {
    base_url "http://localhost:11434/v1"
    model "phi4"
  }
}

client<llm> LlamaClient {
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

client<llm> LlavaClient {
  provider ollama
  options {
    base_url "http://localhost:11434/v1"
    model "llava:7b"
  }
}
