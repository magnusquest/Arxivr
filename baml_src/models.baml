
// Classes //

class Message {
  role string @description("The role of the entity that sent the message.")
  message string @description("Instructions for the agent.")
}

class Task {
  message string @description("Instructions for the agent.")
  tool ToolType @description("The agent that should handle the task.")
}

// Enums //
enum ToolType {
  TimeTool
  @description(#"
    A tool that provides information about the current time.
  "#)

  WeatherTool
  @description(#"
    A tool that provides information about the weather.
  "#)

  RequestTool
  @description(#"
    A tool that sends a request to a url.
  "#)

  SearchTool
  @description(#"
    A tool that searches the web for information.
  "#)

  ScrapeTool
  @description(#"
    A tool that scrapes information from a website.
  "#)

  LLMTool
  @description(#"
    A tool that can process text conceptually to generate a summary, answer questions, or provide disambiguating information.
  "#)
}
