
class ProductSearch {
  query string @description("search query for the product")
  maxPrice float @description("maximum price filter")
  category string @description("product category filter")
}

class ScheduleAppointment {
  customerName string
  serviceType string @description("type of service requested")
  preferredDate string @description("As an ISO8601 timestamp")
  duration int @description("duration in minutes")
}

function ChooseOneTool(user_message: string) -> ProductSearch | ScheduleAppointment {
  client LlamaClient
  prompt #" 
    Choose the right schema that contains all the information in this message and give the output schema filling in the fields.:
    ---
    {{ user_message }}
    ---

    {# special macro to print the output schema. #}
    {{ ctx.output_format }}

    JSON:
  "# 
}

test TestOneFunc {
  functions [ChooseOneTool]
  args {
    user_message #"
      Find me running shoes under $100 in the sports category
    "#
  }
}

test TestOneFunc2 {
  functions [ChooseOneTool]
  args {
    user_message #"
      I need to schedule a haircut appointment for John Smith next Tuesday at 2pm for 30 minutes
    "#
  }
}
