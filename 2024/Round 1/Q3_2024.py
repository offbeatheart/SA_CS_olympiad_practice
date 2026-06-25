


mash = input() + ";"
game_engine_readable = ""
contigous = False
prev_state = False
end_game = ""

for button in range(len(mash)):
    if mash[button] == ";":
            break
    if mash[button] != mash[button+ 1]:
        if contigous:
            contigous = False
            end_game += "S" +mash[button]

        else:
             end_game += mash[button]
    else:
          contigous = True 

print(end_game)

# for button in range(len(mash)):
#     if mash[button] == ";":
#         break

#     if mash[button] == mash[button +1 ]:
#         prev_state = contigous
#         contigous = True
#     else:
#         prev_state = contigous
#         contigous = False

#     if contigous == False and prev_state == False:
#         end_game += mash[button]
#     else:
#         if contigous and prev_state:
#             pass
#         else:

#             end_game += "S" + mash[button]

# print(end_game)


# for button in range(len(mash)):
#     if button > 0:
#         if mash[button] == mash[button -1]:
#             contigous = True 
#         else:
#             if contigous:
#                 game_engine_readable += f"S{mash[button-1]}"
#             else:
#                 game_engine_readable += f"{mash[button]}"
            
#             contigous = False
#     else:




print(game_engine_readable)
    
