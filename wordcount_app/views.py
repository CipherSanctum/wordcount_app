from django.shortcuts import render
import operator


# Create your views here.
def wordcount(request):
    return render(request, 'wordcount_app/wordcount_home.html')


def wordcount_results(request):
    word_list = {}  # store results
    full_text = request.GET['full_text']  # get text from <textarea>
    split_text = full_text.split()  # splits at space
    delete_values = [',', '.', ';', ':']
    for word in split_text:
        clean_this_word = list(word)
        for character in clean_this_word:
            # for ['a', 'b', 'c,'] in ['abc,']
            clean_list = [character for character in clean_this_word if character not in delete_values]
            cleaned_word = ''.join(clean_list)
        if cleaned_word not in word_list:
            word_list[cleaned_word] = 1
        elif cleaned_word in word_list:
            word_list[cleaned_word] += 1
    sorted_word_list = sorted(word_list.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'wordcount_app/wordcount_results.html', {'sorted_word_list': sorted_word_list, 'word_length': len(split_text), 'full_text': full_text})
