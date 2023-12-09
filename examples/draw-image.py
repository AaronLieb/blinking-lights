#!/usr/bin/env python3

import PIL.Image
import asyncio
import libacmchristmas.tree


async def main():
    url = "wss://blinktest.acmcsuf.com/ws/018c4c15-7cd6-7407-80f7-640f781bee51"

    tree = libacmchristmas.tree.TreeController(url)
    await tree.connect()
    print(f"Canvas is {tree.ix}x{tree.iy}")

    imagePath = "static/rainbow.jpg"

    # Example: Loading a file from disk using draw_from_file
    await tree.draw_from_file(imagePath)  # can also use tree.draw()
    print(f"Drew {imagePath}!")

    # Example: Loading a PIL image
    image = PIL.Image.open(imagePath)
    await tree.draw(image)
    print(f"Drew {imagePath} a second time!")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
