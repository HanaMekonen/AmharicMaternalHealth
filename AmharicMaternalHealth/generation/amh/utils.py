from lm_eval.utils import weighted_f1_score


def doc_to_choice_eng(doc):
    choices = doc['English_Answer']
    return choices

def doc_to_choice_amh(doc):
    choices = doc['Amharic_Answer']
    return choices

def doc_to_text_amh_eng_p1(doc):
    output = """ለሚከተለው ጥያቄ መልስ ይስጡ.

                ጥያቄ:
                "{question}"

                መልስ :"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text

def doc_to_text_amh_eng_p2(doc):
    output = """በጥንቃቄ ያንብቡ እና ከዚያ ስለ እሱ ያለዎትን ግንዛቤ የሚፈትሽውን ጥያቄ ይመልሱ።
                
                ጥያቄ:
                "{question}"
                :"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text


def doc_to_text_amh_eng_p3(doc):
    output = """ በጣም ትክክለኛውን መልስ ይምረጡ።
               
                ጥያቄ:
                "{question}"

                መልስ:"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text
