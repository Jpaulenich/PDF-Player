from flask import Flask, request, render_template, jsonify
import fitz  # PyMuPDF
import re

app = Flask(__name__)

# Regex that captures "word-like" chunks and also punctuation as separate tokens
# We keep punctuation tokens so we can pause on them.
TOKEN_RE = re.compile(
    r"""
    [A-Za-z0-9]+(?:'[A-Za-z0-9]+)?   # words / contractions
    |[“”"‘’']                        # quotes
    |[.,;:!?]                        # common punctuation
    |[-–—]                           # dashes
    |\(|\)|\[|\]|\{|\}               # brackets
    """,
    re.VERBOSE,
)

def extract_words_from_pdf(file_bytes: bytes) -> list[str]:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text_parts = []
    for page in doc:
        text_parts.append(page.get_text("text") or "")
    text = "\n".join(text_parts)

    # Tokenize: words + punctuation tokens
    tokens = TOKEN_RE.findall(text)
    # Filter out empty tokens just in case
    tokens = [t for t in tokens if t.strip()]
    return tokens

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/upload")
def upload():
    if "pdf" not in request.files:
        return jsonify({"error": "No file field named 'pdf'"}), 400
    f = request.files["pdf"]
    data = f.read()
    if not data:
        return jsonify({"error": "Empty file"}), 400

    try:
        tokens = extract_words_from_pdf(data)
    except Exception as e:
        return jsonify({"error": f"Failed to parse PDF: {e}"}), 500

    return jsonify({
        "tokens": tokens,
        "total": len(tokens),
    })

if __name__ == "__main__":
    # Listen on 0.0.0.0 so it’s reachable on your LAN too (optional)
    app.run(host="0.0.0.0", port=8080, debug=True)


