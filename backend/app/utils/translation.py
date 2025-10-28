import os
import argostranslate.package
import argostranslate.translate
import langid

TRANSLATION_FUNCS = {}

def load_translation_models(models_path="Translation_Model"):
    """
    Loads Argos Translate models from the given folder and builds translation functions.
    """
    if not os.path.exists(models_path):
        raise FileNotFoundError(f"Translation model path '{models_path}' not found.")

    for fname in os.listdir(models_path):
        if fname.endswith(".argosmodel"):
            path = os.path.join(models_path, fname)
            try:
                argostranslate.package.install_from_path(path)
            except Exception:
                pass

    installed = argostranslate.translate.get_installed_languages()
    funcs = {}
    for from_lang in installed:
        for to_lang in installed:
            if to_lang.code == "en" and from_lang.code != "en":
                funcs[from_lang.code] = from_lang.get_translation(to_lang).translate

    global TRANSLATION_FUNCS
    TRANSLATION_FUNCS = funcs


def detect_language(text: str):
    if not text.strip():
        return "en"
    try:
        lang, _ = langid.classify(text)
        return lang
    except Exception:
        return "en"


def translate_text(text: str):

    if not text.strip():
        return text
    lang = detect_language(text)
    
    if lang == "en":
        return text

    func = TRANSLATION_FUNCS.get(lang)
    if func:
        try:
            return func(text)
        except Exception:
            return text
    return text
