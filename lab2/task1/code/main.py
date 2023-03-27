from colorama import Fore
from helper_functions import color_print, print_result, is_input_valid
from calculations import get_sentences, get_amount_of_sentences, get_top_K_repeated_N_grams, get_average_length_of_sentence, get_average_length_of_word, get_amount_of_non_declarative_sentences


def main():
    while True:
        input_choice = input(
            "Enter 'e' to enter text or 'exit' to quit: ")

        if input_choice == 'e':
            color_print("Write here: ", Fore.YELLOW, '')
            text = input()
            if not is_input_valid(text):
                color_print("Invalid text!", Fore.RED)
                continue
            break
        elif input_choice == 'exit':
            exit()
        else:
            color_print("Invalid choice!", Fore.RED)

    K = None
    N = None

    while True:
        input_choice = input(
            "Do you want to set K and N manually? Type 'y' if yes, 'n' if no or 'exit' to quit: ")

        if input_choice == 'y':
            try:
                color_print("Enter K: ", Fore.YELLOW, '')
                K = int(input())
                color_print("Enter N: ", Fore.YELLOW, '')
                N = int(input())
                print()
            except:
                color_print("Invalid input!", Fore.RED)
                continue
            break
        elif input_choice == 'n':
            break
        elif input_choice == 'exit':
            exit()
        else:
            color_print("Invalid choice!", Fore.RED)

    results = dict()

    results['amount of sentences in the text'] = get_amount_of_sentences(text)
    results['amount of non-declarative sentences in the text'] = get_amount_of_non_declarative_sentences(
        text)
    results['amount of sentences in the text'] = get_amount_of_sentences(text)
    results['average length of the sentence in characters (words count only)'] = get_average_length_of_sentence(
        text)
    results['average length of the word in the text in characters'] = get_average_length_of_word(
        text)

    if (K is not None):
        results[f'top-{K} repeated {N}-grams in the text'] = get_top_K_repeated_N_grams(
            text, K, N)
    else:
        results['top-10 repeated 4-grams in the text'] = get_top_K_repeated_N_grams(
            text)

    print_result(results)


if __name__ == "__main__":
    main()
