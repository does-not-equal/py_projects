# needed help, reviewing slices and indexes. len() is
# self-explanatory

def find_and_replace(text, old_text, new_text):
    replaced_text = ''
    i = 0
    while i < len(text):
        if text[i:i + len(old_text)] == old_text:
            replaced_text += new_text
            i += len(old_text)
        else:
            replaced_text += text[i]
            i += 1
    return replaced_text


assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
assert find_and_replace('fox', 'fox', 'dog') == 'dog'
assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'