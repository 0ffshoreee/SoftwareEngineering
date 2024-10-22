def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    word_count = len(words)

    sentences = text.split('.')
    sentence_count = len([s for s in sentences if s.strip()])


    paragraphs = text.split('n')
    paragraph_count = len([p for p in paragraphs if p.strip()])


    longest_word = max(words, key=len)
    longest_word_length = len(longest_word)
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(f'Количество слов: {word_count}n')
        output_file.write(f'Количество предложений: {sentence_count}n')
        output_file.write(f'Количество абзацев: {paragraph_count}n')
        output_file.write(f'Самое длинное слово: {longest_word} (длина: {longest_word_length})n')


analyze_text('input.txt')
