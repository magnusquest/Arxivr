# from baml_client import b
# from baml_client.types import ProductSearch, ScheduleAppointment
# response = b.ChooseOneTool(user_message="Find me running shoes under $100 in the sports category")
# print(response)

# if isinstance(response, ProductSearch):
#     print(f"Product Search called:")
#     print(f"Query: {response.query}")
#     print(f"Max Price: ${response.maxPrice}")
#     print(f"Category: {response.category}")
# elif isinstance(response, ScheduleAppointment):
#     print(f"Schedule Appointment called:")
#     print(f"Customer: {response.customerName}")
#     print(f"Service: {response.serviceType}")
#     print(f"Date: {response.preferredDate}")
#     print(f"Duration: {response.duration} minutes")

# response = b.ClassifySupport(message="The app keeps crashing when I try to upload files")
# print(f"Category: {response.category}")
# print(f"Priority: {response.priority}")
