
enum Category {
  TECHNICAL_ISSUE
  BILLING_QUESTION
  FEATURE_REQUEST
  OTHER
}

class Response {
  category Category
  priority string @description("high, medium, or low")
  message string @description(#"
  a helpful response to the customer's inquiry
  use triple quote strings for multiline
  "#)
  internal_notes string @description("notes for the support team")
}

function ClassifySupport(message: string) -> Response {
  client DeepseekClient
  prompt #"
    Classify the customer support inquiry and provide appropriate response details.

    {{ ctx.output_format(prefix="Using this:") }}
    {{ _.role("user") }}
    {{ message }}
  "#
}

test TestName {
  functions [ClassifySupport]
  args {
    message "The app keeps crashing when I try to upload files"
  }
  @@assert(category, {{ this.category == "TECHNICAL_ISSUE" }})
}
