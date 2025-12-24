moma_artworks = {"Starry Night", "The Persistence of Memory", "The Scream", "Girl with a Pearl Earring"}

print("moma_artworks",moma_artworks)

louvre_artworks = {"Mona Lisa", "The Scream", "Liberty Leading the People", "Girl with a Pearl Earring"}

print("\nOriginal louvre_artworks",louvre_artworks)

rijksmuseum_artworks = {"The Night Watch", "Girl with a Pearl Earring", "The Milkmaid", "Starry Night"}

print("\nOriginal rijksmuseum_artworks",rijksmuseum_artworks)

moma_artworks.add( "Composition with Red, Blue, and Yellow."
)

print("\nUpdated  Moma artworks",moma_artworks)

Shared_masterpiece=(moma_artworks).intersection(louvre_artworks,rijksmuseum_artworks)

print("\nShared Artwork",Shared_masterpiece)

louvre_artworks.update({"Raft of the Medusa", "Liberty Leading the People"})
rijksmuseum_artworks.update({"The Jewish Bride", "The Milkmaid"})

print("\nUpdated louvre_artworks",louvre_artworks,"\n Updated rijksmuseum_artworks",rijksmuseum_artworks)

unique_master_piece=moma_artworks.union(louvre_artworks,rijksmuseum_artworks)

print("\nUnique Master Piece",len(unique_master_piece),"\n",unique_master_piece)


rijksmuseum_artworks.discard("The Nilkmaid")
print("\nAfter Removing Milkmaid",rijksmuseum_artworks)

Exclusive_pieces=moma_artworks.difference(louvre_artworks,rijksmuseum_artworks)

print("\nThe Exclusive pieces",Exclusive_pieces)