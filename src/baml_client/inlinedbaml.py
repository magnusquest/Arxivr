###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

file_map = {
    
    "chain_think.baml": "class Email {\n  subject string\n  body string\n  from_address string\n}\n\nclass OrderInfo {\n  order_status \"ORDERED\" | \"SHIPPED\" | \"DELIVERED\" | \"CANCELLED\"\n  tracking_number string?\n  estimated_arrival_date string?\n}\n\nfunction GetOrderInfo(email: Email) -> OrderInfo {\n  client LlamaClient\n  prompt #\"\n    Extract the info from this email in the INPUT:\n\n    INPUT:\n    -------\n    from: {{email.from_address}}\n    Email Subject: {{email.subject}}\n    Email Body: {{email.body}}\n    -------\n\n    {{ ctx.output_format }}\n\n    Before you output the JSON, please explain your\n    reasoning step-by-step. Here is an example on how to do this:\n    'If we think step by step we can see that ...\n     therefore the output JSON is:\n    {\n      ... the json schema ...\n    }'\n  \"#\n}\n\ntest ThinkTest {\n  functions [GetOrderInfo]\n  args {\n    email {\n      from_address \"hello@amazon.com\"\n      subject \"Your Amazon.com order of 'Wood Dowel Rods...' has shipped!\"\n      body #\"\n        Hi Sam, your package will arrive:\n        Thurs, April 4\n        Track your package:\n        www.amazon.com/gp/your-account/ship-track?ie=23&orderId123\n\n        On the way:\n        Wood Dowel Rods...\n        Order #113-7540940\n        Ship to:\n            Sam\n            SEATTLE, WA\n\n        Shipment total:\n        $0.00\n    \"#\n\n    }\n  }\n}\n",
    "chat-history.baml": "class MyUserMessage {\n  role \"user\" | \"assistant\"\n  content string\n}\n\nfunction ChatWithLLM(messages: MyUserMessage[]) -> string {\n  client LlamaClient\n  prompt #\"\n    Answer the user's questions based on the chat history:\n    {% for message in messages %}\n      {{ _.role(message.role) }} \n      {{ message.content }}\n    {% endfor %}\n\n    Answer:\n  \"#\n}\n\ntest TestName {\n  functions [ChatWithLLM]\n  args {\n    messages [\n      {\n        role \"user\"\n        content \"Hello!\"\n      }\n      {\n        role \"assistant\"\n        content \"Hi!\"\n      }\n    ]\n  }\n}\n\n",
    "classification.baml": "\nenum Category {\n  TECHNICAL_ISSUE\n  BILLING_QUESTION\n  FEATURE_REQUEST\n  OTHER\n}\n\nclass Response {\n  category Category\n  priority string @description(\"high, medium, or low\")\n  message string @description(#\"\n  a helpful response to the customer's inquiry\n  use triple quote strings for multiline\n  \"#)\n  internal_notes string @description(\"notes for the support team\")\n}\n\nfunction ClassifySupport(message: string) -> Response {\n  client DeepseekClient\n  prompt #\"\n    Classify the customer support inquiry and provide appropriate response details.\n\n    {{ ctx.output_format(prefix=\"Using this:\") }}\n    {{ _.role(\"user\") }}\n    {{ message }}\n  \"#\n}\n\ntest TestName {\n  functions [ClassifySupport]\n  args {\n    message \"The app keeps crashing when I try to upload files\"\n  }\n  @@assert(category, {{ this.category == \"TECHNICAL_ISSUE\" }})\n}\n",
    "clients.baml": "// Learn more about clients at https://docs.boundaryml.com/docs/snippets/clients/overview\n\nclient<llm> GPT4oMini {\n  provider openai\n  options {\n    model \"gpt-4o-mini\"\n    api_key env.OPENAI_API_KEY\n  }\n}\n\nclient<llm> DeepseekClient {\n  provider ollama\n  options {\n    base_url \"http://localhost:11434/v1\"\n    model \"deepseek-r1\"\n  }\n}\n\nclient<llm> PhiClient {\n  provider ollama\n  options {\n    base_url \"http://localhost:11434/v1\"\n    model \"phi4\"\n  }\n}\n\nclient<llm> LlamaClient {\n  provider ollama\n  options {\n    base_url \"http://localhost:11434/v1\"\n    model \"llama3.2\"\n  }\n}\n\nclient<llm> ToolClient {\n  provider ollama\n  options {\n    base_url \"http://localhost:11434/v1\"\n    model \"llama3-groq-tool-use\"\n  }\n}\n\nclient<llm> LlavaClient {\n  provider ollama\n  options {\n    base_url \"http://localhost:11434/v1\"\n    model \"llava:7b\"\n  }\n}\n",
    "generators.baml": "// This helps use auto generate libraries you can use in the language of\n// your choice. You can have multiple generators if you use multiple languages.\n// Just ensure that the output_dir is different for each generator.\ngenerator target {\n    // Valid values: \"python/pydantic\", \"typescript\", \"ruby/sorbet\", \"rest/openapi\"\n    output_type \"python/pydantic\"\n\n    // Where the generated code will be saved (relative to baml_src/)\n    output_dir \"../\"\n\n    // The version of the BAML package you have installed (e.g. same version as your baml-py or @boundaryml/baml).\n    // The BAML VSCode extension version should also match this version.\n    version \"0.73.4\"\n\n    // Valid values: \"sync\", \"async\"\n    // This controls what `b.FunctionName()` will be (sync or async).\n    default_client_mode sync\n}\n",
    "multimodal.baml": "// \"image\" is a reserved keyword so we name the arg \"img\"\nfunction DescribeMedia(img: image) -> string {\n  client LlavaClient\n  // Most LLM providers require images or audio to be sent as \"user\" messages.\n  prompt #\"\n    {{_.role(\"user\")}}\n    Describe this image: {{ img }}\n  \"#\n}\n\n// See the \"testing functions\" Guide for more on testing Multimodal functions\ntest TestMuliModal {\n  functions [DescribeMedia]\n  args {\n    img {\n      url \"https://upload.wikimedia.org/wikipedia/en/4/4d/Shrek_%28character%29.png\"\n    }\n  }\n}\n",
    "resume.baml": "// Defining a data model.\nclass Resume {\n  name string\n  email string\n  experience string[]\n  skills string[]\n}\n\n// Create a function to extract the resume from a string.\nfunction ExtractResume(resume: string) -> Resume {\n  // Specify a client as provider/model-name\n  // you can use custom LLM params with a custom client name from clients.baml like \"client CustomHaiku\"\n  client LlamaClient // Set OPENAI_API_KEY to use this client.\n  prompt #\"\n    Extract from this content:\n    {{ resume }}\n\n    {{ ctx.output_format }}\n  \"#\n}\n\n// Test the function with a sample resume. Open the VSCode playground to run this.\ntest vaibhav_resume {\n  functions [ExtractResume]\n  args {\n    resume #\"\n      Vaibhav Gupta\n      vbv@boundaryml.com\n\n      Experience:\n      - Founder at BoundaryML\n      - CV Engineer at Google\n      - CV Engineer at Microsoft\n\n      Skills:\n      - Rust\n      - C++\n    \"#\n  }\n}\n",
    "symbolTuning.baml": "enum Option {\n    Refund @alias(\"k1\")\n    @description(\"Customer wants to refund a product\")\n\n    CancelOrder @alias(\"k2\")\n    @description(\"Customer wants to cancel an order\")\n\n    TechnicalSupport @alias(\"k3\")\n    @description(\"Customer needs help with a technical issue unrelated to account creation or login\")\n\n    AccountIssue @alias(\"k4\")\n    @description(\"Specifically relates to account-login or account-creation\")\n\n    Question @alias(\"k5\")\n    @description(\"Customer has a question\")\n}\n\nfunction ClassifyMessageWithSymbol(input: string) -> Option {\n  client DeepseekClient\n  prompt #\"\n    Classify the following INPUT into ONE\n    of the following categories:\n\n    INPUT: {{ input }}\n\n    {{ ctx.output_format }}\n\n    RESPONSE:\n\n  \"#\n}\n\ntest Test1 {\n  functions [ClassifyMessageWithSymbol]\n  args {\n    input #\"\n    I can't access my account using my login credentials. I havent received the promised reset password email. Please help.\n    \"#\n  }\n}\n\ntest Test2 {\n  functions [ClassifyMessageWithSymbol]\n  args {\n    input \"I would like to return the product I purchased last week.\"\n  }\n}\n\ntest Test3 {\n  functions [ClassifyMessageWithSymbol]\n  args {\n    input \"I need to cancel my order that I placed yesterday.\"\n  }\n}\n\ntest Test4 {\n  functions [ClassifyMessageWithSymbol]\n  args {\n    input \"My computer is not turning on, can you help me with this technical issue?\"\n  }\n}\n\ntest Test5 {\n  functions [ClassifyMessageWithSymbol]\n  args {\n    input \"I have a question about the features of your new product.\"\n  }\n}",
    "toolCalling.baml": "\nclass ProductSearch {\n  query string @description(\"search query for the product\")\n  maxPrice float @description(\"maximum price filter\")\n  category string @description(\"product category filter\")\n}\n\nclass ScheduleAppointment {\n  customerName string\n  serviceType string @description(\"type of service requested\")\n  preferredDate string @description(\"As an ISO8601 timestamp\")\n  duration int @description(\"duration in minutes\")\n}\n\nfunction ChooseOneTool(user_message: string) -> ProductSearch | ScheduleAppointment {\n  client LlamaClient\n  prompt #\" \n    Choose the right schema that contains all the information in this message and give the output schema filling in the fields.:\n    ---\n    {{ user_message }}\n    ---\n\n    {# special macro to print the output schema. #}\n    {{ ctx.output_format }}\n\n    JSON:\n  \"# \n}\n\ntest TestOneFunc {\n  functions [ChooseOneTool]\n  args {\n    user_message #\"\n      Find me running shoes under $100 in the sports category\n    \"#\n  }\n}\n\ntest TestOneFunc2 {\n  functions [ChooseOneTool]\n  args {\n    user_message #\"\n      I need to schedule a haircut appointment for John Smith next Tuesday at 2pm for 30 minutes\n    \"#\n  }\n}\n",
}

def get_baml_files():
    return file_map