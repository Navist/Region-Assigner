from datetime import datetime
#Command error
# Who issued a command / What command

# Where the command was issued?

# What to have print


# Kick
# Ban

# Member:
#   Join (New / Returning)
#   Leave

# Error
# 

#print(f"[USER-RETURN] | {datetime.datetime.now().strftime('@%H:%M:%S%p')} | {str(member)}:{member.id} joined the server.")

async def console_print(print_type: str, tail_print: str):
    print(f"{datetime.now().strftime('%H:%M:%S%p')} | [{print_type.upper()}] | {tail_print}")
