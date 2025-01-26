from baml_py import Image
from baml_client import b

async def test_image_input():
  # from URL
  res = b.DescribeMedia(
      img=Image.from_url(
          "https://upload.wikimedia.org/wikipedia/en/4/4d/Shrek_%28character%29.png"
      )
  )

  # Base64 image
  image_b64 = "iVBORw0K...."
  res = b.DescribeMedia(
    img=Image.from_base64("image/png", image_b64)
  )
