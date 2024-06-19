import re

my_pattern = r"[A-z]+'?[a-z]*\s[a-z]+'?[a-z]*\s[a-z]+'?[a-z]*\s[a-z]+'?[a-z]*\s[a-z]+'?[a-z]*.?\s[a-z]+[.|?]"
my_regex = re.compile(my_pattern)

