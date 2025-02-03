
function Prompt(messages: string[]) -> string {
  client Llama
  prompt #"
    {% for m in messages %}
      {{ _.role("user" if loop.index % 2 == 1 else "system") }}
      {{ m }}
    {% endfor %}
  "#
}

test PromptTest1 {
  functions [Prompt]
  args {
    messages [
      "I'm a banana!",
      "Nice to meet you!",
      "What am I?",
    ]
  }
}