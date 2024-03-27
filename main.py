from flask import Flask

app = Flask(__name__)

# قائمة بالمعلومات الغريبة
weird_facts = [
    "هل تعلم أن البطريق يمكنه القفز لارتفاعات تصل إلى 3 أمتار؟",
    "في اليابان، هناك مهرجان سنوي لرمي الوسائد.",
    "النمل يمتلك القدرة على النجاة من السقوط من أي ارتفاع دون أن يصاب بأذى."
]

# قائمة بالأسئلة المحرجة
embarrassing_questions = [
    "هل نسيت يومًا ارتداء أحد قطع الملابس الأساسية عند خروجك من المنزل؟",
    "هل تحدثت يومًا بصوت عالٍ وأنت تظن أنك وحيد ثم اكتشفت وجود شخص آخر؟",
    "هل سبق وأن أخطأت في تحية شخص ظننته شخصًا تعرفه لتكتشف لاحقًا أنه غريب؟"
]

# متغيرات لتتبع الفهارس الحالية لكل قائمة
current_fact_index = 0
current_question_index = 0

@app.route('/معلومة')
def get_weird_fact():
    global current_fact_index
    fact = weird_facts[current_fact_index]
    current_fact_index = (current_fact_index + 1) % len(weird_facts)  # الانتقال للعنصر التالي والعودة إلى البداية عند الوصول للنهاية
    return fact

@app.route('/سؤال')
def get_embarrassing_question():
    global current_question_index
    question = embarrassing_questions[current_question_index]
    current_question_index = (current_question_index + 1) % len(embarrassing_questions)  # الانتقال للعنصر التالي والعودة إلى البداية عند الوصول للنهاية
    return question