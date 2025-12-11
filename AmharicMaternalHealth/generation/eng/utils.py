from lm_eval.utils import weighted_f1_score


def doc_to_choice_eng(doc):
    choices = doc['English_Answer']
    return choices

def doc_to_choice_amh(doc):
    choices = doc['Amharic_Answer']
    return choices


def doc_to_text_amh_eng_ep1(doc):
    output = """ Read the question carefully and put the correct answer briefly.

                Question:
                "{question}"

                Your answer :"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text

def doc_to_text_eng_ep1(doc):
    output = """ Read the question carefully and  put the correct answer briefly.

                Question:
                "{question}"

                Your answer :"""

    text = output.format(
        question=doc["English_Questions"]
    )
    return text

def doc_to_text_amh_eng_ep2(doc):
    output = """Read carefully the maternal and child health related questions below and give the correct answer.

                Question:
                "{question}"

                Your answer :"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text

def doc_to_text_eng_ep2(doc):
    output = """ Read carefully the maternal and child health related questions below and give the correct answer.

                Question:
                "{question}"

                Your answer :"""

    text = output.format(
        question=doc["English_Questions"]
    )
    return text


def doc_to_text_amh_eng_ep3(doc):
    output = """ You are a well experienced prenatal and post-natal maternal and child health consultant. You will be provided with questions related to pregnancy, delivery, and postnatal health. Read the question carefully and give the proper answer. 


                Question:
                "{question}"

                Your answer :"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text

def doc_to_text_eng_ep3(doc):
    output = """ You are a well experienced prenatal and post-natal maternal and child health consultant. You will be provided with questions related to pregnancy, delivery, and postnatal health. Read the question carefully and give the proper answer. 

                Story:
                "{story}"

                Question:
                "{question}"

                Your answer :"""

    text = output.format(
        question=doc["English_Questions"]
    )
    return text
