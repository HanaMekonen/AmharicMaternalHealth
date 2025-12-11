from lm_eval.utils import weighted_f1_score


def doc_to_choice_eng(doc):
    choices = ['A','B','C','D']
    return choices


def doc_to_text_amh_eng_ep1(doc):
    output = """Please read the question carefully and choose the correct answer from the four choices.
                Question:
                "{question}"

                Choices:
                A) {choice1}
                B) {choice2}
                C) {choice3}
                D) {choice4}

                Your answer (A, B, C, or D):"""

    text = output.format(
        question=doc["Amharic_Questions"],
        choice1=doc["choice_A_amharic"],
        choice2=doc["choice_B_amharic"],
        choice3=doc["choice_C_amharic"],
        choice4=doc["choice_D_amharic"],
    )
    return text

def doc_to_text_eng_ep1(doc):
    output = """Please read the question carefully and choose the correct answer from the four choices.

                Story:
                "{story}"

                Question:
                "{question}"

                Choices:
                A) {choice1}
                B) {choice2}
                C) {choice3}
                D) {choice4}

                Your answer (A, B, C, or D):"""

    text = output.format(
        question=doc["Amharic_Questions"],
        choice1=doc["choice_A_amharic"],
        choice2=doc["choice_B_amharic"],
        choice3=doc["choice_C_amharic"],
        choice4=doc["choice_D_amharic"],
    )
    return text

def doc_to_text_amh_eng_ep2(doc):
    output = """ Read carefully the maternal and child health related questions below with four possible answers and choose the correct answer by answering only one letter A, B, D, or G.

                Story:
                "{story}"

                Question:
                "{question}"

                Choices:
                A) {choice1}
                B) {choice2}
                C) {choice3}
                D) {choice4}

                Your answer (A, B, C, or D):"""

    text = output.format(
        question=doc["Amharic_Questions"],
        choice1=doc["choice_A_amharic"],
        choice2=doc["choice_B_amharic"],
        choice3=doc["choice_C_amharic"],
        choice4=doc["choice_D_amharic"],
    )
    return text

def doc_to_text_eng_ep2(doc):
    output = """Read carefully the maternal and child health related questions below with four possible answers and choose the correct answer by answering only one letter A, B, D, or G.
                
                Question:
                "{question}"

                Choices:
                A) {choice1}
                B) {choice2}
                C) {choice3}
                D) {choice4}

                Your answer (A, B, C, or D):"""

    text = output.format(
        question=doc["English_Questions"],
        choice1=doc["choice_A_english"],
        choice2=doc["choice_B_english"],
        choice3=doc["choice_C_english"],
        choice4=doc["choice_D_english"],
    )
    return text


def doc_to_text_amh_eng_ep3(doc):
    output = """ You are a well experienced prenatal and post-natal maternal and child health consultant. You will be provided with optional questions related to pregnancy, delivery, and postnatal health. Your task is to read the question carefully and choose the best answer from the options (a, b, d, or g).


                Question:
                "{question}"

                Choices:
                A) {choice1}
                B) {choice2}
                C) {choice3}
                D) {choice4}

                Your answer (A, B, C, or D):"""

    text = output.format(
        question=doc["English_Questions"],
        choice1=doc["choice_A_english"],
        choice2=doc["choice_B_english"],
        choice3=doc["choice_C_english"],
        choice4=doc["choice_D_english"],
    )
    return text

def doc_to_text_eng_ep3(doc):
    output = """ You are a well experienced prenatal and post-natal maternal and child health consultant. You will be provided with optional questions related to pregnancy, delivery, and postnatal health. Your task is to read the question carefully and choose the best answer from the options (a, b, d, or g).

                
                Question:
                "{question}"

                Choices:
                A) {choice1}
                B) {choice2}
                C) {choice3}
                D) {choice4}

                Your answer (A, B, C, or D):"""

    text = output.format(
        question=doc["English_Questions"],
        choice1=doc["choice_A_english"],
        choice2=doc["choice_B_english"],
        choice3=doc["choice_C_english"],
        choice4=doc["choice_D_english"],
    )
    return text
