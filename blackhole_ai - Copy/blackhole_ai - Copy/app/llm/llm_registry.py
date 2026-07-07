# app/llm/llm_registry.py

LLM_CATALOG = {
    "🚀 POWERFUL API MODELS": {
        "OpenAI": ["GPT-4o", "GPT-4 Turbo", "GPT-3.5 Turbo"],
        "Anthropic": ["Claude 3.5 Sonnet", "Claude 3 Opus", "Claude 3 Haiku"],
        "Google": ["Gemini 1.5 Pro", "Gemini 1.5 Flash"],
        "Meta": ["Llama 3.3 70B", "Llama 3.1 405B"],
        "DeepSeek": ["DeepSeek V3", "DeepSeek Coder V2"]
    },
    "🎯 DOMAIN EXPERTS": {
        "Healthcare": ["Med-PaLM 2", "BioGPT"],
        "Finance": ["BloombergGPT", "FinGPT"],
        "Legal": ["LawyerLlama", "LegalBERT"],
        "Science": ["Galactica", "SciPhi"]
    },
    "🦙 LOCAL MODELS (OLLAMA)": {
        "Coding": ["DeepSeek Coder 33B", "CodeLlama 70B"],
        "General": ["Llama 3.1 8B", "Mistral 7B", "Gemma 2 9B"],
        "Reasoning": ["Nous Hermes 2", "Phi-3 Medium"]
    }
}

def get_routing_logic(domain, complexity):
    """
    Intelligent Routing Logic:
    - Complexity > 70: Returns a Heavyweight Model.
    - Complexity <= 70: Returns a Local/Efficient Model.
    """
    d = domain.lower()
    is_complex = complexity > 70

    # Coding Domain
    if any(x in d for x in ["code", "software", "python", "script", "program"]):
        return "Claude 3.5 Sonnet" if is_complex else "DeepSeek Coder 33B (Local)"

    # Medical Domain
    if any(x in d for x in ["health", "med", "bio", "doctor"]):
        return "Med-PaLM 2" if is_complex else "BioGPT (Local)"

    # Legal Domain
    if any(x in d for x in ["legal", "law", "gov", "court"]):
        return "LawyerLlama" if is_complex else "LegalBERT (Local)"

    # Finance Domain
    if any(x in d for x in ["finan", "bank", "price", "stock", "money"]):
        return "BloombergGPT" if is_complex else "FinGPT (Local)"

    # General / Fallback
    if is_complex:
        return "GPT-4o"
    return "Llama 3.1 8B (Local)"