# Вариант 39
def main(s):
    s = s.replace('\n', ' ')  # .replace('\t', '')
    result = dict()
    s = s.split(";")
    for item in s:
        k = item.find("=:")
        if k != -1:
            login = item[k + 2:].strip()
            sub = item[0:k].strip()
            p = sub.rfind(" ")
            password = sub[p:].strip()
            result[login] = password
    return result


in_1 = "<section> <section> declare isqube_386 =: rira_263; </section>\
<section> declare isaron =: ribi_554; </section><section> declare \
atradi_19 =:axeer; </section> <section> declare atarle =: vesoce_684;\
</section> </section>"
main(in_1)

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == '__main__':
    print("\nResults:\n")
    in_2 = "<section> <section>declare leri_316 =:\
    edatri;</section><section>declare riones =: gein; </section>\
    </section>"
    print("Res 1:", main(in_1))
    print("Res 2:", main(in_2))
    print("\n", "-" * 20, "Done!", "-" * 20)
