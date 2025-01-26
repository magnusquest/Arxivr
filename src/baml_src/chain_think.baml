class Email {
  subject string
  body string
  from_address string
}

class OrderInfo {
  order_status "ORDERED" | "SHIPPED" | "DELIVERED" | "CANCELLED"
  tracking_number string?
  estimated_arrival_date string?
}

function GetOrderInfo(email: Email) -> OrderInfo {
  client LlamaClient
  prompt #"
    Extract the info from this email in the INPUT:

    INPUT:
    -------
    from: {{email.from_address}}
    Email Subject: {{email.subject}}
    Email Body: {{email.body}}
    -------

    {{ ctx.output_format }}

    Before you output the JSON, please explain your
    reasoning step-by-step. Here is an example on how to do this:
    'If we think step by step we can see that ...
     therefore the output JSON is:
    {
      ... the json schema ...
    }'
  "#
}

test ThinkTest {
  functions [GetOrderInfo]
  args {
    email {
      from_address "hello@amazon.com"
      subject "Your Amazon.com order of 'Wood Dowel Rods...' has shipped!"
      body #"
        Hi Sam, your package will arrive:
        Thurs, April 4
        Track your package:
        www.amazon.com/gp/your-account/ship-track?ie=23&orderId123

        On the way:
        Wood Dowel Rods...
        Order #113-7540940
        Ship to:
            Sam
            SEATTLE, WA

        Shipment total:
        $0.00
    "#

    }
  }
}
