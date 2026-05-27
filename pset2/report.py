def main():
    cats = {"name":"Dami", "sex":"male","age":8}
    cats.update({"hobby":"play outside", "color":"tabby"})
    print(create_report(cats))

# add a single key(direct assignment):
# cat["hobby"]="play outside"
# add multiple keys,.update method
# cat.update({"","",""})

def create_report(cats):
    return f""":
    ===============report===============

    name: {cats.get("name", "unknow")}
    gender: {cats.get("sex", "unknow")}
    shape: {cats.get("color","unknow")}
    ====================================
    """
# dictionary.get(key, default_value)
#The dict.get() method in Python allows you to safely retrieve a value for a specific key.
# If the key exists, it returns the value;
# if it does not,it returns None (or a custom default value)
# instead of throwing an error

main()