enum Option {
    Refund @alias("k1")
    @description("Customer wants to refund a product")

    CancelOrder @alias("k2")
    @description("Customer wants to cancel an order")

    TechnicalSupport @alias("k3")
    @description("Customer needs help with a technical issue unrelated to account creation or login")

    AccountIssue @alias("k4")
    @description("Specifically relates to account-login or account-creation")

    Question @alias("k5")
    @description("Customer has a question")
}

function ClassifyMessageWithSymbol(input: string) -> Option {
  client DeepseekClient
  prompt #"
    Classify the following INPUT into ONE
    of the following categories:

    INPUT: {{ input }}

    {{ ctx.output_format }}

    RESPONSE:

  "#
}

test Test1 {
  functions [ClassifyMessageWithSymbol]
  args {
    input #"
    I can't access my account using my login credentials. I havent received the promised reset password email. Please help.
    "#
  }
}

test Test2 {
  functions [ClassifyMessageWithSymbol]
  args {
    input "I would like to return the product I purchased last week."
  }
}

test Test3 {
  functions [ClassifyMessageWithSymbol]
  args {
    input "I need to cancel my order that I placed yesterday."
  }
}

test Test4 {
  functions [ClassifyMessageWithSymbol]
  args {
    input "My computer is not turning on, can you help me with this technical issue?"
  }
}

test Test5 {
  functions [ClassifyMessageWithSymbol]
  args {
    input "I have a question about the features of your new product."
  }
}