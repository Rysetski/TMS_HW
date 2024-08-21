

with open('test.txt', 'r', encoding='utf-8') as in_f_obj:
    with open('new_file.txt', 'w', encoding='utf-8') as out_f_obj:
        for line in in_f_obj:
            line = line.strip()
            if not line:  # Пропускаем пустые строки
                continue
            dictionary = {}
            line = line.lower()
            for word in line.split():
                if word not in dictionary:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1

            max_quantity = 0
            word_with_max_quantity = None

            for key, value in dictionary.items():
                if value > max_quantity:
                    max_quantity = value
                    word_with_max_quantity = key

            if word_with_max_quantity:
                most_popular = f"{word_with_max_quantity} {max_quantity}\n"
                out_f_obj.write(most_popular)
