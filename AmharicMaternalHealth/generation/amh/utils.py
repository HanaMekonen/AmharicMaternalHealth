from lm_eval.utils import weighted_f1_score


def doc_to_choice_eng(doc):
    choices = doc['English_Answer']
    return choices

def doc_to_choice_amh(doc):
    choices = doc['Amharic_Answer']
    return choices

def doc_to_text_amh_eng_p1(doc):
    output = """በመቀጠል የተሰጠውን ጥያቄ በጥንቃቄ በማንበብ ትክክለኛ መልስ የሚሆነውን በግልፅ ያስቀምጡ።  

                ጥያቄ:
                "{question}"

                መልስ :"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text

def doc_to_text_amh_eng_p2(doc):
    output = """ከዚህ በታች የተሰጠውን የእናቶችና ህፃናት ጤናን የተመለከተ ጥያቄ በጥንቃቄ በማንበብ ትክክለኛውን መልስ ይስጡ።
                
                ጥያቄ:
                "{question}"
                :"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text


def doc_to_text_amh_eng_p3(doc):
    output = """ በደንብ ልምድ ያሎት የቅድመ ወሊድ እና የድህረ ወሊድ እናቶችና ህፃናት ጤና አማካሪ ኖት። ከእርግዝና፣ ከወሊድና እና ከድህረ ወሊድ ጤና ጋር የተያያዘ ጥያቄ ይሰጥዎታል። ጥያቄውን በጥንቃቄ በማንበብ ተገቢውን መልስ ይስጡ። 
               
                ጥያቄ:
                "{question}"

                መልስ:"""

    text = output.format(
        question=doc["Amharic_Questions"]
    )
    return text
