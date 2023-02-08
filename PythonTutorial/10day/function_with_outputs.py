
def format_name(first, last):
  first_cap = first.title()
  last_cap = last.title()
  return first_cap + " " + last_cap
  
name = format_name("JASON", "wHIsnANT")
print(name)