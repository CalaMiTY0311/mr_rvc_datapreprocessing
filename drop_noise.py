import librosa
import numpy as np

audio_path = 'vocals.wav'
output_path = 'delete_noise.wav'

def denoise_audio(audio_path, output_path):
    # 오디오 파일 불러오기
    audio, sr = librosa.load(audio_path, sr=None)
    
    # 스펙트로그램 계산
    spectrogram = np.abs(librosa.stft(audio))
    
    # 스펙트로그램을 기반으로 노이즈 마스크 생성
    noise_mask = np.mean(spectrogram, axis=1) < 0.01
    
    # 노이즈 마스크를 이용하여 스펙트로그램 수정
    denoised_spectrogram = spectrogram.copy()
    denoised_spectrogram[noise_mask] = 0
    
    # 수정된 스펙트로그램을 이용하여 음성 데이터 복원
    denoised_audio = librosa.istft(denoised_spectrogram)
    
    # 복원된 음성 데이터 저장
    librosa.write_wav(output_path, denoised_audio, sr)

denoise_audio(audio_path, output_path)