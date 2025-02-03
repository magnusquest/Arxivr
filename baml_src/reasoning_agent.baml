
function ReasoningAgent(message: string) -> Task[] {
  client Deepseek
  prompt #"
    {{ _.role("system") }}
    Break down the following instruction message into tasks following these rules:
    - Assign the appropriate tool to each task. Use the SearchTool as a last resort.
    - If there is no way to accomplish the task using the available Tools, return an empty array
    - Make sure the tasks fully complete the initial instructions
    - Final answer in JSON format ONLY with an array of Tasks

    <Example>
      <Message>
        Gather the latest research on AI and summarize it.
      </Message>
      <Tools>
      ... list of Tools ...
      </Tools>
      <OutputJSON>
        {
          "message": "Search the web for the latest AI research",
          "tool": "SearchTool"
        },
        {
          "message": "Scrape the contents of the research web page",
          "tool": "ScrapeTool"
        },
        {
          "message": "Summarize the research",
          "tool": "LLMTool"
        },
      </OutputJSON>
    </Example>

    {{ _.role("user") }}
    <Message>
     {{ message }}
    </Message>

    <Tools>
    {{ ctx.output_format(prefix="</Tools>\n
    If you use this JSON schema correctly I'll tip you $1000:\n
    <OutputJSON>\n") }}
    </OutputJSON>
    ...
  "#
}

test ReasoningAgentTest1 {
  functions [ReasoningAgent]
  args {
    message "What's the weather like in San Diego?"
  }
}

test ReasoningAgentTest2 {
  functions [ReasoningAgent]
  args {
    message "Build me a computer."
  }
}

test ReasoningAgentTest3 {
  functions [ReasoningAgent]
  args {
    message "Use the hammer to strike the nail."
  }
}

test ReasoningAgentTest4 {
  functions [ReasoningAgent]
  args {
    message "Find the latest research on AI and summarize it."
  }
}