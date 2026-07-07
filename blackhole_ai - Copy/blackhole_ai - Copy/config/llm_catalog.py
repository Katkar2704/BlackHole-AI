LLM_CATALOG = {
    "API_MODELS": {
        "OpenAI": ["GPT-4 Turbo", "GPT-4o", "GPT-4", "GPT-3.5 Turbo"],
        "Anthropic": ["Claude 3.5 Sonnet", "Claude 3 Opus", "Claude 3 Haiku"],
        "Google": ["Gemini 1.5 Pro", "Gemini 1.5 Flash", "Gemini Ultra"],
        "Meta": ["Llama 3.3 70B Instruct", "Llama 3.1 405B Instruct", "Llama 3.1 70B"],
        "DeepSeek": ["DeepSeek V3", "DeepSeek Coder V2"],
        "Mistral": ["Mistral Large 2", "Mistral Medium", "Mixtral 8x22B"],
        "Others": ["Grok 2", "Perplexity Sonar", "Cohere Command R+"]
    },
    "LOCAL_MODELS": {
        "Coding": ["CodeLlama 70B", "DeepSeek Coder 33B", "WizardCoder 34B"],
        "General": ["Llama 3.1 8B", "Mistral 7B", "Gemma 2 9B", "Phi-3 Medium"],
        "Reasoning": ["Nous Hermes 2", "OpenHermes 2.5", "Orca 2 13B"]
    },
    "DOMAIN_EXPERTS": {
        "Medical": ["Med-PaLM 2", "BioGPT"],
        "Legal": ["LegalBERT", "LawyerLlama"],
        "Finance": ["BloombergGPT", "FinGPT"],
        "Science": ["Galactica", "SciPhi"]
    }
}