# User input
filename = input("File name: ")

# Make the filename case-insensitive by converting it to lowercase.
new_filename = filename.lower()

if ".gif" in new_filename:
    print("image/gif")
elif ".png" in new_filename:
    print("image/png")
elif ".jpg" in new_filename:
    print("image/jpeg")
elif ".jpeg" in new_filename:
    print("image/jpeg")
elif ".pdf" in new_filename:
    print("application/pdf")
elif ".txt" in new_filename:
    print("text/plain")
elif ".zip" in new_filename:
    print("application/zip")
# Default case when none of the conditions match
else:
    print("application/octet-stream")
