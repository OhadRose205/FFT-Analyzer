import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks

signal, fs = sf.read("example.wav")
if signal.ndim == 1:
    signal = signal.reshape(-1, 1)

channels = signal.shape[1]

for ch in range(channels):
    print(f"\n🔊 Channel {ch+1}:")
    channel_signal = signal[:, ch]
    N = len(channel_signal)
    t = np.linspace(0, N/fs, N)

    yf = fft(signal)
    xf = fftfreq(N, 1/fs)

    magnitude = np.abs(yf[:N // 2])
    freqs = xf[:N // 2]



    plt.figure(figsize=(10, 4))
    plt.plot(t, channel_signal)
    plt.title(f"Time Domain - Channel {ch + 1}")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()
    plt.show()


plt.figure(figsize=(10, 4))
plt.plot(xf[:N // 2], np.abs(yf[:N // 2]))
plt.title("Frequency Domain (FFT)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid()
plt.tight_layout()
plt.show()



