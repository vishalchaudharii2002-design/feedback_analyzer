# tasks.py
from worker_config import celery_app
from translation import load_translation_models, translate_text

MODELS_PATH = "Translation_Model"

try:
    load_translation_models(MODELS_PATH)
except Exception as e:
    print(f"[tasks] Warning: failed to load models - {e}")

@celery_app.task(bind=True)
def translate_texts_task(self, texts: list[str]):
    results = []
    total = len(texts)
    for idx, text in enumerate(texts):
        translated = translate_text(text)
        results.append(translated)
        if idx % 10 == 0:
            progress = int((idx / max(1, total)) * 100)
            self.update_state(state="PROGRESS", meta={"progress": progress})

    return {"translated_texts": results, "count": total}
