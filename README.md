


##  **Backend Repository** (`MiniProject-Backend`)


# LogicWise: Coding Assistant — Backend

This is the **backend** for LogicWise — an AI-powered assistant that helps programmers debug, improve, and understand their code logic in real-time. It connects with the frontend using WebSockets and integrates with LLaMA 3.3 through Groq API to generate intelligent hints and logic-based feedback.

##  Features

-  LLM-based logic guidance (LLaMA 3.3 via Groq)
-  Real-time code analysis using **Socket.IO**
-  REST API for hint requests & prompt processing
-  Firebase user verification via tokens
-  Firestore integration for session-based code saving

##  Tech Stack

- **Python 3**
- **Flask**
- **Socket.IO (Flask-SocketIO)**
- **Groq API (LLaMA 3.3)**
- **Firebase Admin SDK**
- **Piston API** (for optional code execution)

##  LLM Prompting Strategy

- `System Prompts` to define assistant behavior (logic-first, no full code output)
- `User Prompts` from real user input or code
- Adaptive hinting: initial → debug → detailed guidance
- Debounce & trigger on inactivity for live typing support



