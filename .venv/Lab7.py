import re


def analyze_do_while(code_line):
    code_line = code_line.strip()

    if not re.match(r'do\s*\{.*\}\s*while\s*\(.*\)', code_line):
        return "Ошибка: некорректный формат цикла do-while"

    print("Анализ цикла do-while:")


    lexeme_table = []
    lexeme_dict = {}


    lexeme_sequence = []


    def add_lexeme(lexeme_value, lexeme_type, info):
        nonlocal lexeme_table, lexeme_dict


        if lexeme_value in lexeme_dict:
            return lexeme_dict[lexeme_value]


        lexeme_id = len(lexeme_table) + 1
        lexeme_table.append((lexeme_id, lexeme_value, lexeme_type, info))
        lexeme_dict[lexeme_value] = lexeme_id
        return lexeme_id


    tokens = re.findall(r'[a-zA-Z_]\w*|\d+\.?\d*|[+\-*/=<>!&|(){};]+', code_line)

    for token in tokens:
        if token == 'do' or token == 'while':
            lexeme_sequence.append(token)
        elif re.match(r'^[a-zA-Z_]\w*$', token):

            lexeme_id = add_lexeme(token, "per", "переменная")
            lexeme_sequence.append(f"<per>{lexeme_id}")
        elif re.match(r'^\d+\.?\d*$', token):

            lexeme_id = add_lexeme(token, "const", "константа")
            lexeme_sequence.append(f"<const>{lexeme_id}")
        else:

            lexeme_sequence.append(token)


    print(f"{'№':<4} {'Идентификатор':<15} {'Лексема':<15} {'Информация':<20}")
    print("-" * 60)
    for lexeme in lexeme_table:
        print(f"{lexeme[0]:<4} {lexeme[1]:<15} {lexeme[2]:<15} {lexeme[3]:<20}")

    lexeme_string = "".join(lexeme_sequence)

    print(lexeme_string)

    return lexeme_table, lexeme_sequence


while True:
    user_input = input("\nВведите строку цикла do-while (или 'exit' для выхода): ")

    if user_input.lower() == 'exit':
        break

    try:
        analyze_do_while(user_input)
    except Exception as e:
        print(f"Ошибка при анализе: {e}")