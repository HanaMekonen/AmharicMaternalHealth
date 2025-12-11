from lm_eval.utils import weighted_f1_score


def doc_to_choice_eng(doc):
    choices = ['ሀ','ለ','መ','ሰ']
    return choices


def doc_to_text_amh_eng_p1(doc):
    output = """በመቀጠል የተሰጠውን ጥያቄ በጥንቃቄ በማንበብ ከተዘረዘሩት አራት ምርጫዎች መካከል ትክክለኛ መልስ የሚሆነውን ይምረጡ።

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
    output = """ከዚህ በታች የተሰጠውን አራት አማራጮችን የያዘ  የእናቶችና ህናትን ጤናን የተመለከተ ጥያቄ በጥንቃቄ በማንበብ ሀ፣ ለ፣ መ፣ ወይም ሰ በማለት አንድ ፊደል ብቻ በመምረጥ ትክክለኛውን መልስ ይመልሱ።
             
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
    output = """በደንብ ልምድ ያሎት የቅድመ ወሊድ እና የድህረ ወሊድ እናቶችና ህፃናት ጤና አማካሪ ነህ። ከእርግዝና፣ ከወሊድና እና ከድህረ ወሊድ ጤና ጋር የተያያዘ የምርጫ ጥያቄ ይሰጥዎታል። ስራዎ ጥያቄውን በጥንቃቄ በማንበብ ከአማራጮች (ሀ፣ ለ፣ መ፣ ወይም ሰ) ውስጥ አንዱን ምርጥ መልስ መምረጥ ነው። 
    
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
