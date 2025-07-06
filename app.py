# app.py
from flask import Flask, request, render_template, send_from_directory
import os
import uuid
from tts import synthesize

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

import uuid

@app.route("/", methods=["GET", "POST"])
def index():
    output_file = None
    error_message = None
    uploaded_audio = None
    current_text = None

    if request.method == "POST":
        try:
            # 检查是否上传音频
            f = request.files.get('audio')
            text = request.form.get('text', '').strip()
            current_text = text

            if f and f.filename:
                # 生成唯一文件名，防止缓存和冲突
                ext = os.path.splitext(f.filename)[-1]
                audio_filename = f"{uuid.uuid4().hex}{ext}"
                uploaded_audio = audio_filename
                audio_path = os.path.join(UPLOAD_FOLDER, audio_filename)
                f.save(audio_path)

                # 如果有文本，才合成语音
                if text:
                    output_file, _ = synthesize(text, audio_path)

            elif not text:
                error_message = "请上传音频并输入文本。"

        except Exception as e:
            error_message = f"出错：{str(e)}"

    return render_template(
        "index.html",
        output_file=output_file,
        uploaded_audio=uploaded_audio,
        current_text=current_text,
        error_message=error_message
    )


# 访问输出音频（合成后）
@app.route("/outputs/<filename>")
def serve_output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, mimetype="audio/wav")

# 访问上传音频（试听参考音频）
@app.route("/uploads/<filename>")
def serve_uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)
