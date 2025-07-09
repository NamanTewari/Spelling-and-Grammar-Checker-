from textblob import TextBlob
from language_tool_python import LanguageToolPublicAPI

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageToolPublicAPI('en-US')

    def correct_spell(self, text):
        if not text:
            return ""
        try:
            words = text.split()
            corrected_words = [str(TextBlob(word).correct()) for word in words]
            return " ".join(corrected_words)
        except Exception as e:
            return f"Error in spell check: {str(e)}"

    def correct_grammar(self, text):
        if not text:
            return "", 0
        try:
            matches = self.grammar_check.check(text)
            corrected_text = self.grammar_check.correct(text)
            found_mistakes_count = len(matches)
            return corrected_text, found_mistakes_count
        except Exception as e:
            return f"Error in grammar check: {str(e)}", 0