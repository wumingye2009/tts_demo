# tts.py
import os
import shutil
from datetime import datetime
from gradio_client import Client, handle_file

HF_SPACE = "mrfakename/E2-F5-TTS"

def synthesize(text, ref_audio_path, output_dir="static/outputs"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"cloned_voice_{timestamp}.wav"
    output_filepath = os.path.join(output_dir, output_filename)

    # 初始化客户端
    client = Client(HF_SPACE)

    try:
        # 远程推理
        result = client.predict(
            handle_file(ref_audio_path),
            "",         # 空的参考文本
            text,       # 要合成的目标文本
            False,      # 是否去除静音
            0.15,       # 混合参数
            32,         # 推理步数
            1.0,        # 语速
            api_name="/basic_tts"
        )

        # 判断结果结构
        if not isinstance(result, (list, tuple)) or len(result) < 1:
            raise ValueError(f"Unexpected result format: {result}")

        audio_path = result[0]
        transcript = result[2] if len(result) > 2 else ""

        # 保存合成音频
        shutil.copy(audio_path, output_filepath)
        print(f"[INFO] 语音合成完成，已保存为: {output_filepath}")
        print(f"[INFO] 实际参考转录：{transcript}")

        return output_filename, transcript

    except Exception as e:
        print(f"[ERROR] 合成失败: {e}")
        raise
