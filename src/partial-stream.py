import asyncio
from baml_client import b, partial_types, types

# Using a stream:
async def example1(receipt: str):
    stream = b.stream.ExtractReceiptInfo(receipt)

    # partial is a Partial type with all Optional fields
    for partial in stream:
        print(f"partial: parsed {len(partial.items)} items (object: {partial})")

    # final is the full, original, validated ReceiptInfo type
    final = stream.get_final_response()
    print(f"final: {len(final.items)} items (object: {final})")

# Using only get_final_response() of a stream
#
# In this case, you should just use b.ExtractReceiptInfo(receipt) instead,
# which is slightly faster and more efficient.
async def example2(receipt: str):
    final = b.stream.ExtractReceiptInfo(receipt).get_final_response()
    print(f"final: {len(final.items)} items (object: {final})")

# Using the async client:
async def example3(receipt: str):
    # Note the import of the async client
    from baml_client.async_client import b
    stream = b.stream.ExtractReceiptInfo(receipt)
    async for partial in stream:
        print(f"partial: parsed {len(partial.items)} items (object: {partial})")

    final = await stream.get_final_response()
    print(f"final: {len(final.items)} items (object: {final})")

receipt = """
04/14/2024 1:05 pm

Ticket: 220000082489
Register: Shop Counter
Employee: Connor
Customer: Sam
Item	#	Price
Guide leash (1 Pair) uni UNI
1	$34.95
The Index Town Walls
1	$35.00
Boot Punch
3	$60.00
Subtotal	$129.95
Tax ($129.95 @ 9%)	$11.70
Total Tax	$11.70
Total	$141.65
"""

if __name__ == '__main__':
    asyncio.run(example1(receipt))
    # asyncio.run(example2(receipt))
    # asyncio.run(example3(receipt))
