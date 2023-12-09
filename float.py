#!/usr/bin/env python3

import math
import numpy
import cairo
import asyncio
import libacmchristmas.tree


async def main():
    url = "ws://192.168.1.175:9000/ws/018c4c33-5c87-7ff1-bcbe-760acf2affd8"
    fps = 10

    tree = libacmchristmas.tree.TreeController(url)
    await tree.connect()
    assert tree.ix
    assert tree.iy

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, tree.ix, tree.iy)
    context = cairo.Context(surface)
    bg_color = (0, 0, 0)
    fg_color = (0, 0.45, 0.9)
    star_color = (1.0, 1.0, 0)


    height = 0
    dir = 2
    while True:

        context.set_source_rgb(*bg_color)
        context.rectangle(0, 0, tree.ix, tree.iy)
        context.fill()

        context.set_source_rgb(*fg_color)
        context.rectangle(0, tree.iy - height, tree.ix, height)
        context.fill()

        context.set_source_rgb(*star_color)
        context.arc(tree.ix/2, tree.iy - height - 2, 3, 0, 2*math.pi)
        context.close_path()
        context.set_source_rgb(*star_color)
        context.stroke()

        # print(0, tree.iy - height, tree.ix, height)

        if (height < 0):
            dir = 2
        elif (height >= tree.iy):
            dir = -2
        height += dir
        await tree.update_image(numpy.asarray(surface.get_data()))
        await asyncio.sleep(1 / fps)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
