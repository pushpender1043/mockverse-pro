import gradio as gr
import random
import matplotlib.pyplot as plt
import time

# ==========================================
# 1. ADVANCED QUESTION BANK (With Explanations & Difficulty)
# ==========================================
QUESTION_BANK = [
    {"id": 1, "subject": "Physics", "topic": "Mechanics", "level": "Easy", "question": "Dimensional formula of Force?", "options": ["MLT-2", "ML2T-2", "MLT-1", "M0L0T0"], "answer": "MLT-2", "explanation": "Force = Mass x Acceleration = [M] x [LT^-2] = [MLT^-2]"},
    {"id": 2, "subject": "Physics", "topic": "Thermodynamics", "level": "Medium", "question": "First law of thermodynamics is based on?", "options": ["Conservation of Energy", "Newton's Law", "Conservation of Mass", "Entropy"], "answer": "Conservation of Energy", "explanation": "The first law states that energy can neither be created nor destroyed, only transformed."},
    {"id": 3, "subject": "Chemistry", "topic": "Atomic Structure", "level": "Easy", "question": "Shape of s-orbital?", "options": ["Spherical", "Dumbbell", "Double Dumbbell", "Complex"], "answer": "Spherical", "explanation": "s-orbitals are non-directional and spherical in shape."},
    {"id": 4, "subject": "Chemistry", "topic": "Bonding", "level": "Hard", "question": "Which bond is strongest?", "options": ["Ionic", "Covalent", "Hydrogen", "Vander Waals"], "answer": "Ionic", "explanation": "Ionic bonds involve complete transfer of electrons and strong electrostatic forces."},
    {"id": 5, "subject": "Maths", "topic": "Calculus", "level": "Easy", "question": "d/dx of sin(x)?", "options": ["cos(x)", "-cos(x)", "tan(x)", "sec(x)"], "answer": "cos(x)", "explanation": "The derivative of sine function is cosine function."},
    {"id": 6, "subject": "Maths", "topic": "Algebra", "level": "Medium", "question": "Value of i^2?", "options": ["1", "-1", "0", "i"], "answer": "-1", "explanation": "i is the square root of -1, so i^2 is -1."},
    {"id": 7, "subject": "Biology", "topic": "Cell Biology", "level": "Easy", "question": "Powerhouse of cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Lysosome"], "answer": "Mitochondria", "explanation": "Mitochondria produce ATP through respiration."},
    {"id": 8, "subject": "Physics", "topic": "Optics", "level": "Medium", "question": "Sky appears blue due to?", "options": ["Dispersion", "Scattering", "Refraction", "Reflection"], "answer": "Scattering", "explanation": "Rayleigh scattering causes shorter wavelengths (blue) to scatter more."},
    {"id": 9, "subject": "Chemistry", "topic": "Organic", "level": "Hard", "question": "Hybridization of Carbon in Diamond?", "options": ["sp", "sp2", "sp3", "dsp2"], "answer": "sp3", "explanation": "In diamond, each carbon is bonded to 4 other carbons tetrahedrally (sp3)."},
    {"id": 10, "subject": "Maths", "topic": "Vectors", "level": "Medium", "question": "Dot product of two perpendicular vectors?", "options": ["1", "0", "-1", "Infinite"], "answer": "0", "explanation": "cos(90) is 0, so A.B = |A||B|cos(90) = 0."},
]

MAX_UI_QUESTIONS = 5  # Demo ke liye 5 rakha hai

# ==========================================
# 2. SMART LOGIC (Charts & Analytics)
# ==========================================

def start_test_logic(subject, level):
    # Filter Questions
    filtered = [q for q in QUESTION_BANK if q["subject"] == subject]
    
    # Simple Logic: Agar Hard select kiya to random mix, real app me strict filter laga sakte hain
    if len(filtered) < MAX_UI_QUESTIONS:
        filtered = QUESTION_BANK # Fallback if not enough questions
        
    selected = random.sample(filtered, min(len(filtered), MAX_UI_QUESTIONS))
    
    # UI Updates
    updates = []
    for i, q in enumerate(selected):
        label_text = f"Q{i+1}. {q['question']} [{q['level']}]"
        updates.append(gr.Radio(choices=q["options"], label=label_text, visible=True, value=None, interactive=True))
    
    # Hide unused slots
    for _ in range(MAX_UI_QUESTIONS - len(selected)):
        updates.append(gr.Radio(visible=False, value=None))
    
    # Start Timer
    start_time = time.time()
    
    # Return: State(Questions), State(StartTime), Tab(Switch), UI components...
    return [selected, start_time, gr.Tabs(selected=1)] + updates

def generate_performance_chart(correct, wrong, skipped):
    # Create Pie Chart
    labels = ['Correct', 'Wrong', 'Skipped']
    sizes = [correct, wrong, skipped]
    colors = ['#4CAF50', '#F44336', '#9E9E9E'] # Green, Red, Grey
    
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'color':"black"})
    ax.axis('equal')
    plt.close(fig)
    return fig

def submit_test_logic(quiz_state, start_time_state, *user_answers):
    if not quiz_state:
        return "Error", None, "Generate test first!", gr.Tabs(selected=1)

    # Time Calculation
    end_time = time.time()
    time_taken = round(end_time - start_time_state, 2)
    
    score = 0
    correct = 0
    wrong = 0
    skipped = 0
    
    solution_text = "### 📖 Detailed Solutions & Explanations\n\n"
    
    active_len = len(quiz_state)
    active_answers = user_answers[:active_len]

    for i, (q, ans) in enumerate(zip(quiz_state, active_answers)):
        correct_ans = q["answer"]
        explanation = q["explanation"]
        
        if ans is None:
            skipped += 1
            solution_text += f"**Q{i+1}:** {q['question']}\n❌ *Skipped* | ✅ Correct: **{correct_ans}**\n💡 *Reason:* {explanation}\n\n---\n"
        elif ans == correct_ans:
            score += 4
            correct += 1
            solution_text += f"**Q{i+1}:** {q['question']}\n✅ *Correct!* \n\n---\n"
        else:
            score -= 1
            wrong += 1
            solution_text += f"**Q{i+1}:** {q['question']}\n❌ *Your Ans:* {ans} | ✅ Correct: **{correct_ans}**\n💡 *Reason:* {explanation}\n\n---\n"

    # Generate Chart
    chart = generate_performance_chart(correct, wrong, skipped)
    
    # Summary Text
    total_marks = active_len * 4
    accuracy = (correct / active_len) * 100 if active_len > 0 else 0
    summary = f"""
    ### 🏆 Test Results
    **Score:** {score} / {total_marks}
    **Time Taken:** {time_taken} seconds
    **Accuracy:** {accuracy:.2f}%
    """
    
    return summary, chart, solution_text, gr.Tabs(selected=2)

# ==========================================
# 3. MODERN UI SETUP
# ==========================================
with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo", secondary_hue="blue")) as demo:
    
    # State Variables
    quiz_db = gr.State([])
    timer_start = gr.State(0)

    gr.Markdown("""
    # 🚀 MockVerse Pro
    *Advanced AI Mock Test Platform with Analytics & Explanations*
    """)

    with gr.Tabs() as tabs:
        
        # --- TAB 1: SETUP ---
        with gr.TabItem("⚙️ Setup Exam", id=0):
            with gr.Row():
                with gr.Column(scale=1):
                    subject_in = gr.Dropdown(["Physics", "Chemistry", "Maths"], label="Choose Subject", value="Physics")
                    level_in = gr.Radio(["Easy", "Medium", "Hard"], label="Difficulty Level", value="Medium")
                    start_btn = gr.Button("🔥 Start Test", variant="primary", size="lg")
                with gr.Column(scale=2):
                    gr.Markdown("### Instructions:\n1. +4 for Correct, -1 for Wrong.\n2. Timer starts automatically.\n3. Detailed analysis shown after submission.")
                    
        # --- TAB 2: EXAM INTERFACE ---
        with gr.TabItem("📝 Attempt Test", id=1):
            q_components = []
            for i in range(MAX_UI_QUESTIONS):
                r = gr.Radio(visible=False)
                q_components.append(r)
            
            submit_btn = gr.Button("✅ Submit Test", variant="stop")

        # --- TAB 3: ANALYTICS ---
        with gr.TabItem("📊 Analysis & Solutions", id=2):
            with gr.Row():
                with gr.Column(scale=1):
                    result_summary = gr.Markdown("### Waiting for results...")
                    result_plot = gr.Plot(label="Performance Chart")
                with gr.Column(scale=2):
                    solution_box = gr.Markdown("Solutions will appear here.")
            
            restart_btn = gr.Button("🔄 Take Another Test")
            restart_btn.click(lambda: gr.Tabs(selected=0), None, tabs)

    # --- WIRING (Function Connections) ---
    
    # Start Test: Setup -> Exam Tab
    start_btn.click(
        fn=start_test_logic,
        inputs=[subject_in, level_in],
        outputs=[quiz_db, timer_start, tabs] + q_components
    )

    # Submit Test: Exam -> Analytics Tab
    submit_btn.click(
        fn=submit_test_logic,
        inputs=[quiz_db, timer_start] + q_components,
        outputs=[result_summary, result_plot, solution_box, tabs]
    )

demo.launch(debug=True)
