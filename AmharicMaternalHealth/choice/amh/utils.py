from lm_eval.utils import weighted_f1_score


def doc_to_choice_eng(doc):
    choices = ['ሀ','ለ','መ','ሰ']
    return choices


def doc_to_text_amh_eng_p1(doc):
    output = """የሚከተለውን ጥያቄ መልስ ይስጡ.

                ጥያቄ:
                "{question}"

                ምርጫ:
                ሀ) {choice1}
                ለ) {choice2}
                መ) {choice3}
                ሰ) {choice4}

                መልስ (ሀ፣ ለ፣ መ ወይስ ሰ):"""

    text = output.format(
        question=doc["Amharic_Questions"],
        choice1=doc["choice_A_amharic"],
        choice2=doc["choice_B_amharic"],
        choice3=doc["choice_C_amharic"],
        choice4=doc["choice_D_amharic"],
    )
    return text

def doc_to_text_amh_eng_p2(doc):
    output = """በታች ያለውን ታሪክ በጥንቃቄ ያንብቡ እና ከዚያ ስለ እሱ ያለዎትን ግንዛቤ የሚፈትሽውን ጥያቄ ይመልሱ።
             
                ጥያቄ:
                "{question}"

                ምርጫ:
                ሀ) {choice1}
                ለ) {choice2}
                መ) {choice3}
                ሰ) {choice4}

                መልስ (ሀ፣ ለ፣ መ ወይስ ሰ):"""

    text = output.format(
        question=doc["Amharic_Questions"],
        choice1=doc["choice_A_amharic"],
        choice2=doc["choice_B_amharic"],
        choice3=doc["choice_C_amharic"],
        choice4=doc["choice_D_amharic"],
    )
    return text


def doc_to_text_amh_eng_p3(doc):
    output = """የሚከተለውን ምንባብ በጥንቃቄ ያንብቡ እና ከዚያ ለሚከተለው ጥያቄ በጣም ትክክለኛውን መልስ ይምረጡ።
    
                ጥያቄ:
                "{question}"

                ምርጫ:
                ሀ) {choice1}
                ለ) {choice2}
                መ) {choice3}
                ሰ) {choice4}

                መልስ (ሀ፣ ለ፣ መ ወይስ ሰ):"""

    text = output.format(
        question=doc["Amharic_Questions"],
        choice1=doc["choice_A_amharic"],
        choice2=doc["choice_B_amharic"],
        choice3=doc["choice_C_amharic"],
        choice4=doc["choice_D_amharic"],
    )
    return text
