# guest list program

# starting guest list
guests = ["Emmanuel", "Aissatou", "Jean"]

print("invitations:")
for guest in guests:
    print("hey " + guest + ", you are invited to dinner.")

# one guest can't come
print("\n" + guests[1] + " can't come to dinner.")

# replace guest
guests[1] = "Marie"

print("\nnew invitations:")
for guest in guests:
    print("hey " + guest + ", you are invited to dinner.")

# found a bigger table
print("\nfound a bigger table!")

# add more guests
guests.insert(0, "Blaise")       # beginning
guests.insert(2, "Chantal")      # middle
guests.append("Luc")             # end

print("\nall invitations:")
for guest in guests:
    print("hey " + guest + ", you are invited to dinner.")

# only two guests can come
print("\nonly two people can come now.")

while len(guests) > 2:
    removed = guests.pop()
    print("sorry " + removed + ", you can't come.")

print("\nguests still invited:")
for guest in guests:
    print(guest + ", you are still invited.")

# empty the list
guests = []
print("\nfinal guest list:")
print(guests)
