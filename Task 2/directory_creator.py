import os
import shutil
from tqdm import tqdm

audio_path = "Task 2\\Hindi_hin_BCS_NT_Non-Drama"
transcript_path = "Task 2\\transcripts"

dataset_path = "Task 2\Dataset\\"
if not os.path.exists(dataset_path):
    os.mkdir(dataset_path)

audio_files = os.listdir(audio_path)
transcripts = os.listdir(transcript_path)

for i in tqdm(range(len(audio_files))):
    os.mkdir(os.path.join(dataset_path, str(i)))
    shutil.copyfile(
        os.path.join(audio_path, audio_files[i]),
        os.path.join(dataset_path, str(i), "audio.mp3"),
    )
    shutil.copyfile(
        os.path.join(transcript_path, transcripts[i]),
        os.path.join(dataset_path, str(i), "transcript.txt"),
    )
