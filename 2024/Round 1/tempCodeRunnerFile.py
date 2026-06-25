        if mash[button] == mash[button -1]:
            contigous = True 
        else:
            if contigous:
                game_engine_readable += f"S{mash[button-1]}"
            else:
                game_engine_readable += f"{mash[button]}"
            
            contigous = False