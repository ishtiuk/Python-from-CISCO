total_bytes = 0

try:
    stream = open("image.png", "rb")
    buffer = bytearray(1024*64)
    size = stream.readinto(buffer)

    # while size > 0:                     # if we try to write byte file by file loop the file gets corrupted... that's why we've to use 
    #     total_bytes += size             # larger sized "buffer", so that copying all of the bytes can be done and written at the first attempt, and deny looping... 🙂🙂
    total_bytes += size
    output = open("image_md_by_py.png", 'wb')
    output.write(bytearray(buffer[:size]))
        # size = stream.readinto(buffer)

    stream.close()
    output.close()

except IOError:
    print("failed")
else:
    print(f"success\nTotal Written: {total_bytes/1024} kilobytes")



# NOTE: Very interesting experience for me......... 😎😎😎
